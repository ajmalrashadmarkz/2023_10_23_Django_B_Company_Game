from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 
                  'email',
                  'first_name', 
                  'last_name', 
                  'password', 
                  'token', 
                  'user_id',
                  'date_joined' , 
                  'activation_date',
                  )
        
    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        self.send_activation_email(user)
        return user

    def get_token(self, obj):
        user = obj
        token = default_token_generator.make_token(user)
        return token

    def send_activation_email(self, user):
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        subject = 'Activate your account'
        message = f'Please use the following link to activate your account:\nhttp://127.0.0.1:8000/api/users/activate/{uid}/{token}/'
        user.email_user(subject, message)