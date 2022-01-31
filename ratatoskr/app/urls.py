from datetime import datetime
from django.urls import path

from . import views
from . import converters

urlpatterns = [
    path('', views.index, name='index'),
    path('create-schedule/', views.create_schedule, name='create-schedule'),
    path('schedule/<int:schedule_id>', views.schedule, name='schedule'),
    path('schedule/<int:schedule_id>/<datetime:date>', views.schedule_day, name='schedule-day'),
    path('timeslot-gen/<int:schedule_id>', views.timeslot_gen, name='timeslot-gen'),
]
