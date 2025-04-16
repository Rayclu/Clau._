plus_integers:int = 1+2+3
subtract_floats:float = 7.3 - .01 - 10.5

print("My sum is: {}".format(plus_integers))
print("My substraction is: {}".format(subtract_floats))



def max_logic(num_1:int, num_2:int)-> int :
    return num_1 if num_1>num_2 else num_2

#condition ? true : false

num_2 = 7
Marx = max_logic(plus_integers, num_2)#45)
print( f"The max of the numbers {plus_integers} & {num_2} is "+ f"{Marx}")
