# Mission 02 — Become comfortable with the Terminal

## 1. Task / objective

Practise Terminal commands, manage files and folders, understand flags and pipes, and learn about package managers.

## 2. Work completed

### Task 2.1 — Basic Terminal operations

Practised `pwd`, `ls`, `ls -l`, `cd ..`, `mkdir`, `touch`, `cp`, `mv` and `cat` to navigate folders, create files, copy and rename files, and display contents.

### Task 2.2 — File changes

Created `terminal-practice/practice.txt` and added two lines:

- This is my first line.
- This is my second line.

Confirmed both lines appeared and created a backup named `backup-renamed.txt`.

The `>` operator replaces existing contents, while `>>` appends text. Copying creates another file; moving changes a file's location or name.

### Task 2.3 — Flags and pipes

Used `ls`, `ls -l`, `ls -lah` and `ls -lah | head -n 5`.

The `-l` flag displays detailed information, `-a` includes hidden entries and `-h` displays human-readable sizes. The pipe sends one command's output to another command.

### Task 2.4 — Package managers

Checked Homebrew, which was already installed.

- Version: Homebrew 7.0.11
- `brew list`: Successful
- No software was installed or uninstalled.

A package manager helps install, update and remove software and manage dependencies.

## 3. Commands / tools used

| Command | Purpose |
|---|---|
| `pwd` | Displays current directory |
| `ls` | Lists files and folders |
| `ls -l` | Detailed listing |
| `cd ..` | Moves to parent directory |
| `mkdir` | Creates directories |
| `touch` | Creates empty files |
| `cp` | Copies files |
| `mv` | Moves or renames files |
| `cat` | Displays file contents |
| `echo` | Writes text |
| `>` and `>>` | Replace and append contents |
| `ls -lah` | Detailed listing including hidden files |
| `head -n 5` | Displays first five lines |
| `|` | Connects command output to another command |
| `brew --version` | Checks Homebrew version |
| `brew list` | Lists managed packages |

## 4. My understanding

The Terminal helps users manage files and folders using commands. Flags change how commands behave, while pipes connect commands. Package managers make software installation and maintenance easier.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

- `terminal-practice/practice.txt`
- `terminal-practice/backup-renamed.txt`
- `terminal-practice/original.txt`
- `terminal-practice/renamed-copy.txt`

## 8. Commit details

- Commit message: Complete Terminal and file management mission
- Push verification: Pending GitHub verification.