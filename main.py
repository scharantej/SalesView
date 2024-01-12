 
# Import necessary libraries
from flask import Flask, render_template, request
import pandas as pd
import pybigquery

# Initialize the Flask app
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')

# Define the route for the customers page
@app.route('/customers')
def customers():
    # Fetch the top customers' data from BigQuery
    client = pybigquery.Client()
    query = """
        SELECT
            CustomerName,
            Revenue
        FROM
            `bigquery-public-data.samples.shakespeare`
        ORDER BY
            Revenue DESC
        LIMIT 10;
    """
    df = client.query(query).to_dataframe()

    # Render the customers.html template, passing the customers' data
    return render_template('customers.html', customers=df.to_dict('records'))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
