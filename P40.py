# ćwiczenie 40

rzymskie={}
rzymskie[0] = "0"
rzymskie[1] = "I"
rzymskie[2] = "II"
rzymskie[3] = "III"
rzymskie[4] = "IV"
rzymskie[5] = "V"
rzymskie[6] = "VI"
rzymskie[7] = "VII"
rzymskie[8] = "VIII"
rzymskie[9] = "IX"

dajCyfre=input("Podaj cyfrę w systemie dziesiętnym  ")


if(dajCyfre.isdecimal()):
    dajCyfre=int(dajCyfre)
    if(dajCyfre>=0 and dajCyfre<=9):
        print(rzymskie[int(dajCyfre)])
    else:
        print("od 0-9!!!")
else:
    print("Błędne dane")