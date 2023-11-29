from flask import Flask, render_template, request
from math import acos, sqrt, degrees
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    req = bool(request.values)
    size = min(request.values.get('size', 2, int), 4)
    show = request.values.get('show', False, bool)
    render_vec = size > 0 and req
    A = request.values.getlist('a', int)
    B = request.values.getlist('b', int)

    v = len(A) > 0 and len(B) > 0

    if show:
        A = [0]*size
        B = [0]*size

    result = None
    op = request.values.get('op', 'm')

    if not show:
        if v:
            if op == 'm':
                result = sum([a * b for a, b in [(A[i], B[i])
                            for i in range(size)]])
            elif op == 'd':
                result = map(str, [B[i] - A[i] for i in range(size)])
            elif op == 'a':
                m = sum([a * b for a, b in [(A[i], B[i]) for i in range(size)]])
                ma = sqrt(sum([i*i for i in [A[j] for j in range(size)]]))
                mb = sqrt(sum([i*i for i in [B[j] for j in range(size)]]))
                result = "%.2f" % degrees(acos(m / (ma * mb)))
            else:
                result = 'ОШИБКА!!!'

    html = render_template(
        'index.html',
        render_vec=render_vec,
        size=size,
        A=A,
        B=B,
        op=op,
        result=result,
        req=req
    )

    print(
        render_vec,
        size,
        v,
        A,
        B,
        op,
        result,
        req
    )
    return html
