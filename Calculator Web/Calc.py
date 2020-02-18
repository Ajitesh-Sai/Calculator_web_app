from flask import Flask,render_template,request
import CalcBackend

app=Flask(__name__)

@app.route("/",methods=["GET","POST"]) #allows GET requests by defult
def home():
    if request.method == "GET":
        return render_template("index.html")
    if request.method=="POST":
        text1 = request.form.get('textbox1')
        text2 = request.form.get('textbox2')
        if request.form['btn']=='+' :
            return render_template("index.html",output = CalcBackend.add(float(text1),float(text2)),user_text1 = text1, user_text2 = text2)
        if request.form['btn']=='-' :
            return render_template("index.html",output = CalcBackend.sub(float(text1),float(text2)),user_text1 = text1, user_text2 = text2)
        if request.form['btn']=='*' :
            return render_template("index.html",output = CalcBackend.mult(float(text1),float(text2)),user_text1 = text1, user_text2 = text2)
        if request.form['btn']=='/' :
            return render_template("index.html",output = CalcBackend.div(float(text1),float(text2)),user_text1 = text1, user_text2 = text2)
        if request.form['btn']=='%' :
            return render_template("index.html",output = CalcBackend.mod(float(text1),float(text2)),user_text1 = text1, user_text2 = text2)
        if request.form['btn']=='^' :
            return render_template("index.html",output = CalcBackend.exp(float(text1),float(text2)),user_text1 = text1, user_text2 = text2)
if __name__=="__main__":
    app.run()