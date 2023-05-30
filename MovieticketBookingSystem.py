
class User:
    def __init__(self, name, age, email, password):
        self.__name = name
        self.__age = age
        self.__email = email
        self.__password = password

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def save_user_details(self):
        try:
            with open('user_details.txt', 'a') as file:
                file.write(f"Name: {self.__name}\n")
                file.write(f"Age: {self.__age}\n")
                file.write(f"Email: {self.__email}\n")
                file.write(f"Password: {self.__password}\n")
                file.write("--------------------------------\n")
            print("User sign up successful!")
        except IOError as e:
            print(f"An error occurred while saving user details: {e}")


class Movie:
    def __init__(self, name, genre, rating):
        self.name = name
        self.genre = genre
        self.rating = rating

    def display_details(self):
        print(f"Name: {self.name}\tGenre: {self.genre}\tRating: {self.rating}")


class DramaMovie(Movie):
    def __init__(self, name, rating):
        super().__init__(name, "Drama", rating)

    def display_details(self):
        print("Drama Movie Details:")
        super().display_details()


class ActionMovie(Movie):
    def __init__(self, name, rating):
        super().__init__(name, "Action", rating)

    def display_details(self):
        print("Action Movie Details:")
        super().display_details()


class ComedyMovie(Movie):
    def __init__(self, name, rating):
        super().__init__(name, "Comedy", rating)

    def display_details(self):
        print("Comedy Movie Details:")
        super().display_details()


class Theater:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        print(f"Movies in {self.name}:")
        for movie in self.movies:
            movie.display_details()


class BookingApplication:
    def __init__(self):
        self.theaters = []

    def add_theater(self, theater):
        self.theaters.append(theater)

    def book_ticket(self, theater_name, movie_name, ticket_amount):
        theater = None
        for t in self.theaters:
            if t.name == theater_name:
                theater = t
                break

        if theater:
            for movie in theater.movies:
                if movie.name == movie_name:
                    print(f"'{ticket_amount}' tickets booked for '{movie.name}' in '{theater.name}'.")
                    return
            print(f"Movie '{movie_name}' is not available in '{theater_name}'.")
        else:
            print(f"Theater '{theater_name}' is not found in the booking application.")


# ------ Menu -------

def display_menu():
    print("          MOVIE TICKET BOOKING SYSTEM         ")
    print("1. Sign Up")
    print("2. Login")
    print("3. Exit")


def sign_up():
    print("\n")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    user = User(name, age, email, password)
    user.save_user_details()


def login(booking_app):
    print("\n")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    found_user = False

    with open('user_details.txt', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break

            if "Email: " in line and email in line:
                user_password = file.readline().strip().split(": ")[1]
                if user_password == password:
                    found_user = True
                    print("-----Login successful-----")
                    print("\n")
                    for theater in booking_app.theaters:
                        theater.display_movies()
                        print("\n")
                    choice = input("Enter the theater name [a, b, c]: ")
                    if choice == 'a':
                        theater_name = "Mnsuam Theater A"
                    elif choice == 'b':
                        theater_name = "Mnsuam Theater B"
                    elif choice == 'c':
                        theater_name = "Mnsuam Theater C"
                    else:
                        print("Invalid Theater Name")
                        break
                    movie_name = input("Enter the movie name: ")
                    ticket_amount = int(input("Enter the number of tickets: "))
                    print("\n")
                    booking_app.book_ticket(theater_name, movie_name, ticket_amount)
                    print("\n")
                    break

    if not found_user:
        print("Invalid email or password.")


# Main program
booking_app = BookingApplication()

theater_a = Theater("Mnsuam Theater A", "Block A")
theater_b = Theater("Mnsuam Theater B", "Block B")
theater_c = Theater("Mnsuam Theater C", "Block C")

theater_a.add_movie(ActionMovie("Dune", 8.5))
theater_a.add_movie(ComedyMovie("It", 7.9))
theater_b.add_movie(DramaMovie("The Pursuit of Happyness", 8.0))
theater_b.add_movie(ActionMovie("The Dark Knight", 9.0))
theater_c.add_movie(ComedyMovie("The Hangover", 7.7))

booking_app.add_theater(theater_a)
booking_app.add_theater(theater_b)
booking_app.add_theater(theater_c)

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        sign_up()
    elif choice == '2':
        login(booking_app)
    elif choice == '3':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
