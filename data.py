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
    for i in unique:
        if i['name']==name:
            return jsonify({"msg":"error name alreafy exist"})
    new={"name":name,


    "age":age,
    "gender":gender,
    "city":city}
    unique.append(new)
    return jsonify({"msg":"success","msg":new})
if __name__=="_main__":
    app.run(debug=True)




