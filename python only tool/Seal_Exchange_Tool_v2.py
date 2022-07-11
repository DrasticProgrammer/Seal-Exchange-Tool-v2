# Author: DeCota Mathis
# Project start date: 8-7-21
###############################

# This program is designed to query the Universalis API for
# finding the best item to buy from the Grand Company Quartermaster
# to then sell on the market board.

# As of 8-8-21, this program only looks up the values for 7 different items
# that are available in the GCQ shop.

# Keep in mind that the values generated are the most recent purchases of
# those items and may not reflect true value of said item.


#Lets start the program off by importing some modules. ^.^

import requests
import json

Glamour_Prism = 0
Cordial = 0
Grade_6_Dark_Matter = 0
Hardened_Sap = 0
Grade_7_Dark_Matter = 0
Glamour_Dispeller = 0
Coke = 0

def __main__():
    prismcheck()
    Cordialcheck()
    Grade_6_Dark_Mattercheck()
    Grade_7_Dark_Mattercheck()
    Cokecheck()
    sapcheck()
    Glamour_Dispellercheck()
    checkbest()
    print()

    
    input("Press enter to close the program. :)")
    quit()

def prismcheck():
    global Glamour_Prism
    checks = 0
    prismlist = []
    #get prices for Glamour Prisms
    response = requests.get("https://universalis.app/api/history/54/21800/")
    files = response.content

    #write query to json file
    with open('Glamour Prism.json', 'wb') as f:
        f.write(files)
    
    #load json file data
    with open('Glamour Prism.json') as json_file:
        data = json.load(json_file)
    
    #search for pricePerUnit and display it
    while checks < 51:
                for i in data['entries']:
                    #print("Price per Glamour Prism on Faerie:", i['pricePerUnit'])
                
                    prismlist.append((i['pricePerUnit']/200))
                    checks += 1
    

    #print("Gil/Seal for Glamour Prisms based on last purchase",(i['pricePerUnit']/200))
    print("Gil/Seal for Glamour Prisms based on last purchase",prismlist[0])
    Glamour_Prism = (sum(prismlist)/len(prismlist))
    print("Average price per unit based on the last 50 purchases:", Glamour_Prism)
    print("Last sold for:", (prismlist[0]*200))
    print("Seals per item: 200")

    print()
          
    #finish Glamour Prism price check.
        


def Cordialcheck():
    global Cordial
    #get prices for Cordial
    response2 = requests.get("https://universalis.app/api/history/54/6141/")

    files2 = response2.content
    Cordiallist = []
    checks = 0
    #write query to json file
    with open('Cordial.json', 'wb') as f:
        f.write(files2)

    #load json file data
    with open('Cordial.json') as json_file2:
        data2 = json.load(json_file2)

    while checks < 51:
        for i in data2['entries']:
            Cordiallist.append((i['pricePerUnit']/500))
            checks += 1
    
    print("Gil/Seal for Cordial based on last purchase",Cordiallist[0])
    Cordial = (sum(Cordiallist)/len(Cordiallist))
    print("Average price per unit based on the last 50 purchases:", Cordial)
    print("Last sold for:", (Cordiallist[0]*500))
    print("Seals per item: 500")
    print()
    #finish Cordial price check


def Grade_6_Dark_Mattercheck():
    global Grade_6_Dark_Matter
    #get prices for Grade 6 Dark Matter
    response3 = requests.get("https://universalis.app/api/history/54/10386/")

    files3 = response3.content
    Grade_6_Dark_Matterlist =[]
    checks = 0
    #write query to json file
    with open('Grade 6 Dark Matter.json', 'wb') as f:
        f.write(files3)

    #load json file data
    with open('Grade 6 Dark Matter.json') as json_file3:
        data3 = json.load(json_file3)

    while checks < 51:
    
        for i in data3['entries']:

            Grade_6_Dark_Matterlist.append((i['pricePerUnit']/345))
            checks += 1
        
    

    print("Gil/Seal for Grade 6 Dark Matter based on last purchase",Grade_6_Dark_Matterlist[0])
    Grade_6_Dark_Matter = (sum(Grade_6_Dark_Matterlist)/len(Grade_6_Dark_Matterlist))
    print("Average price per unit based on the last 50 purchases:", Grade_6_Dark_Matter)
    print("Last sold for:", (Grade_6_Dark_Matterlist[0]*345))
    print("Seals per item: 345")
    print()
    #finish Grade 6 Dark Matter price check

