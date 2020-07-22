from flask_restplus import fields

from app import db
from .. import api


class Context(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    maxQuota = db.Column(db.Integer, default=500)
    usedQuota = db.Column(db.Integer, default=0)
    enabled = db.Column(db.Boolean, default=True)
    #admin = db.Column(db.String(150), unique=True)
    costumer_id = db.Column(db.Integer, db.ForeignKey('costumer.id'), nullable=False)    

    @property
    def ox_id(self):
        return self.id

    @ox_id.setter
    def ox_id(self, ox_id):
        self.id = ox_id

    # Models
    register_model = api.model('Register Context', {
    'name': fields.String(required=True),
    'password': fields.String(required=True),
    'maxQuota': fields.Integer(),
    'costumer_id': fields.Integer()
    })
    
    resource_model = api.model('Context', {
    'id': fields.Integer(),
    'name': fields.String(),
    'usedQuota': fields.Integer(),
    'maxQuota': fields.Integer(),
    'enabled': fields.Boolean(),
    'ox_id': fields.Integer(),
    'costumer_id': fields.Integer(),

    #'admin': fields.String(),
    })  

