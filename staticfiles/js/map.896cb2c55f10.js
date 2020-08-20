//Function to initialize Map 
function initMap() {
    const artOfTea = {lat: 53.349744, lng: -6.260177};
    const map = new google.maps.Map(document.getElementById('map'), {zoom: 13, center: artOfTea});

    const infowindow = new google.maps.InfoWindow({
        content: document.getElementById('info-window-content')
    });

    const marker = new google.maps.Marker({
        position: artOfTea,
        map: map,
        title: 'Art of Tea'
    });

    marker.addListener('click', function() {
        infowindow.open(map, marker);
    });
};
