from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        user_message = request.form['message']
        # Here, you can save the message to a file or send it to your email
        with open('messages.txt', 'a') as f:
            f.write(f"{user_message}\n")
        return redirect(url_for('thank_you'))
    return render_template('message.html')

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)
