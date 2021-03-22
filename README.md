# About the project
The goal of this project is to make a web application that makes it easier to navigate the collection of a user's timeline on twitter.

We will be making a scheduled job to sync all pushlished tweets from a twitter user timeline to our own database and display the tweets on our UI.


Also we will be integrating a search feature to allow user's search for keywords in all the tweets available

And lastly we will be adding a functionality to allow authenticated user's through the help of twitter social auth to retweet tweets the find interesting.


## Technnologies used
This project was developed using python, django, tweepy, celery, social-auth-app-django, bootstrap4

## How to setup this project
Please ensure you can run celery and bash on your computer and follow the following instruction

Navigate to https://developer.twitter.com/ and get your CONSUMER KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACESS_TOKEN_SECRET

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


## Next step
Integrate docker into the project