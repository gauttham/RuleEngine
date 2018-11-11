from . import models
from .raw_signal import data
from .parser import Parser as signalParser

def loadrow(*args, **kwargs):

    try:
        m = models.SignalData()
        m.signal = kwargs.get("signal")
        m.value = kwargs.get("value")
        m.valueType = kwargs.get("value_type")

        m.save()
        return {"status": True, "message": "Saved Successfully"}
    except Exception as e:
        errorlog = {
            "message": "The following error occurred During saving data into Signal Data: %s".format(str(e)),
            "SignalData": kwargs
        }
        print(errorlog)
        return {"status": False, "message": errorlog}


def loadall():

    failedList = []
    if data:
        for rowItem in data:
            flag, message = loadrow(**rowItem)
            if flag:
                # TODO Invoke the parser module here
                pr = signalParser(**rowItem)
                res = pr.validaterules()
                if res:
                    failedList.append({"failedRow": rowItem.get("signal") + " " + rowItem.get("value_type") + " " + rowItem.get("value"),
                                       "failedRules": res})
            else:
                pass

        return failedList
    else:
        return {"status": False, "message": "No Data"}

