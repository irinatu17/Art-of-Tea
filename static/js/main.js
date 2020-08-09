$(document).ready(function() {

    //Hiding search field on mobile when the page loads
    $('#search-form-container').hide();


    $('#imageForm').hide();

    $('#product_form').submit(function(e){
        e.preventDefault();
        console.log("form submitted!") 
        
        add_product();
        $("#imageForm").slideToggle();
    });
   // AJAX for posting
        function add_product() {
            console.log("add prodyct is working!") // sanity check
            console.log($('#id_name').val())
            console.log($('#id_description').val())
            console.log($('#id_category').val())
            console.log($('#id_sku').val())
            console.log($('#id_price').val())
            console.log($('#id_rating').val())
            console.log($('#tea').val())
            console.log($('#teaware').val())
            console.log($('#nextStep').val())
            $.ajax({
                url : "/products/add/", // the endpoint
                type : "POST", // http method
                data : { name : $('#id_name').val(),
                        description : $('#id_description').val(),
                        category : $('#id_category').val(),
                        sku : $('#id_sku').val(),
                        price : $('#id_price').val(),
                        rating : $('#id_rating').val(),
                        has_weight_value : document.getElementById("tea").checked,
                        product: $('#nextStep').val(), 
                        image_add: $('#image_add').val(), 
                    }, // data sent with the post request

                // handle a successful response
                success : function(json) {
                    // $('#post-text').val(''); // remove the value from the input
                    console.log(json); // log the returned json to the console
                    console.log("success"); // another sanity check
                },

                // handle a non-successful response
                error : function(xhr,errmsg,err) {
                    $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                        " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                }
            });
        };

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







$(function() {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});