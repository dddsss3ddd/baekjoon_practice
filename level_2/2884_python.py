usrin = input().split(' ')

hour = int(usrin[0])
min = int(usrin[1])



if min >= 45:
    print(hour, min-45)
else:
    print(hour-1 if hour-1>=0 else '23', min+15)