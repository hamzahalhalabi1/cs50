# Knights and Knaves Puzzle Solver

## Background
In 1978, Raymond Smullyan introduced "Knights and Knaves" puzzles, where characters called knights always tell the truth and knaves always lie. These puzzles involve determining the identities of characters based on their statements. This README guides you through solving these puzzles using propositional logic and a model-checking algorithm.

## Getting Started
1. Download the distribution code from the provided link.
2. Unzip the downloaded file.

## Understanding
- **logic.py**: Defines classes for logical connectives. These classes can be composed to represent logical sentences.
- **puzzle.py**: Contains propositional symbols for characters and empty knowledge bases. Your task is to fill these knowledge bases to solve the puzzles.

## Specification
Your task is to complete the knowledge bases for four puzzles: 0, 1, 2, and 3. Each puzzle involves determining the identities of characters based on their statements.

### Puzzle 0
- Single character A.
- A says "I am both a knight and a knave."

### Puzzle 1
- Characters A and B.
- A says "We are both knaves."
- B says nothing.

### Puzzle 2
- Characters A and B.
- A says "We are the same kind."
- B says "We are of different kinds."

### Puzzle 3
- Characters A, B, and C.
- A says either "I am a knight." or "I am a knave."
- B says "A said 'I am a knave.'"
- B then says "C is a knave."
- C says "A is a knight."

## Usage
1. Complete the knowledge bases in puzzle.py for each puzzle.
2. Run `python puzzle.py` to see the solution for each puzzle.

## Note
- Ensure your knowledge bases accurately represent the logical implications of the characters' statements.
- Model checking recursively considers all possible models to determine the solution.
- Each character is either a knight or a knave, and their statements follow accordingly.

Now, let's dive into solving these intriguing puzzles!