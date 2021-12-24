from marshmallow import fields
from datetime import datetime
from config import db, ma

#MODEL
class Avocado(db.Model):
    __tablename__ = 'avocado'
    date = db.Column(db.Text)
    avgprice = db.Column(db.Float)
    totalvol = db.Column(db.Integer, primary_key=True)
    avo_a = db.Column(db.Integer)
    avo_b = db.Column(db.Float)
    avo_c = db.Column(db.Float)
    type = db.Column(db.Integer)
    regionid = db.Column(db.Integer, db.ForeignKey('avoregion.regionid'))
    # "date"    TEXT,
    # "avgprice"    REAL,
    # "totalvol"    INTEGER,
    # "avo_a"    INTEGER,
    # "avo_b"    REAL,
    # "avo_c"    REAL,
    # "type"    INTEGER,
    # "regionid"    INTEGER

class Type(db.Model):
    __tablename__ = 'avotype'
    typeid = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)
    # avocado = db.relationship(
    #     'Avocado',
    #     backref='avotype',
    #     cascade='all, delete, delete-orphan',
    #     order_by='asc(Avocado.date)'
    # )

class Region(db.Model):
    __tablename__ = 'avoregion'
    regionid = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String, nullable=False)
    # avocado = db.relationship(
    #     'Avocado',
    #     backref='avoregion',
    #     cascade='all, delete, delete-orphan',
    #     order_by='asc(Avocado.date)'
    # )


# # SCHEMA AVOCADO   
class AvocadoSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Avocado
        # sqla_session = db.session
        load_instance = True

    # # variabel sebelumnya => notes
    # avotype = fields.Nested('AvocadoTypeSchema', default=[], many=True)
    # avoregion = fields.Nested('AvocadoRegionSchema', default=[], many=True)

# # RELATION AVOCADO TO TYPE
# class AvocadoTypeSchema(ma.SQLAlchemyAutoSchema):
#     """
#     This class exists to get around a recursion issue
#     """
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#     typeid = fields.Int()
#     type = fields.Str()

#RELATION AVOCADO TO REGION
# class AvocadoRegionSchema(ma.SQLAlchemyAutoSchema):
#     """
#     This class exists to get around a recursion issue
#     """
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#     regionid = fields.Int()
#     region = fields.Str()

#TYPE SCHEMA
class TypeSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Type
        # sqla_session = db.session
        load_instance = True

    # variable sebelumnya => person
    # avocado = fields.Nested("TypeAvocadoSchema", default=None)

#RELATION TYPE TO AVOCADO
# class TypeAvocadoSchema(ma.SQLAlchemyAutoSchema):
#     """
#     This class exists to get around a recursion issue
#     """
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#     date = fields.Str()
#     avgprice = fields.Float()
#     totalvol = fields.Int()
#     avo_a = fields.Int()
#     avo_b = fields.Float()
#     avo_c = fields.Float()
#     type = fields.Int()
#     regionid = fields.Int()


#REGION SCHEMA
class RegionSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Region
        # sqla_session = db.session
        load_instance = True

    # variable sebelumnya => person
    # avocado = fields.Nested("RegionAvocadoSchema", default=None)

#RELATION REGION TO AVOCADO
# class RegionAvocadoSchema(ma.SQLAlchemyAutoSchema):
#     """
#     This class exists to get around a recursion issue
#     """
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#     date = fields.Str()
#     avgprice = fields.Float()
#     totalvol = fields.Int()
#     avo_a = fields.Int()
#     avo_b = fields.Float()
#     avo_c = fields.Float()
#     type = fields.Int()
#     regionid = fields.Int()