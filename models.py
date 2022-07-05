"""
Modely Prispevkov
"""
from config import db
from utils import dict_to_model
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class Post(db.Model):
    """
    Model Post
    """
    __tablename__ = "post"
    _id     = db.Column(db.Integer, primary_key=True)
    id     = db.Column(db.Integer, nullable=False)
    userId = db.Column(db.Integer, nullable=False)
    title  = db.Column(db.String(128))
    body   = db.Column(db.String())
    
    def setDataFromJson(self, data):
        """
        Prevedie a ulozi data z json formatu do objektu
        """
        self = dict_to_model(self, data)


class PostSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        load_instance = True
        # sqla_session = db.session