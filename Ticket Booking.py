class Tickets:
    def __init__ (self):
        pass
                        
    def accept(self):
        ob = Tickets()
        ob.name=input("Enter Your name : ")
        ob.age=int(input("Enter your age : "))
        ob.gender=input("Enter your gender : ")
        ob.mob_no=int(input("Enter your 10 digit mobile number : "))
        ob.email_id=input("Enter your Email ID")
        ob.type1=int(input("Enter the type of ticket gold-1/silver-2/economy-3 : "))
        
        list.append(ob)
        
    def price(self):
        return 15000/self.type1
                        
    def display(self,ob):
        print("\n    Billing Detils     \n")
        print("    Name : ",ob.name)
        print("    Age : ",ob.age)
        print("    Gender : ",ob.gender)
        print("    Mobile Number : ",ob.mob_no)
        print("    Email ID : ",ob.email_id)
        print("    Type Selected : ",ob.type1,"\n")
        print("   ",ob.price()," USD (inclusive of all taxes .)")
                        
list=[]
ticket=Tickets()
run = True
while run :
    print("\n--------Welcome to the Concert Booking Portal-----------\n")
    print("Headlined by  Girls Genrtion , Also featuring Kard , infinite , Hoody ,Davichi and many more ........ ")
    print("\n 1. Book Tickets ")
    print("\n 2. Billing Details")
    print("\n 3. Exit \n")
    ch=int(input("Enter choice : "))
    if (ch == 1):
        ticket.accept()
        
    elif (ch == 2):
        for i in range(list.__len__()):
            print("\nTicket Successfully Booked\n")
            print(" Details ")
            ticket.display(list[i])
            
    
    else :
        print ("Process Terminated")
        run = False
