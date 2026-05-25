from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS = [{
    id :1,
    "Desgination":" Data Analyst",
    "Salary": 4000000
},
    {id :2,
    "Desgination":"Analyst",
    "Salary": 4030000
},
    {id :3,
    "Desgination":" Data Science",
    "Salary": 5000000
},    
    {id :4,
    "Desgination":" MLEngineer",
    "Salary": 5000000
}
]
@app.route("/")
def hello():
    return render_template("index.html", jobs=JOBS)

'''@app.route("/api/jobs")
def list_jobs():
    return jsonify([JOBS])'''

if __name__ == "__main__":
    app.run(debug=True)