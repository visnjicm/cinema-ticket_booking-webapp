from flask import Flask, request, render_template

from main import run_backend

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    form_dict = request.form
    return run_backend(form_dict.get('full_name'), form_dict.get('seat'), form_dict.get('card_type'),
                       form_dict.get('card_number'), form_dict.get('card_cvc'), form_dict.get('cardholder_name'))


if __name__ == '__main__':
    app.run(debug=True)
