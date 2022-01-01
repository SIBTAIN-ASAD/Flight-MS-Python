# Programming Fundamentals (COSC2531) 

# All customers have a unique ID, unique name 
# (a name will not include any digit). 

import sys

# ==========================================================================================================================
# Customer Class
# ==========================================================================================================================
class Customer(object):

    # default constructor
    def __init__(self):
        self.ID = " "
        self.name = " "
        self.value = 0
        self.Quantity = 1
        self.destination = "D1"
        self.total = 0

    # parameterized constructor
    def __init__(self, id, name, value):
        if any(map(str.isdigit, name)):
            print("A name should not have any digit")
            self.__init__()
        else:
            self.ID = id
            self.name = name
            self.value = value
            self.Quantity = 1
            self.destination = "D1"
    
    # getters
    def getID(self):
        return self.ID
    
    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    # setters
    def setID(self, id):
        self.ID = id

    def setName(self, name):
        if any(map(str.isdigit, name)):
            print("A name should not have any digit")
            self.name = " "
        else:
            self.name = name

    def setValue(self, value):
        self.value = value

    # an empty super method
    def get_discount(self, cost):
        return (0, cost)

    def getDiscount(self):
        return 0


    # A method displayCustomer that prints the ID, 
    # name and value of a customer
    def displayCustomer(self):
        print(f"{self.name} ,{self.ID} ,{self.value}" , end = " ")
    # convert to string
    def getString(self):
        return (f"\n{self.ID}, {self.name}, 0, {self.value}")
    # <customer name > books <quantity> tickets to <destination>.
    # <customer name> gets a discount of <discount percentage>%.
    # Unit price:	<the price of each ticket> (AUD)
    # Total price:	<the total price> (AUD)

    def printData(self):
            print(f"{self.name} books {self.Quantity} tickets to {self.destination}" )
            print(f"{self.name} gets a discount of 0%.")



# ==========================================================================================================================
# Member Class
# ==========================================================================================================================
# A member is a customer with a membership
class Member(Customer):

    # defualt constructors
    def __init__(self):
        self.rate_of_discount = 5
        super().__init__()

    # parameterized cntructors
    def __init__(self, id, name, value, rateOfDiscount):
        super().__init__(id, name, value)
        self.rate_of_discount = rateOfDiscount

    def get_discount(self, cost):
        data = (self.rate_of_discount/100, cost*self.rate_of_discount/100)
        return (data)
    
    # getters
    def getDiscountRate(self):
        return self.rate_of_discount

    # A method displayCustomer that prints the ID, name,
    #  value and discount rate of a member
    def displayCustomer(self):
        super().displayCustomer()
        print(f",{self.rate_of_discount}", end = " ")
        
    # convert to string
    def getString(self):
        return (f"\n{self.ID}, {self.name}, {self.rate_of_discount/2}, {self.value}")
    
    def getDiscount(self):
        return self.rate_of_discount

    # A method setRate to adjust the
    # flat rate of discount
    def setRate(self, rate):
        self.rate_of_discount = rate

    def printData(self):
        print(f"{self.name} books {self.Quantity} tickets to {self.destination}" )
        print(f"{self.name} gets a discount of {self.rate_of_discount}%.")

    

