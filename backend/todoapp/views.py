# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.todoapp.serializer import TodoSerializer
from .models import Todo

# Create your views here.
class TodoView(APIView):
    def get(self, request):
        user = request.user
        todos = Todo.objects.filter(user = user)
        serialize = TodoSerializer(todos, many = True)

        return Response({
            'status' : True,
            'data' : serialize.data,
            'message' : 'Todo fetched successfully'
        })
    
    def post(self, request):
        try:
            user = request.user
            data = request.data

            data['user'] = user.uid
            serializer = TodoSerializer(data = data)

            if not serializer.is_valid():
                return Response({
                    'status' : False,
                    'data' : serializer.errors,
                    'message' : 'Invalid data given'
                })

            serializer.save()

            return Response({
            'status' : True,
            'data' : serializer.data,
            'message' : 'Todo saved successfully'
            })

        except Exception as e:
            return Response({
            'status' : False,
            'data' : {},
            'message' : 'Oops! Something went wrong'
            })