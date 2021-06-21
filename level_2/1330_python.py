usrin = input()

valArray = usrin.split(' ')

val0 = int(valArray[0])
val1 = int(valArray[1])
if val0==val1:
    print("==")
else:
    if val0<val1:
        print("<")
    else:
        print(">")

