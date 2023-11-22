from rest_framework import viewsets

from .models import Contact
from .serializer import ContactSerializer

class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
