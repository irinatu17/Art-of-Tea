$(document).ready(function() {
// gets the form's fields from the Personal Details and Shipping Info sections (step 1 and step 2)
const nameRef = document.getElementById('id_full_name');
const emailRef = document.getElementById('id_email');
const phoneNumberRef = document.getElementById('id_phone_number');
const addressLine1Ref = document.getElementById('id_address_line1');
const addressLine2Ref = document.getElementById('id_address_line2');
const townOrCityRef = document.getElementById('id_town_or_city');
const countyRef = document.getElementById('id_county');
const postcodeRef = document.getElementById('id_postcode');
const countryRef = document.getElementById('id_country');

// gets the hidden input fields from the last final form (step3) 
const nameHiddenInputRef = document.getElementById('full_name');
const emailHiddenInputRef = document.getElementById('email');
const phoneNumberHiddenInputRef = document.getElementById('phone_number');
const addressLine1HiddenInputRef = document.getElementById('address_line1');
const addressLine2HiddenInputRef = document.getElementById('address_line2');
const townOrCityHiddenInputRef = document.getElementById('town_or_city');
const countyHiddenInputRef = document.getElementById('county');
const postcodeHiddenInputRef = document.getElementById('postcode');
const countryHiddenInputRef = document.getElementById('country');
const saveInfoHiddenInputRef = document.getElementById('save_info');

// Personal Details form, step 1
const personalDetailsForm = document.querySelector('#personal-details-form');
const submitButton = document.getElementById('personal-details-btn');
let personalDetailsFormValid;

// Handles the validation of the first(Personal details) step of the form when "Next" button is clicked
submitButton.addEventListener('click', () => {
    personalDetailsFormValid = personalDetailsForm.checkValidity();
    
    if (personalDetailsFormValid) {
        //if valid,  gets the values of the first fieldset
        let name = nameRef.value; 
        let email = emailRef.value;  
        let phoneNumber = phoneNumberRef.value; 
        // stores those values and add them to hidden input fields in the final form to submit
        nameHiddenInputRef.value = name;
        emailHiddenInputRef.value = email;
        phoneNumberHiddenInputRef.value = phoneNumber;

        // sends the user's input to display in a Form Summary table before the final form is submitted
        $("#full_name_table").text(name);
        $("#email_table").text(email);
        $("#phone_number_table").text(phoneNumber);

        // activates the next tab on click, when form-set is valid 
        $('.nav-tabs .active').parent().next('li').removeClass("disabled");
        $('.nav-tabs .active').parent().next('li').find('a[data-toggle]').attr("data-toggle", "tab");
        $('.nav-tabs .active').parent().next('li').find('a').trigger('click');
    }
});

// Shipping Info form, step 2
const shippingInfoForm = document.querySelector('#shipping-info-form');
const submitButton2 = document.getElementById('shipping-info-btn');
let shippingInfoFormValid;

// handles the validation of the second(Shipping Info) step of the form when "Next" button is clicked
submitButton2.addEventListener('click', () => {
    shippingInfoFormValid = shippingInfoForm.checkValidity();

    if (shippingInfoFormValid) {
        //if valid,  gets the values of the second fieldset
        let addressLine1 =  addressLine1Ref.value;
        let addressLine2 =  addressLine2Ref.value; 
        let townOrCity =  townOrCityRef.value;
        let county =  countyRef.value; 
        let postcode =  postcodeRef.value; 
        let country =  countryRef.value; 
        // stores those values and add them to hidden input fields in the final form to submit
        addressLine1HiddenInputRef.value = addressLine1;
        addressLine2HiddenInputRef.value = addressLine2;
        townOrCityHiddenInputRef.value = townOrCity;
        countyHiddenInputRef.value = county;
        postcodeHiddenInputRef.value = postcode;
        countryHiddenInputRef.value = country;

        // sends the user's input to display in a Form Summary table before the final form is submitted
        $("#address_line1_table").text(addressLine1);
        $("#address_line2_table").text(addressLine2);
        $("#town_or_city_table").text(townOrCity);
        $("#county_table").text(county);
        $("#postcode_table").text(postcode);
        $("#country_table").text(country);

        // gets save-info value(true or false) if a user is authenticated(otherwise this field is hidden)
        let saveInfoExist = document.getElementById('id-save-info');
        if (saveInfoExist){
            let saveInfo = document.getElementById('id-save-info').checked;
            saveInfoHiddenInputRef.value = saveInfo;  
        }

        // activates the next tab on click, when the form-set is valid
        $('.nav-tabs .active').parent().next('li').removeClass("disabled");
        $('.nav-tabs .active').parent().next('li').find('a[data-toggle]').attr("data-toggle", "tab");
        $('.nav-tabs .active').parent().next('li').find('a').trigger('click');
    }
});

/**
 *  The method of triggering Next and GoBack buttons is taken and modified from the following source:
 * https://stackoverflow.com/questions/22297964/bootstrap-tabs-next-previous-buttons-for-forms/22298275
 */
  $('.btnGoBack').click(function() {
    $('.nav-tabs .active').parent().prev('li').find('a').trigger('click');
  });

});