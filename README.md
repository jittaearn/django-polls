 # Django Polls Application
 This project is a webpage which contain two major roles used for tracking the number of votes. The admin page allow the admin to create polls and add choices to each poll. Whiles, the user page allow the user to vote. 
 

 ## Requirements

 The application requires
 * Python 3.6.6 or newer
 * Django 2.1.2 or newer
 * Python add-on modules as in [requirements.txt](requirements.txt)

 ## Installation
 ### Step 1:
 Type the following command in your Terminal shell:

    git clone https://github.com/jittaearn/django-polls.git
 ### Step 2:
 Go to the project directory "django-polls" then type the following command:

    On MacOS/Linux: 

        pip3 install -r requirements.txt

        python3 manage.py migrate

    On Windows:

        pip install -r requirements.txt

        python manage.py migrate




 ## How to Run
 ### Step 1:
 Make sure you are in the right directory.
    
    cd django-polls

 ### Step 2:
 To run the server type the following command in the terminal.

    On MacOS/Linux:

        python3 manage.py runserver

    On Windows:

        python manage.py runserver

 ### Step 3:

 To run the server as an admin enter the following site.

    http://127.0.0.1:8000/admin/

 Otherwise, enter this command to enter as a user.

    http://127.0.0.1:8000/polls/


## Author
- Jitta Koopratoomsiri 6110545449