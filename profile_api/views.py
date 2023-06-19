from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profile_api import serializers


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
