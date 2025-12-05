import requests
import sqlite3
import time

def get_wikipedia_image(cricketer_name):
    """Fetch the main image from Wikipedia for a cricketer"""
    try:
        # Wikipedia API endpoint
        url = "https://en.wikipedia.org/w/api.php"
        
        # Add user agent to avoid blocking
        headers = {
            'User-Agent': 'CricketLegendsApp/1.0 (Educational Project)'
        }
        
        # Parameters to get page info and main image
        params = {
            "action": "query",
            "titles": cricketer_name,
            "prop": "pageimages",
            "format": "json",
            "pithumbsize": 400,
            "pilicense": "any"
        }
        
        response = requests.get(url, params=params, headers=headers, timeout=10)
        
        if response.status_code != 200:
            print(f"⚠️  {cricketer_name}: HTTP {response.status_code}")
            return None
            
        data = response.json()
        
        # Extract image URL
        pages = data.get("query", {}).get("pages", {})
        for page_id, page_data in pages.items():
            if "thumbnail" in page_data:
                image_url = page_data["thumbnail"]["source"]
                print(f"✅ {cricketer_name}")
                print(f"   {image_url}")
                return image_url
            else:
                print(f"⚠️  {cricketer_name}: No image in Wikipedia")
                return None
                
    except Exception as e:
        print(f"❌ {cricketer_name}: {str(e)[:50]}")
        return None

# Connect to database
conn = sqlite3.connect('cricketers.db')
c = conn.cursor()

# Get first 10 cricketers
c.execute("SELECT name FROM cricketers ORDER BY id LIMIT 10")
cricketers = c.fetchall()

print("🔍 Fetching images from Wikipedia API...\n")

updated = 0
failed = 0

for (name,) in cricketers:
    image_url = get_wikipedia_image(name)
    
    if image_url:
        c.execute("UPDATE cricketers SET image_url = ? WHERE name = ?", (image_url, name))
        updated += 1
    else:
        failed += 1
    
    # Be respectful to Wikipedia's servers
    time.sleep(1)

conn.commit()
conn.close()

print(f"\n📊 Summary:")
print(f"  ✅ Updated: {updated}")
print(f"  ❌ Failed: {failed}")
print(f"\n🎉 Done! Check the results above.")
