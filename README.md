# Mark McClean

## Milestone Project 4 – Full Stack Frameworks

## Route Share – Django application


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