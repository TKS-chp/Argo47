import feedparser
import json

def fetch_zenn_trend():
    # ZennのトレンドRSSのURL
    url = "https://zenn.dev/feed" 
    
    # RSSをパース
    feed = feedparser.parse(url)
    
    articles = []
    # 最新の5件だけ取得
    for entry in feed.entries[:5]:
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published
        })
    
    # JSONとして保存（後でフロントエンドから読み込む用）
    with open("zenn_trend.json", "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)
        
    print("Zennのトレンドを保存したよ！")

if __name__ == "__main__":
    fetch_zenn_trend()