class chatboox:
    def __init__(self):
        self.username = ''
        self.password = ''    
        self.loggedin=False         
        self.menu()                    


    def menu(self):
       user_input = input("""Welcome to chatboox 
                       how would like to proceed ?
                       1. Press 1 to signup 
                       2. Press 2 to signin 
                       3. Press 3 to wriote a post 
                       4. press 4 to msg friend
                       5. Press any other key to exit 
                       Enter your number -> """)
       if user_input == "1"    :
         self.signup()
       elif user_input == "2" :
        self.signin()
       elif user_input == "3" :
        self.my_post()
       elif user_input == "4" :
        self.sendmessage()
       else:
        exit()

    def signup(self):
        email = input ("enter your email ID -> : ")
        pasw = input (" Enter the password -> ")
        self.username = email
        self.password = pasw
        print("You have signed in successfully !")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password== '':
            print("signup first by presing number 1 in the menu option")
        else:
            uname = input("Enter your username/email here -> ")    
            pasw =input ("enter the password-> ")
            if self.username==uname and self.password==pasw:
                print("you have signed in successfully !!!! ")
                self.loggedin = True        
            else:
                print|("Please input correct credentials")    
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin == True :
            post = input("Enter your message here->  ")
            print("Following content has been posted ")
        else:
            print("You need to sign up ---- siginin first to post here")   
        print("\n")     
        self.menu()
    def sendmessage(self):
       if self.loggedin==True:
          txt = input("Enter your message here -> ")
          frnd = input("Whom to send the message->")
          print(f" your message has been sent to {frnd}")

       else:
          print("You need to signin first to post some content of your own")
       print("\n")
       self.menu()

test_USER = chatboox()       






    