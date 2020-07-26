$(document).ready(function() {

// Personal Details form, step 1
const personalDetailsForm = document.querySelector('#personal-details-form');
const submitButton = document.getElementById('personal-details-btn');
let personalDetailsFormValid;

// handles the validation of the first(Personal details) step of the form when "Next" button is clicked
submitButton.addEventListener('click', () => {
    personalDetailsFormValid = personalDetailsForm.checkValidity();
    
    if (personalDetailsFormValid) {
        //if valid,  gets the values of the first fieldset
        let name = document.getElementById('id_full_name').value; 
        let email = document.getElementById('id_email').value;  
        let phoneNumber = document.getElementById('id_phone_number').value; 

        // store those values and add them to hidden inputs in the final form to submit
        let nameInput = document.getElementById('full_name').value = name;
        let emailInput = document.getElementById('email').value = email;
        let phoneNumberInput = document.getElementById('phone_number').value = phoneNumber;

        // send the user's input to display in a Form Summary table before the final form is submitted
        let fullNameTable = $("#full_name_table").text(name);
        let emailTable = $("#email_table").text(email);
        let phoneNumberTable = $("#phone_number_table").text(phoneNumber);

        // activate the next tab on click, when form-set is valid 
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
    let shippingInfoFormValid = shippingInfoForm.checkValidity();

    if (shippingInfoFormValid) {
        //if valid,  gets the values of the second fieldset
        let addressLine1 =  document.getElementById('id_address_line1').value;
        let addressLine2 =  document.getElementById('id_address_line2').value; 
        let townOrCity =  document.getElementById('id_town_or_city').value;
        let county =  document.getElementById('id_county').value; 
        let postcode =  document.getElementById('id_postcode').value; 
        let country =  document.getElementById('id_country').value; 

        // store those values and add them to hidden inputs in the final form to submit
        let addressLine1Input = document.getElementById('address_line1').value = addressLine1;
        let addressLine2Input = document.getElementById('address_line2').value = addressLine2;
        let townOrCityInput = document.getElementById('town_or_city').value = townOrCity;
        let countyInput = document.getElementById('county').value = county;
        let postcodeInput = document.getElementById('postcode').value = postcode;
        let countryInput = document.getElementById('country').value = country;

        // send the user's input to display in a Form Summary table before the final form is submitted
        let addressLine1Table = $("#address_line1_table").text(addressLine1);
        let addressLine2Table = $("#address_line2_table").text(addressLine2);
        let townOrCityTable = $("#town_or_city_table").text(townOrCity);
        let countyTable = $("#county_table").text(county);
        let postcodeTable = $("#postcode_table").text(postcode);
        let countryTable = $("#country_table").text(country);


        // get save-info value(true or false) if the user is authenticated
        let saveInfoExist = document.getElementById('id-save-info');
        if (saveInfoExist){
            let saveInfo = document.getElementById('id-save-info').checked;
            let saveInfoInput = document.getElementById('save_info').value = saveInfo;  
        }

        // activate the next tab on click, when form-set is valid
        $('.nav-tabs .active').parent().next('li').removeClass("disabled");
        $('.nav-tabs .active').parent().next('li').find('a[data-toggle]').attr("data-toggle", "tab");
        $('.nav-tabs .active').parent().next('li').find('a').trigger('click');
    }
});

// The method of triggering Next and GoBack buttons is taken and modified from the following source:
// https://stackoverflow.com/questions/22297964/bootstrap-tabs-next-previous-buttons-for-forms/22298275
  $('.btnGoBack').click(function() {
    $('.nav-tabs .active').parent().prev('li').find('a').trigger('click');
  });

});