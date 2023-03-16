from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
import random
from flaskr.db import get_db

bp = Blueprint('api', __name__)

totalcalls = 0

@bp.route('/api/getnum', methods=('GET', 'POST'))
def output_num():
    num = random.randint(0,9)
    global totalcalls
    totalcalls = totalcalls + 1
    return jsonify({'number': num})

@bp.route('/api/getcalls', methods=['GET'])
def output_calls():
    return jsonify({'number': totalcalls})
