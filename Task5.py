#Task 5: Create a Flask form to accept a name and greet the user (HTML + Python).
from flask import Flask, request, render_template_string
app =Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def greet_user():
    if request.method == 'POST':
        name = request.form.get('name', 'World')
        return render_template_string('<h1>Hello, {{name}}!</h1><a href="/">Go Back</a>', name=name)
    return '''
        <form method="post">
            Name: <input type="text" name="name">
            <input type="submit" value="Submit">
        </form>
    '''
if __name__ == '__main__':
    app.run(debug=True)
    