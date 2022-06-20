from django.contrib import admin
from django.urls import path
from sports_accessories.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/sport_accessories_list/', sports_accessories_APIList.as_view()),
    path('api/v1/sport_accessories_list/<int:pk>/', sports_accessories_APIUpdate.as_view())

]
