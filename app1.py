from flask import Flask, jsonify
import requests

API_KEY = "717db72625d5422785e06b65284b0983"

url = f"https://newsapi.org/v2/everything?q=tesla&from=2026-04-25&sortBy=publishedAt&apiKey={API_KEY}"

app = Flask(__name__)

@app.route('/api/news', methods=['GET'])
def get_news():

    response = requests.get(url)

    if response.status_code == 200:

        news_data = response.json()

        articles = news_data.get('articles', [])

        if len(articles) == 0:
            return jsonify({"msg": "No articles found"})

        total_articles = len(articles)

        first_article = articles[0]

        output_data = {
            "Total Article Count": total_articles,
            "Title": first_article.get('title'),
            "Author": first_article.get('author'),
            "Published Date": first_article.get('publishedAt')
        }

        return jsonify(output_data)

    else:
        return jsonify({"msg": "Invalid API Key or API Error"})


if __name__ == '__main__':
    app.run(debug=True)