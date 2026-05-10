from flask import Flask, render_template


app = Flask(__name__, template_folder='../templates')

text = '''
Ljcnfxyj nz;tkj, yj gjyznyj
'''

Chialds = [
    {'name': 'Костя', 'age': 25},
    {'name': 'Никита', 'age': 28},
    {'name': 'Игорь', 'age': 22},
]

@app.route('/')
def base():
    return render_template("base.html", dis_text=text, Chialds=Chialds)



if __name__ == '__main__':
    app.run()
