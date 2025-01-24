from flask import Flask,request,jsonify
app=Flask(__name__)
unique=[]
@app.route('/one',methods=['POST'])
def post_data():

    data=request.get_json()

    
    name=data.get('name')
    age=data.get('age')
    gender=data.get('gender')
    city=data.get('city')

    if not name or not age or not gender or not city:
        return jsonify({"msg":"missing field"})
    
    for i in unique:
        if i['name']==name:
            return jsonify({"msg":"error name alreafy exist"})
    new={"name":name,
         "age":age,
    "gender":gender,
    "city":city}

    unique.append(new)

    return jsonify({"msg":"success","data":new})
@app.route('/one/<string:name>',methods=['DELETE'])
def del_data(name):
    for i ,j in enumerate(unique):
        if j['name']==name:
            ans=unique.pop(i)
        return jsonify({"msg":"name deleted","data":ans})
    return jsonify({"error": "Name not found"})
if __name__=='__main__':
    app.run(debug=True)