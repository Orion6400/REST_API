from rest_framework import serializers
from .models import Student

def first_letter_capital(value):
    if value[0].islower():
        raise serializers.ValidationError("First Letter Should Be Capital")
class StudentSerializers(serializers.ModelSerializer):
    name = serializers.CharField(validators=[first_letter_capital])
    city = serializers.CharField(validators=[first_letter_capital])
    class Meta:
        model = Student
        fields = ['id','name','roll','city']



