'''

LAB:
1. Set up the necessary collections to store the information for the library system.
 
Books: Will store details about books in the library, including the title, genre, publication
Authors: Will store information about authors, such as name, birthdate, and nationality.
Users: Will store information about library users, including their name, email, and borrow history.
  
2. Set up three collections: books, authors, and users.

Define the structure (fields and data types) for each collection. For example, books might have a title, author, and published_year, while users will have a name, email, and borrowed books.
 
3. And try Insert at least five records into each collection. You can also practice reading and updating book information, and then deleting some records from the database.

4. You can also try out filtering and sorting on the books and users collection. e.g., find books by a certain author published after the year 2000.


'''



from pymongo import MongoClient 

# 1. set-up the library db and collections: books, authors and users
client = MongoClient('mongodb://localhost:27017')
db = client['library']

books = db['books']
book1 = {
    "title" : "A Thousand Splendid Suns",
    "genre" : "fiction",
    "year" : 2007
}

insert_book1 = books.insert_one(book1)
print(f"The id of the first book inserted to the books collection is: {insert_book1.inserted_id}")

authors = db['authors']
author1 = {
    "name" : "Khaled Hosseini",
    "dob" : "04-03-1965",
    "nationality" : "Afghan-American"
}

insert_author1 = authors.insert_one(author1)
print(f"The id of the first author inserted to the authors collection is: {insert_author1.inserted_id}")

users = db['users']
user1 = {
    "name" : "Noam Cohen",
    "email" : "noam.cohen@gmail.com",
    "history" : [book1]
}

insert_user1 = users.insert_one(user1)
print(f"The id of the first author inserted to the users collection is: {insert_user1.inserted_id}")

# insert multiple records at once:

book2 = {"title" : "The God Delusion", "genre" : "non fiction", "year" : 2006}
book3 = {"title" : "The Family Carnovsky", "genre" : "fiction", "year" : 1943}
book4 = {"title" : "Siddhartha", "genre" : "fiction", "year" : 1922}
book5 = {"title" : "Dubliners", "genre" : "short story", "year" : 1914}
books.insert_many([book2, book3, book4, book5])

author2 = {"name" : "Richard Dawkins", "dob" : "26-03-1941", "nationality" : "British"}
author3 = {"name" : "Israel Joshua Singer", "dob" : "30-11-1893", "nationality" : "Polish-American"}
author4 = {"name" : "Hermann Hesse", "dob" : "09-08-1877", "nationality" : "German"}
author5 = {"name" : "James Joyce", "dob" : "02-02-1882", "nationality" : "Irish"}
authors.insert_many([author2, author3, author4, author5])

user2 = {"name" : "Eli Cohen", "email" : "eli.cohen@gmail.com", "history" : [book1, book2]}
user3 = {"name" : "Elisa Andersson", "email" : "elisa.andersson@gmail.com", "history" : [book2, book3]}
user4 = {"name" : "Sandra Gaetano", "email" : "sandragaetano1@gmail.com", "history" : [book1, book2, book4]}
user5 = {"name" : "Dan Arieli", "email" : "therealdanarieli@gmail.com", "history" : [book3, book4, book5]}
users.insert_many([user2, user3, user4, user5])

# Find, filter and read documents:
all_books = books.find()
print("Here are all the books in the collection books:")
for book in all_books:
    print(book)

print("\n\n")
book2006 = books.find({"year": 2006})
print("The books published in 2006 in the collection books is:")
b = {}
for book in book2006:
    b = book
    print(book["title"])

print("\n\n")
# Update a document:
query = {"year": 2006}
new_name = {"$set": {"title" : b["title"].lower()}}
books.update_one(query, new_name)
book2006_updated = books.find({"year": 2006})
print("After updating the 2006 book's name:")
for book in book2006_updated:
    print(book["title"])

all_books = books.find()
print("Here are all the books in the collection books after updating the 2006 book:")
for book in all_books:
    print(book)
print("\n\n")

# look into users before deleting book2:
all_users = users.find()
print("Here are all the users in the collection users before deleting the 2006 book:")
for user in all_users:
    print(user)
# users 2,3 and 4 have book2 in their history.
print("\n\n")

# Delete a document, in particular book2:
books.delete_one({"year" : 2006})
all_books = books.find()
print("Here are all the books in the collection books after deleting the 2006 book:")
for book in all_books:
    print(book)
print("\n\n")
# look into user after deleting book2:
all_users = users.find()
print("Here are all the users in the collection users after deleting the 2006 book:")
for user in all_users:
    print(user)
print("\n\n")
# DID NOT DELETE THE BOOK FROM USERS, NOR DID IT UPDATE ITS NAME.

# sort books by title:
print("Here are all the books left in the collection books sorted by title:")
books_sorted_by_title = books.find().sort("title")
for book in books_sorted_by_title:
    print(book)
print("\n\n")

# query books published after 1950:
print("Here are all the books left in the collection books published after 1950:")
myquery = { "year": { "$gt": 1950 } }
books_filtered_by_year = books.find(myquery)
for book in books_filtered_by_year:
    print(book)
