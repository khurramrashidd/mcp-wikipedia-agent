from flask import Flask, request, render_template, jsonify
import wikipediaapi
import math

app = Flask(__name__)

# Dynamic Wikipedia instance generator for multi-language support
def get_wiki_instance(lang='en'):
    return wikipediaapi.Wikipedia(
        language=lang,
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent="mcp-agent-ibtidaa/2.0 (khurram@example.com)"
    )

# 🔌 MCP Tool Function (Enhanced)
def get_wikipedia_summary(query: str, lang: str = 'en'):
    wiki = get_wiki_instance(lang)
    page = wiki.page(query)

    if not page.exists():
        return {"error": f"No data found for '{query}' in the selected language."}

    # Extract clean text and calculate analytics
    summary_text = page.summary[:2000] # Expanded summary length
    word_count = len(summary_text.split())
    reading_time = max(1, math.ceil(word_count / 238)) # Avg reading speed

    # Extract a few clean category names (removing 'Category:' prefix)
    raw_categories = list(page.categories.keys())[:4]
    clean_categories = [cat.replace("Category:", "") for cat in raw_categories]

    return {
        "title": page.title,
        "summary": summary_text,
        "url": page.fullurl,
        "word_count": word_count,
        "reading_time": reading_time,
        "categories": clean_categories,
        "language": lang
    }

# 🏠 UI Home
@app.route("/")
def home():
    return render_template("index.html")

# 🔍 UI Search Route
@app.route("/search")
def search():
    query = request.args.get("query", "").strip()
    lang = request.args.get("lang", "en")
    
    if not query:
        return render_template("index.html", error="Please enter a search term.")

    result = get_wikipedia_summary(query, lang)

    if "error" in result:
        return render_template("index.html", error=result["error"])

    return render_template("result.html", result=result)

# 🔌 MCP API Endpoint (For ADK / Cloud Run consumption)
@app.route("/tool")
def tool():
    query = request.args.get("query")
    lang = request.args.get("lang", "en")
    if not query:
        return jsonify({"error": "Missing 'query' parameter"}), 400
        
    result = get_wikipedia_summary(query, lang)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)