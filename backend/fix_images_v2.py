import sqlite3

# Connect to database
conn = sqlite3.connect('cricketers.db')
c = conn.cursor()

# Use a simple, working image URL - a generic cricket icon
cricket_image = 'https://cdn-icons-png.flaticon.com/512/1041/1041916.png'

c.execute("UPDATE cricketers SET image_url = ?", (cricket_image,))

print(f"✅ Updated {c.rowcount} image URLs")

# Verify
c.execute("SELECT name, image_url FROM cricketers LIMIT 3")
print("\n📸 Sample images:")
for row in c.fetchall():
    print(f"  {row[0]}: {row[1]}")

conn.commit()
conn.close()

print("\n🎉 All images updated with working cricket icon!")
print("📝 Now reload your web app on PythonAnywhere")
