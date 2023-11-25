from flask import Flask, render_template, request
from math import acos, sqrt, degrees
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    req = bool(request.values)
    size = request.values.get('size', 2, int)
    a1 = request.values.get('a1', 0, int)
    a2 = request.values.get('a2', 0, int)
    a3 = request.values.get('a3', 0, int)
    a4 = request.values.get('a4', 0, int)

    b1 = request.values.get('b1', 0, int)
    b2 = request.values.get('b2', 0, int)
    b3 = request.values.get('b3', 0, int)
    b4 = request.values.get('b4', 0, int)

    Av = [a1, a2, a3, a4]
    Bv = [b1, b2, b3, b4]

    op = request.values.get('op', 'm')

    if op == 'm':
        result = sum([a * b for a, b in [(Av[i], Bv[i]) for i in range(size)]])
    elif op == 'd':
        result = map(str, [Bv[i] - Av[i] for i in range(size)])
    elif op == 'a':
        m = sum([a * b for a, b in [(Av[i], Bv[i]) for i in range(size)]])
        ma = sqrt(sum([i*i for i in [Av[j] for j in range(size)]]))
        mb = sqrt(sum([i*i for i in [Bv[j] for j in range(size)]]))
        result = "%.2f" % degrees(acos(m / (ma * mb)))
    else:
        result = 'ОШИБКА!!!'

    html = render_template(
        'index.html',
        size=size,
        a1=a1,
        a2=a2,
        a3=a3,
        a4=a4,
        b1=b1,
        b2=b2,
        b3=b3,
        b4=b4,
        op=op,
        result=result,
        req=req
    )
    return html
