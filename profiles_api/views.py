from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """Test the Api view"""
    serializers_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list api view features"""
        an_apiview = ['Uses Http Method as function(get,post,put,patch,delete)',
                      'Is similar to a traditional django view']

        return Response({'message': 'hello', 'an_apiview': an_apiview})
    
    def post(self,request):
        """ Create a hello message with our name """
