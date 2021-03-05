import pandas as pd

def store_csv(email,phone_number,feedback):
    df=pd.read_csv("test.csv")
    #df1=df.to_numpy()
    df=df.append(pd.DataFrame([[email,phone_number,feedback]],columns=["Email","Phone_Number","Feedback"]))
    #df=pd.DataFrame([[email,phone_number,feedback]],columns=["Email","Phone_Number","Feedback"])
    df.to_csv("test.csv",index=False)

#store_csv("smith@yahoo.com","21345489008","heeolll")