# Exercise Location Finder App
## Contents
* [Brief](#brief)
   * [Scope of Project ](#Scope-of-project)
   * [My Approach](#my-approach)
* [Architecture](#architecture)
   * [Database Structure](#database-structure)
   * [CI Pipeline](#ci-pipeline)
* [Project Tracking](#project-tracking)
* [Risk Assessment](#risk-assessment)
* [Testing](#testing)
* [Front-End Design](#front-end-design)
* [Known Issues](#known-issues)
* [Future Improvements](#future-improvements)
* [Authors](#authors)


## Brief
 We have been asked to create an application with the overall objective to create a CRUD application with the utilisation of supporting tools, methodologies and technologies which uses the modules that we have covered during the training. 

### Scope of Project
These are the requirements for the project as it follows:
* A Trello board with full expansion on user stories, use cases, and tasks needed to be complete the project
* A relational database used to store data and at least 2 tables in the database, also it is required to model a relationship.
* Clear documentation from a design phase describing the architecture used for the project, including a detailed Risk Assessment 
* Creation of a functional CRUD application with the use of Python, following best practices and design principles. By CRUD it means to create a web application that can Create, Read, Update and Delete
* Fully designed test suites for the web app that is being created, also including automated tests for validation of the web app. There must be a high test coverage provided 
* Creation of a functioning front-end web app
* Code fully integrated into a Version Control System using the Feature-Branch model which is built through a  CI server and deployed to a cloud-based virtual machine   


### My Approach 
To achieve the requirements, I have decided to create a web app which helps users to locate an area which they can do their daily exercises and exercises that are ideal for the location provided. I wanted to create this web app because I have a passion for staying healthy and especially during lockdown it is important to find local outdoor spaces to conduct your daily exercise. The functionalities of the web app are :
* create an exercise which stores:
    * *Exercise Name*
    * *Description*
    * *Sets*
    * *Reps*

* create a Location which stores:
    * *Location Name*
    * *Description*
    * *Address*

* Add exercises to a location (Many-to-Many database functionality)
* Add location to an exercise (Many-to-Many database functionality)
* Delete exercise from database  
* Delete location from the database
* The user can read the exercise and location in the home page 
* Update location 
* Update exercise
* View locations in an exercise 
* View exercises in a location 

## Architecture 
### Database Structure 
Below I have included an ER diagram which showcases the structure of the database used for the web app. Everything that has been highlighted in green is implemented in the project.  
At the beginning of the project, I started by creating the Logical ER diagram first before proceeding to the physical data model. A logical ERD graphically represents the data architecture without the regard of physical implementation. Mainly used to provide information regarding the entities and relationship.    
![ERD][erd2]
The second image is the physical data model which represents the actual design blueprint of a relational database. A physical data model elaborates on the logical data model by assigning each column with type, length, nullable, etc. 
![ERD][erd1]

From the images above of the ERD it is evident that many-to-many relationship is used as the database model for the web app, which means that a third table needs to be created as the associate table. It will enable the user to create an exercice and add a location to it. The user can also choose a location and add an exercise to it. 
### CI Pipeline
![CI][ciPipe]
The CI pipeline diagram showcases the continuous integration through the main usage of github and jenkins. The use of webhooks within GitHub, the pipeline allows code that has been changed and uploaded to GitHub be automated by jenkins to build the web app in order to conduct tests and generate a report. 

## Project Tracking
For the project tracking I have used the Trello board which can be accessed through here.(https://trello.com/b/RAnNIvyk/exercise-project)
![TRELL][trello]

The Trello board contains:
* *Backlog* In which all of the cards are initially added when the requirements gathering is done. This allows the cards to progress from backlog to being done, which is a movement from left to right. 

* *User Stories* A user story looks at the requirements in the view of the client to better the web app to meet client satisfaction.

* *To-Do* This is where an element is being considered to be implemented 
* *Doing* This is where an element is being built, when code has been written for it .
* *Testing* After an element is completed it is then moved to testing, to see if the element works as intended. 
* *Done* After a review if the element is considered to be finished it is then moved to the done section. 


## Risk Assessment
The full risk assessment can be found by clicking on this link:(https://docs.google.com/document/d/12_SSrU0dpaW754nMieaN5lIhmecfGiWq7A7hjq-EDbQ/edit?usp=sharing)
### Pre-Risk Assessment 
![risk][risk1]
![risk][risk2]

### Post-Risk Assessment 
![risk][risk3]
![risk][risk4]

## Testing
After the application was created, it was moved to the testing stage in which pytest was used for the unit and integrated testing. When conducting the unit test there was coverage of 100% of the code. 
![unit][unit_test]
![unit][int_test]

## Front-End Design
The front end design does not have any CSS styling as it was not deemed necessary as there was more emphasis on the functionalities of the web app rather than the look of it.

![hp][home_page] <br> The navigation which stays consistent throughout the pages allows the user to navigate to the home page, create exercise or create a location. Also outputs the exercises and locations on the home page. 

![hp][home_page_itm]<br>
When items have been added, the user can either Update, Delete, Add Exercise, Add Location, View Exercises or View Locations

![hp][create_exe]<br>
The users are given four forms to fill, which asks for Name of exercise, Description of exercise, Number of sets and Number of reps.

![hp][create_loc]<br>
On this page, the user can create a location, which asks for the location name, description of the location and the address.  

![hp][update_exe]<br>
On this page, the user selects to update their exercise, which allows them to change the description, sets and reps.

![hp][update_loc]<br>
The update location page allows the user to change the name, description and address of the location.

![hp][view_exe_loc]<br>
On the page above you can view the locations in which an exercise is ideal. 

![hp][view_loc_exe]<br>
On the page above you can view the exercises in which the selected location is ideal. 

![hp][add_exe_loc]<br>
The page allows the user to add an exercise to a location selected. 

![hp][add_loc_exe]<br>
The page allows the user to add a location to an exercise selected.

## Known Issues
An issue regarding the web app is that there are no validations in the input fields for the users. This means that the user can type anything they would like and it would be registered to the database. Furthermore, the user is not limited on the number of entries,so they can overfill a web page.
## Future Improvements
There are many imporvements to be made for this web app to become a fully functioning application:
* Creating a login page so the users can have personal entries and be secure.
* Allow the user to upload images so they can have a better understanding of the location or exercise.
* Integrate google maps for the location, which could be done through a google api.
* Improve the look of the website by incorporating CSS styling to make it appealing and well organised for the user.
* A method for users to share their database with other users to see what location have they found in the surrounding neighbourhood so they can see what is nearby. 
* Allow for the uploading of videos which can be used by the user's to demonstrate their exercises. 
## Author
Abaseen Popal






[erd1]: https://i.imgur.com/OMTDVD4.png
[erd2]: https://i.imgur.com/pBEegGz.png
[ciPipe]: https://i.imgur.com/rO1MSUQ.png
[trello]: https://i.imgur.com/Rzkyl5m.png
[risk1]: https://i.imgur.com/xBl7OVM.png
[risk2]: https://i.imgur.com/R7fiozK.png
[risk3]: https://i.imgur.com/6FjDTMr.png
[risk4]: https://i.imgur.com/dZ1qRtd.png
[unit_test]: https://i.imgur.com/v99I92p.png
[int_test]: https://i.imgur.com/xbAGAfP.png
[home_page]:https://i.imgur.com/OqRh866.png
[home_page_itm]:https://i.imgur.com/v3ljrEo.png
[create_exe]:https://i.imgur.com/dNYSnMY.png
[create_loc]:https://i.imgur.com/WhS9QTA.png
[update_exe]:https://i.imgur.com/Tbfiu6T.png
[update_loc]:https://i.imgur.com/Sj9oSaV.png
[view_exe_loc]:https://i.imgur.com/lo8zXIC.png
[view_loc_exe]:https://i.imgur.com/UfYoXcU.png
[add_exe_loc]:https://i.imgur.com/5tTPv92.png
[add_loc_exe]:https://i.imgur.com/VMIMbC6.png



