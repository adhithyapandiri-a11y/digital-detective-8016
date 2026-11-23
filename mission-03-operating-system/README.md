# Mission 3 - Operating system

## 1. Task / objective

Check the OS, processes, storage, paths and file permissions.

## 2. Work completed

| What I checked | What I saw |
| --- | --- |
| OS | macOS 27.2.1 on `arm64`. |
| Current account | The account running the commands was `[redacted]`. |
| Storage | 216 GiB used and 219 GiB available on the data volume. |
| Activity | 811 processes, with 3 running. CPU was about 62% idle. |

A process is a program that is running. The PID is its ID while it runs. After opening VS Code, I saw `Code` with PID 6241 and Chrome with PID 2283.

I moved from the root of the repo to the Terminal practice folder. The absolute path to the note starts at the filesystem root: `/Users/[redacted]/digital-detective-8016/mission-02-terminal/terminal-practice/notes.txt`. From the repo root, the relative path is `mission-02-terminal/terminal-practice/notes.txt`.

The file mode was `-rw-r--r--@`. The owner has `rw-`, so they can read and edit the note. The last dash in that group means there is no execute permission. `x` lets you run a file or enter a directory.

| What the OS manages | What it does | Example |
| --- | --- | --- |
| Processes | Splits up CPU time. | Music plays while a page loads. |
| Memory | Gives apps RAM and takes it back when they close. | Closing Chrome frees memory. |
| Devices | Talks to hardware. | It reads key presses from a keyboard. |
| Files | Organises and saves files. | A note is saved in its folder. |
| User interface | Gives me a way to use the computer. | I can browse files in Finder or Terminal. |
| Security | Checks account permissions. | It blocks a write when the account lacks permission. |

## 3. Commands / tools used

- `sw_vers`, `uname -m` and `id -un` checked the OS, architecture and account.
- `df -h /System/Volumes/Data` checked disk space. `top` and `ps` showed activity and processes.
- `cd` and `pwd` checked the path. `ls -l` showed permissions.

## 4. My understanding

The OS keeps track of running programs and decides which accounts can use or change files.

## 5. Difficulties faced

I had to work out which letters were for the owner.

## 6. How I resolved them

I read the first three permission characters after the file type.

## 7. Evidence / files

The results are above. I used the [practice note](../mission-02-terminal/terminal-practice/notes.txt) for the permission check.

## 8. Commit details

Local. Commit and push pending.
