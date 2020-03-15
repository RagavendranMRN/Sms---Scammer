#Purely for Education Purpose Only - Don't Use for illegial 
#Be responsible and use wisely!

#*********************************Coding************************************

#Importing Required Libraries
import requests, os, sys, time

# Modularization the options available
def Sms_Option() :
    print("1.Send Anonymous sms")
    print("2.Check status of sms")

#Operations 1 - Send Msg , 2 - Status
def Operation() :
    ctrl = input("What you want to do : ")
    if ctrl == "1" :
        sms()
    elif ctrl == "2" :
        status()
    else :
        print("Invalid number")

#Message Scammer function logic
def sms() :
   Mobile_Number = input("Enter the Phone Number : ")
   msg = input("message to send : ")

# Using TextBelt API for scammer
# Only one message per Day
# It has limitation Here Key:'textbelt' is a free demo availabile in Textbelt 
# If you want to send more than one anonymous message, signup to Textbelt api with different pricning available

   	response = requests.post('https://textbelt.com/text',{
	'phone' : Mobile_Number,
	'message' : msg ,
	'key' : 'textbelt'
   })

   print(response.text)
   if '"success" : true' in response.text :
       print('Msg delivered! ')
   if '"success" : false' in response.text :
       print("failed to send msg!\n Sorry!! Try again!! ")

#Message Scammer Status Function
def status() :
  textID = input("Enter textID of sms : ")
  response = requests.post('https://textbelt.com/textID')
  print(response.text)
  if '"status" : DELIVERED' in response.text :
       print('Msg delivered!')

#Main Funcationality
Sms_Option()
Operation()
