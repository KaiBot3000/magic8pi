## Magic8PI

Magic8PI brings the power of a magic 8 ball to the web! 

### Version
v1.0

### Tech
* [Flask] - A Python microframework
* [Flask-RESTful] - 

### Base URL
/magic8pi/v1/

* Versioning within the URL allows for conitnued development without breaking apps using the API.

### Endpoints

/
/languages
/[language]

### Errors

```sh
$ curl http://localhost:5000/magic8pi/v1/tagalog
```

You'll receive a 400: Bad Request error.

```sh
{
    "message": "Language not available"
}
```

### Quickstart

Clone repo:
```sh
$ git clone https://github.com/KaiDalgleish/magic8pi.git magic8pi
$ cd magic8pi
```

Install dependencies:
```sh
$ pip install -r requirements.txt
```

Run Magic8PI server:
```sh
$ python server.py
```

```sh
$ curl http://localhost:5000/magic8pi/v1/cat
{
    "reply": "mouse-t certainly"
}
```

### TODOs

* Return link to image of ball reply
* Authenticate users
* Rate limit users
* Allow users to add custom messages
