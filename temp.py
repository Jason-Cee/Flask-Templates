from flask import Flask, render_template

app = Flask(__name__)
students = {"Naeemah: ": 20, "Godwin: ": 47, "Thapelo: ": 27, "Jason: ": 23}


@app.route('/<name>')
def homepage(name):
    return render_template('home.html', name=name, students=students)


@app.route('/loopy/<int:number>')
def numbers(number):
    return render_template('numbers.html', number=number)


if __name__ == '__main__':
    app.debug = True
    app.run()
