# Create a simple Flask Application
from flask import Flask,render_template,request,redirect,url_for


## Create the flask app
app=Flask(__name__)                     

@app.route('/')
def home():
    return "<h1> Hello to the World of Flask </h1>"       #h1 is html tags

@app.route('/welcome')                        #redirecting to the 2nd page welcome
def welcome():
    return "Hello to the Flask tutorials" 

@app.route('/index')
def index():
    return render_template('index.html')



#Marks Page Use Case
@app.route('/success/<int:score>')
def success(score):
    return "The person is passed and Score is:"+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person is failed and Score is:"+str(score)


@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
      return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3

        result=""
        if average_marks>=50:
            result="success"

        else:
            result="fail"

       # return redirect(url_for(result,score=average_marks))


        return render_template('result.html',results=average_marks)
        
    







if __name__=='__main__':                           #--> Entry point of the program becoz (__name__)
    app.run(debug=True)



