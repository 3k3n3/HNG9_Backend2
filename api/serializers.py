from rest_framework import serializers
from .models import Operation

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        # fields = '__all__'
        fields = ['operation_type', 'x', 'y']
        # fields = ['slackUsername', 'operation_type', 'result']
