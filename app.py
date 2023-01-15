from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def calculate():
    if request.method == "POST":
        gp_grade = request.form.get("gpgrade")
        pw_grade = request.form.get("pwgrade")
        h2_subj_1 = request.form.get("h2subj1")
        h2_grade_1 = request.form.get("h2grade1")
        h2_subj_2 = request.form.get("h2subj2")
        h2_grade_2 = request.form.get("h2grade2")
        h2_subj_3 = request.form.get("h2subj3")
        h2_grade_3 = request.form.get("h2grade3")
        h1_subj = request.form.get("h1subj")
        h1_grade = request.form.get("h1grade")
        if h2_subj_1 == h2_subj_2 or h2_subj_2 == h2_subj_3 or h2_subj_1 == h2_subj_3 or h1_subj == h2_subj_1 or h1_subj == h2_subj_2 or h1_subj == h2_subj_3:
            return redirect(url_for('errorpage'))
    return render_template("index.html")

@app.route("/error")
def errorpage():
    return render_template("error.html")

if __name__ == "__main__": app.run(debug=True)