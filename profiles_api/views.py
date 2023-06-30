from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""
    serializer_class=serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview=[
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your application logic',
        'Is mapped manually to URLS',
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self, request):
        """create a hello message with out name"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,
            status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'message':'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'message':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'message':'Delete'})

class HelloViewSet(viewsets.ViewSet):
    """test API ViewSet"""
    serializer_class=serializers.HelloSerializer

    def list(self, reqest):
        """return a hello message"""
        a_viewset=[
        'Uses action (list, create, retrieve, update, partial_update)',
        'automatically maps to URLs using Routers',
        'prodivdes more functionality with less code'
        ]

        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self, request):
        """create a new hello message"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message=f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(serializer.errors,
            status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """partial update an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """handle ceating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, )

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
