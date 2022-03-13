from board import*
import time

############## 게임 규칙에 따른 경우를 구현하여 게임을 실행할수 있도록 구현해놓은 내부함수 입니다.##########################

#모든 함수는 조건이 걸리지 않는 한 아래로 내려가서 맨 아래에서 처리해주는 방식으로 구현.
#단,중복적으로 걸릴 위험이 있는 함수는 미리 return처리를 하거나 변수를 지정하여 특정 조건을 만족할떄 돌아가도록 설계.
#Class 강의가 올라왔을때 이미 코드를 많이 구현해놓은 상태라서 사용은 못하였기 때문에 변수가 계속 필요하기 때문에
# 필요한 변수들은 계속 가지고 다니도록 설계.

#맨 밑에 게임만 구동하는 전체 함수가 있음.

def countdown(n): #카드 천천히 보여줄 때 사용
    if n > 0:              
        time.sleep(1)
        countdown(n-1)
    else:                   
        return

def countjocker(n):
    if n > 0:
        print("궁금하지?")
        time.sleep(1)
        countjocker(n-1)
    else:                   
        return


#순서프린트함수
def printturn(playercount):
    if playercount%2 == 1:
        print("Player 1의 차례입니다") 
    else :
        print("Player 2의 차례입니다")
#순서 작게프린트
def printsmallturn(d):
    if d%2 == 1:
        return "P1"
    else :
        return "P2"
        
#카드가 7장 넘으면 소멸을 알려주는 함수
def cardover(p1c,p2c,p1l,p2l,d,deck):
    if d==1 :
        if len(p1c) >= 7 :
            print("카드가 7장이 넘어 소멸되었습니다")
    if d==2 :
        if len(p2c) >= 7 :
            print("카드가 7장이 넘어 소멸되었습니다")
    

def more(message):
    answer = input(message)
    while not (str(answer)=="y" or str(answer)=="n"):
        answer = input(message)
    return str(answer)=="y"

#카드뽑기 함수
def hit(deck):
    if deck == []:
        fresh_deck()
    return deck[0], deck[1:]

#순서 세기  함수
def countturn(playercount) :
    playercount+=1
    return playercount

#공격 당할 카드 몇번째카드 선택할지 묻기함수
def cardselect2(p1c,p2c,p1l,p2l,d,deck):
    if d == 1:
        while True:
            try :
                x = int(input("몇번째 카드를 공격하시겠습니까?"))
                if not 0 < x <=int(len(p2c)): raise NegativeInteger
                return int(x-1)
                
            except ValueError :
                print("Error:정수만 입력해주세요.")
            except NegativeInteger :
                print("Error:카드 범위에 맞게 입력해주세요.")

    if d == 2:
        while True:
            try :
                x = int(input("몇번째 카드를 공격하시겠습니까?"))
                if not 0 < x <=int(len(p1c)): raise NegativeInteger
                return int(x-1)
                
            except ValueError :
                print("Error:정수만 입력해주세요.")
            except NegativeInteger :
                print("Error:카드 범위에 맞게 입력해주세요.")


