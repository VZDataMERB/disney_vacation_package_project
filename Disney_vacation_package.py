###############################################################################################
###############################################################################################
##
## Project: WALT DISNEY WORLD RESORT VACATION PACKAGE PLANNER
##
## Course Name: COP 1047C-227 Intro to Python Programming
##
## Group Members:
## Franchesca Nieves, Martha Requena-Smith, Edward Stone
##
## Instructor: Eduardo Salcedo
##
## Date: 12/09/2022
##
## Description: This program will allow the user to plan a Walt Disney World Resort vacation.
## The user will be able to select the type of resort and number of days they want to stay.
## The number of adults, children, and infants within their party will be captured.
## The program will then calculate the total cost of the vacation based on the
## number of days, the number of people in the party, and the season. The program will
## also display the total cost of the vacation in a table format. Credit card information
## will be captured and validated.
##
###############################################################################################
###############################################################################################

# Importing Modules
import calendar, datetime, time, re, sys, random, string

# Global Variables
# Park Ticket Prices
adult_basic_tkt = int(90)
child_basic_tkt = int(75)
infant_basic_tkt = int(0)  # Free, but was included for completeness and in case of future changes
Fl_taxrate = float(1.07)
FL_discount = float(.80)

# Resort Prices, based on a 1 night stay
resort_FLT = int(100)
dlx_rate = int(resort_FLT * 1.30)
prm_rate = int(resort_FLT * 1.60)

# Seasonal rates
low_sea = int(0)  # Baseline rate
reg_sea = low_sea * int(0.05)
peak_sea = low_sea * int(0.25)
blkout_days = low_sea * int(0.50)

# Seasonal date categories
season = ["low_sea", "reg_sea", "peak_sea", "blkout_days"]


# Functions
# Yes No Function
def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("yes", "no", "y", "n", "Y", "N"):
        response = input(question).lower()
    return response


# function to assign customer service rep when customer requests a live agent
def customer_service_rep():
    customer_service_reps = ['Franchesca', 'Martha', 'Edward', 'Bridgette', 'Ruby']
    agent = random.choice(customer_service_reps)
    return agent


# function to generate a random reservation number
def generate_reservation():
    reservation = ''
    for i in range(8):
        reservation += random.choice(string.ascii_letters + string.digits)
    return reservation


# Logo Function

team_logo = f""""                       
                                                 @@@@@                          
                                                 @@                             
                                                 @@                             
                                  @              @@                             
                                  @@@@@@        @@@@                            
                                  @@@          @@@@@@                           
                                  @@          @@@@@@@@                          
                                  @@         @@@@@@@@@@                         
                                 @@@@       @@@@@@@@@@@@                        
                      @@@@@@    @@@@@@        @@@@@@@@                          
                      @@@@     ..@@@@..     @@@@@@@@@@@@                        
                      @         @@@@@@       @@@@@@@@@@                         
                     @@          @@@@         @@@@@@@@                          
                    @@@@&        @@@@         @@@@@@@@   @@                     
                   @@@@@@@       @@@@  @@@@@. @@@@@@@@   @.                     
                 @@@@@@@@@@  @@@ @@@@ @@@@@@@ @@@@@@@@   @@                     
                 @@@@@@@@@@   @  @@@@@@@@@@@@@@@@@@@@@  @@@                     
                 @@@@@@@@@@  @@@ @@@@@@@@@@@@@@@@@@@@@ /@@@@                    
                  @@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@                    
                  @@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@**@@@@**                  
         @@@      @@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      @@@        
          @       @@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@    @@         
        (@@@   .@@@@@@@@@@@@@@@@@@@       @@@@@@   @@@@@@@@@@@@@@@  @@@@        
       @@@@@@    @@@@@@@@@@     @@@     @@@@@@     @@@@@@@@@@@@   @@@@@@       
      @@@@@@@@@  @@@@@@@@@               %@@@@          @@@@@@@@@@@@@@@@@@@     
      @@@@@@@@@@@@@@@@@@@@@                @@            @@@@@@@@@@@@@@@@@/     
        @@@@@@@@@@@@@@@@@@@@@@@               @@@@@@@@@@@@@@@@@@@@@@@@@@@       
       /@@@@@@@@@@@@@@@@@@@@@@@@           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       
      @@█╬╬╬█ ███ █╬ ███ ╬╬ ██▄ █ ██ █╬╬█ ██ █╬█ ╬╬ █╬╬╬█ ███ ███ █╬ ██▄@@
      @@█╬█╬█ █▄█ █╬ ╬█╬ ╬╬ █╬█ █ █▄ ██▄█ █▄ █▄█ ╬╬ █╬█╬█ █╬█ █▄╬ █╬ █╬█@@
      @@█▄█▄█ █╬█ ██ ╬█╬ ╬╬ ███ █ ▄█ █╬██ █▄ ╬█╬ ╬╬ █▄█▄█ █▄█ █╬█ ██ ███@@         
        @@@@@@@@@@@@@@@@@@@@@@                  @@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@@@@@  /@              @@@@@@@@@@@@@@@@@@@@@@@@@@      
      @@@@@@@@@@@@@@@@@@@@@                       @@@@@@@@@@@@@@@@@@@@@@@@      
      @@@@@@@@@@@@@@@@@@@@@@          @@&      @@@@@@@@@@@@@@@@@@@@@@@@@@@      
      @@@@@█▄█ ███ ██ ███ ███ █ ███ █╬╬█ ╬╬ ███ ███ ██ █╬█ ███ ███ ██@@@@@
      @@@@@███ █▄█ █╬ █▄█ ╬█╬ █ █╬█ ██▄█ ╬╬ █▄█ █▄█ █╬ ██▄ █▄█ █╬▄ █▄@@@@@
      @@@@@╬█╬ █╬█ ██ █╬█ ╬█╬ █ █▄█ █╬██ ╬╬ █╬╬ █╬█ ██ █╬█ █╬█ █▄█ █▄@@@@@
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
"""

