from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from .models import Card

class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card


# ViewSets define the view behavior.
class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer