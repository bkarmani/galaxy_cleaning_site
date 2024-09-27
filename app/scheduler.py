# from apscheduler.schedulers.background import BackgroundScheduler
# from .models import Projects
# from flask import current_app as app
# from . import db
# import os

# # Set the timezone
# os.environ['TZ'] = 'Africa/Lagos'

# # Function to increment project count
# def increment_project_count():
#     with app.app_context():  # Ensure the app context is available
#         project_record = Projects.query.first()
#         if project_record:
#             project_record.total_projects += 1
#             db.session.commit()
#             print(f"Project count incremented to {project_record.total_projects}")

# # Scheduler setup
# def start_scheduler():
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(func=increment_project_count, trigger="interval", minutes=1)
#     scheduler.start()