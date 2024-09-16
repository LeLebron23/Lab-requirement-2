from flask import Flask, request, render_template_string

app = Flask(__name__)

def LabRequirement2_Banay_Jonas(prelim, midterm, final):
    try:
        prelim, midterm, final = float(prelim), float(midterm), float(final)

        if not (0 <= prelim <= 100 and 0 <= midterm <= 100 and 0 <= final <= 100):
            return "Grades must be between 0 and 100."

        total_avg = prelim * 0.3 + midterm * 0.3 + final * 0.4

        if total_avg >= 75:
            return f"Congratulations! You passed with an average grade of {total_avg:.2f}."
        else:
            return f"Sorry, you failed with an average grade of {total_avg:.2f}."

    except ValueError:
        return "Please enter valid numeric grades."

@app.route('/', methods=['GET', 'POST'])
def grade_form():
    message = ''
    if request.method == 'POST':
        prelim = request.form['prelim']
        midterm = request.form['midterm']
        final = request.form['final']
        message = LabRequirement2_Banay_Jonas(prelim, midterm, final)

    return render_template_string(html_template, message=message)

html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grade Calculator</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <style>
        body {
            background-color: #e6f7e6;
            font-family: Lucida Console, Monospace;
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
            max-width: 500px;
            width: 100%;
        }
        h1 {
            color: #28a745;
            margin-bottom: 20px;
            text-align: center;
        }
        .form-group label {
            font-weight: bold;
        }
        .btn {
            background-color: #28a745;
            color: white;
        }
        .btn:hover {
            background-color: #218838;
        }
        .message {
            margin-top: 20px;
            text-align: center;
            font-size: 1.2rem;
            color: #006400;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Grade Calculator</h1>
    <form method="POST">
        <div class="form-group">
            <label for="prelim">Prelim Grade:</label>
            <input type="number" class="form-control" id="prelim" name="prelim" required min="0" max="100" step="0.01">
        </div>
        <div class="form-group">
            <label for="midterm">Midterm Grade:</label>
            <input type="number" class="form-control" id="midterm" name="midterm" required min="0" max="100" step="0.01">
        </div>
        <div class="form-group">
            <label for="final">Final Grade:</label>
            <input type="number" class="form-control" id="final" name="final" required min="0" max="100" step="0.01">
        </div>
        <button type="submit" class="btn btn-block">Compute Grades</button>
    </form>

    {% if message %}
    <div class="message">{{ message }}</div>
    {% endif %}
</div>

</body>
</html>
'''

if __name__ == "__main__":
    app.run(debug=True)
