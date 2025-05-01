from transformers import pipeline
from flask import Flask, render_template, request
import webbrowser  # 👈 Add this
import threading   # 👈 And this

app = Flask(__name__)

# Load the summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ''
    if request.method == 'POST':
        input_text = request.form['input_text']
        if input_text.strip():
            summary_output = summarizer(input_text, min_length=30, do_sample=False)
            summary = summary_output[0]['summary_text']
    return render_template('index.html', summary=summary.strip())

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    threading.Timer(1.25, open_browser).start()  # 👈 This will open browser automatically
    app.run(debug=True)
