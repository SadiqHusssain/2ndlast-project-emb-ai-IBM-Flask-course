from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    text_to_analyze = request.args.get("textToAnalyze")
    result = sentiment_analyzer(text_to_analyze)
    if result["label"] is None:
        return "Invalid input ! Try Agian"
    return f"The given text has been identified as {result['label'].split('_')[1]} with a score of {result['score']}."

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
