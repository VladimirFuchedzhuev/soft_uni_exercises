movie = input()
standard = 0
student = 0
kid = 0
total_tickets = 0

while movie != "Finish":
    available_seats = int(input())
    movie_tickets = 0
    while movie_tickets < available_seats:
        ticket_type = input()
        if ticket_type == "standard":
            standard += 1
            total_tickets += 1
            movie_tickets += 1
        elif ticket_type == "student":
            student += 1
            total_tickets += 1
            movie_tickets += 1
        elif ticket_type == "kid":
            kid += 1
            total_tickets += 1
            movie_tickets += 1
        elif ticket_type == "End":
            break
    movie_occupancy = (movie_tickets / available_seats) * 100
    print(f"{movie} - {movie_occupancy:.2f}% full.")
    movie = input()

percent_standard = standard * 100 / total_tickets
percent_students = student * 100 / total_tickets
percent_kids = kid * 100 / total_tickets

print(f"Total tickets: {total_tickets}")
print(f"{percent_students:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kids:.2f}% kids tickets.")