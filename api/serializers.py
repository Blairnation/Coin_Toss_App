from rest_framework import serializers
from .models import Stake

class StakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stake
        fields = ['id', 'user', 'amount', 'prediction', 'result', 'timestamp']
        