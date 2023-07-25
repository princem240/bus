from django.urls import path
from .import views

urlpatterns = [
    path('',views.home),
    path('view/',views.view),
    path('filter',views.filter),
    path('book/<int:bus_id>',views.b),
    path('login',views.login),
    path('register',views.register),
    path('logout',views.logout),
    path('about',views.about),
    path('contact',views.contact),
    path('bookings',views.bookings),
    # path('bookform/<int:bus_id>',views.Book),
    path('cancel/<int:bus_id>',views.cancel),

] 


