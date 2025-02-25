from RFEM.initModel import Model, clearAtributes, ConvertToDlString
from RFEM.enums import LineType, LineArcAlphaAdjustmentTarget

class Line():
    def __init__(self,
                 no: int = 1,
                 nodes_no: str = '1 2',
                 comment: str = '',
                 params: dict = {}):

        '''
        Args:
            no (int): Line Tag
            nodes_no (str): Nodes Defining Line
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Line
        clientObject = Model.clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Nodes No.
        clientObject.definition_nodes = ConvertToDlString(nodes_no)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line to client model
        Model.clientModel.service.set_line(clientObject)

    def Polyline(self,
                 no: int = 1,
                 nodes_no: str = '1 2',
                 comment: str = '',
                 params: dict = {}):

        '''
        Args:
            no (int): Line Tag
            nodes_no (str): Nodes Defining Polyline
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Line
        clientObject = Model.clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Type
        clientObject.type = LineType.TYPE_POLYLINE.name

        # Nodes No.
        clientObject.definition_nodes = ConvertToDlString(nodes_no)

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line to client model
        Model.clientModel.service.set_line(clientObject)

    def Arc(self,
            no: int = 1,
            nodes_no: str = [1,2],
            control_point: list = [10,0,0], # X,Y,Z
            alpha_adjustment_target = LineArcAlphaAdjustmentTarget.ALPHA_ADJUSTMENT_TARGET_BEGINNING_OF_ARC,
            comment: str = '',
            params: dict = {}):

        '''
        Args:
            no (int): Line Tag
            nodes_no (list): Node Tags Defining Arc
            control_point (list): Control Point for Arc in [X, Y, Z]
            alpha_adjustment_target (enum): Line Arc Alpha Adjustment Target Enumeration
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Line
        clientObject = Model.clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Type
        clientObject.type = LineType.TYPE_ARC.name

        # Nodes No.
        clientObject.definition_nodes = ConvertToDlString(nodes_no)
        clientObject.arc_first_node = nodes_no[0]
        clientObject.arc_second_node = nodes_no[1]
        clientObject.arc_alpha_adjustment_target = alpha_adjustment_target.name
        clientObject.arc_control_point_x = control_point[0]
        clientObject.arc_control_point_y = control_point[1]
        clientObject.arc_control_point_z = control_point[2]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line to client model
        Model.clientModel.service.set_line(clientObject)

    def Circle(self,
                no: int = 1,
                center_of_cirle: list = [20,0,0],
                circle_radius: float = 1.0,
                point_of_normal_to_circle_plane: list = [1,0,0],
                comment: str = '',
                params: dict = {}):

        '''
        Args:
            no (int): Line Tag
            nodes_no (str): Nodes on Line of Circle
            center_of_circle (list): Cartesian Co-Ordinates of Circle Centre [X, Y, Z]
            circle_radius (float): Magnitude of Circle Radius
            point_of_normal_to_circle_plane (list): Vector from Circle Centre to this Point [X, Y, Z] defines Vector Normal to Circle Plane
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Line
        clientObject = Model.clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Type
        clientObject.type = LineType.TYPE_CIRCLE.name

        # Center of circle
        clientObject.circle_center_coordinate_1 = center_of_cirle[0]
        clientObject.circle_center_coordinate_2 = center_of_cirle[1]
        clientObject.circle_center_coordinate_3 = center_of_cirle[2]

        clientObject.circle_radius = circle_radius

        # Point of normal to circle plane
        clientObject.circle_normal_coordinate_1 = point_of_normal_to_circle_plane[0]
        clientObject.circle_normal_coordinate_2 = point_of_normal_to_circle_plane[1]
        clientObject.circle_normal_coordinate_3 = point_of_normal_to_circle_plane[2]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line to client model
        Model.clientModel.service.set_line(clientObject)

    def EllipticalArc(self,
                      no: int = 1,
                      p1_control_point: list = [0,-6,0],
                      p2_control_point: list = [20,-6,0],
                      p3_control_point: list = [10,10,3],
                      arc_angle_alpha: float = 0,
                      arc_angle_beta: float = 3.141592653589793,
                      comment: str = '',
                      params: dict = {}):

        '''
        Args:
            no (int): Line Tag
            p1_control_point (list): Control Point 1 [X, Y, Z]
            p2_control_point (list): Control Point 2 [X, Y, Z]
            p3_control_point (list): Control Point 3 [X, Y, Z]
            arc_angle_alpha (float): Alpha Arc Angle (in Radians)
            arc_angle_beta (float): Beta Arc Angle (in Radians)
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Line
        clientObject = Model.clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Type
        clientObject.type = LineType.TYPE_ELLIPTICAL_ARC.name

        # Control points
        clientObject.elliptical_arc_first_control_point_x = p1_control_point[0]
        clientObject.elliptical_arc_first_control_point_y = p1_control_point[1]
        clientObject.elliptical_arc_first_control_point_z = p1_control_point[2]

        clientObject.elliptical_arc_second_control_point_x = p2_control_point[0]
        clientObject.elliptical_arc_second_control_point_y = p2_control_point[1]
        clientObject.elliptical_arc_second_control_point_z = p2_control_point[2]

        clientObject.elliptical_arc_perimeter_control_point_x = p3_control_point[0]
        clientObject.elliptical_arc_perimeter_control_point_y = p3_control_point[1]
        clientObject.elliptical_arc_perimeter_control_point_z = p3_control_point[2]

        clientObject.elliptical_arc_alpha = arc_angle_alpha
        clientObject.elliptical_arc_beta = arc_angle_beta

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line to client model
        Model.clientModel.service.set_line(clientObject)

    def Ellipse(self,
                no: int = 1,
                nodes_no: list = [5,10],
                ellipse_control_point: list = [18,-4.8,0],
                comment: str = '',
                params: dict = {}):

        '''
        Args:
            no (int): Line Tag
            nodes_no (list): Node Tags on Line of Ellipse
            ellipse_control_point (list): Ellipse Control Point [X, Y, Z]
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Line
        clientObject = Model.clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Nodes No.
        clientObject.definition_nodes = ConvertToDlString(nodes_no)
        clientObject.ellipse_first_node = nodes_no[0]
        clientObject.ellipse_second_node = nodes_no[1]

        # Type
        clientObject.type = LineType.TYPE_ELLIPSE.name

        # Control point
        clientObject.ellipse_control_point_x = ellipse_control_point[0]
        clientObject.ellipse_control_point_y = ellipse_control_point[1]
        clientObject.ellipse_control_point_z = ellipse_control_point[2]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line to client model
        Model.clientModel.service.set_line(clientObject)

    def Parabola(self,
                 no: int = 1,
                 nodes_no: str = [3,8],
                 parabola_control_point: list = [10,-3,0],
                 parabola_alpha: float = 0,
                 comment: str = '',
                 params: dict = {}):

        '''
        Args:
            no (int): Line Tag
            nodes_no (list): Node Tags on Line of Parabola
            parabola_control_point (list): Parabola Control Point [X, Y, Z]
            parabola_alpha (float): Alpha Angle (in Radians)
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Line
        clientObject = Model.clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Nodes No.
        clientObject.definition_nodes = ConvertToDlString(nodes_no)
        clientObject.parabola_first_node = nodes_no[0]
        clientObject.parabola_second_node = nodes_no[1]

        clientObject.parabola_alpha = parabola_alpha

        # Type
        clientObject.type = LineType.TYPE_PARABOLA.name

        # Control point
        clientObject.parabola_control_point_x = parabola_control_point[0]
        clientObject.parabola_control_point_y = parabola_control_point[1]
        clientObject.parabola_control_point_z = parabola_control_point[2]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line to client model
        Model.clientModel.service.set_line(clientObject)

    def Spline(self,
               no: int = 1,
               nodes_no: str = '1 3 5',
               comment: str = '',
               params: dict = {}):

        '''
        Args:
            no (int): Line Tag
            nodes_no (str): Node Tags on Line of Spline
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Line
        clientObject = Model.clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Nodes No.
        clientObject.definition_nodes = ConvertToDlString(nodes_no)

        # Type
        clientObject.type = LineType.TYPE_SPLINE.name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line to client model
        Model.clientModel.service.set_line(clientObject)

    def NURBS(self,
              no: int = 1,
              nodes_no: str = '1 2',
              control_points: list = [[0,0,0],[2.33,0,-3,4],[10,0,-11],[17.66,0,-3.4],[20,0,0]],
              weights = [1,1,1,1,1],
              comment: str = '',
              params: dict = {}):

        '''
        Args:
            no (int): Line Tag
            nodes_no (str): Node Tags on Line of NURBS Curve
            control_points (list): Nested List of Respective Control Point's Cartesian Co-Ordinates
            weights (list): Weights of Control Points
            comment (str, optional): Comments
            params (dict, optional): Parameters
        '''

        # Client model | Line
        clientObject = Model.clientModel.factory.create('ns0:line')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Nodes No.
        clientObject.definition_nodes = ConvertToDlString(nodes_no)

        # Type
        clientObject.type = LineType.TYPE_NURBS.name

        if len(control_points) != len(weights):
            print("WARNING: The number of weigths prescribed must equal the number of control points defined.")

        '''
        TODO: bug 24721
        nurbs_control_points = []
        for i,j in enumerate(control_points):
            point = Model.clientModel.factory.create('ns0:line_nurbs_control_points_by_components')
            point.no = i+1
            point.global_coordinate_x = control_points[i][0]
            point.global_coordinate_y = control_points[i][1]
            point.global_coordinate_z = control_points[i][2]
            point.weight = weights[i]
            nurbs_control_points.append(point)
        #clientObject.nurbs_control_points_by_components = Model.clientModel.factory.create('ns0:line_nurbs_control_points_by_components')
        '''
        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Line to client model
        Model.clientModel.service.set_line(clientObject)
