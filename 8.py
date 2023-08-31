"""

For Loop and while loop

"""

# for loop

""" 
number = [1 ,2,3,4,5,20,65,7,80,30,66,3,5]

for x in number:
    if x==5:
        break
    
    print(x)
"""
# Simmilaray
print() # for space only

name = ["Amar" ,"Patel" , "Sonu" , "Satyendra"]

for a in name:
    print(" "+a)



fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x=="banana":
        print(x)



#Next Question

# The following code will stop the loop if i is 3 Fill in the blanks to perform the same i = 1 ______ i < 6: if i == 3: break i += 1


i = 1

while i < 6:
    if i == 3:
        break
    i+=1
print(i)



# again For loop problem

for x in range(1,20):
    if x==6:
        continue
    print(x)
    