import os
import random
from PIL import Image, ImageOps

krawType = "baby"

# bases = MUST BE WHITE

bodymarkings = "images/krawzirds/"+krawType+"/bodymarkings/"
facemarkings = "images/krawzirds/"+krawType+"/facemarkings/"

krawBase = "images/krawzirds/"+krawType+"/base.png"
krawBlackShell = "images/krawzirds/"+krawType+"/blackshell.png"
krawLines = "images/krawzirds/"+krawType+"/lineart.png"
krawFace = "images/krawzirds/"+krawType+"/face.png"

def allMarkings():
    for colorGenre in ["n_","o_","p_"]:
        for colorNum in range(1,9):
            for faceMarking in range (42,47):
                colorImage = Image.open("images/krawzirds/colors/"+colorGenre+str(colorNum)+".png")
                faceMarkingsImg = Image.open(facemarkings+str(faceMarking)+".png").convert("L")
                colorImage.putalpha(faceMarkingsImg)
                wrapFinal = Image.new("RGBA", colorImage.size)
                wrapFinal = Image.alpha_composite(wrapFinal, colorImage)
                wrapFinal.save(f"faces/{colorGenre}{colorNum}_{faceMarking}.png")
            for bodyMarking in range (41,46):
                colorImage = Image.open("images/krawzirds/colors/"+colorGenre+str(colorNum)+".png")
                bodyMarkingsImg = Image.open(bodymarkings+str(bodyMarking)+".png").convert("L")
                colorImage.putalpha(bodyMarkingsImg)
                wrapFinal = Image.new("RGBA", colorImage.size)
                wrapFinal = Image.alpha_composite(wrapFinal, colorImage)
                wrapFinal.save(f"bodies/{colorGenre}{colorNum}_{bodyMarking}.png")

def allEyes():
    for colorNum in range(1,9):
        # left
        colorImage = Image.open("images/krawzirds/colors/eyes_"+str(colorNum)+".png")
        eyebaseImg = Image.open("images/krawzirds/adult/l_k_eyes.png").convert("L")
        colorImage.putalpha(eyebaseImg)
        wrapFinal = Image.new("RGBA", colorImage.size)
        wrapFinal = Image.alpha_composite(wrapFinal, colorImage)
        wrapFinal.save(f"eyes/l_{colorNum}.png")
        # right
        colorImage = Image.open("images/krawzirds/colors/eyes_"+str(colorNum)+".png")
        eyebaseImg = Image.open("images/krawzirds/adult/r_k_eyes.png").convert("L")
        colorImage.putalpha(eyebaseImg)
        wrapFinal = Image.new("RGBA", colorImage.size)
        wrapFinal = Image.alpha_composite(wrapFinal, colorImage)
        wrapFinal.save(f"eyes/r_{colorNum}.png")

def adultMarkings():
    for colorGenre in ["n_","o_","p_"]:
        for colorNum in range(1,9):
            for faceMarking in range (42,47):
                # left
                # colorImage = Image.open("images/krawzirds/adultcolors/"+colorGenre+str(colorNum)+".png")
                # faceMarkingsImg = Image.open("images/krawzirds/adult/left/"+str(faceMarking)+".png").convert("L")
                # colorImage.putalpha(faceMarkingsImg)
                # wrapFinal = Image.new("RGBA", colorImage.size)
                # wrapFinal = Image.alpha_composite(wrapFinal, colorImage)
                # wrapFinal.save(f"faces/left_{colorGenre}{colorNum}_{faceMarking}.png")
                # right
                colorImage = Image.open("images/krawzirds/adultcolors/"+colorGenre+str(colorNum)+".png")
                faceMarkingsImg = Image.open("images/krawzirds/adult/right/"+str(faceMarking)+".png").convert("L")
                colorImage.putalpha(faceMarkingsImg)
                wrapFinal = Image.new("RGBA", colorImage.size)
                wrapFinal = Image.alpha_composite(wrapFinal, colorImage)
                wrapFinal.save(f"faces/right_{colorGenre}{colorNum}_{faceMarking}.png")

#allMarkings()

#allEyes()

adultMarkings()

print("Done")
