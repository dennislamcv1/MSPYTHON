# Step 3.1: Fetch HTML Content
# Please be careful to follow instructions on how to run the program; 
# the Run menu or right-click > Run options do not work in the simulated environment. 
# Ensure you have run the terminal command to install the correct libraries using pip.
# You must use the terminal window as directed in Step 3.
### YOUR CODE HERE ###

from bs4 import BeautifulSoup


# Step 3.2: Extract the Required Data
### YOUR CODE HERE ###

# Specify the path to your local HTML file
file_path = "baseball_stats.html"

# Open and read the file
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

# Parse the HTML content
soup = BeautifulSoup(content, "html.parser")

# Find the table in the HTML
table = soup.find("table")

# Extract table headers
headers = [th.get_text(strip=True) for th in table.find_all("th")]

# Extract table rows
rows = []
for row in table.find_all("tr")[1:]:  # Skip header row
    row_data = [td.get_text(strip=True) for td in row.find_all("td")]
    rows.append(row_data)



# Step 4.1: Convert to a DataFrame
# Import pandas
### YOUR CODE HERE ###
import pandas as pd
# Convert the game data into a pandas DataFrame
### YOUR CODE HERE ###
df = pd.DataFrame(rows, columns=headers)
# Inspect the DataFrame
### YOUR CODE HERE ###
df
# Save and print the shaped data
### YOUR CODE HERE ###
print(df)
# Step 5.1: Save to a CSV File
# Save the DataFrame to a CSV file named sports_statistics.csv
### YOUR CODE HERE ###
df.to_csv("sports_statistics.csv", index=False)