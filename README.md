# Mark McClean

## Milestone Project 4 – Full Stack Frameworks

## Route Share – Django application

### Table of Contents
* [Why make Route Share?](#Why-make-Route-Share)
* [How the website works](#How-the-website-works)
* [UX: Strategy](#UX-Strategy)
* [Scope](#Scope)


### Why make Route Share?

For the fourth milestone project I decided to build an application where users can find new bicycle routes as well as adding and sharing their own favourite routes, therefore building up a community of users that expand the database of routes. 

Due to a recent foot injury which restricts my ability to exercise on foot, I bought a road bike and for the past few months have been enjoying a new lease of life with a new form of exercise that has no effect on my foot injury. 

During this time I have found myself trying to come up with all different routes in and around the area where I live using Google Maps. That’s when I thought it would be a good idea to create an application where cyclists can share and view each other’s favourite routes. 

### How the website works

Users will initially arrive at the home page which will consist of an extensive menu at the top with options to search for, view and filter routes along with login/sign up options and a link to view the users profile. 

Below the menu will be a callout section consisting of 2 large buttons to get the users attention. A ‘View Routes’ button and a ‘Sign in/Sign Up’ button. 

There will be limited functionality for users who are not yet signed up. They will be able to look through the routes, using the search, sort and filter options but will be unable to see full details of the routes or the route itself unless they have signed up and paid for some form of membership. 

There will be 3 layers of membership: 

- A free trial membership allowing members to view one full route detail and map before being restricted again. The user will also have unlimited uploading of routes 

- A limited membership that costs €4.99/month and allows the user to view 5 routes/month. The user will also have unlimited uploading of routes 

- An unlimited membership for €9.99/month that allows full unlimited access to all routes on the site. The user will also have unlimited uploading of routes 

The routes will be displayed in a grid with enough information to enable the user to choose a route that is useful for them. For example they can view the country and area of the route, the length and bicycle type, and a description of the route. Users will also have the ability to upload a photo with their route to enhance the appeal to other users although this will not be required. 

When a user wants to get a route, they first need to click on that route in the grid which links to a new page with further details of the route and in that page there will be a ‘Reveal Route’ button that will enable the user to see the Google Map link where they can open the route. This will be dependent on the current conditions of the users membership. 

For uploading routes there will be some instructions on the site about how users can do that but basically they will have to first create their route in Google maps and copy the URL from Google maps into the upload route form so it can be stored in the database. 

### Technical Details

The application was built using Django 3 and follows a good practise architecture pattern of model-template-view. The application also uses ‘Separation of Concern’ for the apps created within the project to utilise the Django framework effectively. 

Within the development environment sqlite is the default database used along with Django. For the deployment of the site Heroku was used and I switched to a Postgres database which is easily set up through the Heroku dashboard. All data from the sqlite database is then transferred to the Postgres database so the deployed version enjoys all the benefits of the development version. 

There is also an Admin side to this application where the site owner will be able to have CRUD (Create, Read, Update and Delete) functionality through a built in Django admin interface. For the site owner a superuser account is created during the development process so only they can access this interface. This user interface is also customisable to the owner’s needs and allows the owner to adjust records outside of the main user interface ie. the website itself. 

Git and Github are used for version control and Heroku for the full deployment of the site. All project secret keys are stored in the Gitpod Environmental Variables in the settings menu. For deployment these are then stored in the Config. Variables of the Heroku dashboard. This is to keep them hidden to protect the integrity and security of the application.

[↥ Back to top](#Mark-McClean)


## UX: Strategy

### Primary Target Audience

The target audience is for cyclists of all kinds. Regardless of what type of bike you have, there will be routes to enjoy for everyone from leisure bikes, road bikes and mountain bikes. This will be particularly useful for people new to the cycling world, who otherwise have little knowledge of available cycle routes where they live. 

### Appropriate Content

I think it would be appropriate to have many beautiful images of cyclists on the website to give off a feel of excitement and adventure to the potential users. I plan to have a home page with several images below each other separated by some small paragraphs about the website’s content. Some of the other pages will also have striking images to help maintain the theme and feel of the website overall. The users who upload routes also have the opportunity to attach a photo to the route which also adds to the visual aspect of the site and the display of the routes. There will also be a dark theme to the navbar, footer and several buttons along with an orange aspect for the primary buttons. 

Appropriate content also includes giving the users clear instructions on how to use and manage all aspects of the site and ensuring a seamless use of all functions like instructions on how to create the route and paste into the route upload form.

### Why this website?

As I briefly mentioned earlier I have recently taken up cycling with a road bike and am very much enjoying it but I’m always looking for new routes. I thought that a website where people can share and views other people favourite routes would be a good idea.

I have also recently read that, especially since the Covid-19 crisis, cycling has become very popular in many countries. It is a great form of exercise which can be done alone or in small (socially distanced) groups. With this growing popularity people will always be looking for more resources to find routes and this could be a very useful application for many cyclists.

[↥ Back to top](#Mark-McClean)


## Scope

### User Stories

|     Story #    |     User Type            |     Activity                        |     Goal                                                 |     Reason                                                                              |
|----------------|--------------------------|-------------------------------------|----------------------------------------------------------|-----------------------------------------------------------------------------------------|
|     1          |     Member/non-member    |     Viewing & Navigation            |     View a list of routes                                |     To find a suitable cycle route                                                      |
|     2          |     Member/non-member    |     Viewing & Navigation            |     View route details                                   |     To get more information on the route                                                |
|     3          |     Non-member           |     Viewing & Navigation            |     View membership options                              |     To choose the correct membership for myself                                         |
|     4          |     Non-member           |     Viewing & Navigation            |     To see I’ve selected a membership to purchase        |     Incase I forget to follow the purchase procedure                                    |
|     5          |     Member               |     Viewing & Navigation            |     Instructions on how to upload my favourite route     |     To share my favourite route with fellow users                                       |
|                |                          |                                     |                                                          |                                                                                         |
|     6          |     Member/Non-member    |     Sorting & Searching             |     Sort the list of routes                              |     To find the best rated or closest routes to the user                                |
|     7          |     Member/Non-member    |     Sorting & Searching             |     Sort a specific category of route                    |     To find the best rated or closest routes in a specific bike type or route length    |
|     8          |     Member/Non-member    |     Sorting & Searching             |     Search for a route by name or description            |     Find a specific route with a keyword search of the name or description              |
|     9          |     Member/Non-member    |     Sorting & Searching             |     See what I’ve searched for and number of results     |     Quickly find if there’s a route with the keywords I’m looking for.                  |
|                |                          |                                     |                                                          |                                                                                         |
|     10         |     Non-Member           |     Registration/User Accounts      |     Register for an account                              |     To have an account to access full details of all routes                             |
|     11         |     Member               |     Registration/User Accounts      |     Log in and out                                       |     To access my personal information and full route details                            |
|     12         |     Member               |     Registration/User Accounts      |     Recover my lost password                             |     To regain access to my account if I forget password                                 |
|     13         |     Member               |     Registration/User Accounts      |     Receive email notification on registration           |     To confirm that my registration was successful                                      |
|     14         |     Member               |     Registration/User Accounts      |     Have a personalised user profile                     |     To view or update personal details and view membership restrictions                 |
|                |                          |                                     |                                                          |                                                                                         |
|     15         |     Member               |     Purchasing and checkout         |     View membership type in my basket to be purchased    |     To identify the membership type and cost                                            |
|     16         |     Member               |     Purchasing and checkout         |     Enter my payment details                             |     To easily purchase membership type required                                         |
|     17         |     Member               |     Purchasing and checkout         |     View an order confirmation after payment             |     To ensure I have received the product that I have ordered                           |
|     18         |     Member               |     Purchasing and checkout         |     Receive an email confirmation after checkout         |     To have a separate confirmation of what I’ve purchased                              |
|                |                          |                                     |                                                          |                                                                                         |
|     19         |     Member               |     Admin & Route Management        |     Add a route                                          |     Add a route for other members to view                                               |
|     20         |     Member               |     Admin & Route Management        |     Edit or update a route                               |     To change the route details of route I uploaded                                     |
|     21         |     Member               |     Admin & Route Management        |     Delete a route                                       |     To delete a route that is no longer correct                                         |
|     22         |     Member               |     Admin & Route Management        |     Rate and review a route                              |     To have a rating and review of a route posted on the website                        |
|     23         |     Member               |     Admin & Route Management        |     Create a forum post                                  |     Create a post on the site about a subject I’d like to discuss                       |

[↥ Back to top](#Mark-McClean)