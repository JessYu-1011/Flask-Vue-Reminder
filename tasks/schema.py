from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import Subjects

# Marshmallow 
class SubjectsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Subjects
        load_instance = True

subject_schema = SubjectsSchema()