# ==========================================================================================================================
# VIP Memeber Class
# ==========================================================================================================================
# A VIP member is a special member
#  (i.e. a customer with a VIP membership)
class VIPMember(Customer):
    
    # threshold (A static member)
    threshold = 1000

    # Default constructor
    def __init__(self):
        super().__init__()
        self.rate_of_discount_1 = 10
        self.rate_of_discount_2 = 15
    
    # Parameterized constructor
    def __init__(self, id, name, value, rate):
        super().__init__(id, name, value)
        self.rate_of_discount_1 = rate
        self.rate_of_discount_2 = rate + 5
    
    # A method get_discount(self, cost) which takes the
    #  cost and returns both the discount rate and
    #  the discount offered
    def get_discount(self, cost):
        if cost <= VIPMember.threshold:
            data = (self.rate_of_discount_1/100, cost*self.rate_of_discount_1/100)
        else:
            data = (self.rate_of_discount_2/100, cost*self.rate_of_discount_2/100)

        return (data)

    def getDiscount(self):
        return self.rate_of_discount_1

    # getters
    def getDiscountRate_1(self):
        return self.rate_of_discount_1

    def getDiscountRate_2(self):
        return self.rate_of_discount_2

    # A method displayCustomer that prints the ID, name,
    #  value, two discount rates and the threshold 
    # limit of a VIP member.
    def displayCustomer(self):
        super().displayCustomer()
        print(f",{self.rate_of_discount_1} ,{self.rate_of_discount_2} ,{VIPMember.threshold}", end= " ")

    # A method setRate to adjust the discount rates
    #  of each individual VIP member
    def setRate(self, rate):
        self.rate_of_discount_1 = rate
        self.rate_of_discount_2 = rate + 5

    # A method setThreshold to adjust the threshold limit.
    #  This affects all VIP members.
    def setThreshold(thr):
        VIPMember.threshold = thr

    # convert to string
    def getString(self):
        st = super().getString()
        return (f"\n{self.ID}, {self.name}, {self.rate_of_discount_1/2}, {self.value}")


# <customer name > books <quantity> tickets to <destination>.
# <customer name> gets a discount of <discount percentage>%.
# Unit price:	<the price of each ticket> (AUD) 
# Membership price: <the price of VIP membership> (AUD) 
# Total price:		<the total price> (AUD)

    def printData(self):
        print(f"{self.name} books {self.Quantity} tickets to {self.destination}" )
        print(f"{self.name} gets a discount of {self.rate_of_discount_1}%.")


# ==========================================================================================================================
# Destination Class
# ==========================================================================================================================
# This class is to keep track of information of 
# different destinations that the travel agency supports
class Destination:
    
    # Default constructor
    def __init__(self):
        self.ID = " "
        self.Name = " "
        self.Price = 0
        self.SeatAvailable = 0

    # Parameterized Constructor
    def __init__(self, id, name, price, seatAvailable):
        if any(map(str.isdigit, name)):
            print("A name should not have any digit")
            self.__init__()
        else:        
            self.ID = id
            self.Name = name
            self.Price = price
            self.SeatAvailable = seatAvailable


    # setters for class
    def setID(self, id):
        self.ID = id

    def setName(self, name):
        if any(map(str.isdigit, name)):
            print("A name should not have any digit")
            self.Name = " "
        else:
            self.Name = name

    def setPrice(self, price):
        self.Price = price
        
    def setAvailableSeats(self, seatAvailable):
        self.SeatAvailable = seatAvailable
            
    # getters
    def getID(self):
        return self.ID
    
    def getName(self):
        return self.Name
    
    def getPrice(self):
        return self.Price

    def getSeatsAvailable(self):
        return self.SeatAvailable

    # display destination data
    def display(self):
        print(f"{self.ID}, {self.Name}, {self.Price}, {self.SeatAvailable}" ,end = "") 

    # return string of destination
    def getString(self):
        return (f"\n{self.ID}, {self.Name}, {self.Price}, {self.SeatAvailable}") 


# ==========================================================================================================================
# Services Class
# ==========================================================================================================================
# This class is to keep track of information of different extra 
# services (Internet, Snack, Drink, Entertainment, SeatSelection, etc.) 
class Service:

    # default contructor
    def __init__(self):
        self.ID = ""
        self.Name = ""
        self.Price = 0

    # Parameterized Constructor
    def __init__(self, id, name, price):
        self.ID = id
        self.Name = name
        self.Price = price

    # setter for the price
    def setServicePrice(self, price):
        self.Price = price

    def display(self):
        print(f"{self.ID}, {self.Name}, {self.Price}")


