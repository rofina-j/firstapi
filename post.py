from flask import Flask,request,jsonify
app=Flask(__name__)
users=[
    {"id":"1","name":"anu","gender":"f"},
    {"id":"2","name":"anbu","gender":"m"},
    {"id":"3","name":"anish","gender":"m"},
    {"id":"4","name":"anusha","gender":"f"},
    {"id":"5","name":"anil","gender":"m"},
]
@app.route('/one',methods=['GET'])
def get_data():
    gender=request.args.get('gender')
    c=0
    for i in users:
        if i['gender']==gender:
            c+=1
    return jsonify({"gender": gender, "count": c})
if __name__ == '__main__':
    app.run(debug=True)
