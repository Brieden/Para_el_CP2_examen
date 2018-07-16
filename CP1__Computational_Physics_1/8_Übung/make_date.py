N = 1e100
for n in range(int(N)):
    with open("Reihenwerte.txt", "a") as myfile:
        myfile.write("\n%.100e"%(1/(n+1)))