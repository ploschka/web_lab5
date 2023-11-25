from app import app
from flask import render_template, request
import constants


@app.route('/', methods=['GET'])
def index():
    render = bool(request.values)
    name = request.values.get('username','')
    gender = request.values.get('gender', '')
    program_id = request.values.get('program', 0, int)
    subject_id = request.values.getlist('subject[]', int)
    subjects_select = [constants.subjects[i] for i in subject_id]
    # выводим форму
    html = render_template(
        'index.html',
        program_list = enumerate(constants.programs),
        subject_list = enumerate(constants.subjects),
        name=name,
        gender=gender,
        program_id = program_id,
        program=constants.programs[program_id],
        subject_id = subject_id,
        subjects_select = subjects_select,
        render = render
    )
    return html
