import sqlite3

# Connect to database
conn = sqlite3.connect('cricketers.db')
c = conn.cursor()

# Update all image URLs to use the cricket ball image
cricket_image = 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'

c.execute("UPDATE cricketers SET image_url = ?", (cricket_image,))

print(f"✅ Updated {c.rowcount} image URLs")

# Verify
c.execute("SELECT name, image_url FROM cricketers LIMIT 3")
print("\n📸 Sample images:")
for row in c.fetchall():
    print(f"  {row[0]}: {row[1][:50]}...")

conn.commit()
conn.close()

print("\n🎉 All images updated! Reload your web app now.")