#특수카드 처리함수
import random
def spcardfind(p1c,p2c,p1l,p2l,d,deck):
    if d==1:
        for i in p1c :
            if i["rank"] == "A" :
                countdown(0.5)
                if i["suit"]=="Spade":
                    p1c.remove(i)
                    p2l=p2l-10
                    print("Spade A 특수카드 발동! Spade A 카드로 Player 2의 생명력을 -10 합니다.")
                    board(p1c,p2c,p1l,p2l,d,deck)
                else:
                    ss = int(input("A 특수카드를 보유 중입니다."+"\n"+"1.자신의 생명력을 +5 한다."+"\n"+"2.상대의 생명력을 -5 한다."+"\n"+"무엇을 선택하시겠습니까?(1 / 2)"))
                    if ss==1:
                        p1l=p1l+5
                        p1c.remove(i)
                        print("A 특수카드 발동! A 카드로 Player 1의 생명력을 +5 합니다.")
                        board(p1c,p2c,p1l,p2l,d,deck)
                    
                    if ss==2:
                        p2l=p2l-5
                        p1c.remove(i)
                        print("A 특수카드 발동! A 카드로 Player 2의 생명력을 -5 합니다.")
                        board(p1c,p2c,p1l,p2l,d,deck)
                    
                           
            if i["rank"] == "K":
                countdown(0.5)
                p1c.remove(i)
                card, deck = hit(deck)
                p1c.append(card)
                if len(p1c) < 7 : 
                    card, deck = hit(deck)
                    p1c.append(card)
                    print("K 특수카드 발동! K 카드를 버린 뒤 카드 2장을 뽑았습니다.")
                    board(p1c,p2c,p1l,p2l,d,deck)
                else: #7장 꽉 차서 1장만 뽑을 수 있음
                    print("K 특수카드 발동! K 카드를 버린 뒤 카드 1장을 뽑았습니다.")
                    board(p1c,p2c,p1l,p2l,d,deck)
              
            if i["rank"] == "Q":
                countdown(0.5)
                p1c.remove(i)
                card, deck = hit(deck)
                p2c.append(card)
                board(p1c,p2c,p1l,p2l,d,deck)
                print("Q 특수카드 발동 ! Q 카드를 버린 뒤에 상대에게 한장이 주어지며 상대의 턴은 무시됩니다!")
                return p1c,p2c,p1l,p2l,4,deck
                
            if i["rank"] == "J" :
                countdown(0.5)
                p1c.remove(i)
                if len(p1c) == 0 : #J 없애고 패에 카드 없을 때 
                    print("J 특수카드 발동! 패에 카드가 없으므로 1장을 뽑았습니다.")
                else :
                    randomcard=p1c[random.randrange(len(p1c))]
                    p1c.remove(randomcard)
                    print("J 특수카드 발동! 패의 카드를 1장 제거 후 1장을 뽑았습니다.")
                card, deck = hit(deck)
                p1c.append(card)
                board(p1c,p2c,p1l,p2l,d,deck)
                                   
            if i["suit"] == "Jocker" :
                countdown(0.5)
                if i['rank'] == "Black":
                    if more("특수카드 Black Jocker를 사용하시겠습니까?(y/n)"):
                        k=random.randrange(2)
                        countjocker(5)
                        if k == 0:
                            p1l -= 20
                            print("Black Jocker 특수카드 발동! Player 1의 생명력을 -20 합니다.")
                            p1c.remove(i)
                            board(p1c,p2c,p1l,p2l,d,deck)
                        else :
                            p2l -= 20
                            print("Black Jocker 특수카드 발동! Player 2의 생명력을 -20 합니다.")
                            p1c.remove(i)
                            board(p1c,p2c,p1l,p2l,d,deck)
                if i['rank'] == "Color":
                    p2l=p2l-20
                    print("Color Jocker 특수카드 발동! Player 2의 생명력을 -20 합니다.")
                    p1c.remove(i)
                    board(p1c,p2c,p1l,p2l,d,deck) 
           
        return p1c,p2c,p1l,p2l,d,deck
    
    if d==2:
        for i in p2c :
            if i["rank"] == "A" :
                countdown(0.5)
                if i["suit"]=="Spade":
                    p1l=p1l-10
                    p2c.remove(i)
                    print("Spade A 특수카드 발동! Spade A 카드로 Player 1의 생명력을 -10 합니다.")
                    board(p1c,p2c,p1l,p2l,d,deck)
                    
                else:
                    ss = int(input("1.자신의 생명력을 +5 한다."+"\n"+"2.상대의 생명력을 -5 한다."+"\n"+"무엇을 선택하시겠습니까?(1 / 2)"))
                    if ss==1:
                        p2l=p2l+5
                        print("A 특수카드 발동! A 카드로 Player 2의 생명력을 +5 합니다.")
                        p2c.remove(i)
                        board(p1c,p2c,p1l,p2l,d,deck)
                    if ss==2:
                        p1l=p1l-5
                        print("A 특수카드 발동! A 카드로 Player 1의 생명력을 -5 합니다.")
                        p2c.remove(i)
                        board(p1c,p2c,p1l,p2l,d,deck)
               
            if i["rank"] == "K":
                countdown(0.5)
                p2c.remove(i)
                card, deck = hit(deck)
                p2c.append(card)
                if len(p2c) < 7:
                    card, deck = hit(deck)
                    p2c.append(card)
                    print("K 특수카드 발동! K 카드를 버린 뒤 카드 2장을 뽑았습니다.")
                    board(p1c,p2c,p1l,p2l,d,deck)
                else:
                    print("K 특수카드 발동! K 카드를 버린 뒤 카드 1장을 뽑았습니다.")
                    board(p1c,p2c,p1l,p2l,d,deck)

             
            if i["rank"] == "Q":
                countdown(0.5)
                p2c.remove(i)
                card, deck = hit(deck)
                p1c.append(card)
                print("Q 특수카드 발동 ! Q 카드를 버린 뒤에 상대에게 한장이 주어지며 상대의 턴은 무시됩니다!")
                board(p1c,p2c,p1l,p2l,d,deck)
                return p1c,p2c,p1l,p2l,3,deck
               
            if i["rank"] == "J":
                countdown(0.5)
                p2c.remove(i)
                if len(p2c) == 0 :
                    print("J 특수카드 발동! 패에 카드가 없으므로 1장을 뽑았습니다.")
                else :
                    randomcard=p2c[random.randrange(len(p2c))]
                    p2c.remove(randomcard)
                    print("J 특수카드 발동! 패의 카드를 1장 제거 후 1장을 뽑았습니다.")
                card, deck = hit(deck)
                p2c.append(card)
                board(p1c,p2c,p1l,p2l,d,deck)
               
            if i["suit"] == "Jocker" :
                countdown(0.5)
                if i['rank'] == "Black": 
                    if more("특수카드 Black Jocker를 사용하시겠습니까?(y/n)"):
                        countjocker(5)
                        k=random.randrange(2)
                        if k == 0:
                            p1l -= 20
                            p2c.remove(i)
                            print("Black Jocker 특수카드 발동! Player 1의 생명력을 -20 합니다.")
                            board(p1c,p2c,p1l,p2l,d,deck)
                        else :
                            p2l -= 20
                            p2c.remove(i)
                            print("Black Jocker 특수카드 발동! Player 2의 생명력을 -20 합니다.")
                            board(p1c,p2c,p1l,p2l,d,deck)
                if i['rank'] == "Color":
                    p1l=p1l-20
                    p2c.remove(i)
                    print("Color Jocker 특수카드 발동! Player 1의 생명력을 -20 합니다.")
                    board(p1c,p2c,p1l,p2l,d,deck)
                    
        return p1c,p2c,p1l,p2l,d,deck
                    

