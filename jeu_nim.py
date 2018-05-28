import random as r
import math as m
def nouveauTas():
    return [r.randrange(5,24) for i in range(r.randrange(3,8))]
def calculScore(tour):
    tot=0
    for i in range(m.ceil(tour/2)): 
        tot+=i*(10**i)
    return tot
    
def printTop10():
    print("Top 10:")
    scoreList=[]
    index=0
    listrange=0
  
    with open("save.txt",'r') as save:
        for best in save:
            scoreList.append([best.strip('\n').split(':')[0],best.strip('\n').split(':')[2]])
    if len(scoreList) <10:
        listrange=len(scoreList)
    else:
        listrange=10
    for l in range(listrange):
        index=0
        maximum=int(scoreList[0][1])
        for i in range(len(scoreList)):
            if int(scoreList[i][1])>maximum:
                maximum=int(scoreList[i][1])
                index=i 
        print(l+1,".",scoreList[index][0],":",maximum)
        scoreList.remove(scoreList[index])
             
            
    
def setup():
    global nomJoueur1
    global nomJoueur2
    global ancienScore1
    global ancienScore2
    global bestScore1
    global bestScore2
    
    
    nomJoueur1,nomJoueur2=("A déterminer","A déterminer")
    ancienScore1,bestScore1,ancienScore2,bestScore2=0,0,0,0
    joueur1=input("Joueur 1 entrez votre nom: ")
    joueur2=input("Joueur 2 entrez votre nom: ")
    with open("save.txt",'r') as save:
        for ligne in save:
            if ligne.split(':')[0]==joueur1:
                nomJoueur1,ancienScore1,bestScore1=ligne.strip('\n').split(':')
                
            if ligne.split(':')[0]==joueur2:
                nomJoueur2,ancienScore2,bestScore2=ligne.strip('\n').split(':')
                
    if nomJoueur1=="A déterminer":
        nomJoueur1=joueur1
    if nomJoueur2=="A déterminer":
        nomJoueur2=joueur2
    
def printGame(tas):
    string=""
    for i in range(len(tas)):
        string+=str(i+1)+"|"
        for piece in range(tas[i]):
            string+="*"
        for espace in range(23-tas[i]):
            string+=" "
        print(string,"| ",tas[i])
        string=""
def nbrPieceTotal(tas):
    total=0
    for i in tas:
        total+=i
    return total
def play():
    tas=nouveauTas()
    setup()
    print("Joueur1:",nomJoueur1,"| Score partie précédente:",ancienScore1,"| Meilleur Score:",bestScore1)
    print("Joueur2:",nomJoueur2,"| Score partie précédente:",ancienScore2,"| Meilleur Score:",bestScore2)
    tour=1
    while True:
        if tour%2==0:
            print("Au tour de",nomJoueur2)
        else:
            print("Au tour de",nomJoueur1)
        
        printGame(tas)
        print("Choisissez un tas: ")
        numTas=int(input())
        print("Choisissez un nombre de pieces: ")
        nbrPiece=int(input())
        try:
            if tas[numTas-1] or tas[numTas-1]<=0:
                if nbrPiece<=23 and nbrPiece>0:
                    if nbrPieceTotal(tas)-nbrPiece <1:
                        score=calculScore(tour)
                        f = open("save.txt","r")
                        lignes = f.readlines()
                        f.close()
                        if tour%2==0:
                            print(nomJoueur1," GAGNE LA PARTIE ! SCORE:",score)
                            
                            with open("save.txt",'w') as save:
                                    for ligne in lignes:
                                        if ligne.split(':')[0]==nomJoueur1:
                                            pass
                                        else:
                                            save.write(ligne)
                            with open("save.txt",'a') as save:
                                
                                if score>int(bestScore1):
                                    save.write("{}:{}:{}\n".format(nomJoueur1,score,score))
                                else:
                                    save.write("{}:{}:{}\n".format(nomJoueur1,score,bestScore1))

                        else:
                            print(nomJoueur2," GAGNE LA PARTIE ! SCORE:",score)
                            with open("save.txt",'w') as save:
                                    for ligne in lignes:
                                        if ligne.split(':')[0]==nomJoueur2:
                                            pass
                                        else:
                                            save.write(ligne)
                            with open("save.txt",'a') as save:
                                if score>int(bestScore1):
                                    save.write("{}:{}:{}\n".format(nomJoueur2,score,score))
                                else:
                                    save.write("{}:{}:{}\n".format(nomJoueur2,score,bestScore2))
                        print("Game Over!")
                        printTop10()
                        break  
                
                    if tas[numTas-1]-nbrPiece >=0:
                        tas[numTas-1]-=nbrPiece
                        tour+=1
                else:
                    print("Choix du nombre de pieces invalide")
            else:
                print("Choix du tas invalide")
        except:
            print("Il y a eu une erreur veuillez réessayer!")
    nouvPartie=input("Voulez vous lancer une nouvelle partie? oui/non  ")
    if nouvPartie=="oui":
        play()
    else:
        print("Au revoir")
        
play()	
