from flask import Flask, request, render_template
#from py_muffins_cupcakes import customer_churn
import py_muffins_cupcakes

app = Flask(__name__)

@app.route('/')
def entry_page():
    return render_template('index.html')

@app.route('/predict_Churn_proba/', methods=['GET', 'POST'])
def render_message():

    tenure = request.form['Tenure']
    try:
        tenure_int = int(tenure)
    except:
        message = "The amount of tenure must be in numbers."
        return render_template('index.html',
                               message=message)

    Senior_Citizen = request.form['Senior Citizen']
    try:
        sencit_int = int(Senior_Citizen)
    except:
        message = "Senior citizen 1 if yes, otherwise 0."
        return render_template('index.html',
                               message=message)

    isfiber = request.form['InternetService_FiberOptic']
    try:
        isfiber_int = int(isfiber)
    except:
        message = "InternetService_FO must be 1 if yes, otherwise 0."
        return render_template('index.html',
                               message=message)

    contract_two = request.form['Contract_TwoYear']
    try:
        contract_two_int = int(contract_two)
    except:
        message = "Contract two years must be 1 if yes, otherwise 0."
        return render_template('index.html',
                               message=message)


    pm_ec = request.form['PaymentMethod_ElectronicCheck']
    try:
        pm_ec_int = int(pm_ec)
    except:
        message = "PaymentMethod_ElectronicCheck must be 1 if yes, otherwise 0."
        return render_template('index.html',
                               message=message)
    
    mc = request.form['MonthlyCharges']
    try:
        mc_float = float(mc)
    except:
        message = "MonthlyCharges must enter in numbers."
        return render_template('index.html',
                               message=message)

    plessBilling = request.form['PaperlessBilling_Yes']
    try:
        plessBilling_int = int(plessBilling)
    except:
        message = "PaperlessBilling_Yes must be 1 if yes, otherwise 0."
        return render_template('index.html',
                               message=message)

    ols = request.form['OnlineSecurity_Yes']
    try:
        ols_int = int(ols)
    except:
        message = "OnlineSecurity_Yes must be 1 if yes, otherwise 0."
        return render_template('index.html',
                               message=message)

    message = py_muffins_cupcakes.customer_churn(tenure_int,
                            sencit_int,
                            isfiber,
                            contract_two_int,
                            pm_ec_int,
                            mc_float,
                            plessBilling_int,
                            ols_int)

    return render_template('index.html',
                           message=message)


if __name__ == '__main__':
    app.run(debug=True)