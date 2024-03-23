from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        message = request.form.get('message')
        save_message(message)
        return 'Mesaj alındı ve kaydedildi.'

def save_message(message):
    with open('messages.txt', 'a') as file:
        file.write(message + '\n')
    # Yeni bir mesaj kaydedildiğinde, bildirim betiğine sinyal gönder
    subprocess.run(['touch', 'new_message_signal.txt'])

if __name__ == '__main__':
    app.run(debug=True)
