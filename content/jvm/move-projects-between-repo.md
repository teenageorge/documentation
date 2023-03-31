title: How to move projects between repositories [using git filter-repo]
date: 2023-03-31
category: git

#### <span style="color:#ff5f0e">Context of the problem: 
Move a couple of sub-projects from one github repository to another non-empty repository. 

The source repository contains a multi-module Gradle project developed in Java. This project is structured as a modular monolith and has been evolving for over half a decade. Some of these modules are now being split into separate micro services and libraries. Some of these modules will reside on its own separate repositories. This document explains how to move multiple modules along with full commit history from source repository to the target repository. The target repository contains some changes already, so it is not empty.

#### <span style="color:#ff5f0e"> Solution:

The solution to move single folder is described step by step in [an article published by Chuck Boyer](https://boyersnet.com/blog/2021/02/11/moving-a-folder-between-two-git-repos/): 

  
To move multple files or folders, add more `--path` to the `git filter-repo` command. 
Everything else is as explained in this article by Chuck Boyer.

To move 3 folders and a file: ~/fresh-clone/source%git filter-repo --path module1 --path module2 --path module3 --path file1 --force

#### Steps to this solution:

`~/fresh-clone%cd source`

copy the git url for the source repository:

`git@github.com:<username>/<repository-name>.git` (if using SSH). For HTTPS, copy the web url.

Clone the source repository

`~/fresh-clone%git clone git@github.com:<username>/<source>.git`

`~/fresh-clone%cd source`

Remove remote just to ensure no mishaps

`~/fresh-clone/source%git remote rm origin`

Filter what you want to keep in the destination repo and remove everything else

`~/fresh-clone/source%git filter-repo --path module1 --path module2 --path module3 --path file1 --force`

Clone the destination repository

`~/fresh-clone/source%cd ..`

`~/fresh-clone/%git clone git@github.com:<username>/<destination>.git`

`~/fresh-clone%cd destination`

Add the source repo as a remote on the destination repo

`~/fresh-clone/destination%git remote add sourceclone ~/fresh-clone/source`

Fetch the source

`~/fresh-clone/destination%git fetch sourceclone`

Create a branch to track the source clone from the remote main branch

`~/fresh-clone/destination%git branch sourceclone remotes/sourceclone/main`

Merge the sourceclone main branch into the main branch of the destination

`~/fresh-clone/destination%git merge sourceclone --allow-unrelated-histories`

Remove the sourceclone remote

`~/fresh-clone/destination%git remote rm sourceclone`

Delete the local sourceclone branch

`~/fresh-clone/destination%git branch -d sourceclone`

Push the changes to the destination main branch

`~/fresh-clone/destination%git push origin main`
