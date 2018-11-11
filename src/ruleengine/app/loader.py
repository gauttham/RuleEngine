from . import models
from .raw_signal import data


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

    if data:
        for rowItem in data:
            flag, message = loadrow(**rowItem)
            if flag:
                pass
            else:
                pass

        return True
    else:
        return {"status": False, "message": "No Data"}

