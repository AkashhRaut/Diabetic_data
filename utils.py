import numpy as np
import pickle

class DiabeticInfo():
    def __init__(self,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
        self.Glucose = Glucose
        self.BloodPressure = BloodPressure
        self.SkinThickness = SkinThickness
        self.Insulin = Insulin
        self.BMI = BMI
        self.DiabetesPedigreeFunction = DiabetesPedigreeFunction
        self.Age = Age

    def load_data(self):
        with open('logistic_clf.pkl','rb') as f:
            self.model = pickle.load(f)

    def diabetic_pred(self):
        self.load_data()

        test_array = np.zeros([1,self.model.n_features_in_])
        
        test_array[0,0]=self.Glucose
        test_array[0,1]=self.BloodPressure
        test_array[0,2]=self.SkinThickness
        test_array[0,3]=self.Insulin
        test_array[0,4]=self.BMI
        test_array[0,5]=self.DiabetesPedigreeFunction
        test_array[0,6]=self.Age

        prediction = self.model.predict(test_array)[0]

        return prediction
