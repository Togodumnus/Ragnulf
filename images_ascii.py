def splitCubeImg(cube,imgRot):
    cubeSplit = cube.split("\n")
    imgSplit = imgRot.split("\n")
    sizeCube = len(cubeSplit)
    sizeImg = len(imgSplit)
    sizeDebutCube = sizeImg - sizeCube

    for i in cubeSplit:
        print(i)
        print(len(i))
    strImg = ""
    i = 0
    cptCube = 0
    while(i < sizeImg):            
        if i > sizeDebutCube:
            strImg += cubeSplit[cptCube]
            if cptCube > 5 :
                spacesManquant = 10 * ' ' 
                strImg += spacesManquant
            strImg += imgSplit[i] + "\n"
            cptCube += 1
        else :
            spacesManquant = 39 * ' ' 
            strImg += spacesManquant
            strImg += imgSplit[i] + "\n"
        i += 1
    if (cptCube < sizeCube):
        for j in range (cptCube,sizeCube):
            strImg += cubeSplit[j]
    return strImg

def img_B():
    imgStr = ""
    imgStr+=("               __________\n");
    imgStr+=("              |          |\n");
    imgStr+=("              |          |\n");
    imgStr+=("             \/          |\n");
    imgStr+=("        ___ ___  ___     |\n");
    imgStr+=("       /___/___/___/|    |\n");
    imgStr+=("      /___/___/___/||____|\n");
    imgStr+=("     /___/___/__ /|/|  \n");
    imgStr+=("    |   |   |   | /||   \n");
    imgStr+=("    |___|___|___|/|/|   \n");               
    imgStr+=("    |   |   |   | /||   \n");
    imgStr+=("    |___|___|___|/|/  \n");
    imgStr+=("    |   |   |   | /   \n");
    imgStr+=("    |___|___|___|/     \n");

    return imgStr


