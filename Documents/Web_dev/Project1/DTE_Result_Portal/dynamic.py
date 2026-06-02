from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def dteportal():
    return render_template('resultwebpage.html')

@app.route('/resultwebpage2.html')
def result_page():
    return render_template('resultwebpage2.html')


if __name__ == '__main__': 
    app.run(debug=True)