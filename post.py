from flask import Flask,request,jsonify
app=Flask(__name__)
users=[
    {"id":1,"name":"anu","gender":"f","age":24,"city":"chn"},
    {"id":2,"name":"anbu","gender":"m","age":45,"city":"bgl"},
    {"id":3,"name":"anish","gender":"m","age":22,"city":"chn"},
    {"id":4,"name":"anusha","gender":"f","age":33,"city":"bgl"},
    {"id":5,"name":"anil","gender":"m","age":56,"city":"delhi"}
]
@app.route('/one',methods=['GET'])
def get_data():
    minage=int(request.args.get('minage'))
    maxage=int(request.args.get('maxage'))
    count={}
    for i in users:
        if minage <= i["age"] <=maxage:
            city=i["city"]
            if city in count:
                count[city]+=1
            else:
                count[city]=1
    return jsonify(count)
if __name__ == '__main__':
    app.run(debug=True)
