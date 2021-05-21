cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
namearr =["무지","콘","어피치","제이지"," 프로도","네오","튜브","라이언"]

for i in range(len(namearr)):
    print(namearr[i],i,end="")
del namearr[3]
print()
print("------------------")
for i in range(len(namearr)):
    print(namearr[i],i,end="")
