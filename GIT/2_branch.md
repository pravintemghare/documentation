git branch branchname - create branch name
git checkout -b "branchname" - create branch & switch branch
git branch -d branchname - delete branch

-----
Merge steps:
git checkout master
git merge  feature/branch

fast forward merge -- current branch has no extra commits with master
no-fast forward merge -- new merge commit is created 