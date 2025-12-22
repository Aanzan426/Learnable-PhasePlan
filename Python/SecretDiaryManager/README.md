# The Secret Diary Manager

## Problem Statement:
You are tasked with building a Diary Manager in Python that handles a text file called diary.txt.
The program must demonstrate all core file handling operations:

## Requirements:
    File Creation & Writing:
        If diary.txt doesn’t exist, create it using "w+" mode.
        Write an initial entry: "Day 1: Started my secret diary."

    Appending:
        Add new entries at the end using "a" mode.
        Example: "Day 2: Learned about file handling in Python."

    Reading:
        Display the entire diary content using "r" mode.
        Display only the first line using readline().
        Display all lines as a list using readlines().

    Pointer Control:
        Use tell() to show the current pointer position before and after reading.
        Use seek(0) to reset the pointer and re‑read the file.

    Editing (Prepending):
        Using "r+", prepend a line at the beginning:
        "*** Confidential Diary ***"

    Searching:
        Ask the user for a keyword (e.g., "Python").
        Search the diary for occurrences using:
            > in operator (existence check)
            > .find() (position of first occurrence)
            > .count() (frequency)
        Print the line numbers where the keyword appears (using enumerate).

    Closing:
        Ensure the file is properly closed after each operation.
        Demonstrate both manual f.close() and automatic with open(...).

## Deliverables
    - `diary_manager.py` (main script).
    - `diary.txt` (sample file).
