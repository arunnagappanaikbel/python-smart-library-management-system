# python-smart-library-management-system : This python prjects helps to mastering python core skills and in this project admin can add, delete th ebooks from library and member cas borrow and return the book which will update the database with current book count.


✅ Features Overview:
🧑‍💼 Admin Functions
Add a new book

Update existing book details

Delete a book

Search books by ID/title/author

👤 Member Functions
Borrow a book (decreases book count)

Return a book (increases book count)

Check borrowed books

⚙️ System Features
Use of:

Lists: Store available books

Dictionaries: Book/member records

Tuples: For immutable book info

Sets: Track unique borrowed book IDs

Logging:

Log every operation (borrow, return, errors) in logs.txt

Error Handling:

File not found, invalid input, unavailable book, etc.

File Handling:

Books: CSV

Members: JSON

Logs: Text

Config Management:

Load settings from settings.json

smart_library/
│
├── config/
│   └── settings.json             # Configuration settings
│
├── data/
│   ├── books.csv                 # Book records
│   ├── members.json             # Member records
│   └── logs.txt                 # Logs of borrow/return/errors
│
├── core/
│   ├── admin.py                 # Admin functionalities
│   ├── member.py                # Member functionalities
│   ├── models.py                # OOP models (Book, Member, Library)
│   └── utils.py                 # Utility functions (file read/write, validation)
│
├── main.py                      # Entry point of the system
├── requirements.txt             # List of required packages
└── README.md