#몇번째카드 선택할지 묻기함수
def cardselect(p1c,p2c,p1l,p2l,d,deck):
    if d == 1:
        while True:
            try :
                x = int(input("몇번째 카드로 공격하시겠습니까?"))
                if not 0 < x <=int(len(p1c)): raise NegativeInteger
                return int(x-1)
                
            except ValueError :
                print("Error:정수만 입력해주세요.")
            except NegativeInteger :
                print("Error:카드 범위에 맞게 입력해주세요.")

    if d == 2:
        while True:
            try :
                x = int(input("몇번째 카드로 공격하시겠습니까?"))
                if not 0 < x <=int(len(p2c)): raise NegativeInteger
                return int(x-1)
                
            except ValueError :
                print("Error:정수만 입력해주세요.")
            except NegativeInteger :
                print("Error:카드 범위에 맞게 입력해주세요.")    


#상대카드 공격함수
def attackcard(p1c,p2c,p1l,p2l,d,deck):
    x = cardselect(p1c,p2c,p1l,p2l,d,deck) #공격 할 카드
    y = cardselect2(p1c,p2c,p1l,p2l,d,deck) #공격 당할 카드
    if d==1: #player 1이 공격함
        if p1c[x]["rank"] == 0 :
            p1c[x]["rank"] = 10
        if p2c[y]["rank"] == 0 :
            p2c[y]["rank"] = 10
            
        if p1c[x]["rank"]==p2c[y]["rank"]: #카드 공격력 일치할 때
            p1c.remove(p1c[x])
            p2c.remove(p2c[y])
            p1l+=5
            print("Player 2의",str((y+1))+"번째 카드를 파괴하였습니다. "+"\n"+"Player 1 생명력이 5 증가하였습니다.")
            board(p1c,p2c,p1l,p2l,d,deck)       
            
        elif int(p1c[x]["rank"])>int(p2c[y]["rank"]):#내 카드 공격력이 더 클 때
            gap=int(p1c[x]["rank"])-int(p2c[y]["rank"])
            p1c[x]["rank"]=int(gap)
            p2c.remove(p2c[y])
            p1l+=5
            print("Player 2의",str((y+1))+"번째 카드를 파괴하였습니다. "+"\n"+"Player 1 생명력이 5 증가하였습니다.")
            board(p1c,p2c,p1l,p2l,d,deck)

        elif int(p1c[x]["rank"])<int(p2c[y]["rank"]): #상대 카드 공격력이 더 클 때
            gap=int(p2c[y]["rank"])-int(p1c[x]["rank"])
            p1c.remove(p1c[x])
            p2c[y]["rank"]=int(gap)
            print("Player 1의",str((x+1))+"번째 카드가 공격 중 파괴되었습니다.")
            board(p1c,p2c,p1l,p2l,d,deck)
            
    if d==2: #player 2가 공격함
        if p1c[y]["rank"] == 0:
            p1c[y]["rank"] = 10
        if p2c[x]["rank"] == 0:
            p2c[x]["rank"] = 10
        
        if p1c[y]["rank"]==p2c[x]["rank"]: #카드 공격력 일치할 때
            p1c.remove(p1c[y])
            p2c.remove(p2c[x])
            p2l+=5
            print("Player 1의",str((y+1))+"번째 카드를 파괴하였습니다. "+"\n"+"Player 2 생명력이 5 증가하였습니다.")
            board(p1c,p2c,p1l,p2l,d,deck)
            
        elif int(p2c[x]["rank"])>int(p1c[y]["rank"]):#내 카드 공격력이 더 클 때
            gap=int(p2c[x]["rank"])-int(p1c[y]["rank"])
            p2c[x]["rank"]=int(gap)
            p1c.remove(p1c[y])
            p2l+=5
            print("Player 1의",str((y+1))+"번째 카드를 파괴하였습니다. "+"\n"+"Player 2 생명력이 5 증가하였습니다.")
            board(p1c,p2c,p1l,p2l,d,deck)
            
        elif int(p2c[x]["rank"])<int(p1c[y]["rank"]): #상대 카드 공격력이 더 클 때
            gap=int(p1c[y]["rank"])-int(p2c[x]["rank"])
            p2c.remove(p2c[x])
            p1c[y]["rank"]=int(gap)
            print("Player 2의",str((x+1))+"번째 카드가 공격 중 파괴되었습니다.")
            board(p1c,p2c,p1l,p2l,d,deck)
        
    return p1c,p2c,p1l,p2l,d,deck

