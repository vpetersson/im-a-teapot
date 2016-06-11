# im-a-teapot

I always wanted to do something with HTTP [Status Code 418](https://httpstatuses.com/418) so I wrote this little script and attached a Raspberry Pi Zero to my tea pot.

## Server

```
$ pip install -r requirements.txt
$ python app.py
```

## Client

(python code)
```
$ pip install reqests
$ python
>>> r = requests.post('http://127.0.0.1:8080/brew-tea')
>>> r
 <Response [201]>

>>> r.content
'Tea coming right up...'

>>> r = requests.post('http://127.0.0.1:8080/brew-coffee')
>>> r
<Response [418]>

>>> r.content
"I'm a teapot"
```
