from flask import Flask
from flask import render_template
from flask import request
from saveRound import saveRound

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
                qual_bool = 'TRUE'
        except:
            qual_bool = 'FALSE'
        round_data = [x['name_input'], x['round_input'], x['map_input'], x['entering_input'], x['qualifiers_input'], qual_bool]
        print(round_data)
        saveRound(round_data)
    return render_template("data_entry.html")

@app.route('/about')
def about():
    return('Made by Room 406')

app.run()