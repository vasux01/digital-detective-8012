# Mission 03 — Understand the Operating System

## 1. Task / objective

Explore the operating system, running processes, storage, file paths and permissions, and understand the main responsibilities of an operating system.

## 2. Work completed

### Task 3.1 — Explore the operating system

| Information explored | What it tells you | Observation |
|---|---|---|
| Operating system | Identifies the OS running on the computer | macOS 27.2.1 |
| Current account | Identifies the active local account | [redacted for privacy] |
| Available storage | Shows total, used and available disk space | 926 GiB total, 13 GiB used, 779 GiB available |
| System activity | Shows currently running processes | Observed processes such as launchd, logd and configd |

### Task 3.2 — Understand processes

- **What is a process?** A process is a program or service that is currently running on a computer.
- **What does PID represent?** PID means Process Identifier. It is a unique number assigned to each running process.
- **Two examples of processes:** A web browser and a background system process such as launchd.

### Task 3.3 — Understand paths and permissions

An absolute path gives the complete location of a file starting from the root directory. A relative path gives the location in relation to the current directory.

- Relative path example: `terminal-practice/practice.txt`
- Redacted absolute path example: `/Users/[redacted]/digital-detective-8012/terminal-practice/practice.txt`

File permission observation:

| Permission | Meaning | Observation |
|---|---|---|
| r — Read | Allows reading file contents | Owner can read |
| w — Write | Allows changing file contents | Owner can write |
| x — Execute | Allows running a file | Owner cannot execute |

The observed permission string was `-rw-r--r--`. The owner has read and write permissions, while the group and others have read-only permissions.

### Task 3.4 — Operating-system responsibilities

| OS responsibility | Explanation | Example |
|---|---|---|
| Process management | Manages running programs and allocates CPU time | Running a browser and a text editor |
| Memory management | Allocates and manages RAM for programs | Giving memory to an open application |
| Device management | Controls hardware devices and their communication | Managing a keyboard or printer |
| File management | Organises files and folders on storage | Saving and opening documents |
| User interface / shell | Allows users to interact with the computer | macOS desktop and Terminal |
| Security and permissions | Controls access to files and system resources | Restricting who can edit a file |

## 3. Commands / tools used

| Command | Purpose |
|---|---|
| `sw_vers` | Displays macOS version information |
| `whoami` | Displays the current account name |
| `df -h /` | Displays storage information |
| `ps -axo pid,comm` | Displays running processes and their PIDs |
| `head -n 12` | Displays the first 12 lines |
| `pwd` | Displays the current working directory |
| `ls -l` | Displays detailed file information, including permissions |

## 4. My understanding

An operating system acts as a link between computer hardware, software and the user. It manages processes, memory, storage, devices and security. Processes are active programs or services, and each process has a PID. File permissions control who can read, write or execute a file. Absolute paths give the complete file location, while relative paths depend on the current directory.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

- `mission-03-operating-system/README.md`
- Terminal observations recorded in this README.
- File permission observation from `terminal-practice/practice.txt`.

## 8. Commit details

- Commit message: `Document operating system and file management`
- Push status: Pending GitHub verification.