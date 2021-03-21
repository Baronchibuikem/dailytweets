from django.contrib import admin
from tips.models import DailyTip

class DailyTipAdmin(admin.ModelAdmin):
    list_display = ["id", "posted_by", "python_tip"]

admin.site.register(DailyTip, DailyTipAdmin)

# Register your models here.
