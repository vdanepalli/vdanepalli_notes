# Git 

- 2005 Linus Torvalds created version control system, git 
- Github -- say google drive for code 
- brew install git
- Homebrew -- package manager
- 2008 Tom Preston-Werner, Chris Wanstrath, PJ Hyett - created Github, now run by Microsoft
- Git - tool - tracks changes; Github - web platform hosts Git repositories
- working directory - where your project lives 
- staging area - temporary area ready to go online
- commits help us separate different actions in code 
- commit message should explain what we are doing to the code so others can know what was worked on at a glance. 30 words or less
- fork -- copying a repo to your github account. useful when you have only read access but want to experiment; copies of code made outside repo
- BASH : The Bourne Again Shell
- branch - copy of code made inside repo
- Access Types
  - Read
  - Write
  - Admin
  - Maintainer (Org) -- similar to Admin but specific to a repo
  - Contributor  
- Merge conflicts -- happen when changes are made to same part of file; or when one branch deletes while another updates same file; Git doesn't know what to do 
  - Accept Incoming Changes
  - Accept Current Changes
  - Accept Both Changes
- Pull Request (PR) -- suggests changes to a repository; Eventually turns into a merge after code review and approval 
- PR Checklist 
  - pull the latest changes
  - now, test your code/changes again
  - review your code/changes
  - fix merge conflicts if any
----

## Commands

```python
# Set user name
git config --global user.name "John Doe"

# Set user email
git config --global user.email "john.doe@example.com"

# Set default editor to Visual Studio Code
git config --global core.editor "code --wait"

# Enable colored output
git config --global color.ui auto

# Set default branch name
git config --global init.defaultBranch main
```

- `git init` 
- `git config`
  - `git config --global user.name "firstname lastname"`
  - `git config --global user.email "email@domain.com"`
- `git remote add origin https://github.com/username/reponame.git`
- `git branch -M main` 
- `git add` 
    - `git add filename`
    - `git add .`
    - `git add *.html`

- `git commit`
    - `git commit -m "Initial commit"`

- `git reset` -- unstage all files, return to previous state 
    - `git reset filename` -- unstage a specific file 

- `git status`   

- `git push` 
    - `git push -u origin main` ---- origin is remote; -u sets upstream; main is remote branch
  
- `git clone` 
  - `git clone url`
  
- `git branch` -- displays branch names with * on current branch
  - `git branch new_branch_name` -- creates a copy of the current branch you are on 
  - `git checkout new_branch_name` -- switches to the new branch
  - `git checkout -b new_branch_name` -- creates and switches to the new branch
- `git merge branch_name` -- merges branch_name's history with current branch we are on 
- `git log` -- show all commits in current branch

<br/>
<br/>

- staging
- snapshots
- commit -- think of photo album
- untracked
- added - to staging area
- modified
- head
- gitlens plugin 
- Github, gitlab, bitbucket
- `which $SHELL`; `.bashrc | .bash_profile`; `.sh or no extension`; `#! -- shebang`
- `echo "something"`
- `$variable name`; `./filename.sh`
- positional arguments will be assigned variable names `$1` `$2` and so on
- codespaces; `.` -- hitting period while on a github repository opens a web editor where you do not have access to terminal. however, you could open a cloud based VM -- or codespace; it is a paid service per second 
- files affected by merge conflicts are red with an exclamation in vscode 
- merge conflicts; -- accept incoming changes | reject incoming changes and keep existing changes | keep both changes -- will be added one after the other; Also, after making changes, you are required to make a merge commit 
- fork -- copy someone's repo to your account; a link to original repo is maintained called UPSTREAM repository; fork --> work --> pull request to merge your code with the upstream repository
- working directory | staging area | commit 
- rebase -- re-writes history; destructive action; should be done when you are working on your own private feature branch; if you have an active public branch where multiple people are working, you don't want to use rebase
- rebase -- keeping feature branch up to date or in sync with master branch without extra merge commits 
- Github actions
- DevOps -- set of practices to build, test, and release your code
- Continuous Integration -- commit your code to a shared repo frequently; helps in identifying issues early; is about merging new code into the codebase
- Continuous Deployment -- is about pushing code out to your customers
- Firebase -- third party host; `workflow/integrate.yml`; `workflow/deploy.yml`; `${{secrets.FIREBASE_TOKEN}}` 
- YAML
- npm -- node package manager
- gpr -- github package registry
- Actions are reusable chunks of code for your own workflows
- Apps are fully-managed integrations
- crontab guru
- git hooks


<br/>
<br/>

