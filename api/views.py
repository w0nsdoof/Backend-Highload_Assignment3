from rest_framework import generics
from .models import KeyValue
from .serializers import KeyValueSerializer

class KeyValueList(generics.ListCreateAPIView):
    queryset = KeyValue.objects.all()
    serializer_class = KeyValueSerializer
    
class KeyValueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = KeyValue.objects.all()
    serializer_class = KeyValueSerializer