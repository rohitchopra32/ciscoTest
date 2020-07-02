from rest_framework.serializers import ModelSerializer

from router.models import Router

class RouterSerializer(ModelSerializer):
    class Meta:
        model = Router
        fields = '__all__'

    def create(self, validated_data):
        validated_data.update({
            "is_active": True
        })
        return Router.objects.create(**validated_data)

    def update(self, instance, validated_data):
        validated_data.update({
            "is_active": True
        })

        return super(RouterSerializer, self).update(instance, validated_data)