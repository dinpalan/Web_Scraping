#usr/bin/env python3
#Save file as <title>.py in your preferred location. Then start typing
#import module in this space
import argparse
import re
import os
import requests
from bs4 import BeautifulSoup
from loguru import logger
import smtplib
import time
from twilio.rest import Client

def scraping():
    
#write your function here
#argparse with description
#Please change the words given inside <>

       try:
           
            parser = argparse.ArgumentParser(description="<Your description>")
            parser.print_help()
            logger.info("Started scraping website")
            URL="<Enter your URL>"
            r=requests.get(URL)
            soup = BeautifulSoup(r.text, 'html.parser')
            #print(soup)
            l = soup.find('div', class_ = 'YMlKec fxKbKc')
            a = l.text.strip()
            b = "<Any Message you want to send>"+a;
            print(a)
            #while True:
                #time.sleep(2)
            if a<='<some value>':
                logger.success("<Any Message>")
                print("Sending mail")
                def mail():    
                    sender = input("Please enter the sender email id")
                    passwd = input("Please enter the passsword")
                    server = smtplib.SMTP('smtp.gmail.com',587)
                    server.ehlo()
                    server.starttls()
                    server.login(sender,passwd)
                    T=input("Please enter the receiver email id")
                    s="<Any Message>"
                    BODY =f"To: {T}\r\nFrom: {sender}\r\nSubject: {s}\r\n{b}"
                    try:
                        server.sendmail(sender,T,BODY)
                        print("email sent")
                        logger.success("Email is sent")
                    except:
                        print('error sending email')
                    server.quit()
                mail()
                def twilio():
                    sid=input("Please enter the twilio password id")
                    auth=input("Please enter the twilio password")
                    client=Client(sid,auth)
                    fa=input("Please enter the twilio phone number")
                    fb=input("Please enter your phone number")
                    message = client.messages.create(to=fb,
                                                     from_=fa, body=b)
                    print(message.sid)
                    logger.success("SMS is sent")
                twilio()              
            else:
                    #print("<Any Message>")
                logger.error("<Any Message>")

    
       except:
           print("Please try again later")
       
def main():
  scraping()
  

if __name__== '__main__':
    main() 
