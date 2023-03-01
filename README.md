# Character Picture Grid

This is my solution the practice project "Character Picture Grid" at the end of chapter 4 in [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/2e/chapter4/) by Al Sweigart. It prints out the transposed version of the `grid` list of lists, where the rows become columns and columns become rows.

```Python
grid = [['.', '.', '.', '.', '.', '.'],
		['.', 'O', 'O', '.', '.', '.'],
		['O', 'O', 'O', 'O', '.', '.'],
		['O', 'O', 'O', 'O', 'O', '.'],
		['.', 'O', 'O', 'O', 'O', 'O'],
		['O', 'O', 'O', 'O', 'O', '.'],
		['O', 'O', 'O', 'O', '.', '.'],
		['.', 'O', 'O', '.', '.', '.'],
		['.', '.', '.', '.', '.', '.']]
```

The output will be:

```Python
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
```

## Explanation

* The outer loop iterates over the indices 0 to 5 (inclusive) in `range(6)`, which corresponds to the six columns of the original `grid`.
* The inner loop iterates over the indices 0 to 8 (inclusive) in `range(9)`, which corresponds to the nine rows of the original `grid`.
* `grid[y][x]` indexes into the `grid` list with the `y` index representing the row and the `x` index representing the column. However, in the print statement, the order of the indices is swapped because we want to transpose the grid.
* `end=''` is used in the print statement to suppress the default newline character that is added after each print statement.
* Finally, `print()` is called after the inner loop to add a newline character to separate the rows in the output.