- `brew install git`
- `git --version`
- `git config --list`
- `:q` to quit
- `git config --global user.name ""`
- `git config --global user.email ""`
- `git init`
- `git status`
- `touch .gitignore`
- `git add filename`; `git add .` -- adds everything to staging area
- `git reset` -- removes everything from staging
- `git reset --hard commit_hash` -- rollback to previous commit and discard changes; reset commit and delete any changes that were not committed; do not use reset on a commit thats pushed to github
- `git reset commit_hash` -- reset commit and doesn't delete changes. changes are still in working directory
- `git revert commit_id_or_hash -m "message"` -- makes another commit with the revert changes. so it is still in your git history and can bring back
- `git commit -m "initial commit"`
- `git log` -- commit author date
- `git commit -a -m "commit message"` - add and commit `-am` also works
- `git remote` -- list current remote names; `git remote add <remote rep name> <url>`;
- `git remote add origin url` 
- `git remote -v` -- lists url along with names
- `git remote show origin` -- shows other details -- fetch url, push url, head branch, remote branch, local branch, local ref configured for git push
- `git push origin master_or_local_branch_name -u` -- set origin to upstream remote -- allows us to use git pull without additional details
- `git fetch` -- fetch latest changes -- downloads latest changes; doesn't update code yet
- `git merge origin/master` -- merge remote master branch to the current active branch. Fast-Forward -- simplest merge strategy when commits are disconnected together;
- `git pull` -- combines fetch and merge; will fail if you have uncommitted changes; then you either have to commit and pull | stash and pull; you might encounter merge conflicts if you modify same files or same line of code
- `git full origin master`
- `git clone <remote-url> <optional-dir-name>`
- `git branch` -- lists all branches; `git branch -M main` -- renames current branch name
- `git branch branch_name`; doesn't move to created branch
- `git branch -d branch_name`; `-d` -- safe; delete if it hasn't been already merged to master branch or if it has no changes; `-D` -- deletes no matter what
- `git checkout branch_to_move_to`
- `git checkout -b new_branch_name` -- create and move to branch
- `git checkout -` -- move to previous branch you were on
- `git diff` -- difference between two commits; 
- `git merge --abort` -- take you back to the state before merge was started
- `git remote add upstream upstream_url`
- `git fetch upstream`
- `git rebase upstream/master`
- `git commit --ammend -m "better commit message` -- modifies last commit
- `git commit --ammend --no-edit` -- ammends previous commit but keeps the same commit message; ammend will only work if the code isn't already pushed to the remote repo
- `git push origin master --force` overwrite remote commit with state of lcoal code; if there are commits on remote that you don't have locally, you will lose them forever
- `git log --graph --oneline --decorate`
- `git commit --fixup hash` -- tell git in advance that you want to fixup
- `git commit --squash hash` -- tell git in advance that you want to squash
- `git rebase -i --autosquash`
- `git bisect` -- binary search to find the bad commit 
- `git stash` -- save everything in current working directory to stash; temporary area per say
- `git stash pop` -- bring back changes to working directory from stash
- `git stash save give_some_name_you_can_remember`
- `git stash list`
- `git stash apply index-number-of-the-stash-you-want-to-apply`
- `git checkout feature` while on branch `feature` ; `git rebase master` -- takes feature and puts it at the tip of the master branch -- as if you just started working on your feature branch
- `git rebase master --interactive` -- will open a file where you can choose which commits to keep `pick` or which commits to `squash` -- group/flatten commits to one or `fixup` -- same as squash except it omits the commit messagee
- `firebase init` -- hosting locally setup
- `firebase deploy --only hosting` -- deploy locally 
- `firebase login:ci` -- api key or token for authentication; in github settings, add new secret with name FIREBASE_TOKEN 
- `git config --global alias.aliasname "commit -am`; so next time you just type git aliasname "commit_message" to add and commit
- `git fetch origin` -> `git reset --hard orgin/master` -- reset changes to remote state; will lose any changes in local
- `git clean -df` -- removes any untracked files or left-overs after above command


<br/>
<br/>

- ```yaml
  name: Node Continuous Integration

  on:
    pull_request:
      branches: [ master ]


  jobs:
    test_pull_request:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v2
        - uses: actions/setup-node@v1
          with:
            node-version: 12
        - run: npm ci
        - run: npm test
        - run: npm run build
  ```

- ```yaml
  name: CI

  on:
    push:
      branches:
      - master
      - release/*

  jobs:
    firebase-deploy:

      runs-on: ubuntu-latest

      steps:
      - uses: actions/checkout@master
      - uses: actions/setup-node@master
        with:
          node-version: '10.x'
      - run: npm install
      - run: npm run build:prod
      - uses: w9jds/firebase-action@master
        with:
          args: deploy --only hosting
        env:
          FIREBASE_TOKEN: ${{ secrets.FIREBASE_TOKEN }}
  ```

