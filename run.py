# This is the application's entry point. We'll run this file to start the Flask server and launch our application.

from app import app

from app import app

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.run(debug=True)