from app import create_app
from app import db
from app import server_log as logs

app = create_app()

if __name__ == "__main__":

    with app.app_context():
        db.create_all()
        logs.write("Database Ready. \n")
  
    app.run(debug=True)
