#test poprawności logowania
users={"user":"user","admin":"admin"}
uzytkownik= input("wprowadż login")
password=input("wprowadź hasło")

if(uzytkownik not in users.keys()): #błędny login
    print("błedny login")
elif(users[uzytkownik]==password): #poprawnie zalogowany
    print("zalogowany")
else: #błędne hasło
    print("błędne hasło")

