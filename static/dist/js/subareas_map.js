
let map;

function viewInMap(data) {

    if (map != undefined || !data) {
        map.remove();
        document.getElementById('map').innerHTML = "";
    }


    if (data) {
        arr = [];

        document.getElementById('map').innerHTML = "<div id='map' style='height: 180px'></div>";
        data.forEach((numero, index) => {
            
            arr.push([numero.subarea[0],numero.id,numero.number]);


        });
    }

    map = new L.map(document.getElementById('map'), { zoomControl: true }).setView([arr[0][0][0][1], arr[0][0][0][0]], 15);

    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    let drawnItems = new L.FeatureGroup()


    map.addLayer(drawnItems)

    let drawControl = new L.Control.Draw({
        draw: {
            polygon: false,
            marker: false,
            circlemarker: false,
            rectangle: false,
            circle: false,
            polyline: false,
        },
        edit: {
            featureGroup: drawnItems,
            edit: false,
            remove: false,
        }
    });

    map.addControl(drawControl);

    arr.forEach((area) => {
        let areas = []
        area[0].forEach((a) => {
            
            areas.push([a[1], a[0]])
        });

        let polygon = new L.Polygon(areas, { 'id': (area[1]),'color':'red' }).addTo(map);
        polygon.bindPopup("<strong>Área " + (area[2]), + "</strong>");
        polygon.on('click', function (event) {            
            $('#id_area').val(event.target.options.id);
            $('#id_area').trigger('change');
        });   
    });


}

