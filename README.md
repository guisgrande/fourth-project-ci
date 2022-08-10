# Auto Classic

The Auto Classic is a website for people who are passionate about classic and vintage cars. Where users can share their vehicles and suggest events for car gatherings. 

To create a community of classic car owners and enthusiasts, to socialize, evaluate cars, give their opinion, and increase networking for future opportunities.

- Here is the link to the final project > [Auto Classic Club](https://auto-classic.herokuapp.com/)

<div align="center">
    <img src="documentation/images/responsive.PNG">
</div>

## Contents

## UX/UI Design

### Strategy

#### Site owner goals

- The website targets those who are excited by classic and vintage cars. The project was designed to be a great community for everyone who likes the experience of drive, seeing, or understanding more about historic cars.
- The website is designed to be intuitive and easy to navigate.
- The website was designed to be responsive and to meet all screen sizes.
- The website should prioritize the display of the posts and present the content in a good way.

#### Agile

For the development of this project, the Agile methodology was applied. As a support tool, I used the GitHub projects.

- To visualize the project access this link > [Agile Auto Classic](https://github.com/guisgrande/fourth-project-ci/projects/1)

As you can see, we used a simple Kanban board with the fields (To do, Doing, Done). To do the next ones that will be executed, Doing the ones that are currently being developed and Done the ones that were finished.

The final structure after the elaboration was 5 different epics and a total of 26 User Stories distributed among them. In the following image, I detail the EPICs and their respective US.

<details>
    <summary>Agile Structure</summary>
    <div align="center">
        <img src="documentation/images/agile-setup.png">
    </div>
</details> 

To run agile most efficiently, the following Sprints were determined as per the following image. The User Stories __#08 Recovery password__ and __#09 Edit username__ were not implemented in the project at this moment, being on stand by for future updates.

<details>
    <summary>Agile Sprints</summary>
    <div align="center">
        <img src="documentation/images/agile-sprints.png">
    </div>
</details>

#### User stories

- As a user, I want to understand the content of the website, so I can know if it's of my interest.
- As a user, I want to easily navigate the site, so I can load the page with the content I want to access.
- As a user, I want to have access to all the links, so I can connect to the website's social networks.
- As a user, I want to create an account and login/logout, so I can interact with the website and community, access my account and close it on multiple devices.
- As a user, I want to add new posts, edit and delete them, so I can upload my content and manipulate it if necessary.
- As a user, I want to interact with the other posts, so I can give my opinion and interact with my favorites.

### Scope

For the scope of this project the following key points were determined.
- Create a webpage application using the Django framework.
- Use bootstrap to make the site responsive, and custom CSS and Java Script to complement.
- Allow the user to create an account in order to upload content.
- Allow logged in users to interact with other posts through comments and actions.
- Allow users to manipulate their content (CRUD Operations).
- The frontend should be simple and present the content in a clear way.
- The website should be functional, easy to navigate and intuitive.

### Structure

Auto Classic, will have five distinct pages for the first-time user.
- Home page, Garage (Cars), Events, Signup, and Signin.

Unlogged users will be able to navigate through these five pages and will be able to see the details of each Car or Event by clicking on its link. But they will not be able to interact.

When the user creates an account and is logged in, the following pages will be displayed.
- Home page, Garage (Cars), Events, Logout, Members.

Logged-in users will be able to access the site completely. Being able to access the details of the cars and events post and interact with them.

He will be able to access his area (Members) to add new posts, modify the ones already added, or delete them.

### Skeleton

#### Wireframes

The wireframe was created using the Figma tool. During the elaboration of the wireframes, I added what the front end should look like. At the end of the development some changes were made.

- To visualize full desktop wireframe project > [Figma - Auto Classic Desktop](https://www.figma.com/file/zKQz8GjUEB8L82Sxj5U5SQ/PP4?node-id=35%3A3)

<details>
    <summary>Wireframes - Desktop</summary>
    <div align="center">
        <img src="documentation/images/wireframe-desktop-one.PNG">
        <img src="documentation/images/wireframe-desktop-two.PNG">
        <img src="documentation/images/wireframe-desktop-three.PNG">
        <img src="documentation/images/wireframe-desktop-four.PNG">
    </div>
</details>

- To visualize full mobile wireframe project > [Figma - Auto Classic Mobile](https://www.figma.com/file/zKQz8GjUEB8L82Sxj5U5SQ/PP4?node-id=0%3A1)

<details>
    <summary>Wireframes - Mobile</summary>
    <div align="center">
        <img src="documentation/images/wireframes-mobile.PNG">
    </div>
</details>

#### Database diagram

The base data for Auto Classic starts from the logged in user who can create a Car or Event post. 

The Car database relates to the RateCar and CommentCar database. And the Event database relates to the CommentEvent database.

<details>
    <summary>Diagram</summary>
    <div align="center">
        <img src="documentation/images/database-diagram.png">
    </div>
</details>

### Surface

#### Colour scheme

The colors chosen to compose the website are the following.

- The colors white/black will be used for the background and to create contrast between the sections.
- The gray will be used in the forms and cards to stand out from the background.
- Orange will be used to highlight the nav bar/footer/buttons.
- Yellow will be used for title effects, and view more button.

- Bootstrap default colors were also used for some buttons on the forms.

<details>
    <summary>Colour scheme</summary>
    <div align="center">
        <img src="documentation/images/COLORS.png">
    </div>
</details>

#### Typography

The site's font was chosen from google fonts. I chose the Quicksand (Light 300) font. It was used throughout the entire site, including titles and body. The only element with a different font is the custom banner.

#### Imagery

- For the auto classic project, I selected images that can enhance the user's visual response and convey the idea of the website. the images were selected from unsplash (credit mentioned in the readme).
- The first image of the front of a classic car in black and white that was used as a hero image on the home page.
- I selected two default images (placeholders) that are loaded in case the user doesn't add any image in the car or event post, one image for each respectively.

## Features

### Existing Features

#### __Favicon__

- Favicon is loaded on every page, the little logo is also present in the site banner.

<div align="center">
    <img src="documentation/screenshots/favicon.PNG">
</div>

#### __Navbar__

- Navbar that is present on all pages for user navigation through the website, is present the logo/banner with the site name that redirects to the home page,
the link to home page, a link to garage (all cars), a link to events (all events), the next two links alternate if the user is logged in or not.
- If the user does not have an account or is logged out, links to signup (register a new account) and signin (for the user to log in) are available.
user is logged in, the links are available to logout (confirmation page) and link to members (user area). 
to orange, giving a highlight to which page he will be redirected with the click.

<div align="center">
    <img src="documentation/screenshots/navbar-default.png">
    <img src="documentation/screenshots/navbar-logged.png">
    <img src="documentation/screenshots/navbar-hover.png">
</div>

- Navbar is responsive, for mobiles it automatically groups to drowdown menu.

<div align="center">
    <img src="documentation/screenshots/navbar-mobile-closed.PNG">
</div>
<div align="center">
    <img src="documentation/screenshots/navbar-mobile-show.PNG">
</div>

#### __Footer__

- The footer is shown only when reaching the end of the page, it counts with a list with the links that are present in the navbar with the same change in case the user is logged in or not. 
- Is also present three links that redirect the users to the social networks of the page to increase their interaction with the community.

<div align="center">
    <img src="documentation/screenshots/footer-default.PNG">
</div>
<div align="center">
    <img src="documentation/screenshots/footer-logged.PNG">
</div>

- The links present in the footer count with hover effect to increase the highlight of which selection will be executed with the click.

<div align="center">
    <img src="documentation/screenshots/footer-links-hover.png" width="150">
    <img src="documentation/screenshots/footer-social-hover.png" width="150">
</div>

#### __Hero image__

- Present on the index page, and one of the first images that the user sees when he logs into the website, it has a background image of an old car and with the name of the site and a brief description of the site's purpose.

<div align="center">
    <img src="documentation/screenshots/index-hero.PNG">
</div>

#### __About section__

- This section has a short introductory text about what is being made available on the website.

<div align="center">
    <img src="documentation/screenshots/index-about.PNG">
</div>

#### __Latest cars__

- Has a card display of the last four cars added to the site, for users to get an idea of what the content is like. Each car has a button to see more details.
- At the end of this section, a button to explore all cars, with hover effect.

<div align="center">
    <img src="documentation/screenshots/index-garage.PNG">
</div>

#### __Latest events__

- Counts with the card exhibition of the last events added in the site, for the users to visualize how the events are. Each event has a button to see more details.
- At the end of this section, a button to explore all events, with hover effect.

<div align="center">
    <img src="documentation/screenshots/index-events.PNG">
</div>

#### __Join the club__

- The last section of the index page is a text calling the user to action and a button to create an account. In case he is a recurrent user that already has an account and is logged in this text is changed to a greeting and a button (hover effect) to redirect to the memeber area.

<div align="center">
    <img src="documentation/screenshots/index-join-us.PNG">
    <img src="documentation/screenshots/index-user.PNG">
</div>

#### __Sign up__

- Registration page, with a simple form with the field for username, e-mail (optional) and for password twice, a button to register. A short text that calls who already has a registration to the login page.

<div align="center">
    <img src="documentation/screenshots/member-signup.PNG">
</div>

#### __Sign in__

- Access page, with two fields to be filled in (username and password). a button to log in. A short text with a callout for those who don't have an account.

<div align="center">
    <img src="documentation/screenshots/member-signin.PNG">
</div>

#### __Logout__

- Page for logged in users who have selected the logout option, it asks if they really want to perform this action.

<div align="center">
    <img src="documentation/screenshots/member-signout.PNG">
</div>

#### __User area__

- Area for logged in users, display greeting text with user name, four buttons for action: add car, add event, view cars, view events. At the end of the page has the setting account, with option to delete the account.

<div align="center">
    <img src="documentation/screenshots/member-area.PNG">
</div>

- If the user tries to access the page with the url without being logged in, it shows a different screen saying that he must create an account or log in to his existing account.

<div align="center">
    <img src="documentation/screenshots/notuser-memberarea.PNG">
</div>

#### __My cars__

- Page for logged in users that shows a list of the cars added by the user. Each car has three action options: view more (car info), edit (to edit car information) and delete (to delete car).

<div align="center">
    <img src="documentation/screenshots/member-car-list.PNG">
</div>

#### __My events__

- Page for logged in users that shows a list of the cars added by the user. Each event has three action options: view more (event info), edit (to edit event information) and delete (to delete event)

<div align="center">
    <img src="documentation/screenshots/member-event-list.PNG">
</div>

#### __Delete account__

- Area for the user to confirm that he really wants to delete the account. Rephrase the question informing that all data will be deleted when confirming. 
- A button to cancel and a link back to the member area.

<div align="center">
    <img src="documentation/screenshots/member-delete-account.PNG">
</div>

#### __Add car__

- Page for logged in users that provides the form for adding a new car.

<div align="center">
    <img src="documentation/screenshots/car-add.png">
</div>

#### __Edit car__

- Page for logged in users that allows editing of a previously added car, only the user himself can change it. The same page as the add car, but the information is already filled in as it was added and can be modified.

<div align="center">
    <img src="documentation/screenshots/car-edit.png">
</div>

#### __Delete car__

- A page for logged in users that enables them to delete information about their added car, shows a summary of the car's information and a question confirming if they want to continue with the action, which is irreversible.

<div align="center">
    <img src="documentation/screenshots/delete-car.PNG">
</div>

#### __Add event__

- Page for logged in users that provides the form for adding a new event.

<div align="center">
    <img src="documentation/screenshots/event-add.png">
</div>

#### __Edit event__

- Page for logged in users that allows editing of a previously added event, only the user himself can change it. The same page as the add event, but the information is already filled in as it was added and can be modified.

<div align="center">
    <img src="documentation/screenshots/event-edit.png">
</div>

#### __Delete event__

- Page for logged in users that enables them to delete the information of their added event, shows the summarized event information and a question confirming if they want to continue with the action that is irreversible.

<div align="center">
    <img src="documentation/screenshots/delete-event.PNG">
</div>

#### __Garage page__

- Page shows all cars added in the website, by default shows the most recent first. has a search field, a field to sort the list according to the available option.
- Each car is visible in a card with the following information (picture, brand, model, year, username, number of favourites and a button to more details).

<div align="center">
    <img src="documentation/screenshots/garage-page.PNG">
</div>

- By default the page loads only the last 6 cars, but the load more button loads 3 more posts with each click. Until there are no more and it changes to "no more cars".

<div align="center">
    <img src="documentation/screenshots/garage-load.PNG">
</div>

#### __Car info__

- Page with all car informations in more details, and the following sections: favorite, rate review, comment. these sections are presented in different ways for logged in and non logged in users.
- Not logged in user can only see the total of favorites and can not interact, can only see the total of reviews and the score and can not evaluate, can only read the comments and can not comment.
- Logged in user can see everything that the non logged in user can see, but he can interact with the page, by favoriting or un-favoriting a car, he can rate a car (only once per car), and he can send comments.

<div align="center">
    <img src="documentation/screenshots/cardetails-one.PNG">
    <img src="documentation/screenshots/cardetails-two.PNG">
</div>

- Favourite button

<div align="center">
    <img src="documentation/screenshots/favourite.PNG">
    <img src="documentation/screenshots/favoutired.PNG">
</div>

#### __Rate car__

- Shows the average points and a button to show all reviews. Next to it a button is displayed for logged in users if they haven't voted and a message if they have already voted on the car. 

<div align="center">
    <img src="documentation/screenshots/rate-details.PNG">
    <img src="documentation/screenshots/car-rated.PNG">
</div>

- If the user is not logged in. Message that is displayed.

<div align="center">
    <img src="documentation/screenshots/notuser-rate.PNG">
</div>

- Rate form and confirmation

<div align="center">
    <img src="documentation/screenshots/rate-form.PNG">
    <img src="documentation/screenshots/rate-confirm.PNG">
</div>

#### __Events page__

- Page shows all events added in the website, by default shows the most recent first. it has a search field, a field to sort the list according to the available option.
- Each event is visible in a card with the following information (image, title, category, date, location, number of go/maybe, a button to more details).
    
<div align="center">
    <img src="documentation/screenshots/events-page.PNG">
</div>

- By default the page loads only the last 6 events, but the load more button loads 3 more posts with each click. Until there are no more and it changes to "no more events".

<div align="center">
    <img src="documentation/screenshots/events-load.PNG">
</div>

- Presence vote buttons

<div align="center">
    <img src="documentation/screenshots/presence-not-selected.PNG">
    <img src="documentation/screenshots/presence-go.PNG">
    <img src="documentation/screenshots/presence-maybe.PNG">
</div>

#### __Event info__

- Page with all event informations in more details, and the following sections: go or maybe go and comment. these sections are presented in different ways for logged in and not logged in users.
- Not logged in user can only see the total go or maybe go and can't interact, can only read the comments and can't comment.
- Logged in user can see everything that the non logged in user can see, but he can interact with the page, selecting go or maybe go to an event, and can send comments.

<div align="center">
    <img src="documentation/screenshots/eventdetails-one.PNG">
    <img src="documentation/screenshots/eventdetails-two.PNG">
</div>

#### __Comments__

- The comments have the same layout for cars and events. Only logged in users can comment. A message that the comment has been sent for approval will appear as soon as you submit the comment.

<div align="center">
    <img src="documentation/screenshots/comment-display.PNG">
    <img src="documentation/screenshots/comment-aprove.PNG">
</div>

#### __Custom error pages__

- If any of the following errors occur (Error 400, 403, 404 or 500) a custom page will be displayed that will show text specifying the reason for the error and a link back to the home page. All pages have the same layout, only the explanatory text changes.

<div align="center">
    <img src="documentation/screenshots/403page.PNG">
    <img src="documentation/screenshots/404page.PNG">
</div>

### Features Left to Implement

- A section for service providers, such as repair, parts, washing, mechanic, insurance and others, where they can offer their services with better conditions for website users.
- The possibility for users to send private messages to other users, so they can make offers or communicate in a more practical way than comments.
- Add more functionalities in the user area like interaction notifications, more information options like profile (photo, description, interests).

## Testing
    
### Fixed Bugs

### Unfixed Bugs 
    
## Deployment

### Deployment

### Fork

### Clone

## Technologies and tools

- [Gitpod](https://www.gitpod.io/) - to create/edit the code of the project.
- [Github](https://github.com/) - to create repository, hosting files and deployment of the website.

## Credits

### Code

### Content

### Media

## Acknowledgements
