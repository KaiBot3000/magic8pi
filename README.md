<p align=center><img src="https://github.com/KaiDalgleish/magic8pi/blob/master/magic8ball.png"></p>


## Magic8PI brings the power of a magic 8 ball to the web!

### Table of Contents
[Location](https://github.com/KaiDalgleish/magic8pi#location)
[Version](https://github.com/KaiDalgleish/magic8pi#version)
[Base URL](https://github.com/KaiDalgleish/magic8pi#base-url)
[Endpoints](https://github.com/KaiDalgleish/magic8pi#endpoints)
[Errors](https://github.com/KaiDalgleish/magic8pi#errors)
[Quickstart](https://github.com/KaiDalgleish/magic8pi#quickstart)
[Run Magic8PI Locally](https://github.com/KaiDalgleish/magic8pi#Run-Magic8PI-Locally)
[TODOs](https://github.com/KaiDalgleish/magic8pi#todos)


### Location
This API is deployed on my [personal site](http://www.kaidalgleish.io)

### Version
v1.0

### Tech
* [Flask] - A Python microframework
* [Flask-RESTful] - Framework for creating REST APIs

### Base URL
"**http://www.kaidalgleish.io/magic8pi/v1/**"
  
> Versioning within the URL allows for continued API development without breaking apps which rely on consistent responses.  

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
$ curl hhttp://www.kaidalgleish.io/magic8pi/v1/tagalog
```

...you'll receive a 400: Bad Request error.

```sh
{
    "message": "Language not available"
}
```

### Quickstart
Think very hard about your question, and...
...visit an endpoint using your browser to see a prediction!
[http://www.kaidalgleish.io/magic8pi/v1/cat](http://www.kaidalgleish.io/magic8pi/v1/cat)

Or, get a list of the currently supported languages:
[http://www.kaidalgleish.io/magic8pi/v1/languages](http://www.kaidalgleish.io/magic8pi/v1/languages)

### Run Magic8PI Locally
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
X Deploy on kaidalgleish.io
* Return link to image of ball reply
* Authenticate users
* Rate limit users
* Allow users to add custom messages


[Flask]: http://flask.pocoo.org/
[Flask-RESTful]: https://github.com/flask-restful/flask-restful
