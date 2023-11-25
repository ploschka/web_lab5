import constants
from app import app
from flask import render_template, request


@app.route('/hello', methods=['GET'])
def hello():
    # для каждого передаваемого параметра формы нужно задать
    # значение по умолчанию, на случай если пользователь ничего не введет
    name = request.values.get('username','')
    gender = request.values.get('gender', '')
    program_id = request.values.get('program', 0)
    subject_id = request.values.getlist('subject[]')
    subjects_select = [constants.subjects[int(i)] for i in subject_id]
    html = render_template(
        'hello.html',
        name=name,
        gender=gender,
        program=constants.programs[int(program_id)],
        subjects_select = subjects_select,
    )
    return html
