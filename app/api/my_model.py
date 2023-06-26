from datetime import datetime
from flask_restx import Resource, Namespace
from flask import request
from ..app import db, ma

api = Namespace('Mymodel', description='')

class MyModel(db.Model):


    id = db.Column(db.Integer(), primary_key=True)
    created_at = db.Column(db.DateTime(), default=datetime.now())
    #Add the rest of the required fields

    def __init__(self):
        """Add to the init function the required field for the model"""
        pass

    def __str__(self):
        """The return should be changed to the field which could be wanted to display when
        referring the object"""
        return self.id


class MyModelSchema(ma.Schema):
    """Marshmallow MyModel's schema"""
    class Meta:
        """Add the rest of the required fields"""
        fields = ('id','created_at')
        exclude = () #List of non retrievable fields

mymodel_schema = MyModelSchema()
mymodels_schema = MyModelSchema(many=True)

@api.route('/')
class MyModelListResource(Resource):
    """Resource model"""
    @api.doc('Listing the objects')
    def get(self):
        data = MyModel.query.all()
        return mymodels_schema.dump(data)
    
    @api.doc('Persisting a new objec')
    #@api.param('param', 'param description') This should be added to any addition required param needed
    def post(self):
        mymodel = MyModel()
        db.session.add(mymodel)
        db.session.commit()
        return mymodel_schema.dump(mymodel)

@api.route('/<string:id>')
@api.param('id', 'Object id')
@api.response(404, 'My model not found')
class MyModelResource(Resource):
    """Resource model"""
    def get_object(self, id):
        """Perhaps it could be needed to retrieve the object from another unique field"""
        return MyModel.query.get(id) #Use this one if using id
        #return MyModel.query.filter_by(id=id).first()  #Use this one if not using id
    
    @api.doc('Retrieving object by id')
    def get(self,id):
        try:
            return mymodel_schema.dump(self.get_object(id))
        except:
            return "MyModel not found", 404
        
    @api.doc('Deleting object by id')
    def destroy(self,id):
        try:
            object = self.get_object(id)
            db.session.delete(object)
            db.session.commit()
            return mymodel_schema.dump(object)
        except:
            return "MyModel not found", 404
        
    @api.doc('Updating my model')
    #@api.param('param', 'param description') This should be added to any addition required param needed
    def put(self, id):
        try:
            object = self.get_object(id)
        except:
            return "MyModel not found", 404
        #object.property = request.args['property'] #Add here the params that will be sent to be updated
        db.session.add(object)
        db.session.commit()
        return mymodel_schema.dump(object)