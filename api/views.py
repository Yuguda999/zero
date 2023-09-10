# person_api/views.py

from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'name'  # Use name as the lookup field for dynamic operations
