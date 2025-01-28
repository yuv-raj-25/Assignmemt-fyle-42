from marshmallow import Schema, EXCLUDE, fields, post_load
from core.libs.helpers import GeneralObject
from core.models.teachers import Teacher


class TeacherSchema(Schema):
    class Meta:
        model = Teacher
        unknown = EXCLUDE  # Ignore fields that are not explicitly defined in the schema

    id = fields.Integer(dump_only=True)  # Teacher's unique identifier, read-only
    user_id = fields.Integer(required=True)  # Associated user ID, required for creation
    created_at = fields.DateTime(dump_only=True)  # Timestamp when the record was created
    updated_at = fields.DateTime(dump_only=True)  # Timestamp of the last update

    @post_load
    def initiate_class(self, data_dict, many, partial):
        # Convert the validated dictionary into a GeneralObject
        return GeneralObject(**data_dict)
