$(document).ready(function () {
  $('#search-form-container').hide();
  /**
   *  Toggles the searchbar on smaller screens
   */
  $('#search-button').click(function () {
    $('#search-form-container').slideToggle('slow');
  });
  /**
   * Initilizes the Date Time Picker
   * From Tempus Dominus Bootstrap 4 Datetime Picker
   * https://tempusdominus.github.io/bootstrap-4/
   */
  const dateTimePickerInit = () => {
    $('#datetime, div[id^=datetime_cart-]').datetimepicker({
      format: 'DD/MM/YYYY HH:mm',
      minDate: new Date(),
      enabledHours: [12, 13, 14, 15, 16, 17, 18, 19, 20],
      stepping: 30,
    });
    $('div[id^=datetime_cart-]').each(function () {
      $(this).children('input.datetimepicker-input').val($(this).data('value'));
    });
  };
  dateTimePickerInit();
  /**
   *  Initializes Bootstrap toasts
   */
  $('.toast').toast('show');

  /**
   *  Back to Top button
   */

  $('.btt-link').click(function(e) {
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: 'smooth'
    })
  })
});

  bttbutton = document.getElementById("back-to-top-btn");
// When the user scrolls down 30px from the top of the document, show the button
  window.onscroll = function() {scrollFunction()};
  function scrollFunction() {
    if (document.body.scrollTop > 30 || document.documentElement.scrollTop > 30) {
      bttbutton.style.display = "block";
    } else {
      bttbutton.style.display = "none";
    }
  }

 
