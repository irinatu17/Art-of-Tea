$(document).ready(function() {
    // Personal Details form, step 1
const personalDetailsForm = document.querySelector('#personal-details-form');
const submitButton = document.getElementById('personal-details-btn');
let personalDetailsFormValid;
 var $tabs = $('#nav-tab li');


submitButton.addEventListener('click', () => {
    personalDetailsFormValid = personalDetailsForm.checkValidity();
    
    if (personalDetailsFormValid) {
        //$('.nav-tabs .active').parent().next('li').find('a').trigger('click');
        let name = document.getElementById('id_full_name').value; 
        let email = document.getElementById('id_email').value;  
        let phoneNumber = document.getElementById('id_phone_number').value; 

        let nameInput = document.getElementById('full_name').value = name;
        let emailInput = document.getElementById('email').value = email;
        let phoneNumberInput = document.getElementById('phone_number').value = phoneNumber;
        function showPrev() {
            $('.nav-tabs .active').parent().next('li').removeClass("disabled");
            $('.nav-tabs .active').parent().next('li').find('a[data-toggle]').each(function () {
            $(this).attr("data-toggle", "tab");
            });

            $('.nav-tabs .active').parent().next('li').find('a[data-toggle="tab"]').tab('show');

            $tabs.filter('.active').next('li').find('a[data-toggle="tab"]').each(function () {
                $(this).attr("data-toggle", "").parent('li').addClass("disabled");        
            })
        }
    }
});

// Shipping Info form, step 2
const shippingInfoForm = document.querySelector('#shipping-info-form');
const submitButton2 = document.getElementById('shipping-info-btn');
let shippingInfoFormValid;

submitButton2.addEventListener('click', () => {
    let shippingInfoFormValid = shippingInfoForm.checkValidity();

    if (shippingInfoFormValid) {

        // grab input values and store in variables
        let addressLine1 =  document.getElementById('id_address_line1').value;
        let addressLine2 =  document.getElementById('id_address_line2').value; 
        let townOrCity =  document.getElementById('id_town_or_city').value;
        let county =  document.getElementById('id_county').value; 
        let postcode =  document.getElementById('id_postcode').value; 
        let country =  document.getElementById('id_country').value; 
        let saveInfo = Boolean($('#id-save-info'));

       // let saveInfo = document.getElementById('id-save-info').value; 
       
        $('.nav-tabs .active').parent().next('li').find('a').trigger('click');


        let addressLine1Input = document.getElementById('address_line1').value = addressLine1;
        let addressLine2Input = document.getElementById('address_line2').value = addressLine2;
        let townOrCityInput = document.getElementById('town_or_city').value = townOrCity;
        let countyInput = document.getElementById('county').value = county;
        let postcodeInput = document.getElementById('postcode').value = postcode;
        let countryInput = document.getElementById('country').value = country;
        let saveInfoInput = document.getElementById('save_info').value = saveInfo;

        console.log(saveInfoInput)

    }
});
// add the values to hidden inputs in the final form and submit 



// The method of triggering Next and GoBack buttons is taken and modified from the following source:
// https://stackoverflow.com/questions/22297964/bootstrap-tabs-next-previous-buttons-for-forms/22298275
  $('.btnGoBack').click(function() {
    $('.nav-tabs .active').parent().prev('li').find('a').trigger('click');
  });

});