mickey_face = f"""
               ./ddmMMMMMMMMMMddm-                              -ddmMMMMMMMMMMddm\.
           .+ddMMMMMMMMMMMMMMMMMMMMd:                        :ddMMMMMMMMMMMMMMMMMMMMd+.
         :dMMMMMMMMMMMMMMMMMMMMMMMMMMdÂ´                    `dMMMMMMMMMMMMMMMMMMMMMMMMMd:
       .dDMMMMMMMMMMMMMMMMMMMMMMMMMMMMd                    dMMMMMMMMMMMMMMMMMMMMMMMMMMMDd.
      dDMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdÂ´                  `dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMDd
     `MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd                    dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMDÂ´
     .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd,.mMMMMMMMMMMMMMMm..,MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMD
      dDMMMMMMMMMMMMMMMMMMMMMMMMMdm/-Â´     `-+dMMMd+-Â´      `ddmMMMMMMMMMMMMMMMMMMMMMMMMMDd
       dDMMMMMMMMMMMMMMMMMMMMMdd-              :m:              -ddMMMMMMMMMMMMMMMMMMMMMMDd
        `\dMMMMMMMMMMMMMMMMMMdd                 '                 ddMMMMMMMMMMMMMMMMMMMd/Â´
            `:dDMMMMMMmddMMMDd                                     ddMMMdmdddMMMMddm+:Â´
                       -DDMMM+           .mMm.     .mMm.           +DDMMm
                      .DMMMMM\          .MMMMMÂ´   `MMMMM:          /MMMMMD.
                      mMMMMMMM\         :MMMMM:   :MMMMM:         /MMMMMMMm
                     :MM+Â´Â´++dd.         :MMMM:   :MMMM:         .dd++``+MM.
                     .M        `           .ddmDDMddm.           Â´        M.
                      M-    ++            .MMMMMMMMMMM             ++    -M
                      `M.    .D+`          `+ddMMMdm+Â´          Â´+D.    .MÂ´
                       `M:     ddm\`                         Â´/ddm     :MÂ´
                         \M.     +DDMd\_                 _/ddMM+Â´    .M/
                           \M:    `dMMMMMDddmmmmmmmmdddMMMMMMMdÂ´   :M/
                             \.Mm   `+ddMMMMMMMMMMMMMMMMMdd+Â´   mM./
                                `ddm    -ddMMMMMMMMMMdd-    ddmÂ´
                                    -ddm                ddm-
                                         -ddmddmddmddm-
"""

