from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view""" 
    
    def get(self, request, format=None):
        """return a list of apiview features"""
        an_apiview = [
            'uses http methods as function (get, post, patch , put, delete)',
            'is similar to a traditional django view',
            'give you the most control over your application logic', 
            'is mapped manually to urls', 
        ]

        return Response({'message': 'hello world', 'an_apiview': an_apiview})