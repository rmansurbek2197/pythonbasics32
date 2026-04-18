class Movie:
    def __init__(self, title, duration, genre):
        self.title = title
        self.duration = duration
        self.genre = genre

class Hall:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.seats = [Seat(i) for i in range(capacity)]

class Seat:
    def __init__(self, number):
        self.number = number
        self.is_available = True

class Booking:
    def __init__(self, movie, hall, seat, date, time):
        self.movie = movie
        self.hall = hall
        self.seat = seat
        self.date = date
        self.time = time

class Cinema:
    def __init__(self):
        self.movies = []
        self.halls = []
        self.bookings = []

    def add_movie(self, title, duration, genre):
        self.movies.append(Movie(title, duration, genre))

    def add_hall(self, name, capacity):
        self.halls.append(Hall(name, capacity))

    def book_seat(self, hall_name, seat_number, movie_title, date, time):
        for hall in self.halls:
            if hall.name == hall_name:
                for seat in hall.seats:
                    if seat.number == seat_number and seat.is_available:
                        for movie in self.movies:
                            if movie.title == movie_title:
                                booking = Booking(movie, hall, seat, date, time)
                                self.bookings.append(booking)
                                seat.is_available = False
                                return
                        break
                break

    def show_movies(self):
        for movie in self.movies:
            print(f"Title: {movie.title}, Duration: {movie.duration}, Genre: {movie.genre}")

    def show_halls(self):
        for hall in self.halls:
            print(f"Name: {hall.name}, Capacity: {hall.capacity}")

    def show_bookings(self):
        for booking in self.bookings:
            print(f"Movie: {booking.movie.title}, Hall: {booking.hall.name}, Seat: {booking.seat.number}, Date: {booking.date}, Time: {booking.time}")

cinema = Cinema()
cinema.add_movie("The Shawshank Redemption", 2.5, "Drama")
cinema.add_movie("The Godfather", 3, "Crime")
cinema.add_hall("Hall 1", 100)
cinema.add_hall("Hall 2", 50)
cinema.book_seat("Hall 1", 1, "The Shawshank Redemption", "2024-01-01", "10:00")
cinema.book_seat("Hall 1", 2, "The Shawshank Redemption", "2024-01-01", "10:00")
cinema.show_movies()
cinema.show_halls()
cinema.show_bookings()