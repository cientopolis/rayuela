function formatAMPM(date) {
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = minutes < 10 ? '0' + minutes : minutes;
    var strTime = hours + ':' + minutes + ' ' + ampm;
    return strTime;
}

function init_loading() {
    document.getElementById('f_map').className = 'fa fa-spinner fa-spin'
}
function end_loading() {
    document.getElementById('f_map').className = 'fas fa-map-marker-alt'
}


function success(pos) {
    const crd = pos.coords;

    console.log('Tu ubicación actual es:');
    console.log(`Latitud : ${crd.latitude}`);
    console.log(`Longitud: ${crd.longitude}`);
    console.log(`Más o menos ${crd.accuracy} metros.`);



    let current = new Date()
	
    var fecha = current.getFullYear()  + '-' + ( current.getMonth() + 1 ) + '-' + current.getDate() + ' ' + current.getHours() + ':' + (current.getMinutes()<10?'0':'') + current.getMinutes() ;

    document.getElementById("datetime").value = fecha

    document.getElementById("lat").value = crd.latitude;
    document.getElementById("lon").value = crd.longitude;

    let layer = L.marker([crd.latitude, crd.longitude])
    layer.addTo(map);

    drawnItems.addLayer(layer);


    end_loading();


}

function error(err) {
    init_loading();
    console.warn(`ERROR(${err.code}): ${err.message}`);
    end_loading();


}




$('#my_coordinates').click(function () {
    document.getElementById('f_map').classList.toggle('fa')
    document.getElementById('f_map').classList.toggle('fa-spinner')
    document.getElementById('f_map').classList.toggle('fa-spin')
    setTimeout(function () {
        drawnItems.clearLayers();
        navigator.geolocation.getCurrentPosition(success, error, {
            enableHighAccuracy: true,
            timeout: 5000,
            maximumAge: 0
        });

    }, 2000);






});