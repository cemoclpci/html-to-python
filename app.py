import os
import uuid
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/tag_durumu/<isminiz>/<int:oynama_saati>/<int:tag_fiyati>')
def tag_durumu(isminiz, oynama_saati, tag_fiyati):
    if tag_fiyati >= 3000 and oynama_saati >= 150:
        tag_sahibi = True
    else:
        tag_sahibi = False
    user_uuid = str(uuid.uuid4())
    user_directory = f"users/{isminiz}"
    os.makedirs(user_directory, exist_ok=True)
    user_file = f"{user_directory}/index.html"
    with open(user_file, "w") as file:
        file.write(render_template('index.html', isminiz=isminiz, tag_sahibi=tag_sahibi))
    return send_from_directory(os.path.dirname(user_file), os.path.basename(user_file))

if __name__ == '__main__':
    app.run()
