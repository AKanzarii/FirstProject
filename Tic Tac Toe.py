import csv
import random
import time


def menu():
    print("Menu :")
    print("1. Jouer")
    print("2. Règles du jeu")
    print("3. Montrez notre Hall of Fame")
    print("4. Reset")
    print("5. Quitter")



def game_rules():
    print("Deux joueurs s'affrontent dans un jeu au tour par tour sur un plateau 3x3 (3 lignes et 3 colonnes).")
    print("Le joueur 1 aura le symbole 'X' tandis que le joueur 2 aura le symbole 'O'.")
    print("Les joueurs doivent placer leurs symboles sur une case vide du plateau en entrant les coordonnées correspondantes pour la case (Exemple : 1,2 ...)")
    print("Les joueurs placent à tour de rôle un symbole à chaque tour. Le but du jeu est d'aligner trois symboles identiques horizontalement, verticalement,")
    print("Si aucun joueur n'arrive à aligner 3 symboles identiques lorsque le plateau est rempli, la partie se termine par un match nul.")
    print("À la fin du jeu, nos gagnants seront enregistrés dans notre 'Hall of Fame' !")
    time.sleep(1.5)
    back_to_main()



def reset():
    print("Tous les données de ce jeu vont etre supprimés!!")
    rep=get_answer2()
    if rep=='O':
        destroy_csv_file()
    time.sleep(1.5)
    back_to_main()
    
def aff(B):
    ch="\t1\t2\t3\n"
    for i in range(3):
        ch+=str(i+1)+'    '
        for j in range(3):
            if j<2:
                ch+='   '+B[i][j]+'   |'
            else:
                ch+='   '+B[i][j]
                
        if i<2:
            ch+='\n    --------+--------+--------\n'
    print(ch)




def input_coords(user):
    while True:
            cord=input("selectionnez une cellule "+user+'\n')
            try:
                cords=cord.split(',')
            except:
                input_coords()
            if cords[0] in ('1','2','3') and cords[1] in ('1','2','3'):
                return cords


            
def get_coord(board,user):
    while True:
        cords=input_coords(user)
        cords_int=[]
        cords_int.append(int(cords[0]))
        cords_int.append(int(cords[1]))
        cords_int=[x-1 for x in cords_int]
        if board[cords_int[0]][cords_int[1]]==' ':
            return cords_int

        
def initialize():
    board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    aff(board)
    return board




def is_final(board):
    diag1=[]
    diag2=[]
    winner1=['X','X','X']
    winner2=['O','O','O']
    for i in range(3):
        column=[]
        diag1.append(board[i][i])
        diag2.append(board[i][2-i])
        for j in range(3):
            column.append(board[j][i])
        if board[i]==winner1:
            return 1;
        if board[i]==winner2:
            return 2;    
        if column==winner1:
            return 1;
        if column==winner2:
            return 2;
    if diag1==winner1:
        return 1;
    if diag1==winner2:
        return 2;
    if diag2==winner1:
        return 1;
    if diag2==winner2:
        return 2;
    return 0



def play(board,first,user1,user2):
    tour=0
    if first==1:
        print("Le joueur "+user1+" Commence.")
        while (is_final(board)==0 and tour<9):
            if tour%2==0:
                cords=get_coord(board,user1)
                board[cords[0]][cords[1]]='X'
            else:
                cords=get_coord(board,user2)
                board[cords[0]][cords[1]]='O'
            tour+=1
            aff(board)
    else:
        print("Le joueur "+user2+" Commence.")
        while (is_final(board)==0 and tour<9):
            if tour%2==0:
                cords=get_coord(board,user2)
                board[cords[0]][cords[1]]='O'
            else:
                cords=get_coord(board,user1)
                board[cords[0]][cords[1]]='X'
            tour+=1
            aff(board)
    return is_final(board)

def get_answer3():
    while True:
        rep=input('Retour à la page Menu??\n')
        if rep.upper() in ['O','N']:
            return rep.upper()


def get_answer2():
    while True:
        rep=input('Voulez vous Continuer??\n')
        if rep.upper() in ['O','N']:
            return rep.upper()



def get_answer():
    while True:
        rep=input('Voulez vous rejouer??\n')
        if rep.upper() in ['O','N']:
            return rep



def get_dict(result,nullgames,user1,user2):
    d={}
    if result==1:
        print(user1+" a gagné")
        d['Gagnant']=user1
        d['Perdant']=user2
        d['Nombre de parties joués']=nullgames+1
    else:
        print(user2+" a gagné")
        d['Gagnant']=user2
        d['Perdant']=user1
        d['Nombre de parties joués']=nullgames+1
    return d



def game():
    fieldnames = ['Gagnant', 'Perdant', 'Nombre de parties joués']
    f=open('Hall_of_fame.csv', 'a', encoding='UTF8', newline='')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    user1=input("Usename du joueur1\n")
    user2=input("Usename du joueur2\n")
    replay='O'
    null_games=0
    while replay.upper()=='O':
        board=initialize()
        random_to_begin=random.randint(1,2)
        print("Coin toss")
        time.sleep(3)
        result=play(board,random_to_begin,user1,user2)
        if result==0:
            null_games+=1
            print("DRAW")
        else:
            d=get_dict(result,null_games,user1,user2)
            writer.writerow(d)
            null_games=0
        replay=get_answer();

    f.close()
    time.sleep(1.5)
    back_to_main()


def destroy_csv_file():
    fieldnames = ['Gagnant', 'Perdant', 'Nombre de parties joués']
    with open('Hall_of_fame.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
    
def access_csv_file():
    fieldnames = ['Gagnant', 'Perdant', 'Nombre de parties joués']
    try:
        f=open('Hall_of_fame.csv', 'r')
        f.close()
    except:
        with open('Hall_of_fame.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

    
def back_to_main():
    rep=get_answer3()
    if rep=='O':
        main()
    
def Hall_of_fame():
    with open('Hall_of_fame.csv', 'r') as f:
        reader = csv.DictReader(f, fieldnames=['Gagnant', 'Perdant', 'Nombre de parties joués'])
        header=next(reader)
        for row in reader:
            print("Vainqueur : "+str(row['Gagnant'])+" - Perdant : "+str(row['Perdant'])+" - Nombre de parties : "+str(row['Nombre de parties joués']))
    time.sleep(3.5)
    back_to_main()
    

def get_choice():
    try:
        choix=int(input('Choisissez\n'))
    except:
        get_choice()
    return choix


def main():
    menu()
    access_csv_file()
    while True:
        choix=get_choice()
        if choix in range(1,6):
            break
    if choix==1:
        game();
    if choix==2:
        game_rules()
    if choix==3:
        Hall_of_fame()
    if choix==4:
        reset()
    if choix==5:
        exit()
main()
