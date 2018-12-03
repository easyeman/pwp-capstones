class User(object):
   
    def __init__(self, name, email):
       
        if email.find("@") == -1 or (email.find(".com") == -1 and email.find(".edu") == -1 and email.find(".org") == -1):
            print("The email {email} is invalid, please ensure it has an @ and a .com, .edu, or .org domain.".format(email=email))
        else:
            self.name = name
            self.email = email
            self.books = {}

    def __repr__(self):
       
        cnt = 0
        for item in self.books.keys():
            cnt += 1
        return "User {name} with email {email} has read {count} book(s) with an average rating of {rating}".format(name=self.name,email=self.email,count=cnt,rating=self.get_average_rating())

    def __eq__(self, other_user):
        
        if isinstance(other_user, User):
            return self.name == other_user.name and self.email == other_user.get_email()
        else:
            print("Object on the right side of the equality is of type {type}, and should be of type User".format(type=type(other_user)))

    def get_email(self):
       
        return self.email

    def get_name(self):
        
        return self.name

    def change_email(self, address):
       
        if address.find("@") == -1 or address.find(".com") == -1 or address.find(".edu") == -1 or address.find(".org") == -1:
            print("The eamil {email} is invalid, please ensure it has an @ and a .com, .edu, or .org domain.".format(email=address))
        else:
            old_email = self.email
            self.email = address
            print("{name}'s email has changed from {old} to {new}".format(name=self.name,old=old_email,new=self.email))

    def read_book(self, book, rating=None):
       
        if isinstance(book, Book):
            self.books.update({book: rating})
        else:
            print("Argument book is not of type Book. Please pass a Book instance.")

    def get_average_rating(self):
        
        total = 0
        n = 0
        if len(self.books) > 0:
            for rating in self.books.values():
                if rating:
                    total += rating
                    n += 1
                else:
                    continue
        if n > 0:
            return total/n
        else:
            print("There are no books with ratings for {user}".format(user=self.name))

    def get_books_read(self):
       
        return len(self.books)

class Book(object):
    
    def __init__(self, title, isbn, price):
      
        self.title = title
        self.isbn = isbn
        self.price = price
        self.ratings = []

    def __eq__(self, other_book):
       
        if isinstance(other_book, Book):
            return self.title == other_book.title and self.isbn == other_book.isbn
        else:
            print("Object on the right side of the equality is of type {type}, and should be of type User".format(type=type(other_book)))

    def __hash__(self):
       
        return hash((self.title, self.isbn))

    def get_title(self):
        
        return self.title

    def get_price(self):
       
        return self.price

    def get_isbn(self):
       
        return self.isbn

    def set_isbn(self, isbn):
       
        old_isbn = self.isbn
        self.isbn = isbn
        print("{title}'s isbn has changed from {old} to {new}".format(title=self.title,old=old_isbn,new=self.isbn))

    def add_rating(self, rating):
        
        if not rating or rating < 0 or rating > 4:
            print("{rating} is invalid. Please pass a numeric rating between 0 and 4 inclusive.".format(rating=rating))
        else:
            self.ratings.append(rating)

    def get_average_rating(self):
       
        total = 0
        n = 0
        if len(self.ratings) > 0:
            for rating in self.ratings:
                total += rating
                n += 1
            return total/n
        else:
            print("There are no ratings for {title}".format(title=self.title))

class Fiction(Book):
   
    def __init__(self, title, isbn, author, price):
        
        super().__init__(title, isbn, price)
        self.author = author

    def __repr__(self):
       
        return "{title} by {author} for ${price}".format(title=self.title,author=self.author,price=self.price)

    def get_author(self):
        
        return self.author

class Non_Fiction(Book):
    
    def __init__(self, title, isbn, level, subject, price):
       
        super().__init__(title, isbn, price)
        self.level = level
        self.subject = subject

    def __repr__(self):
        
        return "{title}, a {level} manual on {subject} for ${price}".format(title=self.title,level=self.level,subject=self.subject,price=self.price)

    def get_subject(self):
        
        return self.subject

    def get_level(self):
       
        return self.level

