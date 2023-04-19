

var map = L.map(document.getElementById('map'), { zoomControl: false }).setView([-34.92145, -57.95453], 13);

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var drawnItems = new L.FeatureGroup()

map.addLayer(drawnItems)

var drawControl = new L.Control.Draw({
    draw: {
        polygon: false,
        marker: true,
        circlemarker: false,
        rectangle: false,
        circle: false,
        polyline: false,     
    },
    edit: {
        featureGroup: drawnItems,
        edit: false
    }
});

L.drawLocal.draw.toolbar.buttons.circle = 'Seleccionar área.';
L.drawLocal.draw.toolbar.buttons.marker = 'Seleccionar un punto.';
L.drawLocal.draw.handlers.circle.tooltip.start= 'Hacer click en el área.';
L.drawLocal.draw.handlers.marker.tooltip.start= 'Hacer click en el área.';
L.drawLocal.draw.toolbar.actions.title='Cancelar'
L.drawLocal.draw.toolbar.actions.text='Cancelar'
L.drawLocal.edit.toolbar.buttons.removeDisabled= 'Sin área para eliminar'
L.drawLocal.edit.toolbar.buttons.remove='Eliminar área'
L.drawLocal.edit.toolbar.actions.save.title='Guardar cambios.'
L.drawLocal.edit.toolbar.actions.save.text='Guardar cambios.'
L.drawLocal.edit.toolbar.actions.cancel.title='Cancelar y descartar los cambios'
L.drawLocal.edit.toolbar.actions.cancel.text='Cancelar'
L.drawLocal.edit.toolbar.actions.clearAll.title='Eliminar todas las área'
L.drawLocal.edit.toolbar.actions.clearAll.text='Eliminar todo'
L.drawLocal.draw.handlers.simpleshape.tooltip.end='Arrastrar el mouse hasta la ubicación deseada.'
L.drawLocal.edit.handlers.remove.tooltip.text='Click en área para eliminar'


map.addControl(drawControl);
map.on(L.Draw.Event.CREATED, function (e) {
    e.layer.options.color = '#FF0000';

    document.getElementById("lat").value = e.layer._latlng.lat;
    document.getElementById("lon").value = e.layer._latlng.lng;
    let layer = e.layer;
    drawnItems.clearLayers();
    drawnItems.addLayer(layer);
});

map.on(L.Draw.Event.DELETED, function (e) {

    document.getElementById("lat").value = null;
    document.getElementById("lon").value = null;
});