# ==========================================================================================================================
# Bundle Class
# ==========================================================================================================================
# This is a special kind of service. It means multiple
# services can be offered together as one service
class Bundle:
    def __init__(self):
        self.ID = ""
        self.Name = ""
        self.listOfServices = []

    def __init__(self, id, name):
        self.ID = id
        self.Name = name
        self.listOfServices = []

    def display(self):
        print(f"{self.ID}, {self.Name}, {self.listOfServices}")

# ==========================================================================================================================
# Records Class
# ==========================================================================================================================    
# This class is the central data repository of your program
class Records:

    def __init__(self):
        self.destinations = []
        self.customers = []
        self.services = []
        self.bundles = []
        self.bookings = []
    # read a comma separated file called customers.txt
    #  and add the customers in this file to the customer list of the class
    def readCustomers(self, fileCustomers):
        
        with open(fileCustomers, "r") as f:
            if f == False:
                print("Invalid file ")
                exit(0)
            for data in f:
                ls = list(data.strip().split(','))
 
                if(ls[0][0] == 'C'):
                    var1 = Customer(ls[0].strip(), ls[1].strip(), int(ls[3]))
                    self.customers.append(var1)

                if(ls[0][0] == 'M'):
                    var2 = Member(ls[0].strip(), ls[1].strip(), int(ls[3]), 100 * float(ls[2]))
                    self.customers.append(var2)

                if(ls[0][0] == 'V'):
                    var3 = VIPMember(ls[0].strip(), ls[1].strip(), int(ls[3]), 100 * float(ls[2]))
                    self.customers.append(var3)
            
        f.close()


    # can read another comma separated value file called 
    # fileDestination and add the destinations stored in 
    # that file to the destination list of the class
    def readDestinations(self, fileDestination):

        with open(fileDestination, "r") as f:
            if f == False:
                print("Invalid file ")
                exit(0)
            for data in f:
                ls = list(data.strip().split(','))
                var = Destination(ls[0].strip(), ls[1].strip(), int(ls[2]), int(ls[3]))
                self.destinations.append(var)

        f.close()

    # methods to read services and bundles from the file
    def readService(self,fileServices):
        with open(fileServices, "r") as f:
            if f == False:
                print("Invalid file ")
                exit(0)
            for data in f:
                ls = list(data.strip().split(','))
                if ls[0][0] == 'S':
                    var = Service(ls[0].strip(), ls[1].strip(), ls[2].strip())
                    self.services.append(var)
                else:
                    var2 = Bundle(ls[0].strip(), ls[1].strip())
                    for i in range(2, len(ls)):
                        var2.listOfServices.append(ls[i])
                    self.bundles.append(var2)
        f.close()

    #methods to read booking
    def readBookings(self,fileBookings):
        with open(fileBookings, "r") as f:
            if f == False:
                print("Invalid file ")
                exit(0)
            for data in f:
                ls = list(data.strip().split(','))
                var = Booking()
                var.name = ls[0].strip()
                var.destination = ls[1].strip()
                var.tickets = int(ls[2])
                var.service = ls[3].strip()
                var.discount_rate = float(ls[4])
                var.date = ls[5].strip()

                self.bookings.append(var)


    #methods to find customers
    def findService(self, data):
        for i in range(len(self.services)):
            if self.services[i].ID == data or self.services[i].Name == data:
                return i

        for i in range(len(self.bundles)):
            if self.bundles[i].ID == data or self.bundles[i].Name == data:
                return i
        
        return -1

    #methods to find customers
    def findCustomer(self, data):
        for i in range(len(self.customers)):
            if self.customers[i].ID == data or self.customers[i].name == data:
                return i
        
        return -1

    #methods to find destination
    def findDestination(self, data):
        for i in range(len(self.destinations)):
            if ((self.destinations)[i]).ID == data or self.destinations[i].Name == data:
                return i
        
        return -1

    
    # These two methods can list all the existing customers and 
    # destinations on screen. The display format is the same as 
    # in the .txt files shown above
    def listCustomers(self):
        print("---------------------------")
        print("|        Customers        |")
        print("---------------------------")
        # print(len(self.customers))
        for i in range(len(self.customers)):
            self.customers[i].displayCustomer()
            print("")
        # print("---------------------------")

    def listDestinations(self):
        print("---------------------------")
        print("|       Destinations      |")
        print("---------------------------")
        for i in range(len(self.destinations)):
            self.destinations[i].display()
            print("")
        # print("---------------------------")

    def listServices(self):
        print("---------------------------")
        print("|         Services        |")
        print("---------------------------")
        for i in range(len(self.services)):
            self.services[i].display()
        
        print("")
        # print("---------------------------")

        print("---------------------------")
        print("|         Bundles         |")
        print("---------------------------")
        for i in range(len(self.bundles)):
            self.bundles[i].display()
        
        print("")
        # print("---------------------------")

    def listBookings(self):
        print("---------------------------")
        print("|        Bookings         |")
        print("---------------------------")
        for i in range(len(self.bookings)):
            self.bookings[i].display()
        # print("---------------------------")

    # store new data in files
    def store(self, fileCustomers= "customers.txt"):
        with open(fileCustomers, "a") as f:
            f.write(self.customers[-1].getString())
        f.close()
    
    # functio to store new destination into file
    def store2(self,fileDestination= "destinations.txt"):
        with open(fileDestination, "a") as f:
            f.write(self.destinations[-1].getString())

    # functio to store new destination into file
    def store3(self,fileBooking= "bookings.txt"):
        with open(fileBooking, "a") as f:
            f.write(self.bookings[-1].getString())

    # function to return most valuable person
    def getMostValuableCustomer(self):
        max = self.customers[0]
        for i in range(len(self.customers)):
            if max.total < self.customers[i].total:
                max = self.customers[i]

        return max

    # function to return most popular place
    def getMostpopularDestination(self):
        min = self.destinations[0]
        for i in range(len(self.destinations)):
            if min.SeatAvailable < self.destinations[i].SeatAvailable:
                min = self.destinations[i]

        return min


