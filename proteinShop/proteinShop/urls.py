from django.contrib import admin
from django.urls import path
from sports_accessories.views import sports_accessoriesAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/sport_accessories_list/', sports_accessoriesAPIView.as_view()),
    path('api/v1/sport_accessories_list/<int:pk>/', sports_accessoriesAPIView.as_view())

]
