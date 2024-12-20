# Create a dictionary to store information about a book:
# The key "title" should have the name of the book.
# The key "author" should have the author's name.
# The key "year_published" should have the year the book was published.
# The key "genre" should have the genre of the book.
# Print the values for the title, author, and year of publication.
# Add a key-value pair for "rating" (a numeric value, e.g., 4.5).
# Modify the "genre" key to update the genre (e.g., change it to "fiction").
# Remove the "rating" key from the dictionary.
# Print the entire dictionary.
book_info = {
    "title" : "Twelve nights",
    "author" : "Shakespeare",
    "year_published" : 1920,
    "genre" : "Romance",
}
book_info["rating"] = 4.5
book_info["genre"] = "fiction"
del book_info["rating"]
print(book_info["title"])
print(book_info["author"])
print(book_info["year_published"])
print(book_info)




