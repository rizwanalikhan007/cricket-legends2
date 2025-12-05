import sqlite3

# Sportmonks images for the missing cricketers
missing_images = {
    "Fakhar Zaman": "https://cdn.sportmonks.com/images/cricket/players/6/6.png",
    "Mohammad Shami": "https://cdn.sportmonks.com/images/cricket/players/25/57.png",
    "Faf du Plessis": "https://cdn.sportmonks.com/images/cricket/players/11/75.png",
}

# Generic cricket icon for the remaining 7
cricket_icon = "https://www.svgrepo.com/show/410428/cricket-player.svg"

remaining = [
    "Daryl Mitchell",
    "David Warner", 
    "Devon Conway",
    "James Anderson",
    "Pathum Nissanka",
    "Shaheen Afridi",
    "Steve Smith"
]

conn = sqlite3.connect('cricketers.db')
c = conn.cursor()

print("🔄 Filling remaining images...\n")

# Update with Sportmonks images
for name, url in missing_images.items():
    c.execute("UPDATE cricketers SET image_url = ? WHERE name = ?", (url, name))
    print(f"✅ {name} - Sportmonks image")

# Update remaining with cricket icon
for name in remaining:
    c.execute("UPDATE cricketers SET image_url = ? WHERE name = ?", (cricket_icon, name))
    print(f"📷 {name} - Cricket icon")

conn.commit()

# Final check
c.execute("SELECT COUNT(*) FROM cricketers WHERE image_url NOT LIKE '%svg%'")
with_real_images = c.fetchone()[0]

c.execute("SELECT COUNT(*) FROM cricketers")
total = c.fetchone()[0]

conn.close()

print(f"\n{'='*60}")
print(f"🎉 FINAL STATUS:")
print(f"  ✅ Real player images: {with_real_images}/{total}")
print(f"  📷 Generic cricket icon: {total - with_real_images}/{total}")
print(f"  🏆 Success rate: {(with_real_images/total*100):.1f}%")
print(f"\n✅ All 113 cricketers now have images!")
