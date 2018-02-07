minimal setup for docker for ml: https://towardsdatascience.com/beginners-guide-to-data-science-python-docker-3181fd321a5c

python + docker

minimum required number of files to run a docker container with python = 3:

- app.py : your app
- requirements.txt : tells docker's python to install libraries
- Dockerfile: tells docker what to do (the docker container 'cli' on their server)
	- similar to heroku's Procfile

steps (from zero):

1. install docker
2. make a Dockerfile (save a text file as Dockerfile without extensions)
3. make a requirements.txt (with pip freeze or pipenv or just typing it by hand)
4. WRITE APP and save into app.py
5. in terminal, cd to the app folder with 'cd path/to/your/three-files'
6. build docker container with 'docker build -t tag-name-here .' (build with tag -t "your-tag-name", and "." adds everything in that folder)
7. run app with 'docker run tag-name-here'