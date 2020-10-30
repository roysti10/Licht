# Import flask and template operators
from flask import Flask, render_template, request
import subprocess
from helpers import sayFunc
from cli import main
import os
from code2speech import speak

app = Flask(__name__)
app.config.from_object("config")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/tutorial", methods=["GET", "POST"])
def tutorial():
    mp3_file, text = speak("app/text/tutorial1.txt")
    print(request.method)
    if request.method == "POST":
        code = request.form["code"]
        f = open("x.py", "w+")
        f.write(code)
        f.close()
        output = main("x.py")
        if output == 1:
            out = subprocess.check_output(["python3", "x.py"]).decode("utf8")
            if out == "":
                sayFunc(
                    "Great job!, File compiled successfully. The output is. "
                    + "Program returns no output",
                    130,
                )
            else:
                sayFunc(
                    "Great job!, File compiled successfully. The output is. "
                    + str(out),
                    130,
                )
        else:
            out = output
            print(output)
        return render_template(
            "editor.html", code=code, text=text.replace("\n", ""), output=out, fname=""
        )
    return render_template(
        "editor.html", code="", output="", text=text.replace("\n", ""), fname=mp3_file
    )
