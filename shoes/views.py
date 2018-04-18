from django.shortcuts import render
from shoes.models import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
def shoes_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        data = request.query_params.get('coco', None)
        print(data)
        return Response({'success': 'true'})
