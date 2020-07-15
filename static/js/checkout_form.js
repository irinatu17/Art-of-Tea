// Personal Details form, step 1
const personalDetailsForm = document.querySelector('#personal-details-form');
const submitButton = document.querySelector('#personal-details-btn');
submitButton.addEventListener('click', () => {
    if (personalDetailsForm.checkValidity()) {
        // grab input values and store in variables
        let name =  $('#id-full-name').val();
        let email =  $('#id-email').val(); 
        let phoneNumber =  $('#id-phone-number').val(); 
        // use javascript to toggle visibility of next form

        $('.btnNext').click(function() {
            $('.nav-tabs .active').parent().next('li').find('a').trigger('click');
        });

        //console.log(name);
    }
});


// Shipping Info form, step 2
const shippingInfoForm = document.querySelector('#shipping-info-form');
const submitButton2 = document.querySelector('#shipping-info-btn');
submitButton2.addEventListener('click', () => {
    if (shippingInfoForm.checkValidity()) {
        // grab input values and store in variables
        let addressLine1 =  $('#id-address_line1').val();
        let addressLine2 =  $('#id-address_line2').val(); 
        let townOrCity =  $('#id-town_or_city').val();
        let county =  $('#id-county').val(); 
        let postcode =  $('#id-postcode').val(); 
        let country =  $('#id-country').val(); 
        
        //console.log(country);
        // use javascript to toggle visibility of next form 
    }
});
// once the first two forms have validated and the values stored,
// add the values to hidden inputs in the final form and submit 

// The method of triggering Next and GoBack buttons is taken and modified from the following source:
// https://stackoverflow.com/questions/22297964/bootstrap-tabs-next-previous-buttons-for-forms/22298275
  $('.btnGoBack').click(function() {
    $('.nav-tabs .active').parent().prev('li').find('a').trigger('click');
  });
  $('.btnNext').click(function() {
    $('.nav-tabs .active').parent().next('li').find('a').trigger('click');
});