import datetime
from datetime import date

# Class villa encapsulates the following rented villa characteristics: name of villa, 
# name of personal assistant. It also offers functions that inform about the hours that 
# the personal assistant will be on call and the dates that the villa will be cleaned and 
# keys will be changed. In addition, it has a function to print the label of the gift that is 
# left in the room of each new guest.

class Villa(object):
    def __init__(self, n,id):
        self.villasName = n

    def setPersonalAssistant(self,pa):
        self.setPersonalAssistant = pa
        print(f"{self.setPersonalAssistant} will be on call from 8:00 AM to 08:00 PM for villa {self.villasName}")

    def cleanAndChangeKey(self,d1,d2):
        print(f"Villa {self.villasName} will be cleaned and keys will be changed on {d1} and {d2}")
    
    def printGiftLabel(self,s):
        print(f"Welcome at the {self.villasName}, {s} party!")


# Class vipVilla inherits from class villa. It encapsulates the name of the VIP personal 
# assistant and offers an access function to it.

class VipVilla(Villa):
    def __init__(self, nn, id):
        Villa.__init__(self,nn,id)
    
    def setPersonalAssistant(self, pa):
        #return super().setPersonalAssistant(pa)
        self.vipPersonalAssistant  = pa
        print(f"{self.vipPersonalAssistant} will be on call (7:00 AM to 09:00 PM) for villa {self.villasName} and arrange for personal yacht")

#Class guest encapsulates the following attributes of a guest: first and last name, number of 
# adults, and number of children in the room. It offers an access function to last name and a 
# printing function for the guest object.

class Guest():
    def __init__(self, l1,f1,b,c):
        self.firstName = f1
        self.lastName = l1
        self.noOfAdults = b
        self.noOfChildrens = c

    def getLastName(self):
        return self.lastName
    
    def __repr__(self):
        return 'Guest: {%s, %s}' %(self.firstName, self.lastName)

# Class reservation encapsulates the following attributes of a reservation: 
# the name of the reserved villa, checkin date, checkout date, reservation ID, 
# a printing function for the reservation class.

class Reservation(object):
    def __init__(self, n, de, le):
        self.checkinDate = de
        self.lengthOfStay = le
        self.villasName = n
        self.checkoutDate = de + datetime.timedelta(days=le)
    
    def getvillasName(self):
             return self.villasName
    def getcheckinDate(self):
            return self.checkinDate
    def getcheckoutDate(self):
            return self.checkoutDate
    def setreservID(self,id):
        self.reservID=id
    def __repr__(self):
       return 'Reservation: (%s, %s, %s, %s)' % (self.checkinDate, self.lengthOfStay, self.villasName,self.reservID)

# Class resort encapsulates the following attributes: a list with the names of the (standard) 
# villas, a list with the  names of the VIP villas, a guest list, a reservation list and a 
# reservation ID list. It also offers access functions to a Guest object, Reservation object,
# reservation ID and a function that prints all lists.
        
class Resort(object):
      vil = ['Elektra','Persephone','Artemis','Kouros']
      vipVil = ['Zeus','Alexandrian']
      guestList = []
      reservationList = []
      resIDList = [0]
      
      def __init__(self):
          print("Welcome to Myconos Hidden Cove!")
      
      def setGuest(self,g):
          self.guestList.append(g)
      
      def setReservation(self,r):
          self.reservationList.append(r)
      
      def getresID(self):
          return self.resIDList[-1]
      
      def updateResIDList(self):
          i = self.getresID()+1
          self.resIDList.append(i)
          return(self.resIDList[-1])
      
      def printLists(self):
          print(f" The guest list is: {self.guestList}")
          print(f" The reservation list is: {self.reservationList}")
          print(f" The resID list is: {self.resIDList}")

# The next cell is the test module. We create a resort object, and two guests. 
# The first guest reserves a VIP villa and the second, a standard one. Reservations 
# are created, and all lists are printed at the end.

rr = Resort()

#Guest 1
sa = Guest('Albert','Mitchell',2,1)
rr.setGuest(sa)

re = Reservation('Zeus',date(2019,6,3),5)
rr.setReservation(re)

newid = rr.updateResIDList()
re.setreservID(newid)

if re.getvillasName() == 'Zeus' or re.getvillasName() == 'Alexandrian':
    villarese = VipVilla(re.getvillasName(),newid)
else:
    villarese = Villa(re.getvillasName(),newid)

villarese.printGiftLabel(sa.getLastName())
villarese.setPersonalAssistant('Eleni')
villarese.cleanAndChangeKey(re.getcheckinDate(),re.getcheckoutDate())

#Guest 2

sa2=Guest('Simon','Marchese',2,1)
rr.setGuest(sa2)
re2=Reservation('Artemis',date(2019,7,3),8)
rr.setReservation(re2)
newid2=rr.updateResIDList()
re2.setreservID(newid2)
if re2.getvillasName() == 'Zeus' or re2.getvillasName()=='Alexandrian':
    villarese2=VipVilla(re2.getvillasName(),newid2)
else:
    villarese2=Villa(re2.getvillasName(),newid2)

villarese2.printGiftLabel(sa2.getLastName())
villarese2.setPersonalAssistant('Dorian')
villarese2.cleanAndChangeKey(re2.getcheckinDate(),re2.getcheckoutDate())

rr.printLists()