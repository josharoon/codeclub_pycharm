from maya import cmds
import random

def giuseppesFunction(x,y,z):
    for counter in range(10):
        print counter
        boxname = "BOX%s" % counter
        cubename = cmds.polyCube(name=boxname)[0]
        cmds.setAttr(cubename + ".translate",  random.randint(0,counter)*x, random.randint(0,counter)*y, random.randint(0,counter)*z)


giuseppesFunction(7,2,3)



