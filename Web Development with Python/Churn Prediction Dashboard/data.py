from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import pandas as pd


def calc_data():
    # Load customer data
    customer_data = pd.read_csv("customer_data.csv")

    # Display the first few rows of the dataset
    print(customer_data.head())

    # Fill missing values and encode categorical columns
    ### YOUR CODE HERE ### Step 1.4

    state_encoder = LabelEncoder()
    ### YOUR CODE HERE ### Step 1.5

    # Scale numerical columns
    scaler = StandardScaler()
    ### YOUR CODE HERE ### Step 1.6

    print(customer_data.head())

    # Split the data into features and target
    x = customer_data[['tenure', 'monthly_charges', 'encoded_state']]
    y = customer_data['churn']

    # Split into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Train the logistic regression model
    model = LogisticRegression()
    ### YOUR CODE HERE ### Step 2.1

    # Make predictions
    ### YOUR CODE HERE ### Step 2.2

    # Evaluate the model
    print(f"Model Accuracy: {accuracy_score(y_test, y_pred)}")

    # Calculate average churn probability
    churn_probabilities = model.predict_proba(x_test)[:, 1]
    ### YOUR CODE HERE ### Step 3.1

    # Identify high-risk customers (e.g., those with a churn probability above a threshold)
    ### YOUR CODE HERE ### Step 3.2

    # Create lists to store churn rates and high-risk counts by state
    churn_rate_by_state = []
    high_risk_by_state = []

    # Group by state and calculate churn rate and high-risk count
    for state, group in customer_data.groupby('state'):
        # Calculate the churn for the state
        churn_rate, high_risk_count = calculate_churn_and_high_risk(group['churn'], avg_churn_prob)
        # Append the state and churn rate to the list
        churn_rate_by_state.append({'state': state, 'churn_rate': churn_rate})
        # Append the state and high risk count to the list
        high_risk_by_state.append({'state': state, 'high_risk': high_risk_count})

    # Convert lists to DataFrames
    churn_rate_by_state_df = pd.DataFrame(churn_rate_by_state)
    high_risk_by_state_df = pd.DataFrame(high_risk_by_state)

    # Store the results in a text file for autograding. Do not modify this code.
    with open('churn_results.txt', 'w') as f:
        f.write("Do not modify this file. It is used for autograding the processed data from the lab.\n\n")
        f.write(f"Average Churn Probability: {avg_churn_prob}\n\n")
        f.write(f"High-Risk Customers: {high_risk_customers}\n\n")
        f.write(f"Churn Rate by State:\n {churn_rate_by_state_df}\n\n")
        f.write(f"High-Risk Customers by State:\n {high_risk_by_state_df}")

    return avg_churn_prob, high_risk_customers, churn_rate_by_state_df, high_risk_by_state_df

def calculate_churn_and_high_risk(churn_series, avg_churn_prob):
    """Calculate churn rate and count high-risk customers."""
    ### YOUR CODE HERE ### Step 3.3

    high_risk_mask = (churn_series > avg_churn_prob)

    ### YOUR CODE HERE ### Step 3.4

    return churn_rate, high_risk_count

if __name__ == "__main__":
    calc_data()