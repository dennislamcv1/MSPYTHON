from flask import Flask, render_template
import requests

app = Flask(__name__)

# Step 2: Replace with your actual API key
api_key = 'YOUR_API_KEY'
headers = {'X-Auth-Token': api_key}
url = "http://api.football-data.org/v4/matches"

# Function to fetch scores (similar to your previous project)
def fetch_scores():
    """
    Fetch live football match scores from the API.

    Returns:
        list: A list of dictionaries containing match data for the top 5 matches.
              Returns an empty list if no matches are found.
        str: An error message if an exception occurs during the API request.
    """
    response = requests.get(url, headers=headers)
    try:
        data = response.json()
        if 'matches' in data and len(data['matches']) > 0:
            matches = data['matches'][:5]  # Display top 5 matches for brevity
            return matches
        else:
            return []  # Return an empty list if no matches
    except Exception as e:
        return f"Error fetching data: {e}"

# STEP 3: YOUR CODE HERE
def load_index_page():
    """
    Flask route for the main page.

    Renders the index.html template.

    Returns:
        str: Rendered HTML content of the index page.
    """
    # STEP 4: YOUR CODE HERE

# STEP 5: YOUR CODE HERE
def load_scores_page():
    """
    Flask route for the scores page.

    Renders the scores.html template with the current live scores.

    Returns:
        str: Rendered HTML content of the scores page.
    """
    # Initial score fetch
    live_scores = fetch_scores()

    # STEP 6: YOUR CODE HERE

if __name__ == '__main__':
    app.run(debug=True)