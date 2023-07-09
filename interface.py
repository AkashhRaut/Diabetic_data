from flask import Flask,request,render_template
from utils import DiabeticInfo

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def diabetes():

        data = request.form
        print('Data:',data)

        Glucose                  = data['Glucose']
        BloodPressure            = data['BloodPressure']
        SkinThickness            = data['SkinThickness']
        Insulin                  = data['Insulin']
        BMI                      = data['BMI']
        DiabetesPedigreeFunction = data['DiabetesPedigreeFunction']
        Age                      = data['Age']

        Obj = DiabeticInfo(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
        pred = Obj.diabetic_pred()

        if pred == 0:
             result = 'not diabetic'

        else:
             result = 'diabetic'

        return render_template('index.html',prediction=result)
        

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port = 8080)