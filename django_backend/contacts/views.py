from rest_framework import viewsets, generics
from rest_framework.response import Response

from .models import Contact
from .serializer import ContactSerializer
from .forms import ContactsForm, UpdateContactsForm

class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactsFormView(generics.CreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def post(self, request, *args, **kwargs):
        form = ContactsForm(request.data)
        if form.is_valid():
            form.save()
            return Response({'message': 'Form submitted successfully.'}, status=201)
        return Response(form.errors, status=400)
    
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Contact updated successfully.'}, status=200)
        return Response(serializer.errors, status=400)

class ContactDeleteView(generics.DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
