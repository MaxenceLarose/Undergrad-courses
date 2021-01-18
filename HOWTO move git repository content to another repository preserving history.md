# [Moving Git repository content to another repository preserving history](https://stackoverflow.com/questions/17371150/moving-git-repository-content-to-another-repository-preserving-history)

Move only the contents of one repository (`repo1`) to another existing repository (`repo2`) using the following commands :

```
cd repo2
git checkout main
git remote add r1remote **url-of-repo1**
git fetch r1remote
git merge r1remote/main --allow-unrelated-histories
git remote rm r1remote
```

After that `repo2/main` will contain everything from `repo2/main` and `repo1/main`, and will also have the history of both of them.

**IMPORTANT** : Move everything inside `repo1` into a subfolder (inside `repo1`) before you do the merge.