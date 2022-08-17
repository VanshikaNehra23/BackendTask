from rest_framework import serializers
from .models import User,Events,Waiting,UserRegistration

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','password','type']
        extra_kwargs = {
            'password' : {'write_only':True}
        }

    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

    def create(self,validated_data):
        event = Events.objects.create(
            name = validated_data['name'],
            capacity = validated_data['capacity'],
            availability = validated_data['availability'],
            opentime = validated_data['opentime'],
            closetime = validated_data['closetime'],
        )
        return event

class WaitingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiting
        fields = '__all__'

    def create(self,validated_data):
        wait = Waiting.objects.create(
            event_name = validated_data['event_name']
            name = validated_data['name']
        )
        return wait

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = '__all__'

    def create(self,validated_data):
        reg = UserRegistration.objects.create(
            user = validated_data['user']
            events = validated_data['events']
        )
        return reg