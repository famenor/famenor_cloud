import flask
app = flask.Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def predict():
    data = {'success': False}
    
    params = flask.request.json
    if params is None:
        params = flask.request.args
        
    if 'msg' in params.keys():
        data['response'] = params.get('msg')
        data['success'] = True
        
    return flask.jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')