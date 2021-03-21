from django.shortcuts import render
from tips.tasks import send_reminder



# def run_every_ten_seconds(request):

#     print("about running the function")
#     send_reminder.delay()
#     print("stopping the task")
