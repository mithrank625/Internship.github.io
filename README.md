# Internship Finder

The **Internship Finder** is a web application that helps users search and filter internship opportunities. This project uses **Python**, **HTML**, and **CSS**, and integrates the **Adzuna API** to gather real-time job listings.

## Features
- **Keyword-based internship search**: Search for internships based on specific keywords (e.g., role, skills, etc.).
- **Location filtering**: Filter internships by location (e.g., city, country).
- **Real-time data from the Adzuna API**: Fetch up-to-date job listings directly from the Adzuna API.
- **Essential details**: Display key information such as job title, company name, location, and more.

## Technologies Used
- **Python**: Handles backend logic and API interaction.
- **Flask**: Web framework for routing, templating, and rendering.
- **HTML & CSS**: Frontend structure and styling.
- **Adzuna API**: Supplies real-time internship and job listing data.

## Setup

### 1. Clone the Repository

Start by cloning this repository to your local machine:

```bash
git clone https://github.com/yourusername/Internship.github.io.git
cd Internship.github.io
```
### 2. Install Dependencies

Make sure you have all the required dependencies installed. This project uses pip for dependency management. Install them by running the following command:
```bash
pip install -r requirements.txt
pip install flask
```
### 3. Environment Variables

You need to configure the Adzuna API credentials to fetch real-time internship data. Follow these steps:
   1. Create a .env file in the root directory of your project and add your credentials like this:
      ```bash
      ADZUNA_APP_ID=your_app_id
      ADZUNA_API_KEY=your_api_key
      ```
Replace your_app_id and your_api_key with the actual key and id you got from your Adzuna account
### 4. Run the Code

After setting everything up, run the application with the following command:

   ```bash
      python app.py
   ```
## Usage
1.**Search for Internships**:  Enter a keyword or job title (e.g., "Software Developer") in the search bar.
2. **Filter by Location**: Optionally, select a location to filter the results by (e.g., city, state, or country).
3. **View Internship Details**: A list of internships will appear, displaying key details such as job title, company name, and Location
4. **Access the Web Application**: Once the application is running, you can interact with it directly through your browser at http://localhost:5000
