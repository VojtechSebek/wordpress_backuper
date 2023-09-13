from datetime import datetime
import pytz

def aktualnidatumacas():
    zona = pytz.timezone('Europe/Prague')
    cas = datetime.now(zona)
    return cas.strftime("[%Y-%m-%d %H:%M]")

def aktualnidatumacasf():
    zona = pytz.timezone('Europe/Prague')
    cas = datetime.now(zona)
    return cas.strftime(" %Y_%m_%d %H_%M ")

def aktualniden():
    zona = pytz.timezone('Europe/Prague')
    cas = datetime.now(zona)
    return cas.weekday()

# print("Aktuální datum a čas je : " + cas.strftime("[%Y-%m-%d %H.%M]"))
# print("Aktuální den v týdnu je : " + str(cas.weekday()))