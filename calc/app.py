# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

#Part 2 for reference
# operators = {
#         "add": add,
#         "sub": sub,
#         "mult": mult,
#         "div": div,
#         }

# @app.route('/math/<maths>')
# def do_math(maths):
#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     return f'{operators[maths](a,b)}'

@app.route('/add')
def add_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f'{add(a,b)}'

@app.route('/sub')
def sub_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f'{sub(a,b)}'

@app.route('/mult')
def multiply_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f'{mult(a,b)}'

@app.route('/div')
def divide_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return f'{div(a,b)}'


