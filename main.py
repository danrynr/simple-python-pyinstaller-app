"""
import add2vals from sources directory
use it to calculate 2 numbers
"""
from sources import add2vals

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return add2vals.add2('20', '11')

if __name__ == '__main__':
    app.run()