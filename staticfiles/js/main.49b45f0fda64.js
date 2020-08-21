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
});