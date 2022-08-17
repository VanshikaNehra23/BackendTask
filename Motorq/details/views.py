from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics,status,views,permissions
from rest_framework.views import APIView
from .serializers import UserSerializer,EventSerializer,WaitingSerializer,RegisterSerializer
from .models import Events,Waiting
from rest_framework.response import Response
import datetime


def RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.last()
        print(user)
        return Response({ 
            'userid':user.id
        },status=status.HTTP_201_CREATED)

def EventsView(APIView):
    def post(self,request):
        current_datetime = datetime.datetime.now()
        if(request.POST["availability"]>0 and request.POST["opentime"]<= current_datetime and request.POST["closetime"]>=current_datetime):
            request.POST["availability"] -= 1
            request.POST["capacity"] += 1
            serializer = EventSerializer(data = request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({ 
                'status':'success'
            },status=status.HTTP_201_CREATED)
        elif(request.POST["availability"]<0 and request.POST["opentime"]<= current_datetime and request.POST["closetime"]>=current_datetime):
            serializer = WaitingSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({ 
                'status':'added in waiting list'
            },status=status.HTTP_201_CREATED)
        else:
            return Response({ 
                'status':'Registration not possible'
            },status=status.HTTP_400_BAD_REQUEST)

def DeleteRegistration(APIView):
    def delete(request,id):
        member = UserRegistration.objects.filter(id=id)
        member.delete()
        events = Events.objects.all().values()
        for event in events:
            if(request.POST["events"] == event):
                request.POST["availability"] += 1
                request.POST["capacity"] -= 1
                waiting = Waiting.objects.all().values()
                for wait in waiting:
                    if(request.POST["event_name"]==wait):
                        request.POST["availability"] -= 1
                        request.POST["capacity"] += 1
                        waitmember = Waiting.objects.filter(event_name=wait)
                        waitmember.delete()
                        return Response({ 
                            'status':'success'
                        },status=status.HTTP_201_ADDED)






