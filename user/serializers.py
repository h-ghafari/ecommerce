from rest_framework.serializers import ModelSerializer, ValidationError
from user.models import CustomUser, Address

class CustomUserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            'password':{
                'write_only': True
            }
        }
    
    def validate_password(self):
        if len(self.password)<8:
            raise ValidationError("Password must be at least 8 letters.") 
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            age=validated_data['age'],
        )
        return user


class SuperUserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            'password':{
                'write_only': True
            }
        }
    
    def create(self, validated_data):
        user = CustomUser.objects.create_superuser(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            # is_staff=True,
            # is_superuser=True,
        )
        return user
    

class AddressSelializer(ModelSerializer):
    class Meta:
        model = Address
        exclude = ['user']