from board import *
from behavior import *
from login import *

################################최종 실행 파일######################################
###########각각의 파일마다 필요한 주석을 써놓았습니다.####################
##########내부적으로 여러개의 경우에 구동되는 함수를 제작해 모아서 실행되도록 구현하였습니다.################

def stone() : #전체 모든것을 돌리는 총괄함수
    print("Cardsstone 게임 플레이를 환영합니다!")
    members = load_members()
    print("플레이어 1번 로그인을 진행해주세요")
    username1, trypasswd1, score1, tries1, wins1, members = login(members)
    print("플레이어 2번 로그인을 진행해주세요")
    username2, trypasswd2, score2, tries2, wins2, members = login(members)
    p1=username1
    p2=username2 
    i=True              #아래 구동원리에 의해 처음 게임은 실행되어야 하기때문에 True로 놓고 시작한다.
    show_top5(members)
   
    #첫번째 while :점수와 승률을 기록하기 위한 게임 전체 구동함수. 게임진행은 초기화 해야하지만 점수는 초기화 하면 안되기 때문에 while문을 두개 구현.
    #점수와 승률을 따로 기록해놓는 함수가 있어도 while문을 하나로 구현한다면 다시 초기화 되고 복잡하기 때문에 2개로 구현.
    #i == True 일때 돌아가도록 하였고 i = more함수로 게임을 끝낼지 다시 진행할지 여부를 묻고 True or False를 return하도록 만듬.
    #True 이면 게임진행만 초기화 되고 점수와 승률은 기록된다.

    while i == True : # 게임 진행을 계속할때
        p1c=[]
        p2c=[]
        deck=fresh_deck()
        card, deck = hit(deck)
        p1c.append(card)
        card, deck = hit(deck)
        p2c.append(card)
        card, deck = hit(deck)
        p1c.append(card)
        card, deck = hit(deck)
        p2c.append(card)
        card, deck = hit(deck)
        p1c.append(card)
        card, deck = hit(deck)
        p2c.append(card)
        p1l=40
        p2l=40
        playercount=1       #플레이어가 2명이기 때문에 내부적으로도 2개의 경우를 가져야 하고 각 플레이어 마다 다르게 취급해야 하기때문에 플레이어 1,2를 구별하기 위해 설정해놓은 변수.
        d=0                 #플레이어count를 1씩 계속 더하도록 만들었고 내부적으로 홀수이면 p1의 차례가 오도록,짝수면 p2의 차례가 오도록 설계 해놓았다.

        #두번째 while문 : 게임 승률,점수와 별개로 게임 내부 구현함수.
        #게임 내부규칙에 의거하여 생명력이 0이 되기 전까지는 계속 게임이 돌아가게 만들기 위하여 하위 while문을 구현.
        

        while  (p1l>0 and p2l>0) : #생명력0이면 탈출
            countdown(0.5)
            print("*******************************************************************")
            printturn(playercount)
            board(p1c,p2c,p1l,p2l,d,deck)
            p1c,p2c,p1l,p2l,playercount,deck=playerturn(p1c,p2c,p1l,p2l,playercount,deck) #플레이어의 행동기회 2번을 실행하고 행동을 할수 있게 하는 함수.behavior파일에 구현해놓았다.
            
        if p1l <= 0: 
            tries1+=1
            tries2+=1
            score2+=20
            score1-=20
            wins2+=1
            print(str(username2)+" 의 승리입니다! 축하 합니다 !!!!!!!!")
            i=more("******"+str(username1)+"님 ! "+str(username2)+"에게 복수하시겠습니까?(y = 복수한다 // n = 도망간다)*******")
        if p2l <= 0:
            tries1+=1
            tries2+=1
            score1+=20
            score2-=20
            wins1+=1
            print(str(username1)+" 의 승리입니다! 축하 합니다 !!!!!!!!")
            i=more("******"+str(username2)+"님 ! "+str(username1)+"에게 복수하시겠습니까?(y = 복수한다 // n = 도망간다)********")


        members[username1]=(trypasswd1, score1, tries1, wins1)
        members[username2]=(trypasswd2, score2, tries2, wins2)
        store_members(members)
    
    if i == False : #게임 진행을 포기하고 게임 점수 순위를 보여줌.
        show_top5(members)
        print("*******도망을 선택하셨군요!!!!수고하세요!!!*******")
        


stone()

        
