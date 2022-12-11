from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from super_type.models import SuperType
from super_type.serializers import SuperTypeSerializer
from .models import Super
from .serializers import SuperSerializer

@api_view(['GET', 'POST'])
def supers_list(request):

    if request.method == 'GET':

        type_name = request.query_params.get('type')
        print(type_name)

        supers_query = Super.objects.all()

        if type_name:
            supers_query = supers_query.filter(super_type__name=type_name)
        
        serializer = SuperSerializer(supers_query, many=True)
        return Response(serializer.data)


    if request.method == 'POST':
        pass
