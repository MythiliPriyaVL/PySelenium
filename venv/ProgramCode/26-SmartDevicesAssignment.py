'''
#An IPv4 address consists of four numbers, each of which contains one to three digits,
with a single dot (.) separating each number or set of digits. Each of the four numbers can range from 0 to 255

#An IPv6 address consists of eight groups of four hexadecimal digits.
If a group consists of four zeros, the notation can be shortened using a colon to replace the zeros.

Smart Devices Assignemnt:
Each Device Will have
    Name :
    IP :
    Location :
    Status : On/Off
    Charge :
    Updates : Yes / No
Methods :
 - Check (below 20%) and Charge
 - check (if yes) and download latest updates
'''

class sDevices :
    dName = ""
    dIP = ""
    dLocation = ""
    dStatus = ""
    dCharge = ""
    dUpdates = ""

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
            print("Unable to update the latest downloads.")


phone = sDevices()
phone.dName = "IphoneX"
phone.dIP = "192.168.1.2"
phone.dLocation = "33322"
phone.dStatus = "ON"
phone.dCharge = 60
phone.dUpdates = "YES"

tablet = sDevices()
tablet.dName = "Fire8"
tablet.dIP = "192.168.2.125"
tablet.dLocation = "33323"
tablet.dStatus = "OFF"
tablet.dCharge = 10
tablet.dUpdates = "YES"

laptop = sDevices()
laptop.dName = "Hp Pavillion"
laptop.dIP = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
laptop.dLocation = "33321"
laptop.dStatus = "ON"
laptop.dCharge = 30
laptop.dUpdates = "YES"

smartWatch = sDevices()
smartWatch.dName = "Fitbit Versa"
smartWatch.dIP = "2001:0db8:85a3:::8a2e::7334"
smartWatch.dLocation = "33320"
smartWatch.dStatus = "OFF"
smartWatch.dCharge = 16
smartWatch.dUpdates = "YES"

# Working with the Phone object
print("**** Printing status for phone,",phone.dName,"****")
phone.chargeDevice(10)
phone.downloadUpdates("NO")
print("Phone is charged to: ", phone.dCharge)
print("Phone Updates status is: ", phone.dUpdates)

# Working with the Tablet object
print("**** Printing status for Tablet,",tablet.dName,"****")
tablet.chargeDevice(20)
tablet.downloadUpdates("YES")
print("Tablet is charged to: ", tablet.dCharge)
print("Tablet Updates status is: ", tablet.dUpdates)

# Working with the Laptop object
print("**** Printing status for Laptop,",laptop.dName,"****")
laptop.chargeDevice(30)
laptop.downloadUpdates("NO")
print("Laptop is charged to: ", laptop.dCharge)
print("Laptop Updates status is: ", laptop.dUpdates)

# Working with the SmartWatch object
print("**** Printing status for Smart Watch,",smartWatch.dName,"****")
smartWatch.chargeDevice(40)
smartWatch.downloadUpdates("YES")
print("Smart Watch is charged to: ", smartWatch.dCharge)
print("Smart Watch Updates status is: ", smartWatch.dUpdates)

