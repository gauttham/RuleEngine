from rest_framework import serializers
from . import models


class SignalListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SignalData
        fields = ('signal', 'value', 'valueType', 'isViolated')


class RuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Rule
        fields = ('appliesOn', 'valueType', 'ruleType', 'operator', 'value')

