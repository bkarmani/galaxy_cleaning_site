import os
from app import create_app, db
from flask_migrate import Migrate
from app.models import Projects, User, Post
from dotenv import load_dotenv
# from app.scheduler import start_scheduler

load_dotenv()

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

# start_scheduler()

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Projects=Projects, User=User, Post=Post)
