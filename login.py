
###################승률계산,변수 저장 등 로그인 함수들을 구현해놓았습니다.##############3

def show_top5(members):
    print("★★★★★★TOP5★★★★★★")
    #score 역순으로 정렬
    sorted_members = sorted(members.items(),key=lambda x: x[1][1],reverse=True)
    print("점수 상위권 5명을 보여드립니다! 괄호는 승률")
    count = 1
    for k in sorted_members[:5] :
        name = k[0]
        score = members[name][1]
        tries = members[name][2]
        wins = members[name][3]

        percentage = 0
        if tries != 0:
            percent = (wins/tries) * 100
            percentage = "{0:.1f}".format(percent)

        print(str(count)+".",name,":",str(score),"("+str(percentage)+" %)")
        count += 1


def store_members(members):
    file = open("members.txt","w")
    names = members.keys()
    for name in names:
        passwd, score, tries, wins = members[name]
        line = name + ',' + passwd + ',' + str(score) + ',' + str(tries)+ ',' + str(wins)+ '\n'              
        file.write(line)
    file.close()

def load_members():
    file = open("members.txt","r")
    members = {} #사전식으로 나열 
    for line in file:
        name, passwd, score, tries, wins = line.strip('\n').split(',')
        members[name] = (passwd, int(score), int(tries), int(wins))
    file.close()
    return members

#아이디, 비번, 점수, 횟수, 이긴횟수 

def login(members):
    #아이디 받기
    username = input("Enter your name: (6 letters max) ")
    while len(username) > 6:
        username = input("Enter your name: (6 letters max) ")

    #비번 받기
    trypasswd = input("Enter your password: ")

    if username in members: #아이디가 members사전에 있는가
        if members[username][0] == trypasswd : #비밀번호 올바른가
            score = members[username][1]
            tries = members[username][2]
            wins = members[username][3]

            print (username+"님의 점수는",score,"점 입니다.")

            percentage = 0
            if tries != 0:
                percent = (wins/tries) * 100
                percentage = "{0:.1f}".format(percent)
            print(username+"님의 승률은",percentage,"% 입니다.")

            
            return username, trypasswd, score, tries, wins, members

        else :
            return login(members)

    else:
        members[username]=(trypasswd, 1000, 0, 0)
    
        return username, trypasswd, 1000, 0, 0, members

