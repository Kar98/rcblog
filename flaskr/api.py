from flask import Blueprint, flash, g, redirect, request, render_template, session, url_for, jsonify
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

@bp.route('/api/get_quote', methods=['POST'])
def quote():
    print('quote hit')
    j = {}
    rawdata = request.get_data()
    rawdata = rawdata.decode('ascii').lower()
    print(rawdata)
    if 'pants' in rawdata :
        return "I just don't understand"
    elif 'rick' in rawdata:
        return "I'm sweating like a rapist"
    elif 'bob' in rawdata:
        return 'Load up'
    print(j)
    return 'Test'
