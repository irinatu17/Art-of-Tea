
    //Function to initialize Map 
    function initMap() {
        const artOfTea = {lat: 53.349744, lng: -6.260177};
        const map = new google.maps.Map(document.getElementById('map'), {zoom: 13, center: artOfTea});

        const contentMarker = '<div class="m-2">'+
          '<h5 class="landing-about-heading">Art of Tea<i class="fab fa-pagelines icon-green ml-2"></i></h5>'+
          '<h6>Opening hours:</h6>' +
          '<table>' +
          '<tr><th>Monday</th><td>10am - 8pm</td></tr>' +
          '<tr><th>Tuesday</th><td>10am - 8pm</td></tr>' +
          '<tr><th>Wednesday</th><td>10am - 8pm</td></tr>' +
          '<tr><th>Thursday</th><td>10am - 8pm</td></tr>' +
          '<tr><th>Friday</th><td>10am - 10pm</td></tr>' +
          '<tr><th>Saturday</th><td>11am - 10pm</td></tr>' +
          '<tr><th>Sunday</th><td>11am - 9pm</td></tr>' +
          '</table>'
          +'</div>';

        const infowindow = new google.maps.InfoWindow({
            content: contentMarker
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

  initMap();