# Main Program
# Prints the logo
time.sleep(3)
print(team_logo)

# Prints the welcome message
time.sleep(3)
print("""

         Let's help you plan your WALT DISNEY WORLD VACATION PACKAGE;

         Visit WALT DISNEY WORLD and see for yourself what makes it the
         most amazing attractions in the world. Get a free quote for 
         your WALT DISNEY WORLD vacation today! 

         Disney Vacations allows you to customize a vacation package
         to the Magic Kingdom. Take advantage of one of our many 
         packages that include your hotel, park tickets, and dining 
         reservations for one flat rate. 

    """)
# Prints getting started message
time.sleep(3)
print("Let's get some information from you before we get started.")

# Gets the user's name and personalizes the message valdiates the user's input is alpha
name = input("\nWhat is your name? ")
valid = False
while not valid:
    if name.isalpha():
        valid = True
    else:
        print("\nPlease enter a valid first name.")
        name = input("\nWhat is your name? ")

# Prints the personalized message
time.sleep(1)
print("\nHi " + name.title() + "! ", end="")
print("Let's begin building a MAGICAL vacation package!")

# Starts the vacation package builder using a calendar and date functions
see_calendar = ask_yes_no("\nNeed a calendar? 'yes' or 'no': ").lower().strip()
if see_calendar == 'yes' or see_calendar == 'y' or see_calendar == 'Y' or see_calendar == 'Yes' or see_calendar == 'YES':  # ***ADDED 'y' and 'Y' to the list of acceptable answers
    print(calendar.calendar(2023))
elif see_calendar == 'no':  # or see_calendar == 'NO' or see_calendar == 'No' or see_calendar == 'n' or see_calendar == 'N':  # THIS IS WHERE I MADE A CHANGE DUE TO ERRORS IN THE CODE
    print("\nWhat dates are you looking to travel? ")  # THIS REPEATS THE QUESTION

year = 2023

# Collects check in and check out dates
checkin_month = int(input('\nPlease enter numeric check-in month: '))
checkin_day = int(input('\nEnter day: '))

checkout_month = int(input('\nPlease enter numeric check-out month: '))
checkout_day = int(input('\nEnter day: '))



month = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

# validate season of the checkin date

if not (checkin_month in month):
    print("Invalid")

elif checkin_month == 9:
    if not (1 <= checkin_day <= 30):
        print("Invalid")
    elif (2 <= checkin_day <= 4):
        fare = "Blackout holiday"
        # print (fare)
    else:
        fare = "Low season"
        # print(fare)
elif checkin_month == 10:
    if not (1 <= checkin_day <= 31):
        print("Invalid")
    elif (7 <= checkin_day <= 9):
        fare = "Blackout holiday"
        # print(fare)
    else:
        fare = "Low season"
        # print(fare)
elif checkin_month == 11:
    if not (1 <= checkin_day <= 30):
        print("Invalid")
    elif (17 <= checkin_day <= 25):
        fare = "Blackout holiday"
        # print(fare)
    else:
        fare = "Low season"
        # print(fare)
elif checkin_month == 12:
    if not (1 <= checkin_day <= 31):
        print("Invalid")
    elif (16 <= checkin_day <= 31):
        fare = "Blackout holiday"
        # print(fare)
    else:
        fare = "Peak season"
        # print(fare)
elif checkin_month == 1:
    if not (1 <= checkin_day <= 31):
        print("Invalid")
    elif checkin_day == 1:
        fare = "Blackout holiday"
        # print(fare)
    else:
        fare = "Regular season"
        # print(fare)
elif checkin_month == 2:
    if not (1 <= checkin_day <= 28):
        print("Invalid")
    else:
        fare = "Regular season"
        # print(fare)
elif checkin_month == 3:
    if not (1 <= checkin_day <= 31):
        print("Invalid")
    else:
        fare = "Regular season"
        # print(fare)
elif checkin_month == 4:
    if not (1 <= checkin_day <= 30):
        print("Invalid")
    elif (1 == checkin_day <= 15):
        fare = "Blackout holiday"
        # print(fare)
    else:
        fare = "Regular season"
        # print(fare)
