$(document).ready(function() {
    //Hiding search field on mobile when the page loads
   $('#search-form-container').hide();

    //Stiding down and up the search form, when the search icon is clicked
    $("#search-button").click(function(){
    $("#search-form-container").toggle();
  });
});
