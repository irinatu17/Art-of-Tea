$(document).ready(function() {
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
    //Hiding search field on mobile when the page loads
   $('#search-form-container').hide();

    //Stiding down and up the search form, when the search icon is clicked
    $("#search-button").click(function(){
    $("#search-form-container").toggle();
  });

    //Tempus Dominus bootstrap-datetimepicker
    $(function () {
        $("#datetimepicker1").datetimepicker();
      });

initMap();

// The method of triggering Next and GoBack buttons is taken and modified from the following source:
// https://stackoverflow.com/questions/22297964/bootstrap-tabs-next-previous-buttons-for-forms/22298275
  $('.btnNext').click(function() {
    $('.nav-tabs .active').parent().next('li').find('a').trigger('click');
  });

  $('.btnGoBack').click(function() {
    $('.nav-tabs .active').parent().prev('li').find('a').trigger('click');
  });



  initMap();
});
