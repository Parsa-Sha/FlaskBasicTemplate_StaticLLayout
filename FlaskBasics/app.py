from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bg_color = "#ADD8E6"  # Default background color
    text_color = "#000030"

    if request.method == 'POST':
        if 'dark_blue' in request.form:
            bg_color = "#000030"  # Dark blue
            text_color = "#ADD8E6"
            return render_template('layout1.html', bg_color=bg_color, text_color=text_color)
        elif 'light_blue' in request.form:
            bg_color = "#ADD8E6"  # Light blue
            text_color = "#000030"
            return render_template('layout2.html', bg_color=bg_color, text_color=text_color)
        elif 'black' in request.form:
            bg_color = "#000000"
            text_color = "#f0f0f0"
            return render_template('layout3.html', bg_color=bg_color, text_color=text_color)

    return render_template('index.html', bg_color=bg_color, text_color=text_color)

if __name__ == '__main__':
    app.run(debug=True)