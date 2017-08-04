working directory , staging area , 
git init
git status
git add file_name  <file_name2> //to start tracking a file and also to add changes to the file
git diff file_name // tells diff between traked version and file file_name
git commit =m "message often in present tense"
git log  // sha is unique code
    enter q to exit from git log mode
Git is the industry-standard version control system for web developers
git show HEAD /// shows the latest commit /head commit
git checkout HEAD filename //discards changes in working directory
git reset HEAD filename // unstages file changes in staging area
git reset first_7_charec_of_SHA

branching
git branch // shows the current branch
git branch branch_name //create new branch
git checkout branch_name // change to another branch
git merge branch_name //to merge this branch with parent // go to parent and then press this command
git branch -d branch_name // delete branch
remote :- shared git repository
git clone remote_loc_in_ip_or_add clone_name // clone resource located at that location , (called origin)  to your system? 
we need to cd into our clone_name 
git remote -v // get list of git projects remotes

