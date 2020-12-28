from flask import Flask,jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({'status':'success','message':"Hello World... run successfully"})

@app.route('/healthcheck')
def healthcheck():
    return jsonify({'status':'success','message':"service run successfully"})
if __name__=='__main__':
	app.debug = True
	app.run()
