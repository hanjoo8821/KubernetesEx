from flask import Flask, render_template, request
import os,random,socket

app = Flask(__name__)

images = [
    "1.jpg",
    "2.jpg",
    "3.jpg",
    "4.jpg",
    "5.jpg",
    "6.jpg"
]

@app.route('/')
def index():
    host_name = "{} to {}".format(socket.gethostname(), request.remote_addr)

    image_path = "/static/images/" + random.choice(images)

    return render_template('index.html', image_path=image_path, host_name=host_name)

# Main
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    try:
        app.run(host="0.0.0.0", port=port, debug=True)
    except Exception as ex:
        print(ex)