- ```yaml
  name: Sveltefire Package

  on:
    release:
      types: [created]

  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v2
        - uses: actions/setup-node@v1
          with:
            node-version: 12
        - run: npm ci
        - run: npm test

    publish-npm:
      needs: build
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v2
        - uses: actions/setup-node@v1
          with:
            node-version: 12
            registry-url: https://registry.npmjs.org/
        - run: npm ci
        - run: npm build
        - run: npm publish
          env:
            NODE_AUTH_TOKEN: ${{secrets.npm_token}}


      publish-gpr:
          needs: build
          runs-on: ubuntu-latest
          steps:
          - uses: actions/checkout@v2
          - uses: actions/setup-node@v1
              with:
              node-version: 12
              registry-url: https://npm.pkg.github.com/
              scope: '@your-github-username'
          - run: npm ci
          - run: npm publish
              env:
              NODE_AUTH_TOKEN: ${{secrets.GITHUB_TOKEN}}
  ```

- ```yaml
  name: Slack Issues

  on:
    issues:
      types: [opened]


  jobs:
    post_slack_message:
      runs-on: ubuntu-latest
      steps:
      - uses: actions/checkout@v2
      - uses: rtCamp/action-slack-notify@v2.0.0
      env:
          SLACK_WEBHOOK: ${{ secrets.SLACK_WEBHOOK }}
          SLACK_USERNAME: CyberJeff 
          SLACK_CHANNEL: gh-issues
  ```

- ```yaml
  name: Backup Firestore

  on:
    schedule:
      - cron:  '0 0 * * *'

  env:
    PROJECT_ID: YOUR-PROJECT
    BUCKET: gs://YOUR-BUCKET
  
  jobs:
    backup:
      runs-on: ubuntu-latest
      steps:
      - uses: google-github-actions/setup-gcloud@main
        with:
          service_account_key: ${{ secrets.GCP_SA_KEY }}
          export_default_credentials: true
      - run: gcloud info
      - run: gcloud config set project $PROJECT_ID
      - run: gcloud firestore export $BUCKET
  ```

## Tips 

- Always do a `git pull --rebase` first. 
  - Say personA and personB started working from same state0
  - personA pushed to remote
  - personB tries to push to remote but fails. 
    - He can do `git pull`
      - Automatically creates a new merge commit C
      - commit 0, commit A, commit B, merge commit C
    - He can do `git pull --rebase`
      - Pulls their changes. Then cimmits your changes. Linear 
      - commit 0, commit A, commit B
      - It can fail, if merge conflicts arise. 
        - Do `git rebase --abort`; no side effects
  - `git config --global alias.pr "pull -- rebase"` | `git pr`


# Git 

### Intro 
- Git + Github -> build things together, collaborate, maintain applications
- Best time to learn git is yesterday
- Second best time is now

- Learn, Live, Breath GIT 
- https://www.coltsteele.com/discord
- https://www.youtube.com/channel/UCrqAGUPPMOdo0jfQ6grikZw

- Git basics, commit, branch, merge
- Diff, Stash, Undo changes
- Github, Fetch, Pull, Pages, Gists, Collaborative workflows
- Rebase, Squashing, Drop, Tags, Hashing, Git objects, blobs, trees, Reflogs, Aliases

- Git is VCS Version Control System - track and manage changes to files over time
- Subversion, CVS, Mercurial, Perforce, ClearCase : Other VCSs
- Git is free open source distributed VCS

- Linus Torvalds - Linux, Git
- BitKeeper, Mercurial
- Goddamn Idiotic Truckload of Shit
- Global Information Tracker
- Stupid contemptible despicable simple

- Governments, Scientists, Writers

- Github - service hosting git repositories, online
- Git - local

-  brew install git
- git config --global user.name "Vinay Danepalli" 
- git config --global user.email vdanepalli@gmail.com

- GitKraken -- GUI tool 

- ls
  - ls -a  (hidden files)
- cd 2023
- touch hello.txt omg.txt (updates modified time if file exists otherwise creates new one)
- mkdir dir1 dir2 
- rm (permanent deletion)
  - rm file1 file2
  - rm -rf  (recursive force -- removes directories)
- pwd 
- ~ = home dir
- open . in mac = start . in windows



-----

### Git Basics
- Repository - Git workspace that tracks and manages files within a folder

- `git status` 
- `git log`
  - commit hash, author, date, commit message
- `git init` initialize new one or re-initialize existing one
  - creates `.git` dir
  - `rm -rf .git` deletes all history
- Better not to initialize git repo inside a git repo
  - Better do `git status` first and then `git init`
- `git add` moves files from working directory to staging area and `git commit` moves from here to repository
- `git add file1 file2`
- Commit message should summarize the changes included in the commit
- `git commit -m "message"`

### Git commits in detail
- Atomic commits - keep each commit focused on a single thing
- `git config -- global core.editor "code --wait"` sets default code editor for `git commit`
- `git log --oneline`
- `git log --pretty`
- `git commit --amend`
- `.gitignore` - list of files to ignore
  - foldername/
  - *.txt 
  - gitignore.io -- suggested starting template


# 