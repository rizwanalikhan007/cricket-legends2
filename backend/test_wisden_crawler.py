import requests
from bs4 import BeautifulSoup
import time
import sqlite3

def get_wisden_image(cricketer_name):
    """Try to get cricketer image from Wisden"""
    try:
        # Format name for URL (replace spaces with hyphens, lowercase)
        url_name = cricketer_name.lower().replace(' ', '-')
        
        # Try Wisden player profile URL
        url = f"https://www.wisden.com/cricketers/{url_name}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Look for profile image (common patterns)
            img = soup.find('img', {'class': ['player-image', 'profile-image', 'player-photo']})
            
            if not img:
                # Try finding any img with player name in alt
                img = soup.find('img', {'alt': lambda x: x and cricketer_name.lower() in x.lower()})
            
            if not img:
                # Try meta og:image
                meta_img = soup.find('meta', {'property': 'og:image'})
                if meta_img and meta_img.get('content'):
                    img_url = meta_img.get('content')
                    print(f"✅ {cricketer_name}: {img_url[:60]}...")
                    return img_url
            
            if img and img.get('src'):
                img_url = img.get('src')
                # Make absolute URL if needed
                if img_url.startswith('//'):
                    img_url = 'https:' + img_url
                elif img_url.startswith('/'):
                    img_url = 'https://www.wisden.com' + img_url
                    
                print(f"✅ {cricketer_name}: {img_url[:60]}...")
                return img_url
            else:
                print(f"⚠️  {cricketer_name}: No image found on page")
                return None
        else:
            print(f"⚠️  {cricketer_name}: Page not found (HTTP {response.status_code})")
            return None
            
    except Exception as e:
        print(f"❌ {cricketer_name}: {str(e)[:50]}")
        return None

# Test with a few cricketers first
test_cricketers = [
    "Sachin Tendulkar",
    "Virat Kohli", 
    "MS Dhoni",
    "Rohit Sharma",
    "Jasprit Bumrah"
]

print("🔍 Testing Wisden.com crawler...\n")

for name in test_cricketers:
    img_url = get_wisden_image(name)
    time.sleep(2)  # Be respectful to the server

print("\n✅ Test complete!")
