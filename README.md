# 🛒 E-Commerce Web Scraper 

A Flask-based web application that scrapes product information from an e-commerce website and displays it in a styled web table.  
The application also allows users to download the scraped data as a CSV file.

This project combines backend web scraping with a clean frontend interface.

---

##  Features

-  Scrapes product name, price, and rating
-  Displays data in browser using Flask
-  Styled table using CSS
-  Download scraped data as CSV file
-  Basic error handling
-  Clean project structure

---

## Technologies Used

- Python
- Flask
- BeautifulSoup
- Requests
- Pandas
- HTML
- CSS

---

##  Project Structure

web-scraper/
│
├── app.py
├── scraper.py
├── static/
│   └── style.css
└── templates/
    └── index.html

---

## How to Run the Project

1. Make sure Python is installed.
2. Clone the repository:

git clone https://github.com/your-username/your-repository-name.git

3. Navigate into the project folder:

cd web-scraper

4. Install required libraries:

pip install flask requests beautifulsoup4 pandas

5. Run the application:

python app.py

6. Open in browser:

http://127.0.0.1:5000/

---

##  How It Works

1. The application sends a request to the target website.
2. BeautifulSoup parses the HTML content.
3. Product details (name, price, rating) are extracted.
4. Data is stored in a Pandas DataFrame.
5. The data is displayed in a styled table.
6. Users can download the data as products.csv.

---

##  Output

- Styled product table displayed in browser
- Downloadable products.csv file

---

##  Learning Outcomes

Through this project, I improved my understanding of:

- Web scraping fundamentals
- HTML parsing using BeautifulSoup
- Flask routing and template rendering
- Backend and frontend integration
- CSV file generation

---

##  Internship Task

This project was developed as part of my Software Development Internship to strengthen my practical web development and scraping skills.

---

