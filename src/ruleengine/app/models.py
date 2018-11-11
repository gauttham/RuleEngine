from django.db import models
from .raw_signal import data


# Create your models here.

signalValueChoices = sorted(list(set([(x.get("signal"), x.get("signal")) for x in data])), key=lambda x:x[1])
valueTypeChoices = [
    ('Integer', 'Integer'),
    ('String', 'String'),
    ('Datetime', 'Datetime'),
]

ruleTypeChoices = [
    ('Should Be', 'Should Be'),
    ('Should Not Be', 'Should Not Be'),
]

ruleOperatorChoices = [
    ('=', 'equal to'),
    ('<', 'less than'),
    ('>', 'greater than'),
]


class SignalData(models.Model):
    signal = models.CharField(max_length=50, null=True, blank=True)
    value = models.CharField(max_length=50, null=True, blank=True)
    valueType = models.CharField(max_length=50, null=True, blank=True)
    isViolated = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return "{signal: %s, 'value': %s, 'valueType':%s}" % (self.signal, self.value, self.valueType)


class Rule(models.Model):
    # appliesOn = models.CharField(max_length=50, choices=columnChoices, default=None)
    appliesOn = models.CharField(max_length=50,
                                 choices=signalValueChoices,
                                 default=None)
    valueType = models.CharField(max_length=20, choices=valueTypeChoices, default=None)
    ruleType = models.CharField(max_length=50, choices=ruleTypeChoices, default='Should Be')
    operator = models.CharField(max_length=50, choices=ruleOperatorChoices, default=None)
    value = models.CharField(max_length=100, default=None,
                             help_text="If using date, please use the following format 'YYYY-MM-DD HH24:MI:SS'")

    def __str__(self):
        return "%s %s %s %s %s" % (self.appliesOn, self.valueType, self.ruleType, self.operator, self.value)


