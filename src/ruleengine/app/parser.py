from . import models


class Parser(object):

    def __init__(self, *args, **kwargs):
        self.isValid = True
        self.rowItem = kwargs


    def getRules(self, *args, **kwargs):

        """
        Fetches the rules based on an incmong row item
        :param kwargs: Sample rowItem for which the rules will be fetched
        Eg: {'signal': 'ATL1', 'value': '56.679', 'value_type': 'Integer'}
        :return: {"status":True/False, "message": "Successful/Failure Message"}

        """

        rules = models.Rule.objects.filter(signal=kwargs.get("signal"),
                                           valueType = kwargs.get("valueType"))

        if len(rules) > 0:
            # TODO : Invoke rule parser here
            try:
                pass
            except Exception as e:
                return {"status": False, "message": "Some Error Occurred " + str(e)}



