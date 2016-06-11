from bottle import response, Bottle, run

app = Bottle()


def raise_error(error_code, msg):
    response.status = error_code
    return msg


@app.post('/brew-coffee')
def brew_coffee():
    return raise_error(418, "I'm a teapot")


@app.post('/brew-tea')
def brew_tea():
    return raise_error(201, "Tea coming right up....")


@app.route('/')
def root():
    return "Try /brew-coffee or /brew-tea.\n"


if __name__ == '__main__':
    run(
        app,
        host='0.0.0.0',
        port=8080,
        reload=True
    )
