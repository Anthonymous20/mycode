#!/usr/bin/env python3

# create a list containg three items
my_list = [ "192.168.0.5", 5060, "UP"]

#Display the first item in the list
print("The first item in the list (IP): " + my_list[0] )

#Display the second item in the list
print("The second item in the list (port): " + str(my_list[1]) )

#Display the third item in the list
print("The third item in the list (State): " + my_list[2] )

# display only the IP addresses to the screen.
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# example 1 - add up the strings
print("IP addresses: " + iplist[3] + ", and " + iplist[4])

# example 2 - use the comma separator
print("IP addresses:", iplist[3], ", and", iplist[4])

# example 3 - use an 'f-string'
print(f"IP addresses: {iplist[3]}, and {iplist[4]}")

print("If I connect to IP", iplist[3], " or ", iplist[4])
print("I am unable to connect to ports " + str(iplist[0]) + " , " + iplist[1] + " , or " + str(iplist[2]) + " over ", + iplist[5])
