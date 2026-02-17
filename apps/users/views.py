from django.shortcuts import render

# Create your views here.

@api_view(['POST'])
def register(request):
    