# Week 23 Group Assignment
 This folder holds my week23 group assignment.
 
## Week23 Group Assignment Question 1
#### Expand the flask app from class to add functions to create, update, and delete records.Use the mongodb documentation. Create can use insert_one method, update can use update_one, and delete can use delete_one.
 - A / endpoint that displays all of the TV shows
	* !['Screenshot1'](./Week23_Question1_1.PNG?raw=true "all endpoint")

 - A /insert GET endpoint displays the form to enter a TV show, POST endpoint adds user entered data for a TV show in MongoDB
       * !['Screenshot2'](./Week23_Question1_2.PNG?raw=true "GET endpoint")
       * !['Screenshot3'](./Week23_Question1_3.PNG?raw=true "POST endpoint")
       * !['Screenshot6'](./Week23_Question1_6.PNG?raw=true "POST endpoint")

 - A /update<tvshow_name> GET endpoint displays the present data for that tvshow_name in the form. POST endpoint updates the data entered in a form for a show
       * !['Screenshot4'](./Week23_Question1_4.PNG?raw=true " GET endpoint")
       * Notice updated data
       * !['Screenshot8'](./Week23_Question1_8.PNG?raw=true " GET endpoint")
       
 - A /delete<tvshow_name> endpoint that lets you delete a show by its name
       * !['Screenshot5'](./Week23_Question1_5.PNG?raw=true " POST endpoint")
       * !['Screenshot7'](./Week23_Question1_7.PNG?raw=true " POST endpoint")

     