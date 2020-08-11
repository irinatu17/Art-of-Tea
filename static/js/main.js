$(document).ready(function() {

    //Hiding search field on mobile when the page loads
    $('#search-form-container').hide();


    //Sliding down and up the search form, when the search icon is clicked
    $("#search-button").click(function(){
        $("#search-form-container").slideToggle("slow");
    });

    //Tempus Dominus bootstrap-datetimepicker:
    // After the datepickers are initialized, it's calling them again, looping over .each(),
    // and assigning the value to the data-attribute "data-value=''" for the selected datepicker
    $(function () {
        $("#datetime, div[id^=datetime_cart-]").datetimepicker({
            format: 'DD/MM/YYYY HH:mm',
            minDate: new Date(),
            enabledHours: [12, 13, 14, 15, 16, 17, 18, 19, 20],
            stepping: 30,
        });
        $("div[id^=datetime_cart-]").each(function() {
            $(this).children("input.datetimepicker-input").val($(this).data("value"));
        });
    });

    // Initialize Bootstrap toasts
    $('.toast').toast('show');

});
