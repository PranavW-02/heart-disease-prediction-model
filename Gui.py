from tkinter import *
import joblib

model = joblib.load("HeartDiseaseModel.sav")

root = Tk()
root.title("main screen")
root.geometry("800x500")
# title = Label(root,text="Heart Disease Prediction ",fg="white",bg="blue", width="300", height="2", font=("Calibri", 20))
# title.grid(row=0,column=0)

def Predict():
    ans = model.predict([[float(Pregnancies.get()),float(Glucose.get()),float(BloodPressure.get()),float(SkinThickness.get()),float(Insulin.get()),float(BMI.get()),float(DPF.get()),float(Age.get())]])
    if ans == 1:
        ans = "Heart Disease"
    else:
        ans = "No"
    Result = Label(root,text=ans,fg="blue", width="10", height="2", font=("Calibri", 20))
    Result.grid(row=9,column=3)


Pregnancie_label = Label(root,text="Pregnancies",fg="blue", width="10", height="2", font=("Calibri", 20))
Pregnancie_label.grid(row=1,column=1)
Pregnancies = Entry(root)
Pregnancies.grid(row=2,column=1)

Glucose_label = Label(root,text="Glucose",fg="blue", width="10", height="2", font=("Calibri", 20))
Glucose_label.grid(row=1,column=2)
Glucose = Entry(root)
Glucose.grid(row=2,column=2)

BloodPressure_label = Label(root,text="BP",fg="blue", width="10", height="2", font=("Calibri", 20))
BloodPressure_label.grid(row=1,column=3)
BloodPressure = Entry(root)
BloodPressure.grid(row=2,column=3)

SkinThickness_label = Label(root,text="SkinThickness",fg="blue", width="12", height="2", font=("Calibri", 20))
SkinThickness_label.grid(row=1,column=4)
SkinThickness = Entry(root)
SkinThickness.grid(row=2,column=4)

Insulin_label = Label(root,text="Insulin",fg="blue", width="10", height="2", font=("Calibri", 20))
Insulin_label.grid(row=3,column=1)
Insulin = Entry(root)
Insulin.grid(row=4,column=1)

BMI_label = Label(root,text="BMI",fg="blue", width="10", height="2", font=("Calibri", 20))
BMI_label.grid(row=3,column=2)
BMI = Entry(root)
BMI.grid(row=4,column=2)

DPF_label = Label(root,text="DPF",fg="blue", width="10", height="2", font=("Calibri", 20))
DPF_label.grid(row=3,column=3)
DPF = Entry(root)
DPF.grid(row=4,column=3)

Age_label = Label(root,text="Age",fg="blue", width="12", height="2", font=("Calibri", 20))
Age_label.grid(row=3,column=4)
Age = Entry(root)
Age.grid(row=4,column=4)

Gap = Label(root,text="")
Gap.grid(row=5,column=1)

Gap = Label(root,text="")
Gap.grid(row=6,column=1)

predictbtn = Button(root,text="Predict Result",height="1",width="15",fg='white',bg='blue' ,font=("Arial Bold",20),command= Predict)
predictbtn.grid(row=7,column=3,padx=10)

root.mainloop()