$(document).ready(function() {
    //Function to initialize Map 
    function initMap() {
        const artOfTea = {lat: 53.349744, lng: -6.260177};
        const map = new google.maps.Map(document.getElementById('map'), {zoom: 12, center: artOfTea});
        const marker = new google.maps.Marker({position: artOfTea, map: map});
    };
    //Hiding search field on mobile when the page loads
   $('#search-form-container').hide();

    //Stiding down and up the search form, when the search icon is clicked
    $("#search-button").click(function(){
    $("#search-form-container").toggle();
  });

initMap();

});
