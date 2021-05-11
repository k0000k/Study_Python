rsp=['가위','바위','보']
player=rsp[2]
computer=rsp[1]
if player=='가위' and computer=='가위':
    print('비겼어요')
elif player=='바위' and computer=='바위':
    print('비겼어요')
elif player=='보' and computer=='보':
    print('비겼어요')
elif player=='가위' and computer=='보':
    print('이겼어요')
elif player=='바위' and computer=='가위':
    print('이겼어요')
elif player=='보' and computer=='바위':
    print('이겼어요')
else:
    print('졌어요')
