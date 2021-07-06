import random
TEAM_A={"p1":"a","p2":"b","p3":"c","p4":"d","p5":"e","p6":"f","p7":"g","p8":"h","p9":"i","p10":"j","p11":"k"}
TEAM_B={"p1":"A","p2":"B","p3":"C","p4":"D","p5":"E","p6":"F","p7":"G","p8":"H","p9":"I","p10":"J","p11":"K"}
types_of_ball=["wideball","noball","spin","offspin"]
types_of_score=["out",1,2,3,4,6,0]
print("TEAM_A IS GOING TO START")
score_a=0
wicketsteamA=0
ball=0
over=5
firstover=1
while firstover<=over:
    count_of_ball=1
    while count_of_ball<=6:
        random_ball_num=random.randint(0,3)
        k=count_of_ball
        which_ball=types_of_ball[random_ball_num]
        userInput=input("please hit the ball")
        if userInput=="yes":
            if which_ball=="wideball" or which_ball=="noball":
                print("ye",which_ball,"hian")
                score_a+=1
                count_of_ball=k
            else:
                print("ye",which_ball,"is this")
                randomscoreno=random.randint(0,6)
                how_much_score=types_of_score[randomscoreno]
                if how_much_score=="out":
                    wicketsteamA+=1
                else:
                    score_a+=how_much_score
                count_of_ball+=1
            print("Total-score",score_a,"wicketsteamA",wicketsteamA,"Total-overs",over,"cureent-over",firstover,"which ball",count_of_ball)
                
        else:
            count_of_ball=k

    firstover+=1
print("game is over")
TEAM_B={"p1":"A","p2":"B","p3":"C","p4":"D","p5":"E","p6":"F","p7":"G","p8":"H","p9":"I","p10":"J","p11":"K"}
types_of_ball=["wideball","noball","spin","offspin"]
types_of_score=["out",1,2,3,4,6,0]
print("TEAM_B IS GOING TO START")
score_b=0
wicketsteamB=0
ball_b=0
over_b=5
firstover=1
while firstover<=over_b:
    count_of_ball=1
    while count_of_ball<=6:
        random_ball_num=random.randint(0,3)
        k=count_of_ball
        which_ball=types_of_ball[random_ball_num]
        userInput=input("please hit the ball")
        if userInput=="yes":
            if which_ball=="wideball" or which_ball=="noball":
                print("ye",which_ball,"hian")
                score_b+=1
                count_of_ball=k
            else:
                print("ye",which_ball,"is this")
                randomscoreno=random.randint(0,6)
                how_much_score=types_of_score[randomscoreno]
                if how_much_score=="out":
                    wicketsteamA+=1
                else:
                    score_b+=how_much_score
                count_of_ball+=1
            print("Total-score",score_b,"wicketsteamA",wicketsteamA,"Total-overs",over_b,"cureent-over",firstover,"which ball",count_of_ball)
                
        else:
            count_of_ball=k

    firstover+=1
    if score_a>score_b:
        print("TEAM_A IS WON THE MATCH")
    elif score_b>score_a:
        print("TEAM_B IS WON THE MATCH")
    elif score_a==score_b:
        print("MATCH WILL BE DRAW!!")
    else:
        print("game is over")




