elif checkin_month == 5:
    if not (1 <= checkin_day <= 31):
        print("Invalid")
    elif (27 <= checkin_day <= 29):
        fare = "Blackout holiday"
        # print(fare)
    else:
        fare = "Peak season"
        # print(fare)
elif checkin_month == 6:
    if not (1 <= checkin_day <= 30):
        print("Invalid")
    else:
        fare = "Peak season"
        # print(fare)
elif checkin_month == 7:
    if not (1 <= checkin_day <= 31):
        print("Invalid")
    elif (1 <= checkin_day <= 4):
        fare = "Blackout holiday"
        # print(fare)
    else:
        fare = "Peak season"
        # print(fare)
elif checkin_month == 8:
    if not (1 <= checkin_day <= 31):
        print("Invalid")
    else:
        fare = "Peak season"
        # print(fare)

#check in and check out variables
check_in = datetime.date(year, checkin_month, checkin_day)

check_out = datetime.date(year, checkout_month, checkout_day)

# Collects number of adult guests and validates input
adults = input("\nHow many adults are traveling (10+ and older)? ")
valid = False
while not valid:
    if adults.isnumeric():
        valid = True
    else:
        print("\nPlease enter a valid number. (no dashes or spaces)")
        adults = input("\nHow many adults are traveling (10+ and older)? ")

# Collects number of children guests and validates input
children = input("\nHow many children between the ages of 3 - 9 are traveling? ")
valid = False
while not valid:
    if children.isnumeric():
        valid = True
    else:
        print("\nPlease enter a valid number")
        children = input("\nHow many children are traveling between the ages of 3-9? ")
#
# Collects number of infants guests adn validates input
infants = input("\nHow many infants under the age of 3 are traveling? ")
valid = False
while not valid:
    if infants.isnumeric():
        valid = True
    else:
        print("\nPlease enter a valid number")
        infants = input("\nHow many infants are in traveling under the age of 3? ")

# Collects number of rooms and validates input
number_of_rooms = input("\nHow many rooms would you like? ")
valid = False
while not valid:
#     if number_of_rooms.isnumeric():
#         valid = True
#     else:
#         print("\nPlease enter a valid number")
#         number_of_rooms = input("\nHow many rooms would you like? ")

    if int(number_of_rooms) > 1:
        print("invalid")
    elif number_of_rooms.isnumeric():
        valid = True
else:
    print("\nPlease enter a valid number")
    number_of_rooms = input("\nHow many rooms would you like? ")


# Calculates number or guests in total
def guests(adults, children, infants):
    total_num_guests = int(adults) + int(children) + int(infants)
    return total_num_guests


total_num_guests = guests(adults, children, infants)

total_num_paying_guests = int(adults) + int(children)

#
total_days = check_out - check_in
nights = datetime.timedelta(days=1)
total_nights = total_days.days - nights.days

# Date and time import for calculations
from datetime import date

d0 = check_in
d1 = check_out
delta = d1 - d0
# print(delta.days)

# Total Package and ticket prices for each room type without tax discount and sesonality applied
total_pluto_basic = (((delta.days * resort_FLT) * int(number_of_rooms)) + (int(adults) * adult_basic_tkt) + (
        int(children) * child_basic_tkt) + (int(infants) * infant_basic_tkt))
total_minnie_dlx = (((delta.days * dlx_rate) * int(number_of_rooms)) + (int(adults) * adult_basic_tkt) + (
        int(children) * child_basic_tkt) + (int(infants) * infant_basic_tkt))
total_tinkerbell_prm = (((delta.days * prm_rate) * int(number_of_rooms)) + (int(adults) * adult_basic_tkt) + (
        int(children) * child_basic_tkt) + (int(infants) * infant_basic_tkt))

# Determines the seasonal charge

# choice = ""
seasonal_charge = season
if season == 'reg_sea':
    seasonal_charge = reg_sea
elif season == 'peak_sea':
    seasonal_charge = peak_sea
elif season == 'blkout_days':
    seasonal_charge = blkout_days
else:
    seasonal_charge = low_sea

