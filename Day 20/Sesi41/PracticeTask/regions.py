"""
This is the regions module and supports all the REST actions for the
regions data
"""

from flask import make_response, abort
from config import db
from models import Avocado, Region, RegionSchema


def read_all():
    """
    This function responds to a request for /api/regions
    with the complete lists of regions
    :return:        json string of list of regions
    """
    # Create the list of regions from our data
    regions = Region.query.order_by(Region.regionid).all()

    # Serialize the data for the response
    region_schema = RegionSchema(many=True)
    data = region_schema.dump(regions)
    return data


def read_one(regionid):
    """
    This function responds to a request for /api/regions/{regionid}
    with one matching avoregion from regions
    :param regionid:   Id of avoregion to find
    :return:            avoregion matching id
    """
    # Build the initial query
    avoregion = (
        Region.query.filter(Region.regionid == regionid)
        .outerjoin(Avocado)
        .one_or_none()
    )

    # Did we find a avoregion?
    if avoregion is not None:

        # Serialize the data for the response
        person_schema = RegionSchema()
        data = person_schema.dump(avoregion)
        return data

    # Otherwise, nope, didn't find that avoregion
    else:
        abort(404, f"Region not found for Id: {regionid}")


# def create(avoregion):
#     """
#     This function creates a new avoregion in the regions structure
#     based on the passed in avoregion data
#     :param avoregion:  avoregion to create in regions structure
#     :return:        201 on success, 406 on avoregion exists
#     """
#     regionid = avoregion.get("regionid")

#     existing_region = (
#         Region.query.filter(Region.regionid == regionid)
#         .one_or_none()
#     )

#     # Can we insert this person?
#     if existing_region is None:

#         # Create a avoregion instance using the schema and the passed in avoregion
#         schema = RegionSchema()
#         new_region = schema.load(avoregion, session=db.session)

#         # Add the avoregion to the database
#         db.session.add(new_region)
#         db.session.commit()

#         # Serialize and return the newly created avoregion in the response
#         data = schema.dump(new_region)

#         return data, 201

#     # Otherwise, nope, avoregion exists already
#     else:
#         abort(409, f"Region with ID {regionid} already exists")


# def update(regionid, avoregion):
#     """
#     This function updates an existing avoregion in the regions structure
#     :param regionid:   Id of the avoregion to update in the regions structure
#     :param avoregion:      avoregion to update
#     :return:            updated avoregion structure
#     """
#     # Get the avoregion requested from the db into session
#     update_region = Region.query.filter(
#         Region.regionid == regionid
#     ).one_or_none()

#     # Did we find an existing avoregion?
#     if update_region is not None:

#         # turn the passed in avoregion into a db object
#         schema = RegionSchema()
#         update = schema.load(avoregion, session=db.session)

#         # Set the id to the avoregion we want to update
#         update.regionid = update_region.regionid

#         # merge the new object into the old and commit it to the db
#         db.session.merge(update)
#         db.session.commit()

#         # return updated avoregion in the response
#         data = schema.dump(update_region)

#         return data, 200

#     # Otherwise, nope, didn't find that avoregion
#     else:
#         abort(404, f"Region is not found for Id: {regionid}")


# def delete(regionid):
#     """
#     This function deletes a avoregion from the regions structure
#     :param regionid:   Id of the avoregion to delete
#     :return:            200 on successful delete, 404 if not found
#     """
#     # Get the avoregion requested
#     avoregion = Region.query.filter(Region.regionid == regionid).one_or_none()

#     # Did we find a avoregion?
#     if avoregion is not None:
#         db.session.delete(avoregion)
#         db.session.commit()
#         return make_response(f"Region {regionid} deleted", 200)

#     # Otherwise, nope, didn't find that avoregion
#     else:
#         abort(404, f"Region not found for Id: {regionid}")