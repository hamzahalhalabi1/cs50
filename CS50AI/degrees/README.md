# Degrees of Separation Network

This Python program calculates the shortest path between two actors by finding a sequence of movies that connects them. It utilizes a search algorithm, specifically breadth-first search, to accomplish this task. The program is designed to load data from CSV files containing information about people, movies, and their relationships, and then prompt the user to input two actor names. Finally, it displays the shortest path between the two actors.

## Background

The concept of degrees of separation originates from the Six Degrees of Kevin Bacon game, where anyone in the Hollywood film industry can be connected to Kevin Bacon within six steps through shared movie appearances. Similarly, this program seeks to find the shortest path between any two actors by selecting a sequence of movies that link them together.

## Getting Started

1. **Download**: Obtain the distribution code from [here](https://cdn.cs50.net/ai/2023/x/projects/0/degrees.zip) and unzip it.
2. **Understanding**: Familiarize yourself with the CSV data files provided in the `small` and `large` directories. These files contain information about people, movies, and their relationships.

## Implementation

- **degrees.py**: This file contains the main implementation of the program.
  - **Data Structures**: Defines data structures to store information from the CSV files.
  - **Functions**:
    - `load_data`: Loads data from CSV files into the defined data structures.
    - `person_id_for_name`: Retrieves the ID for any person, handling cases where multiple people share the same name.
    - `shortest_path`: Computes the shortest path between two people and returns it as a list of (movie_id, person_id) pairs.
- **Specification**: The `shortest_path` function must be implemented to satisfy the following conditions:
  - Returns the shortest path from the source person to the target person.
  - Each list item in the returned path represents the next (movie_id, person_id) pair in the path.
  - Returns `None` if there is no possible path between two actors.

## Usage

Run the program by executing `python degrees.py <directory>` where `<directory>` is either `small` or `large` to specify the dataset size.

Example usage:
```
$ python degrees.py large
Loading data...
Data loaded.
Name: Emma Watson
Name: Jennifer Lawrence
3 degrees of separation.
1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class
```

## Notes

- The `neighbors_for_person` function can be utilized to obtain all people who starred in a movie with a given person.
- Only modify the `shortest_path` function as per the provided specification.

This program provides an interesting exploration of connections within the film industry, demonstrating the power of search algorithms in finding paths between entities.