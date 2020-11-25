# Mark McClean

## Milestone Project 4 – Full Stack Frameworks

## Route Share – Django application

### Table of Contents
* [Why make Route Share?](#Why-make-Route-Share)
* [How the website works](#How-the-website-works)
* [UX: Strategy](#UX-Strategy)
* [Scope](#Scope)
* [Structure](#Structure)
* [Skeleton](#Skeleton)
* [Surface](#Surface)
* [Technologies Used](#Technologies-Used)

### View the live project
The live website hosted by Heroku can be viewed [here](https://bicycle-route-share.herokuapp.com/).

If you wish to test out the checkout form and payment please use the following test card details:
* Card No: 4242 4242 4242 4242
* Expiry Date: Any future Date
* CVC & ZIP: Any numbers

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

## Structure

### Features
1. Site Name and logo in the top left corner. This then disappears on medium and small screens but the callout remains with a welcome message so users still know where they have arrived.
2. A collapsible navbar element has been implemented for medium and smaller screens. The menu is hidden inside the 'burger' icon and the navbar sweeps down when clicked. When the collapsed menu is open on smaller screens the ‘burger’ icon toggles to an ‘X’ to signify to the user that this button will close the menu, then it toggles back to the ‘burger’ icon.
3. A search bar is visible on larger screens and hidden on smaller screens with a button to toggle the search bar’s visibility on smaller screens. This search bar can be used to search for key words from the routes titles, descriptions, bike types, route types and countries so there are many ways for the users to find the routes they want.
4. A profile icon appears in the top right of the navbar. This provides a dropdown menu giving the users links to sign in, register and access their own profile page if already logged in.
5. A shopping basket icon also appears in the top right corner of the navbar beside the profile icon. When a user adds a membership type to their basket, the icon will change colour to alert the user and display a number ‘1’ underneath, to indicate to the user that there is 1 item in their shopping basket.
6. The bottom section of the navbar is a sorting and filtering menu. Each link is a dropdown menu with filtering and sorting choices the user can make depending on their needs. The routes dropdown will continue to display all routes available but sort them according to your choice, for example length. The routes will then be displayed with the longest first to the shortest route last. The other menu choices are all filtering options so the user will only see routes that correspond with the choice they made, for example if they choose ‘Bike Type’ and ‘Race Bike’ from the dropdown they will only see routes that have a bike type of ‘Race Bike’.
7. Within all the route displays under the navbar is a separate sorting selector. This dropdown selector will give the user further sorting options even within a filter. If a user has selected for example a filter of countries and ‘United Kingdom’, they can sort these routes by length, from longest to shortest and also in reverse order or by bike type A-Z or Z-A.
8. Each route displayed is a link that will take the user to a details page about that particular route. This page will have a few extra details about the route and a button to get the route. This will then reveal the Google Maps URL for this route that the user uploaded when they created this route. The revelation of the Google Maps URL will be dependent on the current state of the users membership. If they have reached their current monthly routes limit, there will be an error message to let the user know they have reached their limit for this month.
9. On the main navigation is a ‘Membership’ option to take the users to the membership choices that they can purchase. The user will be required to have an account and be logged in before they can add a membership option to the basket. If they try to add a membership to the basket without being logged in, an error message will appear to alert them and they will be redirected to the log in page.
10. After a user adds a membership type to the basket, a message will appear to alert them to this and specify what has been added and a link to view the basket. Unlike all other messages on the site which appear for 5 seconds, this one has the alternative functionality of an exit button that the user will have to use to close the message. This is because this particular message has a lot more information than most so it gives the user more time to think about what they want to do.
11. When a user wants to purchase the chosen membership they can navigate to the checkout page through the basket page. This will then display a further order summary and a form to fill out basic user details and payment card details. Within in the payment card element is a hidden card error section where potential card errors will alert the user in real time to prevent them submitting the wrong card details.
12. When the user submits the checkout form, animated loading screen will appear for a few seconds while the payment is being processed. If there is a problem with the form for example they will be redirected back to the checkout page and a message will alert them to the problem. If the checkout was successful they will be directed to a success page where a further summary of their order will be available for them to see.

[↥ Back to top](#Mark-McClean)

## Surface

### Colours and icons
* **Background Colours** - From the beginning I wanted to go with a darker theme throughout the site with regards to the navbar, footer and all the elements that render on the main body of each page with a white background to separate all the elements. Initially I just went the colour of black for all these elements along with an orange trim in the form of a horizontal divider to break up the black elements. This horizontal divider was also used to separate the header section of an element from the main body of the element. For example on the routes page, it separates the name or title of the route form the other details of the route.
* **Colour Adjustments** - I continued to build my site using this combination of black, white and orange which I thought was a good combination, especially when rendered with some of the images I have throughout the site. However when it came to building the forum section of the site, because there were no images and potentially a lot of just black, white and orange, the black started to look a little harsh on the eye so at that point I decided to soften it up a little and played around with a number of dark greys before finally settling on rgb(80,82,81). I think this still works great with the white and orange. As I had a background class of black set up in the CSS I was easily and quickly able to change the colour of all elements on the site to this new dark grey.
* **Text Colours** - For the text on the site I went with white as most of the text was on top of the grey elements so this was the natural choice. There are a few exceptions throughout the site, for example on the navbar, the site name, profile and basket icons are all in the same orange trim colour. The basket icon changes to white, when a user adds a membership to the basket.
* **Button Colours** - For the primary buttons on the site to proceed and go forward with various functions I used the same orange as the orange trim from the elements with white text and a lighter orange colour when hovered over. For the secondary buttons, ie to go back to different pages or cancel various functionality I used an inversion of the primary button with a thin orange outline, a white background and orange text. This again inverted to appear as a primary button when hovered over.
* **Text Links** - Throughout the site there are also some text links, for example on the footer and in the forum pages, which are either in white with an orange hover or orange with a white hover. I did this to try to keep a consistent colour theme throughout the site.
* **Icons** - I also used many Font Awesome icons on the site. I think they really improve the appearance of the site and are also excellent visual indicators for the users to quickly understand what they are looking at.

[↥ Back to top](#Mark-McClean)

## Skeleton

### Wireframes
I used the Balsamiq program for the wireframes and attached them to the directory. The original idea is still recognizable from the finished application. There have obviously been some design changes along the way but the wireframe is useful to have to put the idea in your head down on paper before you start coding. The wireframes can also be viewed her below.<br/>
<details>
    <summary>
        Home Page - Desktop
    </summary>
    <img alt="Homepage-Desktop" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/f7cfa39737d6d1df96308ac81758efe50cc54ce9/static/wireframes/Homepage-Desktop.png">
</details>

<details>
    <summary>
        Home Page - Mobile
    </summary>
    <img alt="Homepage-Mobile" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/Homepage-Mobile.png">
</details>

<details>
    <summary>
        Routes - Desktop
    </summary>
    <img alt="Routes-Desktop" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/Routes-Desktop.png">
</details>

<details>
    <summary>
        Routes - Mobile
    </summary>
    <img alt="Routes-Mobile" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/Routes-Mobile.png">
</details>

<details>
    <summary>
        Route Details - Desktop
    </summary>
    <img alt="RouteDetails-Desktop" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/RouteDetails-Desktop.png">
</details>

<details>
    <summary>
        Route Details - Mobile
    </summary>
    <img alt="RouteDetails-Mobile" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/RouteDetails-Mobile.png">
</details>

<details>
    <summary>
        Membership - Desktop
    </summary>
    <img alt="Membership-Desktop" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/Membership-Desktop.png">
</details>

<details>
    <summary>
        Membership - Mobile
    </summary>
    <img alt="Memebership-Mobile" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/Membership-Mobile.png">
</details>

<details>
    <summary>
        Checkout - Desktop
    </summary>
    <img alt="Checkout-Desktop" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/Checkout-Desktop.png">
</details>

<details>
    <summary>
        Checkout - Mobile
    </summary>
    <img alt="Checkout-Mobile" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/Checkout-Mobile.png">
</details>

<details>
    <summary>
        Profile - Desktop
    </summary>
    <img alt="Profile-Desktop" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/Profile-Desktop.png">
</details>

<details>
    <summary>
        Profile - Mobile
    </summary>
    <img alt="Profile-Mobile" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/Profile-Mobile.png">
</details>

<details>
    <summary>
        Upload Route - Desktop
    </summary>
    <img alt="UploadRoute-Desktop" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/UploadRoute-Desktop.png">
</details>

<details>
    <summary>
        Upload Route - Mobile
    </summary>
    <img alt="UploadRoute-Mobile" src="https://raw.githubusercontent.com/Sparkplug84/route_share_MS4/master/static/wireframes/UploadRoute-Mobile.png">
</details>

[↥ Back to top](#Mark-McClean)

## Technologies Used
* [Gitpod]( https://www.gitpod.io/) – Used as my IDE for the development of the website. 
* HTML – Used to write the code for the structure and layout of all templates in the site.
* CSS – Used for custom styling of many HTML elements and some animations.
* Python – The core backend language used to create the logic for the views.
* [Django](https://www.djangoproject.com/) – This is a Python based framework which uses a model-template-view approach as the architectural engine. 
* Jinja - This templating language was used to project some of the Python functionality and template variables onto the frontend to create a dynamic site which automatically updates when user data is submitted.
* Javascript – Used to provide some interactive features of the website and to handle the checkout form submission
* jQuery – Used for several post-load JS scripts on the templates, the delete route modal and also to initialize some Bootstrap components.
* Popper.JS – Used to aid the responsiveness of the website.
* [Bootstrap]( https://getbootstrap.com/) – Bootstrap was used to provide the navbar, footer and the use of a grid system. Many bootstrap classes were also used throughout the site to add pre-existing colours, padding and margins to elements. 
* [Font Awesome]( https://fontawesome.com/) - for all site icons
* [Google Font](https://fonts.google.com/) - 1 Font was imported from Google Fonts and the URL can be found in the base template.
* sqlite3 – Was used as the backend development database and provided for by the Django framework
* Postgtres – Was used as the deployed database, provided for through Heroku
* [Heroku]( https://www.heroku.com/) – Used to deploy the website and hosted on Heroku’s cloud platform
* Git – Used for version control
* [Github](https://github.com/Sparkplug84/route_share_MS4) – Used to store the repository of all committed versions of the code. Also linked to Heroku to enable automatic deployment simultaneously. 
* Balsamiq - This was used to build the wireframes that were then uploaded to the Gitpod IDE.
* [Tables Generator](https://www.tablesgenerator.com/) - Used to create the tables inserted here in the README file.
* [Codacy](https://www.codacy.com/) – Used to validate all code on the entire site instead of copying and pasting many files one at a time into the various HTML, CSS, JS and Python code validators.
* Google Chrome Developer Tools – Used frequently to check and examine all elements and styles throughout the development. Even adjusting live in the browser before updating the corresponding code in Gitpod.
* [Google Maps](https://www.google.com/maps/) – Used to generate the html <iframe> element of the users route so it can pasted it in to the add route form.

[↥ Back to top](#Mark-McClean)
