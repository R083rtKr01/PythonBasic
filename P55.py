# pokozac ile stopni Celcjisza odpowiada Farenheit-om w przedziale -(20,40)
# 32 F = 0 C
# 212 F = 100 C
def celsiusToFarenheit(celsiusDegree):
    return 32+(9*celsiusDegree)/5
print(celsiusToFarenheit(40))
print(celsiusToFarenheit(30))
print(celsiusToFarenheit(20))
print(celsiusToFarenheit(10))
print(celsiusToFarenheit(100))
print(celsiusToFarenheit(0))


print("|%5s|%6s|"%("C","F"))
for celsiusDegree in range(40,5,-1):
    if(celsiusDegree==0):
        print("|%5i|%6.1f|" % (celsiusDegree, celsiusToFarenheit(celsiusDegree)))
    print("|%+5i|%6.1f|"%(celsiusDegree,celsiusToFarenheit(celsiusDegree)))

def tempTable (start,stop,step):
    print("|%5s|%6s|" % ("C", "F"))
    for celsiusDegree in range(stop,start-step,-step):
        if(celsiusDegree==0):
            print("|%5i|%6.1f|"% (celsiusDegree, celsiusToFarenheit(celsiusDegree))))
    print("|%5i|%6.1f|" % (celsiusDegree, celsiusToFarenheit(celsiusDegree)))