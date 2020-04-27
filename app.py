import sys

sys.path.append('..')
print(sys.path)

from flask import request
from core.tools import wrap_response

from core.config import app, url_prefix
from core.fee import Fee
from core.country import Country
from core.program import Program
from core.partner import Partner
from core.student import Student
from core.require import Require
from core.organization import Organization
from core.university import University

# @app.before_request
# def before_request():
#     session.permanent = True
#     app.permanent_session_lifetime = timedelta(days=365)

@app.route('/', methods=['GET'])
def hello():
    return wrap_response({"result": "Good"})


# @app.route('/organizations', methods=['GET'])
# def get_organizations():




if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5089)