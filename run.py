import os
from app import create_app, db
from flask_migrate import Migrate
from app.models import Projects, User
# from app.scheduler import start_scheduler


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db, User, Projects)

# start_scheduler()

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Projects=Projects, User=User)
