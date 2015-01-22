from flask import Flask, render_template, request


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


def canMakeWord(letters, word):
    """
    Checks if a word (from a dictionary) can be
    constructed with given letters
    """
    listOfLetters = list(letters)
    for index, letter in enumerate(word):
        if letter in listOfLetters:
            listOfLetters.remove(letter)
        else:
            return False
    return True


def compute_solution(letters):
    """
    Computes a list of words that can be
    constructed with letters
    """
    solutions = []
    letters = letters.encode('ascii', 'ignore')
    with open('static/dict.txt', 'r') as f:
        legalWordsList = f.readlines()
    for word in legalWordsList:
        if len(word) <= len(letters):
            if canMakeWord(letters, word.rstrip()):
                solutions.append(word)
    sortedSolutions = sorted(solutions, key=len, reverse=True)
    return sortedSolutions

if __name__ == '__main__':
    # TODO remove the debug flag before deployment!!!
    app.debug = True
    app.run()
