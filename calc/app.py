from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addition():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)

    return str(result)

@app.route('/sub')
def subtraction():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a, b)

    return str(result)

@app.route('/mult')
def multiply():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a, b)

    return str(result)

@app.route('/div')
def division():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a, b)

    return str(result)

operations_dict = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div,
}

@app.route('/math/<op>')
def mathematics(op):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations_dict[op](a, b)

    return str(result)