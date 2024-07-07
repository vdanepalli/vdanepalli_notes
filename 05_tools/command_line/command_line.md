
## Theory

- Command history -- use up and down arrows 
- tab -- for autocompletion


## Commands

- echo -- prints whatever 
  - `echo Hello World`
  - `echo Hello > filename.txt` -- writes to file. Creates file if doesn't exist; using one `>` will overwrite existing file
  - `echo Hello World >> filename.txt` -- appends to file.
- say -- text to speech in Mac
  - `say Hello World`
- pwd -- print working directory
- cd -- change directory
  - `cd dir_name`
  - `cd ..` 
  - `cd ../..`
- ls -- lists whats in current working directory
- cat -- print content of a file
  - `cat file1.txt > file2.txt` -- overwrites file2.txt with file1.txt content.
- clear -- clears terminal. can still see commands by scrolling up
- mkdir -- creates a new directory
- touch -- creates files 
  - `touch filename.txt`
- mv -- move/rename files/directories
  - `mv old_dir_name new_dir_name`
- rm -- remove file
  - `rm file1.txt file2.txt`
  - `rm -r dir_name` -- dir_name need not be empty; r for recursive
- rmdir -- remove directory; dir needs to be empty
- cp -- copy 
  - `cp file1.txt file2.txt`
  - `cp -r dir1/ dir2/`
