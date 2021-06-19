from django.db.models import fields
from rest_framework import serializers

from curs.models import Curs

class CursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curs
        fields = '__all__'
