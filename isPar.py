def marcar_pares(n)->bool:return True if n%2 == 0 else False 

n = int(input("Add any number:\t"))
print("par") if marcar_pares(n) else print(n)