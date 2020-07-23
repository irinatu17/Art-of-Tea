$(document).ready(function() {

    //Hiding search field on mobile when the page loads
    $('#search-form-container').hide();

    //Sliding down and up the search form, when the search icon is clicked
    $("#search-button").click(function(){
        $("#search-form-container").slideToggle("slow");
    });

    //Tempus Dominus bootstrap-datetimepicker
    $(function () {
        $("#datetimepicker1").datetimepicker({
        format: 'DD/MM/YYYY HH:mm',
        });
    });

    // Initialize Bootstrap toasts
    $('.toast').toast('show');

});
