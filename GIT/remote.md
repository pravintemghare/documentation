git remote add origin https://URL -- add remote repository to local repository
git remote -v - to list all remote repository

-----
from local to remote is called push
git push origin branchname

-----
clone remote repository
git clone https://gitrepo.url / ssh link


-----
from remote to local
git fetch - only fetches the changes in remote repo. Then git merge to incorporate the changes to
git pull - fetches & merges the change in local repository

-----
Merge conflicts
this occurs when 2 developers work on the same file in git repository and 1 has already commited the changes to git repository.
the other will have to incorporate the changes and merge code then push it to remote repository.

-----
fork
it is to create your own copy of the git repository. 
you can fork a repository make the changes and create pull request to main git repository.