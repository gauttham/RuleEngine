from . import models
import operator
from datetime import datetime


class Parser(object):

    def __init__(self, *args, **kwargs):
        self.isValid = True
        self.rowItem = kwargs

    def getrules(self):

        """
        Fetches the rules based on an incmong row item
        :param kwargs: Sample rowItem for which the rules will be fetched
        Eg: {'signal': 'ATL1', 'value': '56.679', 'value_type': 'Integer'}
        :return: {"status":True/False, "message": "Successful/Failure Message"}

        """
        try:
            rules = models.Rule.objects.filter(appliesOn=self.rowItem.get("signal"),
                                               valueType=self.rowItem.get("value_type"))
            if len(rules) > 0:
                return {"status": True, "message": rules}
            else:
                return {"status": False, "message": "No Rules"}
        except Exception as e:
            return {"status": False, "message": str(e)}

    def getoperator(self, ruleObj):
        return ruleObj.operator

    def get_truth(self, signal, relate, value):
        """

        :param appliesOn:
        :param relate:
        :param value:
        :return:
        """

        ops = {
            '>': operator.gt,
            '<': operator.lt,
            '>=': operator.ge,
            '<=': operator.le,
            '=': operator.eq
        }

        return ops[relate](signal, value)

    def getFailedRuleText(self, ruleObj):
        return ruleObj.appliesOn + " " + ruleObj.valueType + " " + ruleObj.ruleType + " " + ruleObj.operator + " " +ruleObj.value

    def validaterules(self):

        """

        :param args:
        :param kwargs: combination of two dictionaries: rules and rowItem
        Eg:
        :return: True/False, List of rules that failed
        """
        failedList = []

        try:
            ruleSet = self.getrules()
            if ruleSet.get("status"):
                rulesList = ruleSet.get("message")
                if rulesList:
                    for ruleItem in rulesList:
                        op = self.getoperator(ruleItem)
                        if self.rowItem.get("value_type") == "Integer":
                            isValid = self.get_truth(float(self.rowItem.get("value")), op, float(ruleItem.value))
                        elif self.rowItem.get("value_type") == "String":
                            isValid = self.get_truth(str(self.rowItem.get("value")), op, str(ruleItem.value))
                        elif self.rowItem.get("value_type") == "Datetime":
                            # Assuming that the date time value mentioned in the rule if of the format
                            # YYYY-MM-DD HH24:MI:SS - 2017-06-20 10:53:20
                            inpDate = datetime.strptime(self.rowItem.get("value"), '%Y-%m-%d %H:%M:%S')
                            cutDate = datetime.strptime(ruleItem.value, '%Y-%m-%d %H:%M:%S')
                            isValid = self.get_truth(inpDate, op, cutDate)


                        # The next pass checks for the combination of operator validity against Should be or should not be

                        if isValid and ruleItem.ruleType == "Should Be":
                            pass
                        elif isValid and ruleItem.ruleType == "Should Not Be":
                            failedRule = self.getFailedRuleText(ruleItem)
                            failedList.append(failedRule)
                        elif not isValid and ruleItem.ruleType == "Should Be":
                            failedRule = self.getFailedRuleText(ruleItem)
                            failedList.append(failedRule)
                        elif not isValid and ruleItem.ruleType == "Should Not Be":
                            pass
                        else:
                            pass
                    return failedList
                else:
                    return {"status": True, "message": "No Rules Hence skipping the Parse operation"}
            else:
                {"status": False, "message": "No Ruleset defined"}
        except Exception as e:
            return {"status": False, "message": str(e)}








