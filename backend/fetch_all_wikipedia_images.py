import requests
import sqlite3
import time

def get_wikipedia_image(cricketer_name):
    """Fetch the main image from Wikipedia for a cricketer"""
    try:
        url = "https://en.wikipedia.org/w/api.php"
        headers = {'User-Agent': 'CricketLegendsApp/1.0 (Educational Project)'}
        
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
            return None
            
        data = response.json()
        pages = data.get("query", {}).get("pages", {})
        
        for page_id, page_data in pages.items():
            if "thumbnail" in page_data:
                return page_data["thumbnail"]["source"]
        return None
                
    except Exception as e:
        return None

# Connect to database
conn = sqlite3.connect('cricketers.db')
c = conn.cursor()

# Get ALL cricketers
c.execute("SELECT name FROM cricketers ORDER BY id")
cricketers = c.fetchall()

print(f"🔍 Fetching images for {len(cricketers)} cricketers from Wikipedia API...")
print("⏳ This will take about 2 minutes...\n")

updated = 0
failed = 0
failed_names = []

for i, (name,) in enumerate(cricketers, 1):
    image_url = get_wikipedia_image(name)
    
    if image_url:
        c.execute("UPDATE cricketers SET image_url = ? WHERE name = ?", (image_url, name))
        updated += 1
        print(f"✅ [{i}/{len(cricketers)}] {name}")
    else:
        failed += 1
        failed_names.append(name)
        print(f"⚠️  [{i}/{len(cricketers)}] {name} - No image")
    
    # Be respectful to Wikipedia's servers
    time.sleep(1)

conn.commit()
conn.close()

print(f"\n" + "="*60)
print(f"📊 FINAL SUMMARY:")
print(f"  ✅ Successfully updated: {updated}/{len(cricketers)}")
print(f"  ❌ Failed: {failed}/{len(cricketers)}")

if failed_names:
    print(f"\n⚠️  Cricketers without images:")
    for name in failed_names:
        print(f"    - {name}")

print(f"\n🎉 Database updated with real Wikipedia images!")
print(f"💡 Success rate: {(updated/len(cricketers)*100):.1f}%")
