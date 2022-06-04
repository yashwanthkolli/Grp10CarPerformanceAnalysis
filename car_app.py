from flask import Flask,render_template,request
import pickle
app=Flask(__name__)
model=pickle.load(open('Car.pkl','rb'))

@app.route('/')
def hello():
    return render_template("carperf.html")

@app.route('/login',methods=['POST'])
def User():
    a=request.form["cycle"]
    b=request.form["disp"]
    c=request.form["hp"]
    d=request.form["wt"]
    e=request.form["acc"]
    f=request.form["my"]
    s=request.form["s"]
    
    t=[[int(a),int(b),int(c),int(d),int(e),int(f),int(s)]]
    y=model.predict(t)
    
    return render_template("carperf.html",y="The mpg would be "+str(y[0]))

if __name__=='__main__':
    app.run(debug=True)