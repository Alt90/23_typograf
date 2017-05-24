from flask import Flask, render_template, request

from typograf import review_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    result_text = ''
    if request.method == 'POST':
        result_text = review_text(request.form['text'])
    return render_template('form.html', result_text=result_text)

if __name__ == "__main__":
    app.run()