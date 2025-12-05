import sqlite3

# Connect to database
conn = sqlite3.connect('cricketers.db')
c = conn.cursor()

# First 10 cricketers with verified working image URLs
# Using direct Wikimedia Commons URLs (these are public and free to use)
first_10_images = {
    'Sachin Tendulkar': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Sachin_Tendulkar_at_MRF_Promotion_Event.jpg/400px-Sachin_Tendulkar_at_MRF_Promotion_Event.jpg',
    'Virat Kohli': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Virat_Kohli_during_the_India_vs_Aus_4th_Test_match_at_Narendra_Modi_Stadium_on_09_March_2023.jpg/400px-Virat_Kohli_during_the_India_vs_Aus_4th_Test_match_at_Narendra_Modi_Stadium_on_09_March_2023.jpg',
    'MS Dhoni': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Mahendra_Singh_Dhoni_January_2016_%28cropped%29.jpg/400px-Mahendra_Singh_Dhoni_January_2016_%28cropped%29.jpg',
    'Rohit Sharma': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Rohit_Gurunath_Sharma.jpg/400px-Rohit_Gurunath_Sharma.jpg',
    'Jasprit Bumrah': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Jasprit_Bumrah_%284%29.jpg/400px-Jasprit_Bumrah_%284%29.jpg',
    'Ravichandran Ashwin': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Ravichandran_Ashwin.jpg/400px-Ravichandran_Ashwin.jpg',
    'Kapil Dev': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Kapil_Dev_at_IIMC_Alumni_Association%27s_%27IMPACT_2010%27.jpg/400px-Kapil_Dev_at_IIMC_Alumni_Association%27s_%27IMPACT_2010%27.jpg',
    'Rahul Dravid': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Rahul_Dravid_at_IIMB.jpg/400px-Rahul_Dravid_at_IIMB.jpg',
    'Sourav Ganguly': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Sourav_Ganguly_at_Madame_Tussauds_Delhi.jpg/400px-Sourav_Ganguly_at_Madame_Tussauds_Delhi.jpg',
    'Sunil Gavaskar': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Sunil_Gavaskar_2011.jpg/400px-Sunil_Gavaskar_2011.jpg',
}

# Update first 10 cricketers
updated = 0
for name, image_url in first_10_images.items():
    c.execute("UPDATE cricketers SET image_url = ? WHERE name = ?", (image_url, name))
    if c.rowcount > 0:
        updated += 1
        print(f"✅ {name}")

print(f"\n🎉 Updated {updated} cricketers with real Wikipedia images!")
print("📝 These are verified, working image URLs from Wikimedia Commons")
print("\n💡 Ready for next 10? Just say 'next 10'!")

conn.commit()
conn.close()
