from application import app



@app.route("/")
def index():
    return"""

    <h2>Hello world</h2>
    <p>this is a test</p>

    """

