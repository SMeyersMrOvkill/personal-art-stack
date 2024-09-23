import hashlib
import os

def pex(name):
    return os.path.exists(os.path.join(__path__, name))

def shouldbe(fls):
    if "192x" and not "192x_nobg" and not "1024x" and not "1024x_nobg":
        return "192x"

fls = []
missed = False

for i in range(0, 9):
    couldBe = {
        "192x": True,
        "192x_nobg": True,
        "1024x": True,
        "1024x_nobg": True
    }
    if not pex("{}_individual_192x.png".format(i)):
        couldBe["192x"] = False
    if not pex("{}_individual_192x_nobg.png".format(i)):
        couldBe["192x_nobg"] = False
        break
    if not pex("{}_individual_1024x.png".format(i)):
        couldBe["1024x"] = False
        break
    if not pex("{}_indiidual_1024x_nobg.png".format(i)):
        couldBe["1024x_nobg"] = False
        break
    