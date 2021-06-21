usrinA = int(input())
usrinB = int(input())

val_1 = usrinB%10
val_10 = usrinB//10%10
val_100 = usrinB//100

res_1 = usrinA*val_1
res_2 = usrinA*val_10
res_3 = usrinA*val_100

print(res_1)
print(res_2)
print(res_3)
print(res_1+res_2*10+res_3*100)
