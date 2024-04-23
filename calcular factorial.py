print("ingrese un numero")
num = int(input())
fact=1
for i in range(1,num+1):
    fact*=i
print("el factorial de num",num,"es:",fact)