# ==========================================================================================================================
# Trip Class                                                                                                            |
# ==========================================================================================================================
# This class is to handle the customer booking
class Booking:
    def __init__(self):
        self.name = " "
        self.destination = " "
        self.tickets = 0
        self.service = " "
        self.discount_rate = 0
        self.date = " "

    def display(self):
        print(f"{self.name}, {self.destination}, {self.tickets}, {self.service}, {self.discount_rate}, {self.date} ")

    def getString(self):
        return (f"\n{self.name}, {self.destination}, {self.tickets}, {self.service}, {self.discount_rate}, {self.date} ")



# ==========================================================================================================================
# Booking Class                                                                                                            |
# ==========================================================================================================================
# This class is to handle the customer booking
class MenuDriverClass:

    # Default constructor
    def __init__(self):
        self.customer = None
        self.destination = None
        self.Quantity = 0
        self.r = Records()

    # Parameterized constructor
    def __init__(self, customer = None, destntion = None, quantity = 0):
        self.customer = customer
        self.destination = destntion
        self.Quantity = quantity
        self.r = Records()


        # function to add a newCustomer
    def addCustomer(self):
        print("Enter Customer a (new Name to register) \nor (Old Name OR ID to upgrade)")
        nam = input()
        id = nam
        print("Enter value")
        num = (input())
        while num.isdigit() == False:
            num = input("Please enter a digit: ")
        num = int(num)
        # print("Enter destination name")
        # des = input()
        des = "D1"

        print("=== Ticket prices ===")
        print("0 discount for Customer\n 5'%' discount for Member\n 10'%' discount for VIP member ")

        print("How much tickets do you want")
        tic = (input())
        while tic.isdigit() == False:
            tic = input("Please enter a digit: ")
        tic = int(tic)


        j = self.r.findDestination(des)
        if j >= 0:
            self.r.destinations[j].SeatAvailable -= tic
            if self.r.destinations[j].SeatAvailable < 0:
                print("Sorry Not much seats availabe \n")
                self.r.destinations[j].SeatAvailable += tic
                print("------  Try Again -------")
                self.addCustomer()
                return None
            self.Quantity += tic
            self.destination = des
        else:
            print(" Destination not availabe\n")
            print("------  Try Again -------")
            self.addCustomer()
            return None

        i = self.r.findCustomer(id)
        if i >= 0:
            self.r.customers[i].value = num
            self.r.customers[i].name = nam
            self.r.customers[i].Quantity += tic
            print(f"= Data of {id} is Updated =")
            return None

        # asking for which type of membership the customer want
        print("Alright! You entered a new Name")
        print("Do you want to enter membership, 'y' or 'n' ")
        ch = input()
        # input validations
        while ch != "y" and ch != "n":
            ch = input("Just enter 'y' or 'n' ")

        if(ch == "y"):
            check = input("M-> Normal member ship, V -> VIP membership: ")
            # input validations
            while check != "V" and check != "M":
                check = input("Just enter 'M' or 'V' ")

            rate = (input("Enter Rate: "))
            while rate.isdigit() == False:
                rate = (input("Please enter a digit: "))
            
            rate = int(rate)
                

            if(check == "M"):
                uid = input("Enter unique ID number: ")
                while uid.isdigit() == False:
                    uid = input("Please just provide a number: ")       
                    while self.r.findCustomer("M" + uid) >= 0:
                        uid = input("Please provide a unique ID number: ")

                var2 = Member("M" + uid, nam, num + 100, rate)
