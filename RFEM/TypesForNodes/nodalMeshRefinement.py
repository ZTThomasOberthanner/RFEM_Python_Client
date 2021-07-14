from RFEM.initModel import *
from RFEM.enums import SetType

class NodalMeshRefinement():
    def __init__(self,
                 no: int = 1,
                 comment: str = '',
                 params: dict = {}):

        # Client model | Nodal Mesh Refinement
        clientObject = clientModel.factory.create('ns0:nodal_mesh_refinement')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Nodal Mesh Refinement No.
        clientObject.no = no

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Nodal Mesh Refinement to client model
        clientModel.service.set_nodal_mesh_refinement(clientObject)