from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/bio")
def bio():
    return render_template("bio.html")

@app.route("/education")
def education():
    return render_template("education.html")

@app.route("/experience")
def experience():
    return render_template("experience.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        flash(f"Thank you for reaching out, {name}! We'll get back to you soon.")
        return redirect("/contact")
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