#                var2.value = 100 + (var2.get_discount(var2.getValue()))[1]
                var2.Quantity = tic
                var2.destination = des
                self.r.customers.append(var2)
            else:
                uid = input("Enter unique ID number: ")
                while uid.isdigit() == False:
                    uid = input("Please just provide a number: ")     
                    while self.r.findCustomer("V" + uid) >= 0:
                        uid = input("This ID is already present, try a new number")

                var3 = VIPMember("V" + uid, nam, num + 100, rate)
 #               var3.value = 100 + (var3.get_discount(var3.getValue()))[1]
                var3.Quantity = tic
                var3.destination = des
                self.r.customers.append(var3)
        else:
            uid = input("Enter unique ID number: ")
            while uid.isdigit() == False:
                uid = input("Please just provide a number: ")       
                while self.r.findCustomer("C" + uid) >= 0:
                    uid = input("This ID is already present, try a new number")

            var1 = Customer("C" + uid, nam, num)
            var1.Quantity = tic
            var1.destination = des
            self.r.customers.append(var1)

        print("=== Customer has Registered ===")
        self.storeDataInfiles()   


    # •	Finally, your menu program should have an option "Add a new destination"
    #  to add a new destination to your program. The specifications are as in Assignment 1.
    #  The default value of the number of tickets available is always 50, for any new destination.
    # You should be careful when generating the ID of a new destination. 
    # All the IDs of all the destinations are unique.

    # function to add a Destination
    def addDestination(self):
        print("Enter the name of new destination")
        des = input()
        id = des
        print("Enter seats available: ")            
        num = (input())
        while num.isdigit() == False:
            num = input("Please enter a digit: ")

        num = int(num)
        while num <= 0:
            num = int(input("Please enter a positve number: "))

        print("Enter tickets price: ")
        pric = (input())
        while pric.isdigit() == False:
            pric = input("Please enter a digit: ")
        pric = int(pric)
        while (pric) <= 0:
            pric = int(input("Please enter a positve number: "))


        j = self.r.findDestination(des)
        if j >= 0:
            print("This destination is already available")
            return None
        else:
            id = "D" + str(int(self.r.destinations[-1].ID[1]) + 1)
            var = Destination(id, des,pric, num)
            self.r.destinations.append(var)
            print(f"= Destnation {des} is Added =")

        self.storeDataInfiles2()   


    # Add booking by user input
    def addBooking(self):
        name = input("Enter Customer name or ID: ")
        while(self.r.findCustomer(name) < 0):
            print("==This Customer is not register yet==")
            ch = input("Press 1 to Register customer\nPress 2 to again enter the name\nPress 3 to return to menu \n")
            while(ch != "1" and ch != "2" and ch != "3"):
                ch = input("Just Enter 1, 2 or 3\n")
            if ch == "1":
                self.addCustomer()
                name = input("\nBack to booking\n============================== \nEnter Customer name or ID: ")
            elif ch == "3":
                return None
            else:
                name = input("Enter Customer name or ID: ")
                
        
        destination = input("Enter Destination name or ID: ")
        while(self.r.findDestination(destination) < 0):
            print("==This Destination is not available==")
            ch = input("Press 1 to Add destination\nPress 2 to again enter the destination\nPress 3 to return to menu \n")
            while(ch != "1" and ch != "2" and ch != "3"):
                ch = input("Just Enter 1, 2 or 3\n")
            if ch == "1":
                self.addDestination()
                destination = input("\nBack to booking\n============================== \nEnter Destination name or ID: ")
            elif ch == "3":
                return None
            else:
                destination = input("Enter Destination name or ID: ")

        
        services = "none"
        ch = input("Do you want to add services? (y or n) \n")
        while(ch != "y" and ch != "n"):
            ch = input("Just Enter y or n\n")
        if ch == "y":
            services = input("Enter Service name or ID: ")
            while(self.r.findService(services) < 0):
                services = input("This Service is not available\nEnter Again Service or \"q\" to not add service: ")
                if services == "q":
                    services = "none"
                    break
        else:
            services = "none"
        
        date = input("Please enter date in formate dd/mm/yyyy hh:mm:ss: ")

        i = self.r.findCustomer(name)
        person = self.r.customers[i]

        var = Booking()
        var.name = name
        var.destination = destination
        var.tickets = person.Quantity
        var.service = services
        var.discount_rate = person.getDiscount()
        var.date = date
        self.r.customers[i].destination = destination

        self.r.bookings.append(var)
        self.storeDataInfiles3()   

        print("==== Trip has Booked ====\n")


