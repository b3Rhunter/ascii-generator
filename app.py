from flask import Flask, request, render_template
from pyfiglet import Figlet

app = Flask(__name__)
f = Figlet(font='doom')  # You can choose other fonts too

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['text']
        ascii_art = f.renderText(text)
        return render_template('index.html', ascii_art=ascii_art)
    return render_template('index.html')

if __name__ == '__main__':
    import os
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

