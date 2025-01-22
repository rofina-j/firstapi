from flask import Flask,request,jsonify
app=Flask(__name__)
@app.route('/point',methods=['GET'])
def get_data():
    return jsonify({"msg":"this is my first",
                    "data":"one"})
if __name__=='__main__':
    app.run(debug=True)