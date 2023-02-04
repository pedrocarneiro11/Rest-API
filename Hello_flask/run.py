from flask import Flask

app = Flask(__name__)


@app.route("/<int:number>", methods=['GET', 'POST'])
def hello(number):

    return '<h1>Hello World {}</h1>'.format(number)


if __name__ == "__main__":
    app.run()
