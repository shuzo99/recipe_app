# run.py
from app import app, db

if __name__ == '__main__':
    db.create_all(app=app)
    app.run(debug=True)
