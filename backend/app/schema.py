from app import ma
from app.models import Subjects, SubjectNames

class SubjectsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Subjects

subject_schema = SubjectsSchema()
subjects_schema = SubjectsSchema(many=True)

class SubjectNamesSchema(ma.SQLAlchemyAutoSchema):
    class Meta: 
        model = SubjectNames

subject_names_schema = SubjectNamesSchema(many=True)
