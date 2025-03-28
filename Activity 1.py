print ("Half pyramid pattern of stars (*): ")
n = int(input("How many rows do you want? "))
for i in range(n):
    for j in range(i+1):
        print ("* ", end="")
    print()