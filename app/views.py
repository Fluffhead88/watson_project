from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework import generics

from app.models import Timestamp
from app.serializers import TimestampSerializer 

class IndexView(TemplateView):
    template_name = "index.html"

class ContactView(TemplateView):
    template_name = "contact.html"

class TimestampListCreateAPIView(generics.ListCreateAPIView):
    queryset = Timestamp.objects.all()
    serializer_class = TimestampSerializer


