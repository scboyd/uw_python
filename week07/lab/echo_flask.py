"""
Minimal Flask + forms demo

Send HTML page that echoes message from HTTP request
To get started, point browser at echo_flask.html
"""

from flask import Flask, request

# no need for template here - just a constant string
form_page = """<head>
<title>Echo request</title>
</head>
<body>
<form method="GET" action="echo_flask.py">
Message: <input type="text" name="message" size="40">
<input type="submit" value="Submit">
</form>
</body>
</html>
"""

message_history = []

# No need for message page
# Flask converts view function return string to HTML page

app = Flask(__name__)

app.debug = True # development only - remove on production machines

# View functions generate HTTP responses including HTML pages and headers

@app.route('/echo_flask.html')
def form():
    return form_page

@app.route('/echo_flask.py')
def message_page():
    # Flask Quickstart suggests request.form should work, but here it is empty
    # Flask converts return string to HTML page
    message = request.args['message']
    for m in message_history:
        message += m
    message_history.append(message)
    return 'Message: %s' % (message)

# No function needed for other routes - Flask will send 404 page

if __name__ == '__main__':
    app.run()

