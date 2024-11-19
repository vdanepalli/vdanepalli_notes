# Docker 

- `docker ps -a` -- list all containers including stopped
- `docker rm containerid` -- delete container
- `docker images` -- list all images
- `docker rmi image_tag`
- `docker build -t image_tag_name .` -- . is path to the Dockerfile
- `docker run -it --env-file env_file_path -v local_folder_abs_path:/app/shared image_tag_name bash`


# Git

- git remote -v
- git remote remove origin