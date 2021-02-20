from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import TodoModel
from .serializers import TodoSerializer


class TodoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        todos = TodoModel.objects.filter(owner=request.user.id)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.DATA)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = serializer.data
            owner = request.owner
            todo = TodoModel(owner=owner, title=['title'], completion_date=['completion_date'], )
            todo.save()
            request.DATA['id'] = todo.pk
            return Response(request.DATA, status=status.HTTP_201_CREATED)
