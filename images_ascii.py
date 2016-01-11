def splitCubeImg(cube,imgRot):
    cubeSplit = cube.split("\n")
    imgSplit = imgRot.split("\n")
    sizeCube = len(cubeSplit)
    sizeImg = len(imgSplit)
    sizeDebutCube = sizeImg - sizeCube


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

class AffichageMoves():
    
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

    def img_B2():
        imgStr = ""
        imgStr+=("               __________\n");
        imgStr+=("              |          |\n");
        imgStr+=("              |     x2   |\n");
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

    def img_Bi():
        imgStr = ""
        imgStr+=("               __________\n");
        imgStr+=("              |          |\n");
        imgStr+=("              |          |\n");
        imgStr+=("              |          |\n");
        imgStr+=("        ___ __|_ ___     \/\n");
        imgStr+=("       /___/___/___/|     \n");
        imgStr+=("      /___/___/___/||____\n");
        imgStr+=("     /___/___/__ /|/|  \n");
        imgStr+=("    |   |   |   | /||   \n");
        imgStr+=("    |___|___|___|/|/|   \n");               
        imgStr+=("    |   |   |   | /||   \n");
        imgStr+=("    |___|___|___|/|/  \n");
        imgStr+=("    |   |   |   | /   \n");
        imgStr+=("    |___|___|___|/     \n");

        return imgStr

    def img_F():
        imgStr += ("        ____ ___ ___\n")
        imgStr += ("       /___/___/___/|   \n")
        imgStr += ("      /___/___/___/||  \n")
        imgStr += ("     /___/___/__ /|/|  \n")
        imgStr += ("    |   |   |   | /||    \n")
        imgStr += ("    |___|___|___|/|/|      \n")                 
        imgStr += ("    |   |   |   | /||   \n")
        imgStr += ("    |___|___|___|/|/  \n")
        imgStr += ("    |   |   |   | /   \n")
        imgStr += ("    |___|___|___|/ \n")
        imgStr += ("      ___________\n")
        imgStr += ("     |           |\n")
        imgStr += ("     |           |\n")
        imgStr += ("     |           |\n")
        imgStr += ("     |           \/\n")
        imgStr += ("     |             \n")
        imgStr += ("     |__________\n")

    def img_F2():
        imgStr += ("         ____ ___ ___\n")
        imgStr += ("        /___/___/___/|   \n")
        imgStr += ("       /___/___/___/||  \n")
        imgStr += ("      /___/___/__ /|/|  \n")
        imgStr += ("     |   |   |   | /||    \n")
        imgStr += ("     |___|___|___|/|/|      \n")                 
        imgStr += ("     |   |   |   | /||   \n")
        imgStr += ("     |___|___|___|/|/  \n")
        imgStr += ("     |   |   |   | /   \n")
        imgStr += ("     |___|___|___|/ \n")
        imgStr += ("       ___________\n")
        imgStr += ("      |           |\n")
        imgStr += ("      |           |\n")
        imgStr += ("      |     x2    |\n")
        imgStr += ("      |           \/\n")
        imgStr += ("      |             \n")
        imgStr += ("      |__________\n")

    def img_Fi():
        imgStr += ("         ____ ___ ___\n")
        imgStr += ("        /___/___/___/|   \n")
        imgStr += ("       /___/___/___/||  \n")
        imgStr += ("      /___/___/__ /|/|  \n")
        imgStr += ("     |   |   |   | /||    \n")
        imgStr += ("     |___|___|___|/|/|      \n")                 
        imgStr += ("     |   |   |   | /||   \n")
        imgStr += ("     |___|___|___|/|/  \n")
        imgStr += ("     |   |   |   | /   \n")
        imgStr += ("     |___|___|___|/ \n")
        imgStr += ("       ___________\n")
        imgStr += ("      |           |\n")
        imgStr += ("      |           |\n")
        imgStr += ("      |           |\n")
        imgStr += ("      \/          |\n")
        imgStr += ("                  |  \n")
        imgStr += ("       ___________|\n")


    def img_L():
        imgStr+="             ____ ___ ___   \n"
        imgStr+="      /|    /___/___/___/|   \n"
        imgStr+="     / |   /___/___/___/||  \n"
        imgStr+="    /  |  /___/___/__ /|/|  \n"
        imgStr+="   |   | |   |   |   | /||    \n"
        imgStr+="   |   | |___|___|___|/|/|   \n"                    
        imgStr+="   \/  | |   |   |   | /||   \n"
        imgStr+="      /  |___|___|___|/|/  \n"
        imgStr+="     /   |   |   |   | /   \n"
        imgStr+="    /    |___|___|___|/    \n"

    def img_L2():
        imgStr+="             ____ ___ ___   \n"
        imgStr+="      /|    /___/___/___/|   \n"
        imgStr+="     / |   /___/___/___/||  \n"
        imgStr+="    /  |  /___/___/__ /|/|  \n"
        imgStr+="   |   | |   |   |   | /||    \n"
        imgStr+="   | x2| |___|___|___|/|/|   \n"                    
        imgStr+="   \/  | |   |   |   | /||   \n"
        imgStr+="      /  |___|___|___|/|/  \n"
        imgStr+="     /   |   |   |   | /   \n"
        imgStr+="    /    |___|___|___|/    \n"

    def img_Li():
        imgStr+="             ____ ___ ___   \n"
        imgStr+="      /|    /___/___/___/|   \n"
        imgStr+="     / |   /___/___/___/||  \n"
        imgStr+="    /  |  /___/___/__ /|/|  \n"
        imgStr+="   |   \/|   |   |   | /||    \n"
        imgStr+="   |     |___|___|___|/|/|   \n"                    
        imgStr+="   |     |   |   |   | /||   \n"
        imgStr+="   |  /  |___|___|___|/|/  \n"
        imgStr+="   | /   |   |   |   | /   \n"
        imgStr+="   |/    |___|___|___|/    \n"


    def img_U():

        imgStr += "       ____________   \n"                      
        imgStr += "      /           /   \n"
        imgStr += "     /           / \n"
        imgStr += "    /___________\n"
        imgStr += "       ___ ___ ___\n"
        imgStr += "      /___/___/___/| \n"  
        imgStr += "     /___/___/___/||  \n"
        imgStr += "    /___/___/__ /|/|  \n"
        imgStr += "   |   |   |   | /||    \n"
        imgStr += "   |___|___|___|/|/|       \n"                
        imgStr += "   |   |   |   | /||   \n"
        imgStr += "   |___|___|___|/|/  \n"
        imgStr += "   |   |   |   | /   \n"
        imgStr += "   |___|___|___|/   \n"

    def img_U2():

        imgStr += "       ____________   \n"                      
        imgStr += "      /           /   \n"
        imgStr += "     /    x2     / \n"
        imgStr += "    /___________\n"
        imgStr += "       ___ ___ ___\n"
        imgStr += "      /___/___/___/| \n"  
        imgStr += "     /___/___/___/||  \n"
        imgStr += "    /___/___/__ /|/|  \n"
        imgStr += "   |   |   |   | /||    \n"
        imgStr += "   |___|___|___|/|/|       \n"                
        imgStr += "   |   |   |   | /||   \n"
        imgStr += "   |___|___|___|/|/  \n"
        imgStr += "   |   |   |   | /   \n"
        imgStr += "   |___|___|___|/   \n"

    def img_Ui():

        imgStr += "       ____________   \n"                      
        imgStr += "      /           /   \n"
        imgStr += "     /           / \n"
        imgStr += "     ___________/ \n"
        imgStr += "       ___ ___ ___\n"
        imgStr += "      /___/___/___/| \n"  
        imgStr += "     /___/___/___/||  \n"
        imgStr += "    /___/___/__ /|/|  \n"
        imgStr += "   |   |   |   | /||    \n"
        imgStr += "   |___|___|___|/|/|       \n"                
        imgStr += "   |   |   |   | /||   \n"
        imgStr += "   |___|___|___|/|/  \n"
        imgStr += "   |   |   |   | /   \n"
        imgStr += "   |___|___|___|/   \n"

    

