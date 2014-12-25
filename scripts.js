ymaps.ready(init);
var khMap;

// noprotect

function init(){
  khMap = new ymaps.Map("map", {
    center: [50, 36.25],
    zoom: 12
  });
  place(coordsA, 'red');
  place(coordsB, 'green');
  place(coordsC, 'blue');

}

function place(coords, color){
  var clusterer = new ymaps.Clusterer({preset: 'islands#' + color + 'ClusterIcons'});
  var geoObjects = [];
  for (var i = 0; i<coords.length; i++) {
    geoObjects[i] = new ymaps.GeoObject({
      geometry: {
        type: "Point",
        coordinates: [coords[i][1], coords[i][2]]
      },
      properties: {
        hintContent: coords[i][0]
      }
    }, {
      preset: 'islands#' + color + 'CircleDotIcon'
    });
  }

  clusterer.add(geoObjects);
  khMap.geoObjects.add(clusterer);
}