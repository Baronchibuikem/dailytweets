# About the project
The goal of this project is to make a web application that makes it easier to navigate the collection of a user's timeline on twitter.

We will be making a scheduled job to sync all pushlished tweets from a twitter user timeline to our own database and display the tweets on our UI.


Also we will be integrating a search feature to allow user's search for keywords in all the tweets available

And lastly we will be adding a functionality to allow authenticated user's through the help of twitter social auth to retweet tweets the find interesting.


## Technnologies used
This project was developed using python, django, tweepy, celery, social-auth-app-django, bootstrap4, redis

## How to setup this project

Please Note that both the Django templating and API integration was developed on this project 

To view the application in Django templating mode, navigate to the url below:

            http://127.0.0.1:8000/tips/

To view the API links created for this applications, navigate to the url below

            http://127.0.0.1:8000


Please ensure you can run celery and bash on your computer and follow the following instruction

Navigate to https://developer.twitter.com/, setup an application(if twitter has giving you develper access), set the permission to **Read, Write and Direct Messages** and generate your CONSUMER KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACESS_TOKEN_SECRET

Clone the project and add a .env file in the parent directory. Add the following inside the .env file

            CONSUMER_KEY = "Your own consumer key"
            CONSUMER_SECRET = "Your own consumer_secret"
            ACCESS_TOKEN = "Your own access token"
            ACCESS_TOKEN_SECRET = "Your own access token secret"  

then run the following command:

            python manage.py makemigrations
            python manage.py migrate
            python manage.py createsuperuser
            python manage.py runserver

While your server is running, open two more terminals and run the following code inside each of them

            bash bash_start_celery.sh
            bash bash_start_beat.sh

the first bash command will start your celery task while the second bash command will start your celery beat which is where we are scheduling our jobs to run within a specific time

you can change the duration at which you want the job to run by going to dilytips/celery, and editing the crontab() to the duration you want. currently the job has been set to run every 6hours 
            
            'schedule': crontab(minute='0' , hour='6')

For testing purposes you make configure the job to run every minute

            'schedule': crontab()

**Note** This application has been configured to fetch only 300 tweets by job, incase you want to increase or reduce it, navigate to the setting.py and update this line of code

            NUMBER_OF_TWEETS = "300"

**Note** you can also change the twitter user's timeline you are fetching by updating the code snippet below in your settings.py

            TWITTER_USER = "python_tip"

To read more about scheduling period task using celery, visit https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html

For example of of how to use it, feel free to read my short article here https://baronchibuike.medium.com/scheduling-periodic-task-in-django-rest-using-celery-and-redis-f67754eca013


In order for your API twitter social login to work, you need to go to your admin interface

            Click on the Site Table and add a new site with Domain name and Display name(eg, Domain name: 127.0.0.1, Display name: DailyTips)

            click on "social application" table

            Add a new social application -> you will be required to select a provider(in this case Twitter), add a name for the application, add your twiiter generated CONSUMER_KEY and CONSUMER_SECRET.

            Add your 127.0.0.1 to choosen sites and save 

For further more detailed information, you can checkout this documentation https://django-rest-auth.readthedocs.io/en/latest/installation.html#social-authentication-optional


## Next step
Integrate docker into the project

Write test cases

## Acknowledge
This application was built by Anozie Baron Chibuikem