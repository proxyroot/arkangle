from rest_framework import serializers


class ClusterSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nodes = serializers.IntegerField(required=True)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Cluster` instance, given the validated data.
        """
        instance.nodes = validated_data.get("nodes", instance.nodes)
        instance.save()
        return instance