# Calculates the total cost of the vacation package  (including the seasonal charge)
seasonal_total_pluto_basic = (total_pluto_basic * seasonal_charge) + (total_pluto_basic)

seasonal_total_minnie_dlx = (total_minnie_dlx * seasonal_charge) + (total_minnie_dlx)

seasonal_total_tinkerbell_prm = (total_tinkerbell_prm * seasonal_charge) + (total_tinkerbell_prm)

# Prints the total cost of the vacation package  in a user-friendly format (including the seasonal charge)

t = f"""
{'-' * 100}
\n
     1. Pluto’s Basic Vacation Package:                    **PRICE QUOTE**  ${seasonal_total_pluto_basic:.2f}
            Park tickets
            Standard Hotel (Parking is not included)
\n\n
     2. Minnie’s Deluxe Vacation Package:                  **PRICE QUOTE**  ${seasonal_total_minnie_dlx:.2f}
            Park tickets
            Deluxe Hotel - includes swimming pool and parking
            Breakfast included
\n\n
     3. Tinkerbell's Premium Vacation Package:             **PRICE QUOTE**  ${seasonal_total_tinkerbell_prm:.2f}
            Park tickets
            Premium Hotel-Walking distance to park and includes parking
            Breakfast with Mickey and Minnie
            Adult entertainment included
            2 hour private tour of the park lead by PROFESSOR SALCEDO
\n\n
     4.  Speak to a LIVE Disney Vacation Planner
\n
{'-' * 100}
"""
# Prints the selected price quote for the 3 differnt packages. Also allows to exit to a LIVE agent
time.sleep(3)
print(t)

# Selection of package. Includes a loop back if the number is invalid. Prints specific details of each package using calculation and prior variables.
choice = int(input("\nPlease select the number of the package you would like to purchase: "))
while choice not in (1, 2, 3, 4):
    choice = input("\nOoops that is an invalid selection, please enter a valid choice: ")
    choice = int(choice)
if choice == 1:
    time.sleep(3)
    print(f"""
{'*' * 100}
    Great choice! You have selected the PLUTO'S BASIC VACATION PACKAGE
    Price:      ${seasonal_total_pluto_basic:.2f}  ***does not include taxes and fees***  


    Dates:      {checkin_month}/{checkin_day}/{year} - {checkout_month}/{checkout_day}/{year}  
                Your dates fall within a {fare.upper()} period

    Includes:   {delta.days} night stay at a Standard Disney World Resort
                {number_of_rooms} Standard hotel room(s)
                {total_num_guests} guests (including infants)
                {total_num_paying_guests * delta.days} Disney World Park Passes (infants under 3 do not require a park pass)
                Note: Parking is not included, taxes and other fees will be calculated at checkout  
{'*' * 100}          
    """)
elif choice == 2:
    time.sleep(3)
    print(f"""
{'*' * 100}
    Nice choice! You selected MINNIE'S DELUXE VACATION PACKAGE
    Price:      ${seasonal_total_minnie_dlx:.2f}   ***does not include taxes and fees***  

    Dates:      {checkin_month}/{checkin_day}/{year} - {checkout_month}/{checkout_day}/{year}  
                Your dates fall within a {fare.upper()} period

    Includes:   {delta.days} night stay at a Deluxe Disney World Resort
                {number_of_rooms} Deluxe hotel room(s)
                {total_num_guests} guests (including infants)
                {total_num_paying_guests * delta.days} Disney World Park Passes (infants under 3 do not require a park pass)
                {total_num_guests * delta.days} attending breakfast with Mickey and Minnie  
                {number_of_rooms} parking passes 
                {total_num_paying_guests} vouchers for private tour with Professor Salcedo 
                Note: taxes and other fees will be calculated at checkout    
{'*' * 100}      
    """)

