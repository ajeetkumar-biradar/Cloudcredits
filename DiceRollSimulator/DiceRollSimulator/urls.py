from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dice_simulator.urls')),  # Include dice_simulator URLs
]
