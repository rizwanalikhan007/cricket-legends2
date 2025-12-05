import sqlite3

# Connect to database
conn = sqlite3.connect('cricketers.db')
c = conn.cursor()

# Use a working, generic cricket player silhouette image for all
# This ensures consistency and avoids wrong player images
generic_cricket_image = 'https://images.unsplash.com/photo-1531415074968-036ba1b575da?w=400&h=400&fit=crop'

# Update all cricketers
c.execute("UPDATE cricketers SET image_url = ?", (generic_cricket_image,))

print(f"✅ Updated {c.rowcount} cricketers with consistent cricket image")
print("📝 Using generic cricket image to avoid mismatched player photos")
print("💡 This ensures no wrong player images are shown")

# Verify
c.execute("SELECT name, image_url FROM cricketers LIMIT 3")
print("\n📸 Sample:")
for row in c.fetchall():
    print(f"  {row[0]}: {row[1][:60]}...")

conn.commit()
conn.close()

print("\n🎉 All images updated! Reload your web app.")
print("ℹ️  All cricketers now have the same cricket-themed image")
print("ℹ️  This prevents showing wrong player photos")
