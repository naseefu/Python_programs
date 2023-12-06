
file = open("Fileprogram.txt","w")
file.close()

file = open("Fileprogram.txt","w")
file.write('hai my name is naseef')
file.close()

file = open("Fileprogram.txt","r")
a = file.read()
print(a)

file = open("Fileprogram.txt","a")
file.write("\nMy age is 22")
file.close()

file = open("Fileprogram.txt","r")
a = file.read()
print(a)