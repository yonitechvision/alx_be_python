class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    def __del__(self):
        print(f"Deleting {self.title}")
if __name__ == "__main__":
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the str method
    print(my_book)  # Expected to use str

    # Demonstrating the repr method
    print(__repr__(my_book))  # Expected to use repr

    # Deleting a book instance to trigger del
__del__
    del my_book
