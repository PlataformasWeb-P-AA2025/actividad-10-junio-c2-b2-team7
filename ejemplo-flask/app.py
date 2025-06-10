from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    name = request.args.get('name', 'Invitado')
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