def Grade_7_Dark_Mattercheck():
    global Grade_7_Dark_Matter
    #get prices for Grade 7 Dark Matter
    response4 = requests.get("https://universalis.app/api/history/54/17837/")

    files4 = response4.content
    Grade_7_Dark_Matterlist = []
    checks = 0
    #write query to json file
    with open('Grade 7 Dark Matter.json', 'wb') as f:
        f.write(files4)

    #load json file data
    with open('Grade 7 Dark Matter.json') as json_file4:
       data4 = json.load(json_file4)
    while checks < 51:
        for i in data4['entries']:
            Grade_7_Dark_Matterlist.append((i['pricePerUnit']/575))
            checks += 1
        
    

    print("Gil/Seal for Grade 7 Dark Matter based on last purchase",Grade_7_Dark_Matterlist[0])
    Grade_7_Dark_Matter = (sum(Grade_7_Dark_Matterlist)/len(Grade_7_Dark_Matterlist))
    print("Average price per unit based on the last 50 purchases:", Grade_7_Dark_Matter)
    print("Last sold for:", (Grade_7_Dark_Matterlist[0]*575))
    print("Seals per item: 575")
    print()
    #finish Grade 7 Dark Matter price check

def Cokecheck():
    global Coke
    #get prices for Coke
    response5 = requests.get("https://universalis.app/api/history/54/5530")

    files5 = response5.content
    Cokelist = []
    checks = 0
    #write query to json file
    with open('Coke.json', 'wb') as f:
        f.write(files5)

    #load json file data
    with open('Coke.json') as json_file5:
        data5 = json.load(json_file5)
    while checks < 51:
         for i in data5['entries']:
            Cokelist.append((i['pricePerUnit']/200))
            checks += 1
    
    

    print("Gil/Seal for Coke based on last purchase",Cokelist[0])
    Coke = (sum(Cokelist)/len(Cokelist))
    print("Average price per unit based on the last 50 purchases:", Coke)
    print("Last sold for:", (Cokelist[0]*200))
    print("Seals per item: 200")
    print()
    #finish Coke price check

def sapcheck():
    global Hardened_Sap
    #get prices for Hardened Sap
    response6 = requests.get("https://universalis.app/api/history/54/5532")

    files6 = response6.content
    checks = 0
    saplist = []
    #write query to json file
    with open('Hardened Sap.json', 'wb') as f:
        f.write(files6)

    #load json file data
    with open('Hardened Sap.json') as json_file6:
        data6 = json.load(json_file6)
    while checks < 51:
        for i in data6['entries']:
            saplist.append((i['pricePerUnit']/200))
            checks += 1
    
    

    print("Gil/Seal for Hardened Sap based on last purchase",saplist[0])
    Hardened_Sap = (sum(saplist)/len(saplist))
    print("Average price per unit based on the last 50 purchases:", Hardened_Sap)
    print("Last sold for:", (saplist[0]*200))
    print("Seals per item: 200")
    print()
    #finish hardened sap price check

def Glamour_Dispellercheck():
    global Glamour_Dispeller
    #get prices for Glamour Glamour_Dispeller
    response7 = requests.get("https://universalis.app/api/history/54/7621")

    files7 = response7.content
    checks = 0
    Glamour_Dispellerlist = []
    #write query to json file
    with open('Glamour_Dispeller.json', 'wb') as f:
        f.write(files7)

    #load json file data
    with open('Glamour_Dispeller.json') as json_file7:
        data7 = json.load(json_file7)
    while checks < 51:
    
        for i in data7['entries']:
            Glamour_Dispellerlist.append((i['pricePerUnit']/200))
            checks += 1
    

    print("Gil/Seal for Glamour_Dispeller based on last purchase",Glamour_Dispellerlist[0])
    Glamour_Dispeller = (sum(Glamour_Dispellerlist)/len(Glamour_Dispellerlist))
    print("Average price per unit based on the last 50 purchases:", Glamour_Dispeller)
    print("Last sold for:", (Glamour_Dispellerlist[0]*200))
    print("Seals per item: 200")
    print()
    #finish Glamour Glamour_Dispeller price check
def checkbest():
    global Glamour_Prism
    global Glamour_Dispeller
    global Hardened_Sap
    global Coke
    global Grade_6_Dark_Matter
    global Grade_7_Dark_Matter
    global Cordial

    #This is currently the best and fastest way I've found to calculate the highest return
    #this a much better implementation than before
    list1 = [Glamour_Dispeller, Hardened_Sap, Coke, Grade_6_Dark_Matter, Grade_7_Dark_Matter, Glamour_Prism, Cordial]
    list1.sort()
 
    best = (list1[6])
    print(list1[6])
    variable_name = [k for k, v in globals().items() if v == best][0]
    print("Best gil/seal ratio is:", variable_name, "at", (list1[6]))


    
__main__()
