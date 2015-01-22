from flask import Flask, render_template, request, url_for


app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def show_main_page(name=None):
    return render_template('main.html', name=name)


@app.route('/letters/', methods=['GET', 'POST'])
def show_results():
    user_input = request.form['letters']
    solutions = compute_solution(user_input)
    return render_template('show_results.html', solutions=solutions)


def compute_solution(letters):
    solutions = []
    for letter in letters:
        solutions.append(letter)
    return solutions

if __name__ == '__main__':
    # TODO remove the debug flag before deployment!!!
    app.debug = True
    app.run()
