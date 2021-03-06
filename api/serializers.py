from django.db.models import fields
from rest_framework import serializers

from curs.models import Curs, Student

class CursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curs
        fields = '__all__'


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    cursuri = CursSerializer(many=True)
    
    class Meta:
        model = Student
        fields = '__all__'
