from flask import Flask,request,jsonify
app=Flask(__name__)
@app.route('/point',methods=['GET'])
def get_data():
    return jsonify({"msg":"this is my first",
                    "data":"one"})
@app.route('/point',methods=['POST'])
def post_data():
    data=request.get_json()
    return jsonify({"msg":"data received",
                   "data":data})
if __name__=='__main__':
    app.run(debug=True)