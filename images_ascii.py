def splitCubeImg(cube,imgRot):
    cubeSplit = cube.split("\n")
    imgSplit = imgRot.split("\n")
    sizeCube = len(cubeSplit)
    sizeImg = len(imgSplit)

    strImg = ""

    for i in range(0,max(sizeCube,sizeImg)):
        if i > sizeCube and i > sizeImg:
            pass
        elif i > sizeCube:
            strImg += imgSplit[i] + "\n"
        elif i > sizeImg:
            strImg += cubeSplit[i] + "\n")
        else:
            strImg += imgSplit[i]
            strImg += cubeSplit[i] + "\n"

    return strImg


def img_B():
    imgStr = ""
    imgStr+=("                              __________\n");
    imgStr+=("                             |          |\n");
    imgStr+=("                             |          |\n");
    imgStr+=("                            \/          |\n");
    imgStr+=("                       ___ ___  ___     |\n");
    imgStr+=("                      /___/___/___/|    |\n");
    imgStr+=("                     /___/___/___/||____|\n");
    imgStr+=("                    /___/___/__ /|/|  \n");
    imgStr+=("                   |   |   |   | /||   \n");
    imgStr+=("                   |___|___|___|/|/|   \n");               
    imgStr+=("                   |   |   |   | /||   \n");
    imgStr+=("                   |___|___|___|/|/  \n");
    imgStr+=("                   |   |   |   | /   \n");
    imgStr+=("                   |___|___|___|/     \n");

    return imgStr


