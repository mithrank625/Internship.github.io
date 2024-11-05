from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

# Your Adzuna API credentials
ADZUNA_APP_ID = '32208980'  # Replace with your actual App ID
ADZUNA_APP_KEY = '54526b78bda2f238faa3c7293820d4f3'  # Replace with your actual App Key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    internship_type = request.form.get('type')  # Get the internship type
    company_name = request.form.get('company')  # Get the company name
    location = request.form.get('location')  # Get the location
    internships = get_internship_listings(internship_type, company_name, location)
    
    # Add company name to the render context to retain user input
    return render_template('results.html', internships=internships, internship_type=internship_type, company_name=company_name, location=location)

def get_internship_listings(internship_type, company_name, location):
    # Define the API endpoint for the first page
    page = 1
    url_template = 'https://api.adzuna.com/v1/api/jobs/us/search/{}'

    internships = []

    # Loop through pages until no more results
    while True:
        url = url_template.format(page)
        params = {
            'app_id': ADZUNA_APP_ID,
            'app_key': ADZUNA_APP_KEY,
            'results_per_page': 10,  # Change to 10 internships per page
            'what': internship_type + ' internship' if internship_type else 'internship',
            'where': location,
            'distance': 100,
            'content-type': 'application/json'
        }
        
        # Fetch data from the API
        response = requests.get(url, params=params)
        if response.status_code != 200:
            break  # Stop if there is an error
        
        try:
            data = response.json()
        except json.JSONDecodeError:
            break  # Stop if the data is not in JSON format
        
        # Stop if there are no more results
        if 'results' not in data or not data['results']:
            break

        # Filter results by company name if provided
        for result in data['results']:
            if company_name:
                if company_name.lower() in result['company']['display_name'].lower():
                    internships.append(result)
            else:
                internships.append(result)

        page += 1

    return internships

if __name__ == '__main__':
    app.run(debug=True)
