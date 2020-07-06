from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test the Api view"""
    def get(self, request, format=None):
        """Return a list api view features"""
        an_apiview = ['Uses Http Method as function(get,post,put,patch,delete)',
        'Is similar to a traditional django view']

        return Response({'message':'hello','an_apiview':an_apiview})
