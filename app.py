from flask import Flask
import joblib

model = joblib.load("dbs.jl")

app = Flask(__name__)
from flask import request, render_template
@app.route("/", methods = ["GET", "POST"])
def i():
    if request.method == "POST":
        num = float(request.form.get("rates"))
        result = model.predict([[num]])[0]
        print(result)
        # return(render_template("index.html", result = 90.2-(50.6*num)))
        return(render_template("index.html", result = result))
    else:
        return render_template("index.html", result ="Waiting……….")
if __name__=="__main__":
    app.run()