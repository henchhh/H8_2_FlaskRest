"""
This is the types module and supports all the REST actions for the
types data
"""

from flask import make_response, abort
from config import db
from models import Avocado, Type, TypeSchema


def read_all():
    """
    This function responds to a request for /api/types
    with the complete lists of types
    :return:        json string of list of types
    """
    # Create the list of types from our data
    types = Type.query.order_by(Type.typeid).all()

    # Serialize the data for the response
    type_schema = TypeSchema(many=True)
    data = type_schema.dump(types)
    return data


# def read_one(typeid):
#     """
#     This function responds to a request for /api/types/{typeid}
#     with one matching avotype from types
#     :param typeid:   Id of avotype to find
#     :return:            avotype matching id
#     """
#     # Build the initial query
#     avotype = (
#         Type.query.filter(Type.typeid == typeid)
#         .outerjoin(Avocado)
#         .one_or_none()
#     )

#     # Did we find a avotype?
#     if avotype is not None:

#         # Serialize the data for the response
#         type_schema = TypeSchema()
#         data = type_schema.dump(avotype)
#         return data

#     # Otherwise, nope, didn't find that type
#     else:
#         abort(404, f"Type not found for Id: {typeid}")


# def create(avotype):
#     """
#     This function creates a new avotype in the types structure
#     based on the passed in avotype data
#     :param avotype:  avotype to create in types structure
#     :return:        201 on success, 406 on avotype exists
#     """
#     typeid = avotype.get("typeid")

#     existing_type = (
#         Type.query.filter(Type.typeid == typeid)
#         .one_or_none()
#     )

#     # Can we insert this avotype?
#     if existing_type is None:

#         # Create a avotype instance using the schema and the passed in avotype
#         schema = TypeSchema()
#         new_type = schema.load(avotype, session=db.session)

#         # Add the avotype to the database
#         db.session.add(new_type)
#         db.session.commit()

#         # Serialize and return the newly created avotype in the response
#         data = schema.dump(new_type)

#         return data, 201

#     # Otherwise, nope, avotype exists already
#     else:
#         abort(409, f"Type with ID {typeid} exists already")


# def update(typeid, avotype):
#     """
#     This function updates an existing avotype in the types structure
#     :param person_id:   Id of the avotype to update in the types structure
#     :param avotype:      avotype to update
#     :return:            updated avotype structure
#     """
#     # Get the avotype requested from the db into session
#     update_type = Type.query.filter(
#         Type.typeid == typeid
#     ).one_or_none()

#     # Did we find an existing avotype?
#     if update_type is not None:

#         # turn the passed in avotype into a db object
#         schema = TypeSchema()
#         update = schema.load(avotype, session=db.session)

#         # Set the id to the avotype we want to update
#         update.person_id = update_type.person_id

#         # merge the new object into the old and commit it to the db
#         db.session.merge(update)
#         db.session.commit()

#         # return updated avotype in the response
#         data = schema.dump(update_type)

#         return data, 200

#     # Otherwise, nope, didn't find that avotype
#     else:
#         abort(404, f"Type not found for Id: {typeid}")


# def delete(typeid):
#     """
#     This function deletes a avotype from the types structure
#     :param typeid:   Id of the avotype to delete
#     :return:            200 on successful delete, 404 if not found
#     """
#     # Get the avotype requested
#     avotype = Type.query.filter(Type.typeid == typeid).one_or_none()

#     # Did we find a avotype?
#     if avotype is not None:
#         db.session.delete(avotype)
#         db.session.commit()
#         return make_response(f"Type {typeid} deleted", 200)

#     # Otherwise, nope, didn't find that avotype
#     else:
#         abort(404, f"Type not found for Id: {typeid}")