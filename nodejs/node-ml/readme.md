# minimal node.js app

SUPER DUPER EASY
- make your javascript + html + css using node
1. npm init
2. write your server (use the one in this code) in a js file
3. write your client side stuff in html + css + js however you want
4. `git init`, `git add .`, `git commit -m "your message"`
5. `heroku login`, `heroku create`, `git push heroku master`
6. open your app!

two things:
1. the `node.js` is only a static file server
2. the `index.html` is what the `node.js` serves, it doesn't call anything from the server part of the app.

when you type `localhost:3000/index.html` in the search bar, you get the `index.html` file.

the index.html runs all on its own (because brain.js is CDN-ed and app.js is not called)