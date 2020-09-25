'''
Smart Devices Assignemnt:
Each Device Will have: Name, IP, Location, Status : On/Off, Charge, Updates : Yes / No
Methods :
 - Check (below 20%) and Charge
 - check (if yes) and download latest updates
'''

class sDevices :
    #The __init__ method is a constructor and runs as soon as an object of a class is instantiated.
    def __init__(self, dName, dIP, dLocation, dStatus, dCharge, dUpdates):
        self.dName = dName
        self.dIP = dIP
        self.dLocation = dLocation
        self.dStatus = dStatus
        self.dCharge = dCharge
        self.dUpdates = dUpdates

    def chargeDevice(self, addCharge) :
        if(self.dCharge<=20):
            print("Current charge level is: ", self.dCharge)
            self.dCharge += addCharge
        else:
            print("Unable to charge, current charge is above 20")

    def downloadUpdates(self, updateStatus) :
        if (updateStatus == 'YES') :
            print("Updating the latest downloads.")
        else:
            print("Unable to update the latest downloads. Update status is given as : ", updateStatus)

#Initializing the device details
phone = sDevices("IphoneX","192.168.1.2","33322","ON",60,"YES")
tablet = sDevices("Fire8","192.168.2.125","33323","OFF",10,"YES")
laptop = sDevices("Hp Pavillion","2001:0db8:85a3:0000:0000:8a2e:0370:7334","33321","ON",30,"YES")
smartWatch = sDevices("Fitbit Versa","2001:0db8:85a3:::8a2e::7334","33320","OFF",16,"YES")

# Working with the Phone object
print("\n**** Printing status for phone,",phone.dName,"****")
phone.chargeDevice(10)
phone.downloadUpdates("NO")
print("Phone is charged to: ", phone.dCharge)
print("Original Phone Updates status: ", phone.dUpdates)

# Working with the Tablet object
print("\n**** Printing status for Tablet,",tablet.dName,"****")
tablet.chargeDevice(20)
tablet.downloadUpdates("YES")
print("Tablet is charged to: ", tablet.dCharge)
print("Original Tablet Updates status: ", tablet.dUpdates)

# Working with the Laptop object
print("\n**** Printing status for Laptop,",laptop.dName,"****")
laptop.chargeDevice(30)
laptop.downloadUpdates("NO")
print("Laptop is charged to: ", laptop.dCharge)
print("Original Laptop Updates status: ", laptop.dUpdates)

# Working with the SmartWatch object
print("\n**** Printing status for Smart Watch,",smartWatch.dName,"****")
smartWatch.chargeDevice(40)
smartWatch.downloadUpdates("YES")
print("Smart Watch is charged to: ", smartWatch.dCharge)
print("Original Smart Watch Updates status: ", smartWatch.dUpdates)

