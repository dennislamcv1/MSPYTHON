from flask import Flask
from flask import render_template
from data import calc_data

app = Flask(__name__)

@app.route('/')
def home():
    avg_churn_prob, high_risk_customers, churn_rate_by_state, high_risk_by_state = calc_data()
    return render_template("index.html", 
                           avg_churn_prob=avg_churn_prob, 
                           high_risk_customers=high_risk_customers, 
                           churn_rate_by_state=churn_rate_by_state.to_dict(orient='records'), 
                           high_risk_by_state=high_risk_by_state.to_dict(orient='records')
                           )
if __name__ == "__main__":
    app.run(debug=True)