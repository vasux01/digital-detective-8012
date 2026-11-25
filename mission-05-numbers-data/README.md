# Mission 05 — Number Systems, Python and Text Encoding

## 1. Task / objective

The objective of this mission was to understand decimal, binary and hexadecimal number systems, verify conversions using Python, build a number converter and learn about ASCII and UTF-8 encoding.

## 2. Work completed

### Task 5.1 — Number system conversions

| Conversion | Answer |
|---|---:|
| 13 (decimal) to binary | 1101 |
| 25 (decimal) to binary | 11001 |
| 1010 (binary) to decimal | 10 |
| 1101 (binary) to decimal | 13 |
| A (hexadecimal) to decimal | 10 |
| 1F (hexadecimal) to decimal | 31 |
| 1111 (binary) to hexadecimal | F |

### Task 5.2 — Python verification

Python's built-in functions can verify number conversions:

- `bin(13)` gives `0b1101`.
- `bin(25)` gives `0b11001`.
- `int("1010", 2)` gives `10`.
- `int("1101", 2)` gives `13`.
- `int("A", 16)` gives `10`.
- `int("1F", 16)` gives `31`.
- `hex(15)` gives `0xf`, which corresponds to hexadecimal F.

### Task 5.3 — Number converter program

Created `number_converter.py`, which accepts a positive decimal whole number and displays its binary and hexadecimal representations.

The program uses:
- `input()` to accept user input.
- `int()` to convert the input into an integer.
- `bin()` to calculate the binary representation.
- `hex()` to calculate the hexadecimal representation.
- `try` and `except` to handle invalid input.

**Test results:**

| Decimal input | Binary output | Hexadecimal output |
|---:|---:|---:|
| 13 | 1101 | D |
| 25 | 11001 | 19 |
| 31 | 11111 | 1F |

All three test values produced the expected results.

### Task 5.4 — ASCII and UTF-8

ASCII assigns numerical values to characters.

- Capital letter A has ASCII value 65.
- Small letter a has ASCII value 97.

UTF-8 is a character encoding system that represents text using one to four bytes per character. It supports characters from many languages and is widely used on the internet.

## 3. Commands / tools used

| Command / function | Purpose |
|---|---|
| `python3` | Runs the Python converter |
| `input()` | Accepts user input |
| `int()` | Converts input into an integer |
| `bin()` | Converts an integer to binary |
| `hex()` | Converts an integer to hexadecimal |
| `int(value, 2)` | Converts binary to decimal |
| `int(value, 16)` | Converts hexadecimal to decimal |
| `try` / `except` | Handles invalid input |

## 4. My understanding

Decimal uses digits from 0 to 9, binary uses only 0 and 1, and hexadecimal uses digits 0 to 9 and letters A to F. Python provides built-in functions that make number conversion easier. I also learned that computers represent text using character encoding systems such as ASCII and UTF-8.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

- `mission-05-numbers-data/number_converter.py` — Working Python converter.
- `mission-05-numbers-data/README.md` — Mission documentation.
- Three successful converter tests using inputs 13, 25 and 31.

## 8. Commit details

- Commit message: `Build number converter and practise data representation`
- Push status: Pending GitHub verification.