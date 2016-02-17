<p align=center><img src="https://github.com/KaiDalgleish/magic8pi/blob/master/magic8ball.png"></p>


Magic8PI brings the power of a magic 8 ball to the web! A simple GET request returns a JSON-formatted prediction.

### Table of Contents
1. [Version](https://github.com/KaiDalgleish/magic8pi#version)
2. [Base URL](https://github.com/KaiDalgleish/magic8pi#base-url)
3. [Endpoints](https://github.com/KaiDalgleish/magic8pi#endpoints)
4. [Errors](https://github.com/KaiDalgleish/magic8pi#errors)
5. [Quickstart](https://github.com/KaiDalgleish/magic8pi#quickstart)
6. [TODOs](https://github.com/KaiDalgleish/magic8pi#todos)


### Version
v1.0

### Tech
* [Flask] - A Python microframework
* [Flask-RESTful] - Framework for creating REST APIs

### Base URL
"**/magic8pi/v1/**"

    > Versioning within the URL allows for continued development without breaking apps which use the API.

### Endpoints

* "**/**" : Returns a single reply in English, the default language
    >{
    >    "reply": "I think so"
    >}

* "**/[language]**" : Returns a single reply in [language]
    >{
    >    "reply": "mouse-t certainly"
    >}
* "**/languages**" : Returns a list of available languages
    >{
    >    "languages": [
    >         "cat", 
    >         "spanish", 
    >         "french", 
    >         "english"
    >     ]
    > }

### Errors
If you request a reply in an unavailable language...
```sh
$ curl http://localhost:5000/magic8pi/v1/tagalog
```

...you'll receive a 400: Bad Request error.

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
Think very hard about your question, and... make a request:
```sh
$ curl http://localhost:5000/magic8pi/v1/cat
{
    "reply": "mouse-t certainly"
}
```

### TODOs
* Deploy on kaidalgleish.io
* Return link to image of ball reply
* Authenticate users
* Rate limit users
* Allow users to add custom messages


[Flask]: http://flask.pocoo.org/
[Flask-RESTful]: https://github.com/flask-restful/flask-restful
