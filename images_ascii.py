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
    
    def img_B(self):
        imgStr = ""
        imgStr+=("                    __________\n");
        imgStr+=("                   |          |\n");
        imgStr+=("                   |          |\n");
        imgStr+=("                  \/          |\n");
        imgStr+=("             ___ ___  ___     |\n");
        imgStr+=("            /___/___/___/|    |\n");
        imgStr+=("           /___/___/___/||____|\n");
        imgStr+=("          /___/___/__ /|/|  \n");
        imgStr+=("         |   |   |   | /||   \n");
        imgStr+=("         |___|___|___|/|/|   \n");               
        imgStr+=("         |   |   |   | /||   \n");
        imgStr+=("         |___|___|___|/|/  \n");
        imgStr+=("         |   |   |   | /   \n");
        imgStr+=("         |___|___|___|/     \n");

        return imgStr

    def img_B2(self):
        imgStr = ""
        imgStr+=("                    __________\n");
        imgStr+=("                   |          |\n");
        imgStr+=("                   |     x2   |\n");
        imgStr+=("                  \/          |\n");
        imgStr+=("             ___ ___  ___     |\n");
        imgStr+=("            /___/___/___/|    |\n");
        imgStr+=("           /___/___/___/||____|\n");
        imgStr+=("          /___/___/__ /|/|  \n");
        imgStr+=("         |   |   |   | /||   \n");
        imgStr+=("         |___|___|___|/|/|   \n");               
        imgStr+=("         |   |   |   | /||   \n");
        imgStr+=("         |___|___|___|/|/  \n");
        imgStr+=("         |   |   |   | /   \n");
        imgStr+=("         |___|___|___|/     \n");

        return imgStr

    def img_Bi(self):
        imgStr = ""
        imgStr+=("                    __________\n");
        imgStr+=("                   |          |\n");
        imgStr+=("                   |          |\n");
        imgStr+=("                   |          |\n");
        imgStr+=("             ___ __|_ ___     \/\n");
        imgStr+=("            /___/___/___/|     \n");
        imgStr+=("           /___/___/___/||____\n");
        imgStr+=("          /___/___/__ /|/|  \n");
        imgStr+=("         |   |   |   | /||   \n");
        imgStr+=("         |___|___|___|/|/|   \n");               
        imgStr+=("         |   |   |   | /||   \n");
        imgStr+=("         |___|___|___|/|/  \n");
        imgStr+=("         |   |   |   | /   \n");
        imgStr+=("         |___|___|___|/     \n");

        return imgStr

    def img_F(self):
        imgStr = ""
        imgStr += ("                            \n") 
        imgStr += ("                            \n") 
        imgStr += ("                            \n") 
        imgStr += ("                            \n") 
        imgStr += ("             ____ ___ ___\n")
        imgStr += ("            /___/___/___/|   \n")
        imgStr += ("           /___/___/___/||  \n")
        imgStr += ("          /___/___/__ /|/|  \n")
        imgStr += ("         |   |   |   | /||    \n")
        imgStr += ("         |___|___|___|/|/|      \n")                 
        imgStr += ("      ___|___|__ |   | /||    \n")
        imgStr += ("     |   |___|__||___|/|/   \n")
        imgStr += ("     |   |   |  ||   | /    \n")
        imgStr += ("     |   |___|__||___|/  \n")
        imgStr += ("     |          |       \n")
        imgStr += ("     |          \/     \n")
        imgStr += ("     |__________       \n")
        imgStr += ("                  \n")
        imgStr += ("                  \n")
        imgStr += ("                  \n")
        imgStr += ("                   \n")
        return imgStr

    def img_F2(self):
        imgStr = ""
        imgStr += ("                            \n") 
        imgStr += ("                            \n") 
        imgStr += ("                            \n") 
        imgStr += ("                            \n") 
        imgStr += ("             ____ ___ ___\n")
        imgStr += ("            /___/___/___/|   \n")
        imgStr += ("           /___/___/___/||  \n")
        imgStr += ("          /___/___/__ /|/|  \n")
        imgStr += ("         |   |   |   | /||    \n")
        imgStr += ("         |___|___|___|/|/|      \n")                 
        imgStr += ("      ___|___|__ |   | /||    \n")
        imgStr += ("     |   |___|__||___|/|/   \n")
        imgStr += ("     |   |   |  ||   | /    \n")
        imgStr += ("     |   |___|__||___|/  \n")
        imgStr += ("     |          |       \n")
        imgStr += ("     |    x2    \/     \n")
        imgStr += ("     |__________       \n")
        imgStr += ("                  \n")
        imgStr += ("                  \n")
        imgStr += ("                  \n")
        imgStr += ("                   \n")
        return imgStr

    def img_Fi(self):
        imgStr = ""
        imgStr += ("                        \n") 
        imgStr += ("                        \n") 
        imgStr += ("                        \n") 
        imgStr += ("                        \n") 
        imgStr += ("             ____ ___ ___\n")
        imgStr += ("            /___/___/___/|   \n")
        imgStr += ("           /___/___/___/||  \n")
        imgStr += ("          /___/___/__ /|/|  \n")
        imgStr += ("         |   |   |   | /||    \n")
        imgStr += ("         |___|___|___|/|/|      \n")                 
        imgStr += ("      ___|___|__ |   | /||    \n")
        imgStr += ("     |   |___|__||___|/|/   \n")
        imgStr += ("     |   |   |  ||   | /    \n")
        imgStr += ("     |   |___|__||___|/  \n")
        imgStr += ("     |          |       \n")
        imgStr += ("     \/         |     \n")
        imgStr += ("      __________|       \n")
        imgStr += ("                  \n")
        imgStr += ("                  \n")
        imgStr += ("                  \n")
        imgStr += ("                   \n")
        return imgStr

    def img_L(self):
        imgStr = ""
        imgStr+="                        \n" 
        imgStr+="                        \n" 
        imgStr+="                        \n" 
        imgStr+="                        \n" 
        imgStr+="             ____ ___ ___\n"
        imgStr+="      /|    /___/___/___/|   \n"
        imgStr+="     / |   /___/___/___/||  \n"
        imgStr+="    /  |  /___/___/__ /|/|  \n"
        imgStr+="   |   | |   |   |   | /||    \n"
        imgStr+="   |   | |___|___|___|/|/|   \n"                    
        imgStr+="   \/  | |   |   |   | /||   \n"
        imgStr+="      /  |___|___|___|/|/  \n"
        imgStr+="     /   |   |   |   | /   \n"
        imgStr+="    /    |___|___|___|/    \n"
        return imgStr

    def img_L2(self):
        imgStr = ""
        imgStr+="                        \n" 
        imgStr+="                        \n" 
        imgStr+="                        \n" 
        imgStr+="                        \n" 
        imgStr+="             ____ ___ ___\n"
        imgStr+="      /|    /___/___/___/|   \n"
        imgStr+="     / |   /___/___/___/||  \n"
        imgStr+="    /  |  /___/___/__ /|/|  \n"
        imgStr+="   |   | |   |   |   | /||    \n"
        imgStr+="   | x2| |___|___|___|/|/|   \n"                    
        imgStr+="   \/  | |   |   |   | /||   \n"
        imgStr+="      /  |___|___|___|/|/  \n"
        imgStr+="     /   |   |   |   | /   \n"
        imgStr+="    /    |___|___|___|/    \n"
        return imgStr

    def img_Li(self):
        imgStr = ""
        imgStr+="                        \n" 
        imgStr+="                        \n" 
        imgStr+="                        \n" 
        imgStr+="                        \n" 
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
        return imgStr

    def img_U(self):
        imgStr = ""
        imgStr+="                        \n" 
        imgStr += "             ____________   \n"                      
        imgStr += "            /           /   \n"
        imgStr += "           /           \/ \n"
        imgStr += "          /___________\n"
        imgStr += "             ___ ___ ___\n"
        imgStr += "            /___/___/___/| \n"  
        imgStr += "           /___/___/___/||  \n"
        imgStr += "          /___/___/__ /|/|  \n"
        imgStr += "         |   |   |   | /||    \n"
        imgStr += "         |___|___|___|/|/|       \n"                
        imgStr += "         |   |   |   | /||   \n"
        imgStr += "         |___|___|___|/|/  \n"
        imgStr += "         |   |   |   | /   \n"
        imgStr += "         |___|___|___|/   \n"
        return imgStr

    def img_U2(self):
        imgStr = ""
        imgStr+="                        \n" 
        imgStr += "             ____________   \n"                      
        imgStr += "            /           /   \n"
        imgStr += "           /    x2     \/ \n"
        imgStr += "          /___________\n"
        imgStr += "             ___ ___ ___\n"
        imgStr += "            /___/___/___/| \n"  
        imgStr += "           /___/___/___/||  \n"
        imgStr += "          /___/___/__ /|/|  \n"
        imgStr += "         |   |   |   | /||    \n"
        imgStr += "         |___|___|___|/|/|       \n"                
        imgStr += "         |   |   |   | /||   \n"
        imgStr += "         |___|___|___|/|/  \n"
        imgStr += "         |   |   |   | /   \n"
        imgStr += "         |___|___|___|/   \n"
        return imgStr

    def img_Ui(self):
        imgStr = ""
        imgStr+="                        \n" 
        imgStr += "             ____________   \n"                      
        imgStr += "            /           /   \n"
        imgStr += "           \/          / \n"
        imgStr += "           ___________/ \n"
        imgStr += "             ___ ___ ___\n"
        imgStr += "            /___/___/___/| \n"  
        imgStr += "           /___/___/___/||  \n"
        imgStr += "          /___/___/__ /|/|  \n"
        imgStr += "         |   |   |   | /||    \n"
        imgStr += "         |___|___|___|/|/|       \n"                
        imgStr += "         |   |   |   | /||   \n"
        imgStr += "         |___|___|___|/|/  \n"
        imgStr += "         |   |   |   | /   \n"
        imgStr += "         |___|___|___|/   \n"
        return imgStr

    def img_D(self):
        imgStr = ""     
        imgStr+="                             \n" 
        imgStr+="                             \n" 
        imgStr+="                             \n" 
        imgStr+="                             \n" 
        imgStr+="             ___ ___ ___    \n"
        imgStr+="            /___/___/___/|   \n"
        imgStr+="           /___/___/___/||  \n"
        imgStr+="          /___/___/__ /|/|  \n"
        imgStr+="         |   |   |   | /||   \n" 
        imgStr+="         |___|___|___|/|/|   \n"                    
        imgStr+="         |   |   |   | /||   \n"
        imgStr+="         |___|___|___|/|/  \n"
        imgStr+="         |   |   |   | /   \n"
        imgStr+="         |___|___|___|/       \n"  
        imgStr+="            ____________         \n"                
        imgStr+="           /           /   \n"
        imgStr+="          \/          / \n"
        imgStr+="          ___________/ \n"
        return imgStr

    def img_D2(self):
        imgStr = ""    
        imgStr+="                             \n" 
        imgStr+="                             \n" 
        imgStr+="                             \n" 
        imgStr+="                             \n" 
        imgStr+="             ___ ___ ___    \n"
        imgStr+="            /___/___/___/|   \n"
        imgStr+="           /___/___/___/||  \n"
        imgStr+="          /___/___/__ /|/|  \n"
        imgStr+="         |   |   |   | /||   \n" 
        imgStr+="         |___|___|___|/|/|   \n"                    
        imgStr+="         |   |   |   | /||   \n"
        imgStr+="         |___|___|___|/|/  \n"
        imgStr+="         |   |   |   | /   \n"
        imgStr+="         |___|___|___|/       \n"  
        imgStr+="            ____________         \n"                
        imgStr+="           /           /   \n"
        imgStr+="          \/   x2     / \n"
        imgStr+="          ___________/ \n"
        return imgStr

    def img_Di(self):
        imgStr = ""
        imgStr+="                             \n" 
        imgStr+="                             \n" 
        imgStr+="                             \n" 
        imgStr+="                             \n" 
        imgStr+="             ___ ___ ___    \n"
        imgStr+="            /___/___/___/|   \n"
        imgStr+="           /___/___/___/||  \n"
        imgStr+="          /___/___/__ /|/|  \n"
        imgStr+="         |   |   |   | /||   \n" 
        imgStr+="         |___|___|___|/|/|   \n"                    
        imgStr+="         |   |   |   | /||   \n"
        imgStr+="         |___|___|___|/|/  \n"
        imgStr+="         |   |   |   | /   \n"
        imgStr+="         |___|___|___|/       \n"  
        imgStr+="            ____________         \n"                
        imgStr+="           /           /   \n"
        imgStr+="          /           \/ \n"
        imgStr+="         /___________ \n"
        return imgStr

    def img_R(self):
        imgStr = ""
        imgStr+="                             \n" 
        imgStr+="                             \n" 
        imgStr+="                             \n" 
        imgStr+="                             \n" 
        imgStr+="             ___ ___ ___          \n"
        imgStr+="            /___/___/___/|    /|  \n"
        imgStr+="           /___/___/___/||   / |  \n"
        imgStr+="          /___/___/__ /|/|  /  |\n"
        imgStr+="         |   |   |   | /|| |   |\n"
        imgStr+="         |___|___|___|/|/| |   \/  \n"                  
        imgStr+="         |   |   |   | /|| |       \n"
        imgStr+="         |___|___|___|/|/  |  /   \n"
        imgStr+="         |   |   |   | /   | /     \n"
        imgStr+="         |___|___|___|/    |/      \n"
        return imgStr

    def img_R2(self):
        imgStr = ""
        imgStr+="                             \n" 
        imgStr+="                             \n" 
        imgStr+="                             \n" 
        imgStr+="                             \n" 
        imgStr+="             ___ ___ ___          \n"
        imgStr+="            /___/___/___/|    /|  \n"
        imgStr+="           /___/___/___/||   / |  \n"
        imgStr+="          /___/___/__ /|/|  /  |\n"
        imgStr+="         |   |   |   | /|| |   |\n"
        imgStr+="         |___|___|___|/|/| |   \/  \n"                  
        imgStr+="         |   |   |   | /|| | x2    \n"
        imgStr+="         |___|___|___|/|/  |  /   \n"
        imgStr+="         |   |   |   | /   | /     \n"
        imgStr+="         |___|___|___|/    |/      \n"
        return imgStr

    def img_Ri(self):
        imgStr = ""
        imgStr+="                             \n" 
        imgStr+="                             \n" 
        imgStr+="                             \n" 
        imgStr+="                             \n" 
        imgStr+="             ___ ___ ___          \n"
        imgStr+="            /___/___/___/|     /|  \n"
        imgStr+="           /___/___/___/||    / |  \n"
        imgStr+="          /___/___/__ /|/|   /  |\n"
        imgStr+="         |   |   |   | /||  |   |\n"
        imgStr+="         |___|___|___|/|/|  |   |  \n"                  
        imgStr+="         |   |   |   | /||  |   |    \n"
        imgStr+="         |___|___|___|/|/   \/ /   \n"
        imgStr+="         |   |   |   | /      /     \n"
        imgStr+="         |___|___|___|/      /      \n" 
        return imgStr