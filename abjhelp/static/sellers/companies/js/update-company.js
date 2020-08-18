let currentLayer = null;

$(document).ready(function () {
  let map = L.map('company-map').setView([6.150096, -75.637175], 13);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  let drawnItems = new L.FeatureGroup();
  map.addLayer(drawnItems);

  addControls(map, drawnItems);

  // Add translations
  L.drawLocal = leafletDrawTranslations;

  drawCurrentBranchPolygon(map)

  $("a[href='#content-2']").on('shown.bs.tab', function (e) {
    map.invalidateSize();
  });

  map.on(L.Draw.Event.CREATED, function (e) {
    mapEventCreated(e, map, drawnItems)
  });

  map.on(L.Draw.Event.DELETED, function (e) {
    mapEventDeleted();
  })

});

function addControls(map, drawnItems) {
  let drawControl = new L.Control.Draw({
    edit: {
      featureGroup: drawnItems,
      remove: true,
      edit: true
    },
    draw: {
      polygon: true,

      circle: false,
      polyline: false,
      rectangle: false,
      marker: false,
      circlemarker: false,
    }
  });
  map.addControl(drawControl);

}

function drawCurrentBranchPolygon(map) {
  let currentBranchPolygon = JSON.parse($('#branch-profile-polygon-value').val())
  if (currentBranchPolygon !== "") {
    currentLayer = L.geoJSON(currentBranchPolygon).addTo(map);
  }

}

function mapEventCreated(e, map, drawnItems) {
  let type = e.layerType, layer = e.layer;

  if (type === 'polygon') {
    let coordinates = ""
    $.each(layer.getLatLngs()[0], function (key, value) {
      coordinates = coordinates.concat(`${value.lng} ${value.lat},`)
    });

    coordinates = coordinates.slice(0, -1)
    $('#branch-profile-polygon').val(coordinates)

  } else if (type === 'circle') {
    let coordinates = layer.getLatLng()
    let radius = layer.getRadius()

    let data = {
      'latitude': coordinates.lat,
      'longitude': coordinates.lng,
      'radius': radius,
    }

    $('#branch-profile-polygon').val(JSON.stringify(data))
  }

  // Delete the previous layers
  if (currentLayer) {
    map.removeLayer(currentLayer);
  }

  drawnItems.addLayer(layer);
  currentLayer = layer;
  map.addLayer(layer);
}

function mapEventDeleted() {
  $('#branch-profile-polygon').val("")

}