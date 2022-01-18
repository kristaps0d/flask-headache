import re
from flask import Blueprint, render_template, request, jsonify

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def root():
    return render_template("index.html")

@views.route('/terms-of-service', methods=['GET'])
def tos():
    return render_template("components/terms-of-service.html")

@views.route('/room/join' , methods=['POST'])
def join():
    # MISSING A REQUEST DATA HANDLER
    # TODO, FIX

    req = request.json
    print(req)

    res = jsonify(success="213")
    return res