from django.urls import path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('contacts', ContactsViewSet)

urlpatterns = [path('contactsform/', ContactsFormView.as_view())]
urlpatterns += router.urls
