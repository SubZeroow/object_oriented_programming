class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Method to display book details
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

    # Method to check if the book is thick or short
    def check_thickness(self):
        if self.pages > 300:
            return "Thick book!"
        else:
            return "Short read!"

# Creating an object of Book class
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 200)
book1.display_info()
print(book1.check_thickness())

# Another object with more pages
book2 = Book("War and Peace", "Leo Tolstoy", 1200)
book2.display_info()
print(book2.check_thickness())