# -------------------------------------------------------------
# -------------------------------------------------------------
# <customer name > books <quantity> tickets to <destination>.
# <customer name> gets a discount of <discount percentage>%.
#  Unit price:	<the price of each ticket> (AUD)
# Total price:	<the total price> (AUD)

    # function to display the data of  customers
    def viewCustomers(self):
        for i in range(len(self.r.customers)):
            num = self.r.findDestination(self.r.customers[i].destination)
            price = self.r.destinations[num].Price
            quantity = self.r.customers[i].Quantity
            var3 = self.r.customers[i]
            print("------------------------------------------------")
            self.r.customers[i].printData()
            if self.r.customers[i].ID[0] != 'V':
                print(f"Unit Price: {price}")
                print(f"Total Price: {price*quantity* + (var3.get_discount(var3.getValue()))[1]}")  
                self.r.customers[i].total = price*quantity* + (var3.get_discount(var3.getValue()))[1]          
            else:
                print(f"Unit Price: {price}")
                print(f"Membership Price: {(price+ 100)*quantity}")
                print(f"Total Price: {(100 + price)*quantity* + (var3.get_discount(var3.getValue()))[1]}")
                self.r.customers[i].total = (100 + price)*quantity* + (var3.get_discount(var3.getValue()))[1]
                

    def initiate(self):
        for i in range(len(self.r.customers)):
            num = self.r.findDestination(self.r.customers[i].destination)
            price = self.r.destinations[num].Price
            quantity = self.r.customers[i].Quantity
            var3 = self.r.customers[i]
            if self.r.customers[i].ID[0] != 'V':
                self.r.customers[i].total = price*quantity* + (var3.get_discount(var3.getValue()))[1]          
            else:
                self.r.customers[i].total = (100 + price)*quantity* + (var3.get_discount(var3.getValue()))[1]
           
    # Function to show data
    def showData(self):
        self.r.listCustomers()
        self.r.listDestinations()
        self.r.listServices()

    # function to read data from files
    def readData(self,fileCustomers, fileDestination, fileServices, fileBookings):
        self.r.readDestinations(fileDestination)
        self.r.readCustomers(fileCustomers)
        self.r.readService(fileServices)
        self.r.readBookings(fileBookings)

    def storeDataInfiles(self):
        self.r.store()

    def storeDataInfiles2(self):
        self.r.store2()

    def storeDataInfiles3(self):
        self.r.store3()

    def showBookings(self):
        self.r.listBookings()

    def valuable(self):
        var = self.r.getMostValuableCustomer()
        print("--------------------------------------------------------->")   
        print("The most Valuable person is: ", end = " ")
        var.displayCustomer()
        print("\n--------------------------------------------------------->")   

    def popular(self):
        print("--------------------------------------------------------->")   
        print("The most Popular place is: ", end = " ")
        var = self.r.getMostpopularDestination()
        var.display()
        print("\n--------------------------------------------------------->")   

    # •	The menu now has an option "Display all the bookings of a customer" 
    # to reveal all the bookings of a particular customer. The user needs 
    # to enter the customer name, and the program will provide the booking
    #  history is in the format as above.
    # •	The menu also has an option "Display the most valuable customer" 
    # to reveal the most valuable customer, that is the customer with the 
    # highest money spent to date.
    # •	The menu also has an option "Display the most popular destination" 
    # to reveal the destination with the highest number of bookings 
    # (not based on tickets, but bookings).
    # •	When your program terminates, it will update the all the files 
    # (customer, destinations, services, and bookings) based on the 
    # information when the program executes

    # function to show manu to user
    def menu(self, fileCustomers = "customers.txt", fileDestination = "destinations.txt",
             fileServices = "services.txt", fileBookings = "bookings.txt"):
        
        inp = "0"
        # reading data from files
        self.readData(fileCustomers, fileDestination, fileServices, fileBookings)

        # displaying data one time
        self.showData()

        # loops for the manu
        while inp != "q":

            # printing the Menu
            print("=========================")   
            print("|          MENU         |")   
            print("=========================")   
            print("Press 1 to \"Book\" a new trip")
            print("Press 2 to \"Display\" the current customer list")
            print("Press 3 to \"Display\" the current destination list")
            print("Press 4 to \"Add\" a Customer")
            print("Press 5 to \"Add\" a new destination")
            print("Press 6 to \"Display\" current bookings List")
            print("Press 7 to \"Display\" services")
            print("Press 8 to \"Display\" the most valuable customer")
            print("Press 9 to \"Display\" the most popular destination \n")

            print("Press q to exit list")

            # getting inout and showing data
            inp = input()  
            if inp == "1":
                self.addBooking()
            elif inp == "2":
                self.viewCustomers()
            elif inp == "3":
                self.r.listDestinations()
            elif inp == "4":
                self.addCustomer()
            elif inp == "5":
                self.addDestination()
            elif inp == "6":
                self.showBookings()
            elif inp == "7":
                self.r.listServices()
            elif inp == "8":
                self.initiate()
                self.valuable()
            elif inp == "9":
                self.initiate()
                self.popular()
            elif inp == "q":
                break
            else:
                print("Invalid Input")
            


# ==========================================================================================================================
# MAIN 
# ==========================================================================================================================
# < -------   Operations    -----------> #
# This can be considered as a main class of your program.

def main():
    # getting command line arguments
    n = len(sys.argv)
    
    # main class for all booking functionalities
    b = MenuDriverClass()
    # menu driver function
    
    if n < 5 and n > 1:
        print("In complete arguments passed")   
        b.menu() 
    elif n == 0 or n == 1:
        b.menu()
    else:
        fileCustomers = sys.argv[1]
        fileDestination = sys.argv[2]
        fileServices = sys.argv[3]
        fileBookings = sys.argv[4]

        b.menu(fileCustomers, fileDestination, fileServices, fileBookings)


# calling main
if __name__ == "__main__":
    main()


# ==========================================================================================================================
# END
# ==========================================================================================================================