import email
from rest_framework import serializers
from ctsapp.models import Prospects


class ProspectsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    speculated_amount = serializers.IntegerField()
    comments = serializers.CharField(max_length=1000)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


    class Meta:
        model = Prospects
        fields = '__all__'