from rest_framework import serializers
from .models import MemeModel




class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = MemeModel
        fields = (
            'id', 'name', 'caption', 'url'
        )