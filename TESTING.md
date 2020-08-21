# Testing
## Manual Testing
Manual testing was conducted with each feature and user story on different screen resolutions, devices and in different browsers. Some results and the actions that took place during the manual testing phase are displayed below:
### Navbar, Search and Footer
- All links in the navbar and the footer were tested to ensure that they are pointing to the correct destination.
- On the smaller devices the **search** button collapses the search input box and redirects to the products page with correct results displayed. I've tried to submit an empty search query, the error appeared informing that no search word was entered. Also, I've tried to enter key that doesn't exist in the database to check if I get the paragraph telling that no results were found for the entered query.
- The hover effect on the nav-items was checked as well as the active page was highlighted correctly depending on which page I am currently on.
- In footer all the social media links lead to the corresponding pages and open in the new tabs.
### Landing page 
- The animation on scroll works as expected
- All the links lead to the correct pages
- All the image-carousels work properly
### About page
- Information is displayed correctly, animation on scroll and image gallery work as expected
### Events page 
- The data from the Events model is displayed correctly in the events table- Facebook link opens in the new tab leading to the main Facebook page (since there is no real page exists for the website)
### Contact
- I've tried to submit the empty form, or enter incorrect email address (without @), that led to the corresponding validation messages displayed. 
- If the form was valid and "Send" button clicked, I was redirected to the "Thank you" page, informing that the message was sent. As well as that, being an admin of the website, I received the real message on my email, that was assigned in the environment variables.
- Map on the contact page displays the correct location, the Info Window shows the opening hours, when the red marker is clicked. Zoom buttons also work correctly.
### Products and product details pages
- I tried to select the category, sorting results were displayed correctly, the number of the products found shown in parentheses. 
- Logged in as an admin I could see Edit/Delete buttons, while when I tried to manually enter the `/edit/` and `/delete/` urls I got the error message displayed as expected.
- Clicking the "View details" button or product image redirects to the products details page.
- Breadcrumbs navigation works correctly on both products and product detailes pages.
- On the product details page I tried to submit the form with negative number (or higher than 999), but got the validation error messages as expected.
- Clicking on the category leads to the Products page with the filtering by the selected category.
- If the quantity form is submitted correctly, I can see the grand total in the navbar reflects this addition. Toast success message is displayed as expected.
### Services and service details pages
- Edit/delete buttons on both pages are visible only for the admin of the store
- Clicking "Learn more" button redirects me to the service details page
- Contact us button redirects to the contact page
- I tried to submit empty form, leave the datetime field blank, put the incorrect number or datetime manually, after all these actions the validation errors were displayed not allowing me to submit the form with incorrect data.
- If the quantity form is submitted correctly, I can see the grand total in the navbar reflects this addition. Toast success message is displayed as expected.
- Bredcrumbs navigation works correctly on both services and service detailes pages.
- I added some itinerary items, page reloaded and I could see new itinerary item added and displayed. As well as that, I could remove the itinerary item by clicking the trash icon, toggling the delete modal and confirming the deletion. I tested this functionality from different accounts to make sure that only authenticated admin has an access to that.
### Cart page
- All the items added to the cart are displayed correctly.
- Clicking "Continue shopping" leads to the products page.
- I tested update/remove functionality with different products and services to make sure that everything works as expected. Clicking remove button toggles the remove modal asking to confirm the action. Update functionality works well for both products and services, subtotal changes correspondingly to reflect the update.
- Clicking "Checkout" button redirects to the Checkout page.
- Toast messages are displayed as expected after update/remove actions.
### Checkout and checkout success pages
- Order summary displays the order correctly, clicking "Edit cart" redirects back to the cart.
-I tried to submit an empty form or filled out incorrectly. The validation error messages were displayed correctly, not allowing to go to the next step before the current section is filled up with correct information.
- I created a large number of orders as logged in or non-logged in user, ticking or not the save-info checkbox. There was an issue with save-info field, that is described in the Bugs section and was successfully fixed.
- Also, I checked if the webhooks work as expected by temporary commenting out the part of `stripe.js` code that's responsible for submission and also by closing the page straight after clicking the "Proceed to payment" button. After that I checked the Stripe Dashboard to make sure that the order was created via webhooks and was saved to the database.
- 4242 4242 4242 4242 card number leads to the successfull payment.
- During testing of this feature I was always checking the Stripe dashboard to see if the charge was successfull.
- I tried to put the incorrect or incomplete card details to make sure that the error messages are displayed correctly.
- After the valid form was submitted, I received the confirmation email with all the correct order info. As well as that, the checkout page renders showing the order summary.
- When the order was completed by the logged-in user in the checkout success page, the "View full order history" button led to the Order history page.
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
Automated testing is implemented to support manual testing during the development process as required.   
Unit tests can be found in the `tests_models.py`, `tests_views.py`, `tests_forms.py` files of applicable applications within the repository.     
*Note:* The tests should be added in local database, as The Heroku hobby-tier does not give permissions to allow creation of databases that are required for python automated testing. To run the test and check the output, the database (Postgres) code configuration in `settings.py` should be temporarily removed or commented out.     
**Command used to tun the tests**:    
`python3 manage.py test`
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