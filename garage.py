class Garage():
    def __init__(self):
        self.tickets_today = 0
        self.tickets = [10,9,8,7,6,5,4,3,2,1]
        self.parkingSpaces = ['space', 'space', 'space', 'space', 'space', 'space', 'space', 'space', 'space', 'space']
        self.currentTickets = {'paid':[], 'unpaid':[]}

    def take_ticket(self):
        if self.parkingSpaces:
            unpaid_ticket = self.tickets.pop()
            self.currentTickets['unpaid'].append(unpaid_ticket)
            self.parkingSpaces.remove('space')
            print(f"Your ticket number is {unpaid_ticket}.")
        else:
            print("The garage is full. Come back again later.")

    def pay_for_parking(self):
        ticket_number = int(input("What is your ticket number? "))
        if ticket_number in self.currentTickets['unpaid']:
            payment = input("Tickets at this garage are $5. Enter 5 to continue and pay $5. ")
            if payment == '5':
                print("Your ticket has been paid and you have 15 minutes to leave.")
                self.currentTickets['unpaid'].remove(ticket_number)
                self.currentTickets['paid'].append(ticket_number)
                self.tickets_today += 1
            else:
                print("You must pay before parking.")
        else:
            print("That's an invalid ticket number. Please enter again.")
  
    def leave_garage(self):
        leave = int(input("What is your ticket number? "))
        if leave in self.currentTickets['unpaid']:
            leave_payment = input("Your ticket has not been paid. Enter 5 to pay the $5 amount due. ")
            if leave_payment == '5':
                print("--Paid-- Thank you for parking with us today.")
                leave_ticket_unpaid = self.currentTickets['unpaid'].remove(leave)
                self.tickets.append(leave)
                self.parkingSpaces.append('space')
        elif leave in self.currentTickets['paid']:
            print("Thank you for parking with us today.")
            leave_ticket_paid = self.currentTickets['paid'].remove(leave)
            self.tickets.append(leave)
            self.parkingSpaces.append('space')
        else:
            print("That's an invalid ticket number. Please enter again.")

    def admin_commands(self):
        admin_response = input("What's the admin password? ")
        if admin_response == '7654':
            admin_request = input("What would you like to do?\n1: Print today's paid tickets | 2: Print current garage data ")
            if admin_request == '1':
                print(f"The total of paid tickets today are: {self.tickets_today}")
            elif admin_request == '2':
                print(f"The current available tickets are: {self.tickets}")
                print(f"The current available spaces are: {self.parkingSpaces}")
                print(f"The current tickets being used are: {self.currentTickets}")
            else:
                print("Sorry. That's an invalid admin command.")
        else:
            print("Incorrect password.")



garage_user = Garage()


def park():
    while True:
        response = input("What would you like to do?\nEnter | Pay | Exit ")
        if response.lower() == 'enter':
            garage_user.take_ticket()
        elif response.lower() == 'pay':
            garage_user.pay_for_parking()
        elif response.lower() == 'exit':
            garage_user.leave_garage()
        elif response.lower() == 'admin':
            garage_user.admin_commands()
        else:
            print("Invalid. Please try again.")

park()



