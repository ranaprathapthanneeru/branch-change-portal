Group No:18


honour code:

We pledge on our honour that we have not given or received any unauthorized assistance on this
assignment or any previous task.




(ranaprathap,140050068)    100%

(sreenivasulu,140050078)   100%

(srinath,140050080)        100%

Instructions to run:

   OUR PRE DATA::

        We imported all roll numbers of form 1500a00bc for testing purpose in the students model

   ADMIN::

     create a super user yourself or use ours  

         usrname:srinath
         password:srinath

   IMPORTING and EXPORTING::

       for exporting the data filled by users ,go to admin ->branch changes : select all and select Export CSV in the actions
       
       for importing branch change data put the 'input_options.csv' file in the webapp folder and run the command in terminal "python3  
       import_branchchange_data.py"

       for importing result data put the 'allotment.csv' file in the webapp folder and run the command in terminal "python3  
       import_results.py"

       for importing students data put the 'initialise_data.csv' file in the webapp folder and run the command in terminal "python3  
       import_random_data.py" to enroll new students

       for deleting any data go to admin select the model to delete and in actions select delete selected items 

   HANDLING GUI::

       runserver and you will see a login page you can navigate from there:
       use password as 'password' we made it for simplicity

       For checking the results type '/results' at the url of login page and hit enter
          sample results were provided in that page the data is imported by us priorly
      
   FOR RUNNING THE CPP FILE :

       Compile the cpp file with c++11 flag.
       program prompts for input files.Provide them
       program output files are allotment.csv,  output_stats.csv

       ***Important if the code doesn't work. Mostly this doesn't occur***
         1)While importing the final results to the webpage, due to some error it gives
               ""value error : invalid literal for int with base 10""
           Then try deleting the last trailing spaces of the first line and last line of 'allotment.csv'
            
         2)While running the cpp file if it gives segmentation fault, try the previous things for both files input_options and input_programmes files.

         3)Try renaming the file if it gives other weird errors.

         We think these errors are, most probably, not due to code bcoz we renamed the file from input_options.csv to test.csv and again to input_options.csv and the code ran perfectly.


   We are commiting  to 2 late days








