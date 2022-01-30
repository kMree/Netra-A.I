import time
from PIL import Image
import os
print("NETRA AI")
print("Background PNG's save with backback1,backback2... ")
print("Character PNG's save with lasthead1,lasthead2... ")
print("Extra PNG's save with lasthat1,lasthat2... ")
print("Copy your all PNG's in a file")
print("")
fileStr = str(input("File Location(C:/...) : "))
fileStr = fileStr.replace("\\","/")
print(fileStr)
print("")
bacCo = int(input("How many backgrounds do you have: "))
manCo = int(input("How many character do you have: "))
hatCo = int(input("How many extra do you have: "))

tt = str(input("Enter last number of save file: "))
savestr = "savesave"
backstr = "backback"
manstr = "lasthead"
hatstr = "lasthat"
for e in range(hatCo):
    for i in range(bacCo):
        istr = str(i + 1)
        foldback = fileStr + "/" + backstr + istr + ".png"
        img1 = Image.open(foldback)
        img1 = img1.convert("RGBA")
        for i2 in range(manCo):
            i2str = str(i2 + 1)
            foldman = fileStr + "/" + manstr + i2str + ".png"
            img2 = Image.open(foldman)
            img2 = img2.convert("RGBA")
            intermediate = Image.alpha_composite(img1, img2)
            intermediate = intermediate.convert("RGBA")
            for i4 in range(hatCo):
                i4str = str(i4 + 1)
                foldhat = fileStr + "/" + hatstr + i4str + ".png"
                img3 = Image.open(foldhat)
                img3 = img3.convert("RGBA")
                lastInter = Image.alpha_composite(intermediate, img3)
                lastSave = fileStr + "/" + savestr + str(i2) + str(i) +str(i4)+ str(tt) + ".png"
                lastInter = lastInter.save(lastSave)





