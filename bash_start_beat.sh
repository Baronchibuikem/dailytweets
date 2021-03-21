#!/bin/bash
celery -A dailytips beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler