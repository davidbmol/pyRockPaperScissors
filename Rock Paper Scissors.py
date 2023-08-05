def parseName(t, player):
  tItem = iter(t)
  sRes = ""
  #sItem = next(tItem)
  for sItem in tItem:
    s = sItem.lower()
    #print("item", s)

    if s[0] == player.lower():
        sRes = sItem
        print("item", sRes)
        return sRes

  if sRes == "":
    print("parse error: ", player)
  else:
    print("item selected:", sRes)
   
  return sRes


#concatonate for print
def parseConc(sW, s1, sAc, s2):
    #return sW + " " + s1 + " " + sAc + " " + s2
    return "{sW} {s1} {sAc} {s2}".format(sW=sW,s1=s1,sAc=sAc,s2=s2)


# parse and compare
def parseComp(computer, player, t):
    # is it a Tie?
    bTie = False
    #game win/lose 0=l, 1=w
    iWin = -1

    if player[0].lower() == computer[0].lower():
        sRes = ("Tie!")
        bTie = True
    elif player[0].lower() == "r":
        if computer == "Paper":
            #sRes = ("You lose!", computer, "covers", parseName(t,player))
            sRes = parseConc("You lose!", computer, "covers", parseName(t,player)) 
            iWin = 0
        else:
            sRes = parseConc("You win!", parseName(t,player), "smashes", computer)
            iWin = 1
    elif player[0].lower() == "p":
        if computer == "Scissors":
            sRes = parseConc("You lose!",computer,"cut",parseName(t,player))
            iWin = 0
        else:
            sRes = parseConc("You win!",parseName(t,player),"covers",computer)
            iWin = 1
    elif player[0].lower() == "s":
        if computer == "Rock":
            sRes = parseConc("You lose!",computer,"smashes",parseName(t,player))
            iWin = 0
        else:
            sRes = parseConc("You win!",parseName(t,player),"cut",computer)
            iWin = 1
    else:
        sRes = ("Error. Invalid play.")
    print(iWin)
    return sRes, bTie, iWin


###
# Main
###

from random import randint
#from getkey import getkey, keys
from readchar import readkey, key

t = ["Rock", "Paper", "Scissors"]

#counter
countGame = 0
countWon = 0
countLoss = 0


player = False
playing = True

#print(sRes)
while playing:
    playing = False
    #while player == False:
    computer = t[randint(0,2)]
    b = True
    while b:
        b = False

        #player = input("Rock, Paper, Scissors?")
        print("Rock, Paper, Scissors?")
        player = readkey()
        if parseName(t, player) == "":
            b = True
    print("valasztas neve:",parseName(t,player))
    #exit()
    # parseComp ret: string, bool
    aRes = parseComp(computer,player,t)
    a = iter(aRes)
    strRes = next(a)
    isTie = next(a)
    isWin = next(a)

    print (strRes)
    ++countGame
    if isTie:
        playing = True
    if isWin>0:
        ++countWon

    b = True
    while b:
        b = False
        print("Play again? y/n:")
        plAg = readkey()
        if plAg == "y":
          playing = True
        elif plAg == "n":
            exit()
        else:
            print("Error. Invalid response" )
            b = True
#end while playing
print("=====")


# end of code
exit()













"""    if player[0].lower() == computer[0].lower():
        print("Tie!")
        playing = True
        player= False
    elif player[0].lower() == "r":
        #rUp = player[0].lower().replace(player[0].lower(), "Rock")
        if computer == "Paper":
            print("You lose!", computer, "covers", parseName(t,player))
        else:
            print("You win!", parseName(t,player), "smashes", computer)
    elif player[0].lower() == "p":
        #pUp = player[0].lower().replace(player[0].lower(), "Paper")
        if computer == "Scissors":
            print("You lose!", computer, "cut", p)
        else:
            print("You win!", p, "covers", computer)
    elif player[0].lower() == "s":
        #sUp = player[0].lower().replace(player[0].lower(), "Scissor")
        if computer == "Rock":
            print("You lose!", computer, "smashes", s)
        else:
            print("You win!", s, "cut", computer)
    else:
        print("Error. Invalid play.")"""




