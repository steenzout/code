# Magical Web Servers

## Date(s) of talk
May 11, 2017


## Synopsis

 - Just making a simple web server/service
 - Going over some HTTP verbs, ie GET, PUT, PATCH, POST and DELETE
 - Some common responses (html/image/json)
 - Integrate it with our LastFM Collage maker!


## Requirements

Before you start be sure you have the following installed:
- [Python][python] 3.6
- [tox][tox]
- [virtualenv][virtualenv]


## Steps

```bash
$ pip install virtualenv tox
```

To setup this exercise's virtual environment do:
```bash
$ tox
# a new directory .tox/B002/ will be created
```

After that you should source the project [virtualenv][virtualenv]:

```
$ source .tox/B002/bin/activate
```

You can run the web service:

```bash
$ python mag-web-srv.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
```


[meetup]:   https://www.meetup.com/PythonAtThePoint/events/239300523/   "Beginners: Magical Web Services!"
[python3]:   https://www.python.org/downloads/  "Python"
[tox]:  http://tox.readthedocs.io/en/latest/    "tox"
[virtualenv]:   https://virtualenv.pypa.io/en/stable/   "virtualenv"
