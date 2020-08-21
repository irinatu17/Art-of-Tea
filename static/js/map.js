/**
 * Initilizes the map
 * from Google Maps API
 */
function initMap() {
  const mapRef = document.getElementById('map');
  const contentRef = document.getElementById('info-window-content');
  const artOfTeaLocation = { lat: 53.349744, lng: -6.260177 };
  const map = new google.maps.Map(mapRef, { zoom: 13, center: artOfTeaLocation });
  const infowindow = new google.maps.InfoWindow({
    content: contentRef,
  });
  const marker = new google.maps.Marker({
    position: artOfTeaLocation,
    map: map,
    title: 'Art of Tea',
  });
  marker.addListener('click', () => {
    infowindow.open(map, marker);
  });
};