#카드뽑기 함수
def drawcard(p1c,p2c,p1l,p2l,d,deck):
    if d == 1:
        card, deck = hit(deck)
        if len(p1c)>=7 :
            cardover(p1c,p2c,p1l,p2l,d,deck)
        else :
            p1c.append(card)
            print("당신이 뽑은 카드는",card["suit"],card['rank']," 입니다")
        board(p1c,p2c,p1l,p2l,d,deck)
        return p1c,p2c,p1l,p2l,1,deck
        
    if d == 2 :
        card, deck = hit(deck)
        if len(p2c)>=7 :
            cardover(p1c,p2c,p1l,p2l,d,deck)
        
        else :
            p2c.append(card)
            print("당신이 뽑은 카드는",card["suit"],card['rank']," 입니다")
        board(p1c,p2c,p1l,p2l,d,deck)
        return p1c,p2c,p1l,p2l,2,deck

    
#상대 생명력 공격함수
def attackheart(p1c,p2c,p1l,p2l,d,deck):
    if d == 1:
        x=cardselect(p1c,p2c,p1l,p2l,d,deck)
        if p1c[x]["rank"] == 0 :
            p2l=int(p2l)-10
            p1c.remove(p1c[x])
            print("당신의 공격으로 인해 상대방의 생명력이 "+str(10)+"만큼 감소하였습니다.")
        else :
            p2l=int(p2l)-int(p1c[x]["rank"])
            print("당신의 공격으로 인해 상대방의 생명력이 "+str(p1c[x]["rank"])+"만큼 감소하였습니다.")
            p1c.remove(p1c[x])
        board(p1c,p2c,p1l,p2l,d,deck)
        return p1c,p2c,p1l,p2l,1,deck
        
    if d == 2:
        x=cardselect(p1c,p2c,p1l,p2l,d,deck)
        if p2c[x]["rank"] == 0 :
            p1l=int(p1l)-10
            p2c.remove(p2c[x])
            print("당신의 공격으로 인해 상대방의 생명력이 "+str(10)+"만큼 감소하였습니다.")
        else :
            p1l=int(p1l)-int(p2c[x]["rank"])
            print("당신의 공격으로 인해 상대방의 생명력이 "+str(p2c[x]["rank"])+"만큼 감소하였습니다.")
            p2c.remove(p2c[x])
        board(p1c,p2c,p1l,p2l,d,deck)
        return p1c,p2c,p1l,p2l,2,deck

        
    
