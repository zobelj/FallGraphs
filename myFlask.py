from flask import Flask
from flask import render_template
from flask import request
from saveRound import saveRound
from sheets_append import append_data
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template("homepage.html")

@app.route('/data_entry', methods=['GET', 'POST'])
def data_entry():
    if(request.method == "POST"):
        x = request.form
        try:
            if x['qualified_bool'] == 'on':
                qual_bool = True
        except:
            qual_bool = False
        try:
            round_data = ['', x['name_input'], int(x['round_input']) - 1, x['map_input'], '', int(x['entering_input']), int(x['qualifiers_input']), qual_bool]
            print(round_data)
            append_data(round_data)
        except:
            pass
    return render_template("data_entry.html")

@app.route('/about')
def about():
    return('Made by Room B406')

if __name__ == "__main__":
    app.run(host='localhost', port=80)