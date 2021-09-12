from rest_framework import serializers
from django.contrib.auth import get_user_model
from marketplace.models import Organisation, Parameter

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ("id", 'username', 'password', 'email')

        extra_kwargs = {
            'password': {'write_only': True}
        }


class ParameterSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Parameter
        depth = 1
        fields = '__all__'


class OrganisationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    user = UserSerializer(required=False)
    parameters = ParameterSerializer(required=False, many=True)

    class Meta:
        model = Organisation
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        validated_data = self.update_validated_data(validated_data)
        validated_data = self.create_parameter(validated_data)
        parameters = validated_data.pop("parameters")
        org = Organisation.objects.create(**validated_data)
        for parameter in parameters:
            org.parameters.add(parameter)
        org.save()
        return org

    def update_validated_data(self, validated_data):
        user_data = validated_data.pop("user")
        user_id = user_data.get("id")
        user_obj = User.objects.get(pk=user_id)
        validated_data["user"] = user_obj
        return validated_data

    def create_parameter(self, validated_data):
        parameter_data = validated_data.pop("parameters")
        validated_data["parameters"] = list()
        print(parameter_data)
        for parameter in parameter_data:
            name = parameter.get("name")
            parameter_obj, created = Parameter.objects.get_or_create(name=name)
            validated_data["parameters"].append(parameter_obj)

        return validated_data


