#HOMEWORK 4
CFG Nanodegree / Software 3
Isobel Gladman
##TASK 1 (Git and GitHub)

Complete definitions for key Git & GitHub terminology

###GIT WORKFLOW FUNDAMENTALS

**Working Directory**

The place in which you are working and writing your code ahead of staging it for commitment, and commitment itself. The working directory is sort of like a workbench, it's where you work on your files (you edit them, you add new files, you delete files etc.). On the other hand, the . git folder (which is a hidden folder) represents the repository.

**Staging Area**

A sort-of holding bay for code that you have finished working on, where it is ready to be assessed for being committed. Staging area is files that are going to be a part of the next commit, which lets git know what changes in the file are going to occur for the next commit.

**Local Repo (head)**

The cloned repository on your machine in which you make your edits and changes, before staging them for committing back to the main/master remote repo. HEAD is a reference variable used to denote the most current commit of the repository in which you are working. When you add a new commit, HEAD will then become that new commit.

**Remote repo (master)**

The main/master project you and your collaborators are working off. It’s what you pull from and push to. The primary branch of all repositories. All committed and accepted changes should be on the master branch. You can work directly from the master branch, or create other branches.
 
###WORKING DIRECTORY STATES

**Staged**

Waiting to be committed

**Modified**
Has been changed since last time it was committed

**Committed**
Saved/added permanently
 
###GIT COMMANDS
**Git add**

add a file as it looks now to your next commit (stage)

**Git commit**

commit your staged content 

**Git push**

Transmit local branch commits to the remote repository branch

**Git fetch**

fetch down all the branches from that Git remote

**Git merge**

merge a remote branch into your current branch to bring it up to date

**Git pull**

fetch and merge any commits from the tracking remote branch
