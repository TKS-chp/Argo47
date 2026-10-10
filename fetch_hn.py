import requests
import json

def fetch_hn_top():
    # トップ記事のIDリストを最大500件取得できるエンドポイント
    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(top_stories_url)
    story_ids = response.json()
    
    articles = []
    # とりあえず上位5件だけ詳細を取得
    for story_id in story_ids[:5]:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        story_res = requests.get(story_url)
        story_data = story_res.json()
        
        articles.append({
            "title": story_data.get("title"),
            "url": story_data.get("url", f"https://news.ycombinator.com/item?id={story_id}"),
            "score": story_data.get("score") # いいね数みたいなもの
        })
        
    with open("hn_top.json", "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)
        
    print("Hacker Newsのトップ記事を保存したよ！")

if __name__ == "__main__":
    fetch_hn_top()