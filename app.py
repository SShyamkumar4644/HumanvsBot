from flask import Flask, render_template_string, request

app = Flask(__name__)

html = '''
<!doctype html>
<title>Login</title>
<h2>Login Page</h2>
<form method="POST">
  Username: <input type="text" name="username"><br><br>
  Password: <input type="password" name="password"><br><br>
  <input type="submit" value="Login">
</form>
{% if message %}
<p>{{ message }}</p>
{% endif %}
'''

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        message = f"Logged in as {username}"
    return render_template_string(html, message=message)

if __name__ == "__main__":
    app.run(port=5000)
