#!/usr/bin/env python3
import os 
from flask import Flask, request, current_app, g, make_response

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
