answer=''
while True:
    answer=input('서울,도쿄,평양,런던,베이징 중에서 영국의 수도는 어디일까요?')
    if answer=='서울':
        print('힌트: 서울은 한국의 수도입니다.')
    elif answer=='도쿄':
        print('힌트: 도쿄는 일본의 수도입니다.')
    elif answer=='평양':
        print('힌트: 평양은 북한의 수도입니다.')
    elif answer=='베이징':
        print('힌트: 베이징은 중국의 수도입니다.')
    elif answer=='런던':
        print('정답!')
        break
    else:
        print('제시된 도시중에서 골라주세요.')
