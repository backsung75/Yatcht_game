from calcFunctions import *
upperScoreList = [
    'Aces', 'Twos', 'Threes', 
    'Fours', 'Fives', 'Sixes', 
]

lowerScoreList = [
    'Choice', '3card', '4card', 
    'Full house', 'S.Straight', 'L.Straight', 
    'Yatcht', 
]

functionMap = {
    'Aces': aces, 'Twos': twos, 'Threes': threes, 
    'Fours': fours, 'Fives': fives, 'Sixes': sixes, 
    'Choice':choice, '3card': tcard, '4card': fcard, 
    'Full house': fhouse, 'S.Straight': s_straight, 'L.Straight': l_straight, 
    'Yatcht': yatcht, 
}

tool_tip = [
    '1값을 모두 더함', '2값을 모두 더함', '3값을 모두 더함',
    '4값을 모두 더함', '5값을 모두 더함', '6값을 모두 더함',
    '주사위에 모든 수를 더함' , '같은 수 3개가 있다면 모두 더함', '같은 수 4개가 있다면 모두 더함',
    '같은수 3개, 2개 일때 25점', '4숫자가 나열될때 30점', '5숫자가 나열될때 40점',
    '모든 숫자가 같을때 50점'
]