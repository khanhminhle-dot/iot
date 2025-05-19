from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)
status = True

@app.route("/")
def index():
    now = datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")
    print("-----------> Check: A user connected!")
    return render_template("main.html", now=now, status=status)

@app.route("/update")
def updateStatus():
    global status
    statusUser = request.args.get("status", default="false").lower()
    status = statusUser == "true"
    print("Status cập nhật:", status)
    return redirect("/")  # 👈 Trả về trang chủ sau khi cập nhật

if __name__ == "__main__":
    app.run(debug=True)
