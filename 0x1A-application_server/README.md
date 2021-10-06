# 0x1A. Application server

## Concepts
For this project, students are expected to look at these concepts:

* [Web Server](https://intranet.hbtn.io/concepts/17)
* [Server](https://intranet.hbtn.io/concepts/67)
* [Web stack debugging](https://intranet.hbtn.io/concepts/68)

Your web infrastructure is already serving web pages via `Nginx` that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your `Nginx` and make is serve your Airbnb clone project.

## Resources
**Read or watch:**

* [Application server vs web server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)
* [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04 (As mentioned in the video, do not install Gunicorn using virtualenv, just install everything globally)](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04)
* [Running Gunicorn](https://docs.gunicorn.org/en/latest/run.html)
* [Be careful with the way Flask manages slash in route](https://werkzeug.palletsprojects.com/en/0.14.x/routing/)- `strict_slashes`
* [Upstart documentation](http://upstart.ubuntu.com/cookbook/)

## Tasks
0. Set up development with Python
1. Set up production with Gunicorn
2. Serve a page with Nginx
3. Add a route with query parameters
4. Let's do this for your API
5. Serve your AirBnB clone