elif choice == 3:
    time.sleep(3)
    print(f"""
{'*' * 100}
    Outstanding choice! You selected TINKERBELL'S PREMIUM VACATION PACKAGE
    Price:     ${seasonal_total_tinkerbell_prm:.2f}  ***does not include taxes and fees***  

    Dates:      {checkin_month}/{checkin_day}/{year} - {checkout_month}/{checkout_day}/{year}  
                Your dates fall within a {fare.upper()} period
    Includes:   {delta.days} night stay at a Premium Disney World Resort
                {number_of_rooms} Premium hotel room(s)
                {total_num_guests} guests (including infants)
                {total_num_paying_guests * delta.days} Disney World Park Passes (infants under 3 do not require a park pass)
                {total_num_guests * delta.days} Character breakfast vouchers (infants under 3 do not require a breakfast voucher)  
                {number_of_rooms} parking passes  
                Note: taxes and other fees will be calculated at checkout  
{'*' * 100}      
    """)

elif choice == 4:
    print(f"""
    You have selected to speak to a LIVE Disney Vacation Planner, please hold while we connect you to a representative
    """)
    time.sleep(3)
    print(f"""
    Thank you for your patience, you are now connected to a LIVE Disney Vacation Planner
    """)
    time.sleep(3)
    print(f"""
    Hello, my name is {customer_service_rep()} and I will be your Disney Vacation Planner today. How can I help you?
    """)  ## this is where we would need to add the code to connect to the live agent/ chatbot. the code would need to be able to take the user input and
    # then respond with the appropriate response. We have chosen to terminate at this point as the handoff has been made to the bot.
    quit()

# Print the Mickey Face
time.sleep(3)
print(mickey_face)

# Established the variable for different packages that can be pulled later in the code
if choice == 1:
    total_package = seasonal_total_pluto_basic
elif choice == 2:
    total_package = seasonal_total_minnie_dlx
elif choice == 3:
    total_package = seasonal_total_tinkerbell_prm
elif choice == 4:
    total_package = "pricing will be available soon"  # this is a placeholder for the live agent pricing as it exits the system

# Setting up the user's information
time.sleep(3)
print("\nWe'll need to gather some more information to secure your WALT DISNEY WORLD Vacation package")

# Collecting the user's information using alpha validation
first_name = input("\nPlease provide the first name that should appear on the reservation? ")
valid = False
while not valid:
    if first_name.isalpha():
        valid = True
    else:
        print("\nPlease enter a valid first name.")
        first_name = input("\nWhat is your first name? ")

# Collecting the user's information using alpha validation
last_name = input("\nWhat is your last name? ")
valid = False
while not valid:
    if last_name.isalpha():
        valid = True
    else:
        print("\nPlease enter a valid last name.")
        last_name = input("\nWhat is your last name? ")

# Collecting the user's information using and if statemen and @ validation
email = input("\nWhat is your email address? ")
valid = False
while not valid:
    if "@" in email:
        valid = True
    else:
        print("\nPlease enter a valid email address.")
        email = input("\nWhat is your email address? ")

# Collecting the user's information using numeric validation
phone = input("\nWhat is your phone number? (no dashes or spaces) ")
valid = False
while not valid:
    if phone.isnumeric():
        valid = True
    else:
        print("\nPlease enter a valid phone number, no dashes or spaces.")
        phone = input("\nWhat is your phone number? ")

# Collecting the user's stree information using alpha and numeric validation
street_address = input("\nWhat is your home mailing address? ")
# valid = False
# while not valid:
#     if street_address.isalnum():
#         valid = True
#     else:
#         print("\nPlease enter a valid address.")
#         street_address = input("\nWhat is your home mailing address? ")



# Collecting the user's city information using alpha validation
city = input("\nWhat is your city? ")
valid = False
while not valid:
    if city.isalpha():
        valid = True
    else:
        print("\nPlease enter a valid city.")
        city = input("\nWhat is your city? ")

# Collecting the user's state information using alpha and 2 character validation
state = input(
    "\nWhat is your state? Please use 2 letter abbreviation ").upper()  # I added this to make sure the user enters a valid state and we can use for discount code later
valid = False
while not valid:
    if state.isalpha() and len(state) == 2:
        valid = True
    else:
        print("\nPlease enter a valid state.")
        state = input("\nWhat is your state? ")

# Collecting the user's zip code information using numeric validation
zip_code = input("\nWhat is your zip/postal code? ")
valid = False
while not valid:
    if zip_code.isnumeric():
        valid = True
    else:
        print("\nPlease enter a valid zip code.")
        zip_code = input("\nWhat is your zip code? ")

