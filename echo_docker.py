import flask
app = flask.Flask(__name__)

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    data = {'success': False}
    
    params = flask.request.json
    if params == None:
        params = flask.request.args
        
    if params != None:
        data['response'] = params.get('msg')
        data['success'] = True
        
    return flask.jsonify(data)

app.run(host='0.0.0.0', port=80)
