from rest_framework import serializers
from supers.models import Super

class SuperSerializer(serializers.Serializer):
    class Meta:
        model = Super
        fields = ['id', 'name''alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase', 'super_type']
        depth = 1