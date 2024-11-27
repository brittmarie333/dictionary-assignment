#Task 1: Customer Service Ticket Tracker Demonstrate your ability to use 
# nested collections and loops by creating a system to track customer service tickets.

#Problem Statement: Develop a program that:
#Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).

#Implement functions to:
#Open a new service ticket.
#Update the status of an existing ticket.
#Display all tickets

# Function to generate the next ticket number / using class and while loop to store informationand keep code running until done w/program
class Ticket:
    def __init__(self, ticket_id, customer_name, issue_description, status="open"):
        self.ticket_id = ticket_id
        self.customer_name = customer_name
        self.issue_description = issue_description
        self.status = status

    def __str__(self):
        return f"Ticket ID: {self.ticket_id}, Customer: {self.customer_name}, Issue: {self.issue_description}, Status: {self.status}"

class TicketSystem:
    def __init__(self):
        self.tickets = []
        self.ticket_counter = 1 

    def create_ticket(self, customer_name, issue_description):
        ticket_id = self.ticket_counter
        self.ticket_counter += 1
        new_ticket = Ticket(ticket_id, customer_name, issue_description)
        self.tickets.append(new_ticket)
        print(f"Ticket Created: {new_ticket}")

    def view_tickets(self):
        if not self.tickets:
            print("No tickets to display.")
        else:
            for ticket in self.tickets:
                print(ticket)

    def update_ticket_status(self, ticket_id, new_status):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                if new_status.lower() in ['open', 'closed']:
                    ticket.status = new_status.lower()
                    print(f"Ticket ID {ticket_id} status updated to {new_status}.")
                else:
                    print("Invalid status. Please choose 'open' or 'closed'.")
                return
        print(f"Ticket ID {ticket_id} not found.")

def main():
    ticket_program = TicketSystem()

    while True:
        print("\nTicket System Menu:")
        print("1. Create a New Ticket")
        print("2. View All Tickets")
        print("3. Update Ticket Status")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        try:
            if choice == '1':
                customer_name = input("Enter customer name: ")
                issue_description = input("Enter issue description: ")
                ticket_program.create_ticket(customer_name, issue_description)
            
            elif choice == '2':
                ticket_program.view_tickets()

            elif choice == '3':
                ticket_id = int(input("Enter ticket ID to update: "))
                new_status = input("Enter new status (open/closed): ")
                ticket_program.update_ticket_status(ticket_id, new_status)
            
            elif choice == '4':
                print("Thank you, your session is ending.")
                break
            
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("OOPS, something went wrong!")
        
if __name__ == "__main__":
    main()
    