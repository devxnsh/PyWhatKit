#pywhatkit guide thingy
import pywhatkit as kit
from pywhatkit.exceptions import CountryCodeException, InvalidBrowserName
import countrydatabase
# About : PyWhatKit is a Python library with no addition setup. Can do a lot of things other than sending a text
# Can be installed via pip :  pip install pywhatkit

# First import the library using the command import pywhatkit as kit and then proceed to call the functions
# Functions:
# kit.sendwhatmsg() : Main function.
# Parameters:
    # phone_num  - Phone number of target with country code
    # message  - Message that you want to sendwhatmsg
    # time_hour  - Hours at which you want to send message in 24 hour format
    # time_min  - Minutes at which you want to send message
    # wait_time (optional, val=20) - Seconds after which the message will be sent after opening the web
    # print_waitTime (optional, val=True) - Will print the remaining time if set to true
ch=input("Do you want to send message to a person or a group p/g?")
def personmessage():
    phone = input("Enter phone number with country code" )
    hour = int(input("Enter the hour you want to send the message in"))
    min = int(input("Enter the minute you want to send the message in"))
    browser = str(input("Enter your browser"))
    message = str(input("Enter Message to Send"))
    lmao = "Open "+ browser +". When opened fully, press any key to continue"
    wait= input(lmao)
    print("Please Open your browser using Alt + Tab. Try not to move your mouse.")
    try:
        kit.sendwhatmsg(str(phone), message,hour,min,20,True,browser)
    except CountryCodeException:
        country = input("Please enter your country")
        dialcode= countrydatabase.country_use(country)
        phone = dialcode + phone
        kit.sendwhatmsg(str(phone), message,hour,min,20,True,browser)
    except InvalidBrowserName:
        browser=input("please select browser from chrome, firefox, brave, opera")
        kit.sendwhatmsg(str(phone), message,hour,min,20,True,browser)
def groupmessage():
    
    try:
        group = input("Enter group ID" )
        hour = int(input("Enter the hour you want to send the message in"))
        min = int(input("Enter the minute you want to send the message in"))
        browser = str(input("Enter your browser"))
        lmao = "Open ", browser,". When opened fully, press any key to continue"
        message=input("Enter what message to send")
        wait= input(lmao)
        kit.sendwhatmsg_to_group(group, message,hour,min,20,True,browser)
    except InvalidBrowserName:
        browser=input("please select browser from chrome, firefox, brave, opera")
        kit.sendwhatmsg_to_group(group, message,hour,min,20,True,browser)

if ch=="p":
    personmessage()
if ch=="g":
    groupmessage() 
#Common errors :
    # Message not getting delivered - Check internet speed and increase wait_time to 30 or above 
    # CallTimeException - The web takes some time to load so some delay is required, make sure the seconds left is greater than the wait_time
    # SyntaxError - Make sure the first two parameters are string and the rest are int

# kit.playonyt()
# This function can be used to search and play a particular video on YouTube by using just the keyword, like "Shape of You song"
# Parameters : topic
yt=input("Do you want to play something on youtube?")
if yt == 'y':
    search = input("Enter whatever you wanna search. It will play most relevant video automatically.")
    kit.playonyt(search)
#Errors : Video not opening - Make sure the topic exists or you have provided proper spelling

# pywhatkit.search() : This function can be used to make a google search for any term. Parameters : topic
search = input("Do you wanna search something on google?")
if search == 'y':
    keyword = input("Enter what do you wanna search.")
    kit.search(keyword)

# pywhatkit.info() This function can be used to fetch information about any topic. Parameters :
# topic (required) ; lines (optional, val=3) - Number of lines that you want to print about it
info = input("press y to get info about a topic of choice")
if info=='y':
    infogainer=input("What do you wanna get info about?")
    kit.info(infogainer)
#Errors:
    # Not returning paragraph - Make sure the topic exists and you are providing specific title
    #DisambiguateError

# pywhatkit.text_to_handwriting(): This function can be used to convert text to hand written characters
# Parameters:
    # string (required) - String that you want to convert to handwritten text
    # save_to (optional, val = "pywhatkit.png") - Path where the image will be saved
    # rgb (optional, val = [0,0,138]) - Color of the handwritten character in rgb format
hand=input("press y to get funny handwriting for your text")
if hand =='y':
    text = input("Input what do you wanna convert")
    kit.text_to_handwriting(text)

# kit.image_to_ascii_art()
# This function can be used to convert any image to ASCII art
# Parameters:
    # imgpath (required) - Path to the image that you want to convert
    # output_file (optional, val=pywhatkit_asciiart.txt") - File where you want to save the output characters
asciiart=input("if you have an image which you want should look funny, press y")
if asciiart=='y':
    loc=input("Enter its full location with name and extension")
    kit.image_to_ascii_art(loc)
# Some common errors
# File not found - Make sure that the path of the image is valid


# Some other functions
# pywhatkit.showHistory() # Will show information of all the messages sent using this library
history=input("Show History?")
if history == 'y' :
    kit.showHistory()
# pywhatkit.shutdown(time=100) # Will shutdown the system
shutdownquestion=input("Press y to shutdown")
if shutdownquestion=='y':
    kit.shutdown()
# pywhatkit.cancelShutdown() # Will cancel the scheduled shutdown
cancelshutdownquestion=input("Press y to cancel shutdown")
if cancelshutdownquestion=='y':
    kit.cancelShutdown()
# pywhatkit.tutorial_hindi/english() # Will open a tutorial on how to use this library on YouTube in respective language
tutorial=input("if you want a tutorial, press y")
if tutorial=='y':
    language=input("Enter tutorial language")
    if language.lower == 'english':
        kit.tutorial_english()
    elif language.lower == 'hindi':
        kit.tutorial_hindi()
discord= input("do you want to join our discord?")
if discord == 'y':    
    kit.join_discord() #Will redirect you to our Discord server
mailer=input("do you want to send an email?")
def emailwrite():
    mailid = input("Enter your email address")
    mailpass=input("ENter your email password (SECURE LINE)")
    mailsub=input("Enter subject of email")
    mailcontent=input("Enter content of your email.")
    mailrecvid=input("Enter Email ID Of person you want to send an e-mail.")
    kit.send_mail(mailid, mailpass, mailsub, mailcontent, mailrecvid) 

if mailer == 'y':
    emailwrite()
#    kit.help.<function>() # For more information
