from flask_restful import Resource, reqparse
from flask import Request, session
from JSONpredict import *
def model_predict(img_path):
    data = uploadedData(img_path, csvbool = True)
    sr = data[0]

    data = data[1:]
    size = len(data)
    if size > 9001:
        size = 9001
        data = data[:size]
    div = size // 1000
    data, peaks = preprocess(data, config)
    return predictByPart(data, peaks)

class dataAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('data', required=True, help='Raw Data is required')
    '''
    {
        "data":[0,0,0,0]
    }
    '''
    def post(self):
        arg = self.parser.parse_args()
        data = arg["data"]


        return {"success": False}