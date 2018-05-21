# hosting to docker with nginx

https://hub.docker.com/_/nginx/

## examples from ./code folder
- a python frozen-flask app and a javascript nodejs app
1. you have an app
2. make it static (browserify it or similar) so that it can be served by clicking on a `.html` file
	- static file == when you double click on `.html` it works (it is served statically by the browser)
3. push your static directory to a docker container [like this](https://hub.docker.com/_/nginx/)
4. 