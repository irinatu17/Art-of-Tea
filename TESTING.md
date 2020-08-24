# Testing
 1. [**Manual Testing**](#manual-testing)
 2. [**Automated Testing**](#automated-testing)
 3. [**Validators**](#validators)
 4. [**Compatibility and Responsiveness**](#compatibility-and-responsiveness)
 5. [**Bugs**](#bugs)
## Manual Testing
Manual testing was conducted with each feature and user story on different screen resolutions, devices and in different browsers.  
### Responsiveness
- **User story being tested**:       
*As a user, I expect to access the website from any device, so that I can use the website anytime and anywhere.*
- **Test implementation**:
    - check each page of the website from multiple devices and multiple browsers
    - open the website in the Google Dev Tooles and click on "Responsive" to check all pages for all resolutions from 320px and above
    - more detailed information about responsiveness testing can be found in [Compatibility and Responsiveness](#compatibility-and-responsiveness) section
- **Results**: Some minor responsiveness issues were found (e.g. in the landing and events pages) and fixed by adding media queries, adjusting some box model components, adding some Bootstrap utilities for layout.   
- **Verdict**: The issues were fixed, the test passed.

### Navbar
- **User story being tested**:      
*As a user, I expect to easily navigate the website, so that I can quickly find what I'm looking for.*
- **Test implementation**:
    - click on all the links in the navbar, to check if they work properly pointing to the correct destination
    - check all links on the different devices (navbar looks different for mobile, tablet and desktop screens)
    - on mobile devices make sure that navbar is collapsed and the side bar shows up when the hamburger menu is clicked 
    - scroll down the page to see if the navbar is visible for a user all the time
    - on the large devices hover over the links to see if the highlighted effect (change colour to green and expand) works properly
    - check if the active page was highlighted correctly(active link's colour changes to green) depending on which page a user is currently on
    - on the smaller devices the search button collapses the search input box and redirects to the products page
    - test the navbar being non-logged in, logged in and admin user and to see if the user's status is reflected in the navbar links (login|register - for guests users, my profile, order history, logout - for all logged in users, for admin additional link - product management)
    - check when an item is added to the cart, a cart icon's colour changes to yellow and a badge with cart total appears, the total updates each time new item is added or deleted from the cart
- **Results and Verdict**: Test passed. All the functionality works as expected, no bugs were found during the testing.

### Footer
- **User stories being tested**:     
*As a user, I want to easily access social media links of the company, so that I can read more information about it.*     
*As a user, I expect to easily navigate the website, so that I can quickly find what I'm looking for.*
- **Test implementation**:
    -  click on the social media icons to check if they lead to the corresponding pages and open in the new tabs 
    -  check if GitHub and LinkedIn icons open my profiles, while Instagram and Facebook icons open the main pages (as it's an educational project and there are no real pages exist)
    - check different devices to test if the footer id displayed correctly (with additional top section on large resolutions)
    - on large resolution, click on all the links in the footer (Quick links section, logo), to check if they work properly pointing to the correct destination
    - hover over the links and social media icons to test if the hover effect is working properly
- **Results and Verdict**: Test passed. All the functionality works as expected, no bugs were found during the testing.

### Search bar
- **User story being tested**:     
*As a user, I want to search and filter the products easily, so that I can quickly find a specific product I am looking for.*
- **Test implementation**
    - enter any search word into the search box to see if it redirects to the products page with correct results displayed
    - submit an empty search query without entering anything
    - enter some search words that expected to be found in the website (e.g. "matcha", "green", "teapot")
    - enter some search words that not expected to be found in the website, from totally different areas (e.g. "coding", "microbiology") or just random letters/numbers
    - make search queries from different pages to make sure it works accross all the website
 - **Results**:       
    - when an empty form is submitted without any queries, the error message appeares informing that no search word was entered
    - if the search query exists in the database, the products page renders, displaying the search word, number of the results found and all products that satisfy the query
    - if the search query does not exists in the database, the products page renders, displaying the search word, numer of results equal to 0 and a paragraph telling that no results were found for the entered query
    - search box works accross all the app, no matter which page a user is currently on
 - **Bugs found and fixed**: After refactoring the delete products admin functionality and adding *Discontinued* field (described more detailed in the corresponding section), the search number of results showed the total number of all products including the out of stock, discountinued products. To fix that, an if statement was added to the `def all_products`:     
 `active_products = all_products.filter(discontinued=False)`     
So after that the query functionality is being applied only to the active products, that are in stock. The bug was successfully fixed. 
 - **Verdict**: The bug is fixed. Test passed.
 
### Landing page 
- **User story being tested**:     
*As a user, I want to read a summary info about the business, its ideas and benifits, so that I can quickly decide if it satisfies my needs.*
- **Test implementation**:
    - click all the buttons accross the page
    - scroll down the page to check the animation on scroll (AOS)
    - ckeck all the image-carousels and reviews-carousel by clicking on chevrons
    - verify that the expected text, icons and  images are displayed 
 - **Results**:
    - all the buttons redirect to the corresponding pages (About, Services, Products, Events and Contact)
    - the hover effect on buttons works as expected(expanding, checnging background colour)
    - animation on scroll works as expected on all sections and across all devices
    - image and review carousels display correctly when chevrons are clicked
    - all the text sections, icons and all the images display correctly, changing the position, size when viewed on different screens
- **Verdict**: Test passed. All the functionality works as expected, no bugs were found during the testing.

### About page
- **User story being tested**:     
*As a user, I want to find an information about the company, to know what they do, what their main principles and ideas*
- **Test implementation**:
    - verify that the expected text is displayed correctly
    - check that the correct images are displayed for each of the sections 
    - scroll down the page to check the animation on scroll (AOS)
    - ckeck the image-carousel in the "Our mission" section by clicking on chevrons
- **Results**:
    - all the text sections are displaied correctly on different screens
    - all images are are displaied correctly, the position, layout changes on different screens as expected
    - animation on scroll works as expected on all sections and across all devices
    - an image carousel works correctly when chevrons are clicked
- **Verdict**: Test passed. All the functionality works as expected, no bugs were found during the testing.

### Events page 
- **User story being tested**:     
*As a user, I want to view events that happen in the tea club this week in Dublin, so that I can come and join any event.*
- **Test implementation**:
    - verify that images are displayed correctly
    - verify that the data from the Events model is displayed correctly in the events table
    - scroll down the page to check the animation on scroll (on the text an teapot image)
    - click on the Facebook link 
- **Results**:
    - all the images and texts are displaied correctly on different screens
    - animation on scroll works as expected on all sections and across all devices
    - Facebook link opens in the new tab leading to the main page (since there is no real page exists for the website)
- **Verdict**: Test passed. All the functionality works as expected, no bugs were found during the testing.

### Contact
- **User stories being tested**:     
*As a user, I want to see the location of the Tea Club on a map, so that I can find the address easily and come to the advertised events.*      
*As a user, I want to be able to easily contact the owner/manager of the company, so that I can write an additional query or ask a question.*    
**Admin**: *As a user, I want to receive emails from the users when they fill out the contact form, so that I can reply on them satisfying users queries.*
- **Test implementation**:
    - check that a graphic image is displayed only on the large screen
    - try to submit an empty Contact form
    - try to enter incorrect email address (without @)
    - try to submit the form with all valid information
    - check the contact form as authenticated user to see if the full name and email fields are pre-populated
    - check the map, clicking on the red marker, zoom controllers
- **Results**:
    - the image and contact information are displaied correctly on different screens
    - after attempts to submit invalid form (empty or invalid informations) corresponding validation messages appears to prevent the submission
    - if the form was valid and "Send" button clicked, a user is redirected to the "Thank you" page, informing that the message was sent
    - if the form was submitted successfully, an admin of the website received the real message on the email (it is assigned in the environment variables as EMAIL_HOST_USER)
    - if the user is authenticated, the email field is always pre-populated
    - if the user is authenticated and has the full name is saved in the Profile information, the full name is pre-populated in the contact form
    - map on the contact page displays the correct location, the Info Window shows the opening hours, when the red marker is clicked. Zoom controllers also work correctly.
    - after successfull contact form submission, admin of the store receives the message on their personal email, getting user's email and full name, so an admin can answer the query directly to the user's email
- **Verdict**: Test passed. All the functionality works as expected, no bugs were found during the testing.

### Products and product details pages
- **User stories being tested**:     
*As a user, I want to view product details (e.g. image, price, description), so that I can buy some of them.*    
*As a user, I want to search and filter the products easily, so that I can quickly find a specific product I am looking for.*
- **Test implementation**:
    - verify that the expected text and images are displayed correctly in both products and product details pages
    - select the category, clicking on the category-links (e.g. Teaware, Black Tea) in the all products page
    - login with superuser credentials and verify that the Edit/Delete buttons appear in both products and product details pages under the image
    - being a guest or logging in as a regular user, try manually enter the `/edit/` and `/delete/` urls 
    - click on the "View Details" button and on the product image on the all prodcuts page
    - click on different Breadcrumbs links
    - click on the "Add to Cart" button on the both products and product details pages
    - on the products page try to enter a negative or higher than 999 number in the quality form and click on "Add to cart" button
    - enter the quantity in the range of 1-999 and click on the "Add to cart" button
    - on the product details page click on the "Products" button
    - on the product details page click on the category
    - on the product details page click on the product's image    
- **Results**:
    - the texts, icons and images are displaied correctly on different screens
    - after selecting the certain category, sorting results were displayed correctly, the number of the products found shown in parentheses as well as the selected category
    - Edit/Delete buttons are visible only to the superuser
    - after manually entering the `..products/edit/<prduct_id here>` and `..products/delete/<prduct_id here>` urls, the error messages were displayed as expected.
    - clicking the "View details" button or product image redirects to the products details page.
    - clicking the "Add to cart" button on the all products page, adds the product to the cart with quantity of 1; clicking it again increases the quantity by 1 and updates the cart
    - Breadcrumbs navigation works correctly on both products and product detailes pages.
    - after submission the  ivalid quantity form (when a number is negative or higher than 999), the validation error messages appeared as expected.
    - if the quantity form is submitted correctly, the grand total in the navbar reflects this addition. Toast success message appeared as expected.
    - clicking on the "Products" button redirects to the all products page as expected
    - on the product details page clicking on the category leads to the all products page with the filtering by the selected category.
    - clicking on the image on product details page opens an image in a new tab (if an image URL was assigned, as it's an optional field) as expected
- **Bugs found and fixed**: the bug with searching/filtering products (discontinued products were counted in the filtering results) is described in the [Search bar](#search-bar) section.
- **Verdict**: Test passed. All the functionality works as expected, the bug was fixed.

### Services and service details pages
- **User stories being tested**:     
*As a user, I want to learn more about different types of tea ceremonies, so that I can choose and book one of the tea ceremonies.*     
*As a user, I want to view service details (e.g. image, price, description), so that I can book one.*
- **Test implementation**:
    - verify that the expected text and images are displayed correctly in both service and service details pages
    - scroll down the page to check the animation on scroll (AOS)
    - login with superuser credentials and verify that the Edit/Delete buttons appear in both service and service details pages
    - being a guest or logging in as a regular user, try manually enter the `/edit/` and `/delete/` urls 
    - click on the "Learn more" button on the services page
    - click on the "Contact us" button at the bottom of the services page
    - click on different Breadcrumbs links
    - on the services details page try to enter a negative or higher than 100 number in the Number of participants field and click on "Add to cart" button
    - enter the Number of participants in the range of 1-100 and click on the "Add to cart" button
    - check that datatime picker works correctly, unabling to pick only the dates in the future
    - try to submit the form with empty Number of participants and/or Date and Time fields
    - on the product details page click on the "Services" button
    - on the product details page click on the product's image 
    - login with superuser credentials and add fill out the itinerary form. Check an admin panel to see if an itinerary item was added
    - login with superuser credentials and click on the trash icon, removing an itinerary form. Check an admin panel to see if an itinerary item was deleted
    - test itinerary item create/delete functionality from different accounts to make sure that only authenticated admin has an access to that.
- **Results**:
    - the texts, icons and images are displaied correctly on different screens
    - animation on scroll works as expected on all service cards across all devices
    - Edit/Delete buttons are visible only to the superuser
    - after manually entering the `../services/edit/<service_id here>` and `../services/<prduct_id here>` urls, the error messages were displayed as expected.
    - clicking the "Learn more" button redirects to the service details page.
    - "Contact us" button redirects to the contact page
    - Breadcrumbs navigation works correctly on both services and service detailes pages.
    - after submission an empty or ivalid form (when a number is negative or higher than 100), the validation error messages appeared as expected.
    - if the form is submitted correctly, the grand total in the navbar reflects this addition. Toast success message appeared as expected.
    - clicking on the "Services" button redirects to the servicess page as expected
    - clicking on the image on service details page opens an image in a new tab (if an image URL was assigned)
    - itinerary items manipulations available only to the superuser
    - after adding an itinerary items, page reloads and a new itinerary item added and displayed as expected.
    - after removing an itinerary item by clicking the trash icon, the delete modal is toggled asking an admin to confirm the deletion. Clicking "Delete" button in the model will delete the itinerary item from the database and reload the page, the info toast message appears informing about the deletion.
- **Verdict**: Test passed. All the functionality works as expected, no bugs were found during the testing.
    
### Cart page
- **User stories being tested**:     
*As a user, I want to view and modify my order in the cart before completing it, so that I can make last changes easily before proceeding to payment.*     
*As a user, I want to view a total price of my purchases and delivery cost, so that I will understand and see how much I will be charged.*
- **Test implementation**:
    - verify that the text and images of the added items are displayed correctly 
    - click on the "Continue shopping" link at the top of the page
    - try to update the item quantity/number of participants and datatime (for services) with different products and services
    - try to manually enter invalid quantity(negative or grater that 999)
    - click on the red trash icon(remove button)
    - click on the "Checkout" button
    - remove all the items and check the empty cart, click on the "Go shopping" button
- **Results**:
    - all the items' information is displaied correctly on different screens
    - clicking "Continue shopping" link leads to the products page
    - update functionality works well for both products and services (the bug during the resting was found and fixed, see **bugs** paragraph below)
    - clicking remove button toggles the remove modal, asking to confirm the action. After clicking "Remove" button, the page reloads, the item is removed and the toast message confirms the deletion
    - subtotal changes correspondingly to reflect the update/remove
    - cicking "Checkout" button redirects to the Checkout page.
    - toast messages are always displayed as expected after each update/remove action
    - if the cart is empty, the paragraph informs a user that the cart is empty; clicking "Go shopping" button redirects to the products page
 - **Bugs found and fixed**: 
 - **Verdict**: The bug was fixed, all the functionality works as expected. Test passed. 

### Checkout and checkout success pages
- **User stories being tested**:     
*As a user, I expect to make payments by card in a safe and secure way, so that I won't be concerned about the safety of my card details and won't be charged incorrectly.*      
*As a user, I want to receive an email confirmation after checkout, so that I can make sure that payment was successfull.*      
- **Test implementation**:
     - verify that the text and images(Order summary) are displayed correctly 
     - click on the "Edit cart" link
     - try to submit an empty field set (check each section- Personal details, Shipping Info and Payment)
     - try to put an incorrect information (e.g. email without @)
     - create a large number of orders as logged in and non-logged in user, ticking or not the save-info checkbox.
     - in the Payment section enter **4242 4242 4242 4242** card number, any expiration date in future and any CVC, and then click on the "Proceed to payment" button (this was also checked on Stripe Dashbord to see if the order was created)
     - try to enter different and incomplete card numbers, the expiration date in the past to check the error messages
     - temporary comment out the code line `form.submit();` in `stripe.js` file and then try to submit the form clicking the "Proceed to payment" button. After that check the Stripe Dashboard and also Order model in Admin panel to make sure the order was created via webhooks and was saved to the database.
- **Results**:
    - order summary displays the order correctly
    - clicking "Edit cart" redirects back to the cart.
    - if an empty form was submitted or filled out incorrectly, the validation error messages were displayed correctly, when the "Next" button is clicked, not allowing to go to the next step before the current section is filled up with correct information.
    - when an order is created by non-authenticated user, the save-info checkbox is hidden from the view, instead the links to the Create account and Login pages are displayed offering a user to login to save the information and the order to the order history. 
    - if an authenticated user ticks the save-info checkbox, all the personal and shipping information is saved to their profile. There was an issue with the save-info field found during testing, that is described in the Bugs section and was successfully fixed
    - 4242 4242 4242 4242 card number leads to the successfull payment, that was confirmed in the Stripe Dashboard.
    - if the incorrect or incomplete card details were entered, the error messages are displayed as expected under the Payment field.
    - when the order was created via webhooks (after commenting out `form.submit();` in `stripe.js`), the payment was successfully proceeded and the order was saved in the database
    - after the valid form was submitted, the confirmation email was recieved in the email provided with all the correct order info. As well as that, the checkout page renders showing the order summary.
    - when the order was completed by the logged in user in the checkout success page, the "View full order history" button redirects to the Order history page. "Keep shopping" button is displayed for both non-logged in and logged in users and redirects to the products page
 - **Bugs found and fixed**: 
 - **Verdict**: The bugs were fixed, all the functionality works as expected. Test passed. 

### Profile and Order History
- These features were tested to check if they are available only to the logged-in users.
- Clicking on the Order number on the order history page opens the past confirmation (checkout success) page with the corresponding toast info message.
- Profile page displayes all the personal info (email and username), clicking on the "Change password" and "Manage emails" buttons leads to the correct destinations.
- If all the shipping information on the profile page was deleted, then on the checkout page all the fields were empty. At the same time when I saved some shipping details on the profile page, the checkout form fields were prefilled, confirming that the shipping info was saved into the Profile model.
### Admin product management functionality
- Add product/service forms work as expected: validation error messages in place, after successfull addition it redirects to the new created product/service page.
- I added few products/services without the image to test the no-image assignment.
- In production all images are stored in the AWS S3, so the Basket was constantly checked to make sure it works as expected.
- Edit/Delete functionality was tested many times, all the changes straight away can be seen in the database.
- The defensive design worked well allowing only superuser to have an access to this functionality.
### Login/sign up/logout/forgot password
These features are built-in components of Django allauth package were tested manually as well, as about 5-10 different accounts were created.     
Forgot password, verification email, login - all work as expected.
- Entering incorrect emails, incorrect password and case sensitivity works as expected.
- Trying to register with an already registered email works as expected.
- Entering two different passwords and trying to enter old password when re-setting password works as expected.
- Registration and login pages are only available to anonymous users.

## Automated Testing
Automated testing is implemented to support manual testing during the development process.   
Unit tests can be found in the `tests_models.py`, `tests_views.py`, `tests_forms.py` files of applicable applications within the repository.     
*Note:* The tests should be added in local database, as The Heroku hobby-tier does not give permissions to allow creation of databases that are required for python automated testing. To run the test and check the output, the database (Postgres) code configuration in `settings.py` should be temporarily removed or commented out.     
- **Command used to run the tests**:    
`python3 manage.py test`   
- To run the tests within a specific app only:
`python manage.py test <app name here>`
### Travis
[Travis](https://travis-ci.org/) was also used throughout the unit testing of this project to provide continuous integration with the deployed site when pushing code to GitHub. It is configured via the `.travis.yml` file. All information about how to set it up can be found in [Travis Documentation](https://docs.travis-ci.com/).
## Validators
### HTML
All the HTML files were tested through [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input). Since it does not recognize Jinja2 templating language, it showed a number of errors. Apart from that, no other errors were found across the html pages.   
### CSS
CSS files were tested through [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). Since it does not recognize CSS variables (I use :root{} for colours and fonts variables), there were several Parse Errors found.
As well as that, there are a few error warnings for some -webkit, -moz pseudo element selectors. Both errors can be safely ignored as they are not errors in fact. The rest of the CSS files was completely valid.   
### JavaScript
JS file was tested through [Esprima](https://esprima.org/demo/validate.html) and [JSHint](https://jshint.com/) validators, code was syntactically valid. "$" was not defined by JSHint (it is necessary for jQuery Materialize initializing).    
### Python
All python files were tested through [PEP8 Online](http://pep8online.com/) validator and further changes were made to make the code PEP8 compliant.

## Compatibility and Responsiveness
This website had been being tested during the development across **multiple browsers** (Chrome, Safary, Opera, FireFox, Internet Explorer) and on **multiple devices**: mobile (iPhone 5, 6, 8, Samsung Galaxy, Sony Xperia), tablets(iPad, iPadPro) and laptops (with HiDPI and MDPI and touch screens).              
Also, the following tools were used to constantly test the project:
- **Google Chrome's developer tools** to see how it looks across all the different device screen sizes to ensure compatibility and responsiveness.       
-  [Am I Responsive](http://ami.responsivedesign.is/) and [Responsinator](http://www.responsinator.com/) online tools for checking responsiveness on different devices.
Plenty of changes were made and necessary media queries added to make the website is fully responsive.        
The website renders poorly on Internet Explorer browser (as it is outdated). However, the website renders well as expected on all the other browsers.

## Other Testing 
- The app was constantly testing with **debugger** locally: `debug=True` throughout all the development process. Every time when there was an error (when app crashed), the debugger displayed an error message to the view, that allowed me to find the location of the error and fix it.
- I also asked my friends, family members and fellow students in Slack to thoroughly test my website in different devices, try to break it and to give me a feedback about the design, functionality and their user experience. Some further improvement took placed to enhance UX after this testing phase.

## Bugs
### Save info field
During the testing phase in production there was found an issue with save_info checbox: despite not being ticked(meaning that a user does not want to save the shipping information to the profile), it always saved that information. As the first two steps of the Checkout form are handling via JavaScript, its "true" and "false" values were not recognisable by Python(were not equal to True and False).     
To fix that few additional line od code was added to 
-  **stripe.js** file:    
`var saveInfo = document.getElementById('save_info').value;`
- **checkout/views.py** file:
```bash 
if request.POST['save_info'] == "true":
                request.session['save_info'] = True
            else:
                request.session['save_info'] = False
```   

Now first I get the value of "save_info" field, if it's equal to "true" I assign it as True, if "false" - to False. The issue was successfully solved.
 - As well as that, I had an issue with non-logged in user. The save info field is visible only for authenticated users, so if it's a guest it's should be set to None.
Therefore the following line was added to the **webhook_handler.py** file:    
`save_info = intent.metadata.save_info if hasattr(intent.metadata, 'save_info') else None`  

### Comment field
Similar to the save_info field, I got an issue with optional comment field when the form was handled via webhooks. If the comment field was empty, that throw an error and didn't save the order properly in the database. The problem was that if the field was empty, it wasn't set as None, so adding the following line successfully solved the issue:    
`comment = intent.metadata.comment if hasattr(intent.metadata, 'comment') else None`     


[Back to README](https://github.com/irinatu17/Art-of-Tea/blob/master/README.md#testing)
