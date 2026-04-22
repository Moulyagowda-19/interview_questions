# Ticket Booking System

def ticket_booking_system(seats, requests):
    print("Total Seats:", seats)
    print("Booking Status:")

    for i in range(len(requests)):
        if seats > 0:
            print("Booked")
            seats -= 1
        else:
            print("Waiting List")

if __name__ == "__main__":
    seats = 3
    requests = [1, 1, 1, 1]

    ticket_booking_system(seats, requests)
