# Degrees of Separation

This Python program determines the "degrees of separation" between two actors by finding the shortest path of movies connecting them. It utilizes data from IMDb's database to establish relationships between actors based on shared movie appearances.

## Usage

To run the program, execute the following command:

```
$ python degrees.py <dataset>
```

Where `<dataset>` is either `small` or `large` depending on the dataset size you want to use.

## Example

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

## Background

The concept of "degrees of separation" originates from the Six Degrees of Kevin Bacon game, where individuals in the film industry are connected to Kevin Bacon within six steps, each step being a shared movie appearance.

This program extends this idea to find the shortest path between any two actors through shared movies. It utilizes breadth-first search to navigate through the network of actors and movies.

## Understanding

### Data Structure

The program utilizes three CSV files:
1. `people.csv`: Contains information about actors including unique IDs, names, and birth years.
2. `movies.csv`: Contains details about movies such as unique IDs, titles, and release years.
3. `stars.csv`: Establishes relationships between actors and movies through their respective IDs.

### Implementation

- `names` dictionary: Maps actor names to corresponding IDs.
- `people` dictionary: Maps actor IDs to their details including name, birth year, and movies starred in.
- `movies` dictionary: Maps movie IDs to details such as title, release year, and actors starred in the movie.

The `load_data` function loads data from CSV files into these data structures.

The `shortest_path` function, which is to be implemented, finds the shortest path between two actors based on shared movies.

## Specification

- Implement the `shortest_path` function to return the shortest path from the source actor to the target actor.
- Return a list of `(movie_id, person_id)` pairs representing the path.
- If there's no path between two actors, return `None`.
- You can use the `neighbors_for_person` function to get all actors who starred in a movie with a given actor.

## Further Instructions

You are expected to complete the implementation of the `shortest_path` function according to the provided specifications. You can write additional functions or import other Python standard library modules if needed, but refrain from modifying other parts of the codebase.