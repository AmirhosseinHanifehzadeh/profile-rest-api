from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profile_api import serializers, models
from profile_api import permissions

class HelloApiView(APIView):
    """Test API view""" 
    serailizer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """return a list of apiview features"""
        an_apiview = [
            'uses http methods as function (get, post, patch , put, delete)',
            'is similar to a traditional django view',
            'give you the most control over your application logic', 
            'is mapped manually to urls', 
        ]

        return Response({'message': 'hello world', 'an_apiview': an_apiview})
    
    def post(self, request):
        """create a hello message with our name"""
        serailizer = self.serailizer_class(data=request.data)
        
        if serailizer.is_valid():
            name = serailizer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        
        else:
            return Response(serailizer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None): 
        """Handle undating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None): 
        """Handle a partial update an object"""
        return Response({'method': 'PATCH'})


    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet): 
    """Test api view set"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'uses action (list, create, retrieve, update, partial_update)',
            'automatically maps to urls using routers', 
            'provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """create a new hello message"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'

            return Response({'message': message})

        else: 
            return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)
        

    def retrieve(self, request, pk=None):
        """handle getting an object by its id"""

        return Response({'http_method': 'get'})

    def update(self, request, pk=None):
        """handle updating an object"""

        return Response({'http_method': 'update'})

    def partial_update(self, request, pk=None):
        """handle updating part of na object"""

        return Response({'http_method': 'patch'})

    def destroy(self, request, pk=None):
        """handle removing an object"""

        return Response({'http_method': 'delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer 
    queryset = models.UserProfile.objects.all() 
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """handle creating use authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""    
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all() 
    permission_classes = (
        permissions.UpdateOwnProfile, 
        IsAuthenticated
    )
    
    def perform_create(self, serializer):
        """sets the user profile to the logged in user"""   
        print("self.request: ", self.request)     
        serializer.save(user_profile=self.request.user)        
