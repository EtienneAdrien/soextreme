from flask import Flask

app = Flask(__name__)


def get_hit_count():
    print("azeaaez")


@app.route('/')
def hello():
    get_hit_count()
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')