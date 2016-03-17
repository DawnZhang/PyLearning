"""This is a calendar. Users can view, add, update, or delete an event on the calendar"""

from time import sleep, strftime

FIRST_NAME = "Dawn"
calendar = {}

def welcome():
  print("Welcome! " + FIRST_NAME)
  print("Calendar is opening...")
  sleep(1)
  print("Today is: " + strftime("%A %B %d, %Y"))
  print("Time is:" + strftime("%H:%M:%S"))
  sleep(1)
  print("What would you like to do?")
  
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print("Calendar is empty!")
      else:
        print(calendar)
    elif user_choice == "U":
      data = input("What date? ")
      update = input("Enter the update: ")
      calendar[data] = update
      print("Update being successful!")
      print(calendar)
    elif user_choice == "A":
      event = input("Enter event: ")
      date = input("Enter date(MM/DD/YYYY): ")
      if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
        print("You entered an invalid date!")
        try_again = input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print("Event was successfully added!")
        print(calendar)
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print("Calendar is empty!")
      else:
        event = input("What event? ")
        for date in calendar.keys():
          if event == calendar[date]:
            del(calendar[date])
            print("Event was successfully deleted!")
            print(calendar)
          else:
            print("An incorrect event was specified!")
    elif user_choice == "X":
      start = False
    else:
      print("Invalid command was entered! Exiting...")
      break
    
start_calendar()
