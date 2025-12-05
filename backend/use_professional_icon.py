import sqlite3

# Connect to database
conn = sqlite3.connect('cricketers.db')
c = conn.cursor()

# Use a professional cricket player icon/silhouette
# This is better than showing WRONG player photos
# Using a reliable, free cricket icon from a CDN
professional_cricket_icon = 'https://cdn-icons-png.flaticon.com/512/3774/3774299.png'

# Update all cricketers
c.execute("UPDATE cricketers SET image_url = ?", (professional_cricket_icon,))

print(f"✅ Updated {c.rowcount} cricketers")
print("📝 Using professional cricket player icon")
print("💡 This is better than showing wrong player photos!")
print("ℹ️  All cricketers have consistent, professional appearance")

# Verify
c.execute("SELECT name, image_url FROM cricketers LIMIT 3")
print("\n📸 Sample:")
for row in c.fetchall():
    print(f"  {row[0]}: {row[1]}")

conn.commit()
conn.close()

print("\n🎉 Database updated! Reload your web app.")
print("\n💡 NOTE: To get individual player photos:")
print("   1. You would need to manually find each player's photo")
print("   2. Upload to an image host (Cloudinary/ImgBB)")
print("   3. Update database with those URLs")
print("   This ensures 100% accuracy but takes significant time")
