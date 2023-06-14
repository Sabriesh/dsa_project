class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author

class ListNode:
    def __init__(self, book):
        self.book = book
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, book):
        new_node = ListNode(book)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_node(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

class BinarySearchTree:
    class Node:
        def __init__(self, book):
            self.book = book
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, book):
        new_node = BinarySearchTree.Node(book)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if book.isbn < current.book.isbn:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def search(self, isbn):
        current = self.root
        while current is not None:
            if isbn == current.book.isbn:
                return current.book
            elif isbn < current.book.isbn:
                current = current.left
            else:
                current = current.right
        return None

class Library:
    def __init__(self):
        self.capacity = 10  # Hash table capacity
        self.hash_table = [None] * self.capacity
        self.bst = BinarySearchTree()

    def _hash_function(self, isbn):
        return hash(isbn) % self.capacity

    def add_book(self, book):
        hash_value = self._hash_function(book.isbn)
        if self.hash_table[hash_value] is None:
            linked_list = DoublyLinkedList()
            linked_list.add_node(book)
            self.hash_table[hash_value] = linked_list
        else:
            self.hash_table[hash_value].add_node(book)
        self.bst.insert(book)

    def find_book(self, isbn):
        return self.bst.search(isbn)

    def remove_book(self, isbn):
        hash_value = self._hash_function(isbn)
        linked_list = self.hash_table[hash_value]
        if linked_list is not None:
            current = linked_list.head
            while current is not None:
                if current.book.isbn == isbn:
                    linked_list.remove_node(current)
                    break
                current = current.next
        self.bst.remove(isbn)

    def display_books(self):
        for i in range(self.capacity):
            linked_list = self.hash_table[i]
            if linked_list is not None:
                current = linked_list.head
                while current is not None:
                    print(f"ISBN: {current.book.isbn}, Title: {current.book.title}, Author: {current.book.author}")
                    current = current.next

    def count_books(self):
        count = 0
        for i in range(self.capacity):
            linked_list = self.hash_table[i]
            if linked_list is not None:
                current = linked_list.head
                while current is not None:
                    count += 1
                    current = current.next
        return count

    def get_books_by_author(self, author):
        books = []
        for i in range(self.capacity):
            linked_list = self.hash_table[i]
            if linked_list is not None:
                current = linked_list.head
                while current is not None:
                    if current.book.author == author:
                        books.append(current.book)
                    current = current.next
        return books

def main():
    library = Library()
    
    
    book1 = Book("97801348", "Singly linked list", "Tom")
    book2 = Book("97814493", "Binary Search Trees", "Tony")
    book3 = Book("97815932", "Doubly linked List", "Bruce")
    book4 = Book("97801351", "Hash Table", "Dhoni")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    
    
    while True:
        print("1. Add a book")
        print("2. Find a book by ISBN")
        print("3. Remove a book")
        print("4. Display all books")
        print("5. Count the number of books")
        print("6. Get books by author")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            isbn = input("Enter the ISBN: ")
            if(isbn<0):
                print("ISBN number you have entered is wrong")
                break
            title = input("Enter the title: ")
            author = input("Enter the author: ")
            book = Book(isbn, title, author)
            library.add_book(book)
            print("Book added to the library.")

        elif choice == "2":
            isbn = input("Enter the ISBN to find: ")
            if(isbn<0):
                print("ISBN number you have entered is wrong")
                break
            book = library.find_book(isbn)
            if book is not None:
                print(f"Book with ISBN {isbn} found:")
                print(f"Title: {book.title}, Author: {book.author}")
            else:
                print(f"Book with ISBN {isbn} not found.")

        elif choice == "3":
            isbn = input("Enter the ISBN to remove: ")
            if(isbn<0):
                print("ISBN number you have entered is wrong")
                break
            library.remove_book(isbn)
            print(f"Book with ISBN {isbn} removed.")

        elif choice == "4":
            print("All Books in the Library:")
            library.display_books()

        elif choice == "5":
            count = library.count_books()
            print(f"Number of Books in the Library: {count}")

        elif choice == "6":
            author = input("Enter the author: ")
            books_by_author = library.get_books_by_author(author)
            print(f"Books by {author}:")
            for book in books_by_author:
                print(f"ISBN: {book.isbn}, Title: {book.title}")

        elif choice == "7":
            break

        else:
            print("Invalid choice. Please try again.")

        print()    
if __name__ == "__main__":
    main()
