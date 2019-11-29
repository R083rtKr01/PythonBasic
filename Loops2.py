# druga wersja loops1

# a= [.3,.4,3.2,.3,1,5.4,2,1,17,7,-1]
# tresholdLow=float(input("podaj próg odcięcia dół"))
# tresholdTop=float(input("podaj próg odcięcia góra"))
# catogorizedresult=[] #lista wypadkowa
# class0 =[] #lista przechowujaća wartości sklasoyfikowane jako 0
# class1 =[] #lista przechowujaća wartości sklasoyfikowane jako 1
# labelsDict={0:class0,1:class1}
# index =0
#
# while(index <len(a)):
#     if(a[index]>tresholdLow and a[index]<tresholdTop):
#         catogorizedresult.append(1)
#         class1.append(a[index])
#     else:
#         catogorizedresult.append(0)
#         class0.append(a[index])
#     index +=1
# print(a)
# print(catogorizedresult)
# print(labelsDict)

#pętla
lvls = ["A1","A2","B1","B2","C1","C2"]

for lvl in lvls:
    print(lvl)
for i,lvl in enumerate(lvls):
    print(i,lvl)

# iterowanie po słownikach w for in
lvlsNames={lvls[0]:"basic",
            lvls[1]:"basic",
            lvls[2]:"independent",
            lvls[3]:"independent",
            lvls[4]:"proficient",
            lvls[5]:"proficient",
           }
for key in lvlsNames.keys():
    print(key,lvlsNames[key])