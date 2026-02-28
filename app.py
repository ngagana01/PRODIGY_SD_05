from flask import Flask, render_template, send_file
from scraper import scrape_data
import io

app = Flask(__name__)

@app.route("/")
def home():
    df = scrape_data()
    return render_template("index.html", tables=df.to_html(classes="styled-table", index=False))

@app.route("/download")
def download():
    df = scrape_data()
    buffer = io.StringIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)

    return send_file(
        io.BytesIO(buffer.getvalue().encode()),
        mimetype="text/csv",
        as_attachment=True,
        download_name="products.csv"
    )

if __name__ == "__main__":
    app.run(debug=True)