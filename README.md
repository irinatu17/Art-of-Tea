# Art of Tea

"Art of Tea" - Full Stack Frameworks with Django Milestone Project

---


## Table of Contents
1. [**UX**](#ux)
    - [**Project Goals**](#project-goals)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)
3. [**Information Architecture**](#information-architecture)
    - [**Database Choice**](#database-choice)
    - [**Data Modelling**](#data-modelling)

4. [**Technologies Used**](#technologies-used)
    - [**Languages**](#languages)
    - [**Libraries and Frameworks**](#libraries-and-frameworks)
    - [**Tools**](#tools)
    - [**Databases**](#databases)

5. [**Testing**](#testing)
    - [**Manual Testing**](#manual-testing)
    - [**Validators**](#validators)
    - [**Compatibility**](#compatibility)

6. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)

7. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)
8. [**Disclaimer**](#disclaimer)

---

## UX

### Project Goals
#### Target Audience
- People who love tea
- People who want to get acquainted with tea culture
- People who want to organise a party in Chineese or Japaneese style, search for tea ceremony service
- People who want to get a new experiance, who curious about new things and want to get more knowldge about tea practise
- People who is interedted in Eastern culture in general
- People who want to buy tea and teaware, cary about good quality
- People who are into meditation, youga and similar practices   

#### Visitor/user goals:
- Purchase products/services shown on the website in a safe and secure way
- Read more about tea ceremonies and different aspects of drinking tea
- Organise the own custom tea event with special preferences

#### Business goals(site owner's goals):
- Provide users a secure professional e-commerce online shop
- Make profit from selling teas and tea ceremony services
- Promote tea culture in Ireland
- Make a brand more recognisable and expand the buisiness
### User Stories
:white_check_mark: *implemented*    

**As a user, I want/expect:**
- to access the website from any device (laptop, tablet, mobile)
- to easily navigate the website
- to read information about the business, its ideas and offers
- to learn more about different types of tea ceremonies, tea culture in general
- to view all the services and products information
- to view individual service/product details(e.g. image, price, quantity, description)
- being a new user, to create my own account
- being a returning user, to easily login/logout
- to reset my password if I forgot it 
- to have my personal profile with my personal information, needed for making payments
- to view my order history
- to be able to update my personal information, upload profile picture and delete it anytime
- to delete my account at any time
- to read reviews on the services/products
- to write my own review and to be able to edit/delete it
- to search and filter the products/services easily in order to buy a specific product I am looking for
- to sort all products/services by specific category
- to buy services/products: to be able to add them to my cart and to view my cart at any time
- to edit my cart and remove products/services from the cart 
- to view a total price of my purchases 
- to view delivery coast and to see how much more I need to spend to reach free delivery
- to make payments for the products/services by card in a safe and secure way
- to receive an email confirmation after checkout to make sure that payment was successfull
- to be able to read the company's private policy and delivery information
- to easily access social media links 
- to see the location of the company as well as its contact details
- to be able easily contact the owner/manager of the company if I have an additional query

**As a website owner, I want/expect:**
- to be able to add, edit and remove products/services
- to be able to be contacted by users through email if they have any special queries
### Design
#### Framework
#### Colour Scheme
#### Typography
#### Icons

#### Further styling decisions
### Wireframes

---

## Features
### Existing Features
:white_check_mark: *implemented*     

#### Home page
#### Navbar
#### Contact
#### Footer
#### Register account
#### Login
#### Logout
#### About Page
#### Services
#### Products
#### Single product details
#### Search
#### Cart
#### Checkout
#### Profile
#### Order history
#### Review
#### Admin Status
### Features Left to Implement

---
## Information Architecture
### Database choice
During the development phase I worked with **sqlite3** database which is installed with Django.   
For deployment, a **PostgreSQL** database is provided by Heroku as an add-on.

### Data Modelling
#### User
The User model used in this project is provided by Django as a part of defaults "django.contrib.auth.models". More information about Django’s authentication system can be found [here](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/).
#### Profile
#### Service/Ceremony
#### Product
| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Sku | sku | CharField | max_length=254
 Name | name | CharField | max_length=254 
 Description | description | TextField | max_length=500 
 Category | category | ForeignKey 'Category' | null=True, blank=True, on_delete=models.SET_NULL
 Price | price | DecimalField |max_digits=6, decimal_places=2 
 Rating | rating | DecimalField | max_digits=6, decimal_places=2, null=True, blank=True
 Weight | weight | IntegerField | null=True, blank=True
 Image1 | image1| ImageField | null=True, blank=True
 Image2 | image2| ImageField | null=True, blank=True
 Image3 | image3| ImageField | null=True, blank=True
 Availability | in_stock | Boolean | default=False
 
#### Category
#### Order
#### Review
#### 


---

## Technologies Used

### Languages
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) 
- [JavaScript](https://www.javascript.com/)
- [Python](https://www.python.org/) 
### Libraries and Frameworks
- [Django](https://www.djangoproject.com/) - Python framework for building the project.
- [Bootstrap](https://www.bootstrapcdn.com/) - as the front-end framework for layout and design.
- [Google Fonts](https://fonts.google.com/) - to import fonts.
- [FontAwesome](https://fontawesome.com/) - to provide icons used across the project. 
- [JQuery 3.5.0](https://jquery.com/) - to simplify DOM manipulation and to initialize Bootstrap functions.

### Tools
- [GitPod](https://www.gitpod.io/) - an online IDE for developing this project.
- [Git](https://git-scm.com/) - for version control.
- [GitHub](https://git-scm.com/) - for remotely storing project's code.
- [PIP](https://pip.pypa.io/en/stable/installing/) - for installation of necessary tools.
- [Jinja 2.10.1](https://jinja.palletsprojects.com/en/2.10.x/) - templating language for Python, to display back-end data in HTML.
- [Heroku](https://heroku.com/) - to host the project.
- [Stripe](https://stripe.com/ie) - to handle financial transactions.
- [AWS S3 Bucket](https://aws.amazon.com/) -  to store static files required on the site.
- [Gunicorn](https://pypi.org/project/gunicorn/) - a Python WSGI HTTP Server to enable deployment to Heroku.
- [Psycopg2](https://pypi.org/project/psycopg2/) - to enable the PostgreSQL database to function with Django.
- [Travis](https://travis-ci.org/) - for integration testing.
- [Coverage](https://coverage.readthedocs.io/en/coverage-5.1/) - 
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - to custom-style Django forms.
- [TinyPng](https://tinypng.com/) - for compressing images.
- [ImgBB](https://imgbb.com/) - to host images.
- [GIMP2](https://www.gimp.org/) - for editing and resizing images.
- [Balsamiq](https://balsamiq.com/) - to create wireframes.

### Databases
- [SQlite3](https://www.sqlite.org/index.html) - a development database.
- [PostgreSQL](https://www.postgresql.org/) - a production database.
---


## Testing
### Manual Testing

### Validators

### Compatibility

---

## Deployment
### Local Deployment

### Remote Deployment

---

## Credits

### Content
### Media
### Code

---
### Acknowledgements

## Disclaimer
