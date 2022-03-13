
###########################게임 보드 구현과 카드 목록을 다루는 함수들을 구현해놓았습니다.########################

#덱 생성 함수
import random
def fresh_deck():
    suits = {"Spade", "Heart", "Diamond", "Club","Jocker"}
    ranks = {"A", 2, 3, 4, 5, 6, 7, 8, 9, 0, "J", "Q", "K","Black","Color"}
    deck = []
    co=0
    for i in suits :
        for j in ranks:
            if i == "Jocker" and co == 0 :
                deck.append({"suit": i, "rank": "Black"})
                deck.append({"suit": i, "rank": "Color"})
                co+=1
            if i != "Jocker" and j != "Black" and j != "Color" :
                deck.append({"suit": i, "rank": j})
                
    random.shuffle(deck)

    return deck

#더할지 물어보기
def more(message):
    answer = input(message)
    while not (str(answer)=="y" or str(answer)=="n"):
        answer = input(message)
    return str(answer)=="y"


#카드뽑기함수
def hit(deck):
    if deck == []:
        fresh_deck()
    return deck[0], deck[1:]


#보드를 구현하는 함수
def board(p1c,p2c,p1l,p2l,d,deck):
    p1cb1=[] # = 실제 플레이어 1의 카드 목록
    p1cb2=[] # = 실제 플레이어 2의 카드 목록
    p2cb1=[] # = 플레이어 1의 카드목록을 판 형식에 맞추기 위해 모양만 str목록으로  저장해놓은 목록
    p2cb2=[] # = 플레이어 2의 카드목록을 판 형식에 맞추기 위해 모양만 str목록으로  저장해놓은 목록
    
    def lifehp1() :  #플레이어 1의 생명력에 따라 하트 모양을 구현해주는 함수
        if (50<=int(p1l) ):
            return "♥♥♥♥♥"
        if  (40<=int(p1l)<50) :
            return "♥♥♥♥"
        if  (30<=int(p1l)<40) :
            return "♥♥♥♡"
        if (20<=int(p1l)<30) :
            return "♥♥♡♡"
        if  (10<=int(p1l)<20) :
            return "♥♡♡♡"
        if  int(p1l)<10 :
            return "⟁⟁⟁⟁⟁⟁"
    def lifehp2() : #플레이어 2의 생명력에 따라 하트 모양을 구현해주는 함수
        if (50<=int(p2l) ):
            return "♥♥♥♥♥"
        if  (40<=int(p2l)<50) :
            return "♥♥♥♥"
        if  (30<=int(p2l)<40) :
            return "♥♥♥♡"
        if (20<=int(p2l)<30) :
            return "♥♥♡♡"
        if  (10<=int(p2l)<20) :
            return "♥♡♡♡"
        if  int(p2l)<10 :
            return "⟁⟁⟁⟁⟁⟁" 

    for i in p1c : # 플레이어 1의 목록을 판의 형식에 따라 str형식으로 넣어두기 위하여 for문을 이용.
        if i["suit"] == "Diamond" :
            p1cb1.append("◆ "+str(i['rank']))
        if i["suit"] == "Heart":
            p1cb1.append("♥ "+str(i['rank']))
        if i["suit"] == "Spade":
            p1cb1.append("♠ "+str(i['rank']))
        if i["suit"] == "Club":
            p1cb1.append("♣ "+str(i['rank']))
        if i["suit"] == "Jocker" :
            if i['rank'] == "Black":
                p1cb1.append("☠ B")
            if i['rank'] == "Color":
                p1cb1.append("☠ C")
    for i in p1c : 
        if i["suit"] == "Diamond" :
            p1cb2.append(str(i['rank'])+" ◆")
        if i["suit"] == "Heart":
            p1cb2.append(str(i['rank'])+" ♥")
        if i["suit"] == "Spade":
            p1cb2.append(str(i['rank'])+" ♠")
        if i["suit"] == "Club":
            p1cb2.append(str(i['rank'])+" ♣")
        if i["suit"] == "Jocker" :
            if i['rank'] == "Black":
                p1cb2.append("B ☠")
            if i['rank'] == "Color":
                p1cb2.append("C ☠")
            
    if len(p1c) != 7 : #플레이이어 카드가 7개가 안될경우 보드의 빈칸에 표현할 그림을 넣는 단계
        for i in range(7-len(p1c)):
            p1cb1.append("X  X")
            p1cb2.append("X  X")

    for i in p2c : # 플레이어 2의 목록을 판의 형식에 따라 str형식으로 넣어두기 위하여 for문을 이용.
        if i["suit"] == "Diamond" :
            p2cb1.append("◆ "+str(i['rank']))
        if i["suit"] == "Heart":
            p2cb1.append("♥ "+str(i['rank']))
        if i["suit"] == "Spade":
            p2cb1.append("♠ "+str(i['rank']))
        if i["suit"] == "Club":
            p2cb1.append("♣ "+str(i['rank']))
        if i["suit"] == "Jocker" :
            if i['rank'] == "Black":
                p2cb1.append("☠ B")
            if i['rank'] == "Color":
                p2cb1.append("☠ C")
    for i in p2c :
        if i["suit"] == "Diamond" :
            p2cb2.append(str(i['rank'])+" ◆")
        if i["suit"] == "Heart":
            p2cb2.append(str(i['rank'])+" ♥")
        if i["suit"] == "Spade":
            p2cb2.append(str(i['rank'])+" ♠")
        if i["suit"] == "Club":
            p2cb2.append(str(i['rank'])+" ♣")
        if i["suit"] == "Jocker" :
            if i['rank'] == "Black":
                p2cb2.append("B ☠")
            if i['rank'] == "Color":
                p2cb2.append("C ☠")
            
    if len(p2c) != 7 : #플레이이어 카드가 7개가 안될경우 보드의 빈칸에 표현할 그림을 넣는 단계
        for i in range(7-len(p2c)):
            p2cb1.append("X  X")
            p2cb2.append("X  X")


            
               
    print("                          P1 Life is:"+ str(p1l))
    print("                          ",str(lifehp1()))
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃                                                          ┃")
    print("┃ ┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐ ┃")
    print("┃ │"+str(p1cb1[0])+"││"+str(p1cb1[1])+"││"+str(p1cb1[2])+"││"+str(p1cb1[3])+"││"+str(p1cb1[4])+"││"+str(p1cb1[5])+"││"+str(p1cb1[6])+"│ ┃")
    print("┃ │    ││    ││    ││    ││    ││    ││    │ ┃")
    print("┃ │"+str(p1cb2[0])+"││"+str(p1cb2[1])+"││"+str(p1cb2[2])+"││"+str(p1cb2[3])+"││"+str(p1cb2[4])+"││"+str(p1cb2[5])+"││"+str(p1cb2[6])+"│ ┃")
    print("┃ └──┘└──┘└──┘└──┘└──┘└──┘└──┘ ┃")
    print("┃                                                          ┃")
    print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    print("┃                                                          ┃")
    print("┃ ┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐ ┃")
    print("┃ │"+str(p2cb1[0])+"││"+str(p2cb1[1])+"││"+str(p2cb1[2])+"││"+str(p2cb1[3])+"││"+str(p2cb1[4])+"││"+str(p2cb1[5])+"││"+str(p2cb1[6])+"│ ┃")
    print("┃ │    ││    ││    ││    ││    ││    ││    │ ┃")
    print("┃ │"+str(p2cb2[0])+"││"+str(p2cb2[1])+"││"+str(p2cb2[2])+"││"+str(p2cb2[3])+"││"+str(p2cb2[4])+"││"+str(p2cb2[5])+"││"+str(p2cb2[6])+"│ ┃")
    print("┃ └──┘└──┘└──┘└──┘└──┘└──┘└──┘ ┃")
    print("┃                                                          ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print("                          ",str(lifehp2()))
    print("                         P2 Life is:"+ str(p2l))