class TomeRater(object):
    
    def __init__(self):
       
        self.users = {}
        self.books = {}

    def __repr__(self):
        
        n_books = len(self.books)
        n_users = len(self.users)
        most_read = self.most_read_book()
        highest_rated = self.highest_rated_book()
        most_positive = self.most_positive_user()

        return "This TomeRater has {books} book(s) and {users} user(s).\nWith {most_read} being read the most, {highest} having the highest average rating,\nand {most_positive} giving the most positive reviews.".format(books=n_books,users=n_users,most_read=most_read,highest=highest_rated,most_positive=most_positive)

    def __eq__(self, other_rater):
        
        if isinstance(other_rater, TomeRater):
            return self.books == other_rater.books and self.users == other_rater.users
        else:
            print("Object on the right side of the equality is of type {type}, and should be of type TomeRater".format(type=type(other_rater)))


    def create_book(self, title, isbn, price):
        
        isbns = [book.get_isbn() for book in self.books.keys()]
        if isbn in isbns:
            print("The isbn {isbn} already exists for another book. Please give a unique isbn.".format(isbn=isbn))
        else:
            return Book(title, isbn, price)

    def create_novel(self, title, author, isbn, price):
        
        isbns = [book.get_isbn() for book in self.books.keys()]
        if isbn in isbns:
            print("The isbn {isbn} already exists for another book. Please give a unique isbn.".format(isbn=isbn))
        else:
            return Fiction(title, isbn, author, price)

    def create_non_fiction(self, title, level, subject, isbn, price):
        
        isbns = [book.get_isbn() for book in self.books.keys()]
        if isbn in isbns:
            print("The isbn {isbn} already exists for another book. Please give a unique isbn.".format(isbn=isbn))
        else:
            return Non_Fiction(title, isbn, subject, level, price)

    def add_book_to_user(self, book, email, rating=None):
        
        if self.users.get(email):
            self.users[email].read_book(book, rating)
            self.books[book] = self.books.get(book, 0) + 1
            if rating:
                    book.add_rating(rating)
        else:
            print("No user with email {email}!".format(email=email))

    def add_user(self, name, email, books=None):
        
        if email.find("@") == -1 or (email.find(".com") == -1 and email.find(".edu") == -1 and email.find(".org") == -1):
            print("The eamil {email} is invalid, please ensure it has an @ and a .com, .edu, or .org domain.".format(email=email))
        else:
            user = self.users.get(email)
            if user:
                print("User {name} currently exists with email {email}. Please use a different email.".format(name=user.get_name(),email=email))
            else:
                self.users.update({email: User(name, email)})
                if books:
                    for book in books:
                        self.add_book_to_user(book, email)

    def print_catalog(self):
        
        for book in self.books.keys():
            print(book)

    def print_users(self):
       
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        
        max_reading = 0
        max_book = ""
        for book, reading in self.books.items():
            if reading > max_reading:
                max_book = book
                max_reading = reading
            else:
                continue
        return max_book

    def highest_rated_book(self):
        
        max_rating = 0
        max_book = ""
        for book in self.books.keys():
            rating = book.get_average_rating()
            if rating > max_rating:
                max_book = book
                max_rating = rating
            else:
                continue
        return max_book

    def most_positive_user(self):
       
        max_rating = 0
        max_user = ""
        for user in self.users.values():
            rating = user.get_average_rating()
            if rating > max_rating:
                max_user = user
                max_rating = rating
            else:
                continue
        return max_user

    def get_n_most_read_books(self, n):
        
        if type(n) == int:
            books_sorted = [k for k in sorted(self.books, key=self.books.get, reverse=True)]
            return books_sorted[:n]
        else:
            print("The argument n = {n} is not of type int. Please pass an int.".format(n=n))

    def get_n_most_prolific_readers(self, n):
        
        if type(n) == int:
            readers = [(reader, reader.get_books_read()) for reader in self.users.values()]
            readers_sorted = [k[0] for k in sorted(readers, key=lambda reader: reader[1], reverse=True)]
            return readers_sorted[:n]
        else:
            print("The argument n = {n} is not of type int. Please pass an int.".format(n=n))

    def get_n_most_expensive_books(self, n):
        
        if type(n) == int:
            books = {book: book.get_price() for book in self.books.keys()}
            books_sorted = [k for k in sorted(books, key=books.get, reverse=True)]
            return books_sorted[:n]
        else:
            print("The argument n = {n} is not of type int. Please pass an int.".format(n=n))

    def get_worth_of_user(self, user_email):
        
        if user_email.find("@") == -1 or (user_email.find(".com") == -1 and user_email.find(".edu") == -1 and user_email.find(".org") == -1):
            print("The {email} is invalid, please ensure it has an @ and a .com, .edu, or .org domain.".format(email=user_email))
        else:
            user = self.users.get(user_email)
            if not user:
                print("User does not currently exist with email {email}. Please use an email for a valid user.".format(email=user_email))
            else:
                price = 0
                for book in user.books.keys():
                    price += book.get_price()
                return price