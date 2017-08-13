from rest_framework import serializers
from .models import Belema

class BelemaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Belema
        fields = ['name', 'skin_colour', 'age', 'instituition']