# Collecting the user's country information using alpha validation
country = input("\nWhat country do you live in? ")
valid = False
while not valid:
    if country.isalpha():
        valid = True
    else:
        print("\nPlease enter a valid country.")
        country = input("\nWhat is your country do you live in? ")

# Confirming the user's information with a confirmatoin message and input has mulitple options for yes, It will all be printed out with case structure
confirm_text = input("\nWould you like to see your information? (y/n) ")
if confirm_text == "y" or confirm_text == "Y" or confirm_text == "yes" or confirm_text == "Yes":  # giving lots of options for yes
    print(
        "\nYour name is: " + first_name.title() + " " + last_name.title() + "\nYour email is: " + email.lower() + "\nYour phone number is: " + phone + "\nYour address is: " + street_address.upper() + "\nYour city is: " + city.title() + "\nYour state is: " + state.upper() + "\nYour zip code is: " + zip_code + "\nYour country is: " + country.upper())
else:
    print("\nNo problem, we'll move on.")

# Calculating the tax and discount rates for Florida residents
total_wo_disc = total_package * Fl_taxrate
total_with_discount = total_wo_disc * FL_discount

# Getting to the last part of the program, asking them to hold on before we finalize their package
time.sleep(3)
print("\nWe're ready to finalize your Walt Disney World Vacation Package")

# Florida discount confirmation and total validation
if state == "FL":
    time.sleep(3)
    print("\nWe see you are a *Florida Resident*,  Great news you qualify for a 20% discount!")
    time.sleep(3)
    print(
        f'\nYour total Disney Vacation Package, including taxes, fees and your Florida discount is ${total_with_discount:.2f}')  # ----- variable for grandtotal with Florida discount and 2 decimal places.
else:
    time.sleep(3)
    print(
        f'\nYour total Walt Disney Vacation Package, including taxes and fees is ${total_wo_disc:.2f}')  # -------- variable for Grandtotal without discount and 2 decimal places.

# Final confirmation message before payment information is collected
time.sleep(3)
print("\nPlease enter your payment information below to complete your Walt Disney Vacation Package purchase")

# Credit Card Information including validation length and numeric. It's a 6 digit number but should be 16
cc = input("\nWhat is your creidt card 6 digit number? ")
valid = False
while not valid:
    if cc.isnumeric() and len(cc) == 6:
        valid = True
    else:
        print("\nPlease enter a valid credit card number.")
        cc = input("\nWhat is your creidt card 6 digit number? ")

# Expiration date and validation of length and numeric
exp_date = input("\nWhat is the expiration date of your card, using 4 numeric values MMYY? ")
valid = False
while not valid:
    if len(exp_date) == 4 and exp_date.isdigit():
        valid = True
    else:
        print(
            "\nYour expiration date is valid - make sure to use MMYY format, no dashes and two digits for each (example 0123 for Jan 2023)")
        exp_date = input("\nWhat is the expiration date of your card, using 4 numeric values MMYY? ")

# CVV and validation of length and numeric
cvv = input("\nWhat is the 3 digit CVV?  ")
valid = False
while not valid:
    if len(cvv) == 3 and cvv.isdigit():
        valid = True
    else:
        print("\nYour CVV is not valid, please try again")
        cvv = input("\nWhat is the 3 digit  CVV?  ")

# Payment confirmation message before the program ends
time.sleep(3)
print("\nThank you for your payment information, we are now processing your Walt Disney Vacation Package")

# Generating a random 6 digit reservation number and confirming it with the user that it will be sent to the email they provided
time.sleep(3)
print("\nCONGRATULATIONS your Walt Disney Vacation Package confirmation is", generate_reservation().upper(),
      "and will be sent to your email", email.lower(), "real soon!")

# Final message before the program ends
time.sleep(3)
print("\nYour all set - Thank you for choosing Walt Disney Resorts Vacation Packages for your upcoming holiday!")

print()




# Disney quote and Mickey Mouse face
time.sleep(3)
print("\nHave a magical day, we'll see ya real soon!\n\n")
time.sleep(3)
print(mickey_face)

# end of program