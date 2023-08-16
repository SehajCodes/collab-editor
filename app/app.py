import os
import sys
import shutil
from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

files = os.listdir("../files/")
for file in files:
  if file == ".DS_Store":
    files.remove(file)
    continue
  shutil.copy2(str("../files/"+file), str("../temp/"+file))
read_files = {}

@app.route("/")
def editor():
  # print(files, file=sys.stderr)
  # print(os.listdir("./templates/"), file=sys.stderr)
  filename = request.args.get("filename")
  if filename is None:
    return render_template("editor.html", files=files)
  file = open(str("../temp/"+filename), "r")
  text = file.read()
  read_files[filename] = text
  # print(text, file=sys.stderr)
  return render_template("editor.html", files=files, filename=filename, text=text)

@app.route("/save", methods=["POST"])
def save():
  filename = request.form.get("cur_filename")
  text = request.form.get("text")
  print(filename, file=sys.stderr)
  print(text, file=sys.stderr)
  if filename == None:
    return redirect("/editor")
  with open(str("../files/"+str(filename)), "w") as f:
    f.write(text)
  return render_template("editor.html", files=files, filename=filename, text=text)

@socketio.on("update_editor")
def update_editor(data):
  with open(str("../temp/"+str(data["filename"])), "w") as f:
    f.write(data["text"])
  emit("update_editor", data, broadcast = True, include_self=False)

if __name__ == '__main__':
  app.jinja_env.auto_reload = True
  app.config["TEMPLATES_AUTO_RELOAD"] = True
  app.debug = True
  # app.run(debug = True, host="0.0.0.0")
  socketio.run(app, allow_unsafe_werkzeug=True, host="0.0.0.0")

def update_edit(filename, text):
  print()