import random
rsp=['가위','바위','보']
while True:
    player=input('가위/바위/보/끝')
    computer=random.choice(rsp)
    if player=='끝':
        break
    print(player,computer)
    if player==computer:
        print('비겼어요')
    elif player=='가위':
        if computer=='바위':
            print('졌어요')
        elif computer=='보':
            print('이겼어요')
    elif player=='바위':
        if computer=='보':
            print('졌어요')
        elif computer=='가위':
            print('이겼어요')
    elif player=='바위':
        if computer=='보':
            print('졌어요')
        elif computer=='가위':
            print('이겼어요')
    else:
        print('보기에서 골라주세요.')