#공격 정한 다음함수
def select3(x,p1c,p2c,p1l,p2l,d,deck):
    if int(x) == 1 :
        return attackcard(p1c,p2c,p1l,p2l,d,deck)
    if int(x) == 2:
        return attackheart(p1c,p2c,p1l,p2l,d,deck)


#공격하기 정하기 함수
class NegativeInteger(Exception): pass
def selecttarget(p1c,p2c,p1l,p2l,d,deck):
    while True:
        try :
            x = int(input("-------------------------("+printsmallturn(d)+")"+"\n"+"1.상대카드공격하기"+"\n"+"2.상대직접공격하기"+"\n"+"무엇을 선택하시겠습니까?(1 / 2)"))
            if not (x == 1 or x == 2): raise NegativeInteger
            return select3(x,p1c,p2c,p1l,p2l,d,deck)
            
        
        except ValueError :
            print("Error:1과 2 둘중 하나를 입력해주세요")
        except NegativeInteger :
            print("Error:1과 2 둘중 하나를 입력해주세요")

    

#선택하기 다음  함수
def select2(x,p1c,p2c,p1l,p2l,d,deck):
    if d==1:
        if  p1c!=[]:
            if int(x) == 1 :
                return selecttarget(p1c,p2c,p1l,p2l,d,deck)
            if int(x) == 2:
                return drawcard(p1c,p2c,p1l,p2l,d,deck)
        else :
            print("당신의 카드가 존재하지 않기 때문에 카드를 한장 뽑습니다.")
            return drawcard(p1c,p2c,p1l,p2l,d,deck)
    if d==2:
        if p2c!=[]:
            if int(x) == 1 :
                return selecttarget(p1c,p2c,p1l,p2l,d,deck)
            if int(x) == 2:
                return drawcard(p1c,p2c,p1l,p2l,d,deck)
        else :
            print("당신의 카드가 존재하지 않기 때문에 카드를 한장 뽑습니다.")
            return drawcard(p1c,p2c,p1l,p2l,d,deck)
        

#게임 기회 두번중 선택하기
class NegativeInteger(Exception): pass
def select(p1c,p2c,p1l,p2l,d,deck):#d는 플레이어 1 2 구별하는 역할.위에서 d 조건을 걸어서 카드랑 생명력 변경
    p1c,p2c,p1l,p2l,k,deck=spcardfind(p1c,p2c,p1l,p2l,d,deck)
    while True:
        try :
            x = int(input("-------------------------("+printsmallturn(d)+")"+"\n"+"1.공격하기"+"\n"+"2.카드뽑기"+"\n"+"무엇을 선택하시겠습니까?(1 / 2)"))
            if not (x == 1 or x == 2): raise NegativeInteger
            return select2(x,p1c,p2c,p1l,p2l,d,deck)
            
        
        except ValueError :
            print("Error:1과 2 둘중 하나를 입력해주세요")
        except NegativeInteger :
            print("Error:1과 2 둘중 하나를 입력해주세요")

#게임 구동함수. 위에 있는 많은 행동함수들을 while문을 통해 게임이 정상적으로 진행 되도록 만들었다.
#한 플레이어에 행동기회는 2번이기 때문에 따로 함수를 구현하였다.
def playerturn(p1c,p2c,p1l,p2l,playercount,deck) :
    co = 0#행동기회가 몇번인지 세는것.
    if playercount%2 == 1:
        k=1
        
    if playercount%2 == 0 :
        k=2
        
          
    while (co<2 and p1l>0 and p2l>0): # co는 플레이어의 행동기회를 뜻한다.한번 행동을 마칠시 1이 올라가도록 하였으며 행동을 2번하게 되면
                                      # while문을 탈출하여 값을 return 하며 전체 구동함수로 나가게 된다.
        if k == 1:
            p1c,p2c,p1l,p2l,k,deck=select(p1c,p2c,p1l,p2l,1,deck)
        if k == 2:
            p1c,p2c,p1l,p2l,k,deck=select(p1c,p2c,p1l,p2l,2,deck)
        co+=1
        p1c,p2c,p1l,p2l,playercount,deck=spcardfind(p1c,p2c,p1l,p2l,k,deck)
        if (playercount == 4 or playercount == 3): # 이것은 특수카드 처리 기능을 위해 구현했는데 , 특수카드에 의해 강제로 플레이어의 행동기회를 박탈할 경우 강제로 while문을 탈출하도록 함.
            break
            
    playercount+=1 #플레이어 차례를 세기 위해 1을 더한다.
            
    
    return p1c,p2c,p1l,p2l,playercount,deck
        


    
    
