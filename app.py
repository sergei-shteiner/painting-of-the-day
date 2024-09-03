from flask import Flask, render_template
from babel.dates import format_date
from datetime import datetime
import locale

app = Flask(__name__)

@app.route('/')
def index():
    # User locale detection
    user_locale = locale.getdefaultlocale()[0]
    
    # Getting the current date
    today = datetime.now()
    
    # Formatting the date using Babel
    formatted_date = format_date(today, locale=user_locale)
    
    return render_template('index.html', date=formatted_date)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
 