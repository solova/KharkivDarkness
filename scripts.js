ymaps.ready(init);
var khMap;

function init(){
  khMap = new ymaps.Map("ymap", {
    center: [50, 36.25],
    zoom: 12
  });
  place(coordsA, 'red');
  place(coordsB, 'green');
  place(coordsC, 'blue');

  if (window.location.hash === ''){
    window.location.hash = 'map';
  }

}

function place(coords, color){
  var clusterer = new ymaps.Clusterer({preset: 'islands#' + color + 'ClusterIcons'});
  var geoObjects = [];
  for (var i = 0; i<coords.length; i++) {
    var dx=Math.floor(Math.random() * 2)/100000+0.00001;
    var dy=Math.floor(Math.random() * 2)/100000+0.00001;

    if (Math.floor(Math.random() * 2) == 1 ) {
        dx=-dx
    }

    if (Math.floor(Math.random() * 2) == 1 ) {
        dy=-dy
    }

    var xx=coords[i][1]+0.0001
    var yy=coords[i][0]+0.0001
    geoObjects[i] = new ymaps.GeoObject({
      geometry: {
        type: "Point",
        coordinates: [xx+dx,yy+dy]
      }
    }, {
      preset: 'islands#' + color + 'CircleDotIcon'
    });
  }

  clusterer.add(geoObjects);
  clusterer.options.set({ gridSize: 32  })
  khMap.geoObjects.add(clusterer);
}