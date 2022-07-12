# Assignment 04
## Requirements

- The program must provide a menu-driven console user interface.
- Use classes to represent the following:
    - The domain entity (`complex`,  `expense`,  `student`, `book`)
    - A services class that implements the required functionalities
    - The ui class which implements the user interface
- Have 10 programmatically generated entries in the application at start-up.
- Unit tests and specifications for non-UI functions related to the first functionality.

## Problem Statement

### Books
Manage a list of books. Each book has an `isbn` (string, unique), an `author` and a `title` (strings). Provide the following features:
1. Add a book. Book data is read from the console.
2. Display the list of books.
3. Filter the list so that book titles starting with a given word are deleted from the list.
4. Undo the last operation that modified program data. This step can be repeated.
