from rest_framework import serializers
from factchecking.models import Report

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
        read_only_fields = ['created_on', 'updated_on', 'user', 'active']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return Report.objects.create(**validated_data)  

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
