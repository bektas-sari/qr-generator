from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_img = None
    if request.method == "POST":
        url = request.form["url"]
        if url:
            qr = qrcode.make(url)
            img_io = BytesIO()
            qr.save(img_io, format="PNG")
            img_io.seek(0)
            return send_file(img_io, mimetype="image/png")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

