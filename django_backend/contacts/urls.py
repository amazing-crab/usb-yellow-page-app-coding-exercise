from django.urls import path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('contacts', ContactsViewSet)

urlpatterns = [path('contactsform/', ContactsFormView.as_view()),
               path('contactsform/<int:pk>/', ContactsFormView.as_view()),
               path('contacts/<int:pk>/', ContactDeleteView.as_view())]
urlpatterns += router.urls
