from rest_framework import serializers


class CreateNoteSerializer(serializers.Serializer):
    writer_id = serializers.IntegerField()
    creator_id = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return

    def update(self, instance, validated_data):
        return instance
