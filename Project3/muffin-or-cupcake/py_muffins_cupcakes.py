import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression

# model_info = pickle.load( open( "pkl_muffins_cupcakes.p", "rb" ), encoding='latin1' )
# mc_model = model_info['muffin_cupcake_model']
#clf = LogisticRegression(C=0.1)
df=pd.read_pickle('Flask_Churn.pkl')
df1=df.filter(['Churn_Yes','tenure','SeniorCitizen_Yes','InternetService_Fiber optic','Contract_Two year','PaymentMethod_Electronic check','MonthlyCharges','PaperlessBilling_Yes','OnlineSecurity_Yes'],axis=1)
X_train=df1.iloc[:,1:]
y_train = df1.iloc[:,0]
clf = LogisticRegression(C=0.1)
clf.fit(X_train,y_train)

#Index(['Churn_Yes', 'tenure', 'MonthlyCharges', 'gender_Male',
 #      'SeniorCitizen_Yes', 'Partner_Yes', 'Dependents_Yes',
  #     'PhoneService_Yes', 'MultipleLines_Yes', 'InternetService_Fiber optic',
   #    'InternetService_No', 'OnlineSecurity_Yes', 'OnlineBackup_Yes',
  #     'DeviceProtection_Yes', 'TechSupport_Yes', 'StreamingTV_Yes',
   #    'StreamingMovies_Yes', 'Contract_One year', 'Contract_Two year',
   #    'PaperlessBilling_Yes', 'PaymentMethod_Credit card (automatic)',
  #     'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check'],
   #   dtype='object')

def customer_churn(tenure, SeniorCitizen_Yes, InternetService_Fiber_optic,
                        Contract_Two_year, PaymentMethod_Electronic_check, MonthlyCharges,
                        PaperlessBilling_Yes, OnlineSecurity_Yes, mc_model=clf):
    
 #   total = 16 * flour_cups_float + \
  #          16 * milk_cups_float + \
   #         16 * sugar_cups_float + \
    #        16 * butter_cups_float + \
     #       3 * eggs_num_float + \
      #      .33 * bp_tsp_float + \
       #     .33 * vanilla_tsp_float + \
        #    .33 * salt_tsp_float

#    flour_cups_prop = 16 * flour_cups_float * 100.0 / total
 #   milk_cups_prop = 16 * milk_cups_float * 100.0 / total
 #   sugar_cups_prop = 16 * sugar_cups_float * 100.0 / total
  #  butter_cups_prop = 16 * butter_cups_float * 100.0 / total
   # eggs_num_prop = 3 * eggs_num_float * 100.0 / total
#    bp_tsp_prop = .33 * bp_tsp_float * 100.0 / total
 #   vanilla_tsp_prop = .33 * vanilla_tsp_float * 100.0 / total
  #  salt_tsp_prop = .33 * salt_tsp_float * 100.0 / total

    input_df = pd.DataFrame({'Tenure': tenure,
                          'Senior Citizen': SeniorCitizen_Yes,      
                         'InternetService_FiberOptic': InternetService_Fiber_optic,
                          'Contract_TwoYear': Contract_Two_year,
                          'PaymentMethod_ElectronicCheck': PaymentMethod_Electronic_check,
                          'MonthlyCharges': MonthlyCharges,
                          'PaperlessBilling_Yes': PaperlessBilling_Yes,
                          'OnlineSecurity_Yes' : OnlineSecurity_Yes
                                
                                },index=[0])

  #  input_df = pd.DataFrame({'Flour': flour_cups_prop,
                            # 'Sugar': sugar_cups_prop}, index=[0])
                             #'Milk': milk_cups_prop,
                             #'Butter': butter_cups_prop,
                             #'Eggs': eggs_num_prop,
                             #'Baking Powder': bp_tsp_prop,
                             #'Vanilla': vanilla_tsp_prop
                             #'Salt': salt_tsp_prop

    prediction = clf.predict_proba(input_df)[0]
    prediction_str=str(round(clf.predict_proba(input_df)[0][1],4)*100)
    

    message_array = ["Probability of getting churn is " + prediction_str + "%"]
                   

    return message_array