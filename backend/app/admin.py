from . import admin, db
from .models import *
from flask_admin.contrib.sqla import ModelView

admin.add_view(ModelView(Subjects, db.session))
admin.add_view(ModelView(SubjectNames, db.session))