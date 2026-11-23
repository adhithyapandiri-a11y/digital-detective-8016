# Mission 6 - Git and GitHub

## 1. Task / objective

Check the Git history, make a branch and learn how a pull request works.

## 2. Work completed

`git status` showed local changes and an empty staging area. `git log` showed the existing commits for Missions 0, 1 and 2.

I made `update-about` locally. It points to `214ca11`, the same commit as `main`. I wrote [My Learning](../README.md#my-learning) in the root README. That change is still in the working folder.

Draft PR from `update-about` to `main`: Add My Learning to the README. It covers what I learned about IPOS, number bases and DNS.

If the instructor asks for a merge, I can pull the result into the local `main` branch afterward.

| Command | Use |
| --- | --- |
| `git init` | Set up a repo. |
| `git status` | See what changed and what is staged. |
| `git add README.md` | Pick the current README for the next commit. |
| `git commit -m "Add learning notes"` | Save the staged changes in history. |
| `git log --oneline` | See the commit history. |
| `git branch update-about` | Make a branch. |
| `git branch --list` | List branches. |
| `git switch update-about` | Change to that branch. |
| `git push` | Send commits to GitHub. |
| `git fetch` | Download updates from the remote. |
| `git pull` | Download updates and bring them into my branch. |

## 3. Commands / tools used

`git status`, `git diff` and `git log` checked the work and history. `git branch update-about` made the branch and `git branch --list` showed it.

## 4. My understanding

Staging picks changes. A commit saves them. A branch is a separate line of work. A pull request shows the changes so people can review them before a merge.

## 5. Difficulties faced

Both branches point to the same commit, so there is no change to show in a pull request yet.

## 6. How I resolved them

I checked the branch tips and saved the PR text above for later.

## 7. Evidence / files

[My Learning in the root README](../README.md#my-learning).

## 8. Commit details

Local branch created. Staging, commit, push and pull request pending.
