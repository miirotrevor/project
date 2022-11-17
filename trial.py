import getpass
database = {"miiro": "1234", "suzan": "1234"}
username = input("Enter Your Username : ")
password = getpass.getpass("Enter Your Password : ")
for i in database.keys():
    if username == i:
       while True:
        print("*" * 28 + "WELCOME TO COURSE WORK RESTAURANT" + "*" * 24 + "\n") 
        print("*" * 31 + "RESTAURANT MENU" + "*" * 32 + "\n"     
              "\t(O) ORDER\n"                              
              "\t(R) RESERVATIONS\n"
              "\t(P) PAYMENTS AND RECEIPTS\n"
              "\t(E) EXIT\n" +
              "_" * 72)
        break