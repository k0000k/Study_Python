while True:
    num=int(input('2이상의 정수를 입력하세요 (종료:-1)'))
    if num==-1:
        break
    count=2
    is_prime=True
    while count<num:
        if num%count==0:
            is_prime=False
            break
        count=count+1
    if is_prime:
        print('소수입니다.')
    else:
        print('소수가 아닙니다.')
