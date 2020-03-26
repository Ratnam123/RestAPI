#This is main class were all the application logic takes place

from flask import Blueprint, Response, request

coMakeIT_routes_blueprint = Blueprint('coMakeIT_routes', __name__)

@coMakeIT_routes_blueprint.route('/api/addition', methods=['POST','GET'])
def addition():
    try:
        val1 = request.args.get('val1')
        val2 = request.args.get('val2')
        res = int(val1) + int(val2)
        response_data = "Sum of the given two values is %s" %res
        return Response(response_data, status=200)
    except ValueError:
        response_data = "Didn't get proper values"
        return REsponse(response_data, status=400)
    

