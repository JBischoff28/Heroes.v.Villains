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

        supers_query = Super.objects.all()
        heroes_query = Super.objects.filter(super_type=1)
        villains_query = Super.objects.filter(super_type=2)

        if type_name:
            supers_query = supers_query.filter(super_type__type=type_name)
        
        hero_serializer = SuperSerializer(heroes_query, many=True)
        villains_serializer = SuperSerializer(villains_query, many=True)
        
        custom_response = {
            'Heroes': [hero_serializer.data],
            'Villains': [villains_serializer.data]
        }
        
        return Response(custom_response)

    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
