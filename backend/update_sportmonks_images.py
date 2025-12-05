import sqlite3

# Your provided image data
sportmonks_images = {
    "Ahmed Shehzad": "https://cdn.sportmonks.com/images/cricket/players/2/2.png",
    "Anwar Ali": "https://cdn.sportmonks.com/images/cricket/players/3/3.png",
    "Sarfraz Ahmed": "https://cdn.sportmonks.com/images/cricket/players/4/4.png",
    "Azhar Ali": "https://cdn.sportmonks.com/images/cricket/players/5/5.png",
    "Fakhar Zaman": "https://cdn.sportmonks.com/images/cricket/players/6/6.png",
    "Imam ul Haq": "https://cdn.sportmonks.com/images/cricket/players/7/7.png",
    "Babar Azam": "https://cdn.sportmonks.com/images/cricket/players/8/8.png",
    "Asad Shafiq": "https://cdn.sportmonks.com/images/cricket/players/9/9.png",
    "Haris Sohail": "https://cdn.sportmonks.com/images/cricket/players/10/10.png",
    "Usman Salahuddin": "https://cdn.sportmonks.com/images/cricket/players/11/11.png",
    "Yasir Shah": "https://cdn.sportmonks.com/images/cricket/players/12/12.png",
    "Shadab Khan": "https://cdn.sportmonks.com/images/cricket/players/13/13.png",
    "Bilal Asif": "https://cdn.sportmonks.com/images/cricket/players/14/14.png",
    "Mohammad Abbas": "https://cdn.sportmonks.com/images/cricket/players/15/15.png",
    "Hasan Ali": "https://cdn.sportmonks.com/images/cricket/players/16/16.png",
    "Wahab Riaz": "https://cdn.sportmonks.com/images/cricket/players/17/17.png",
    "Faheem Ashraf": "https://cdn.sportmonks.com/images/cricket/players/18/18.png",
    "Mir Hamza": "https://cdn.sportmonks.com/images/cricket/players/19/19.png",
    "Mohammad Rizwan": "https://cdn.sportmonks.com/images/cricket/players/20/20.png",
    "Mohammad Hafeez": "https://cdn.sportmonks.com/images/cricket/players/21/21.png",
    "Tim Paine": "https://cdn.sportmonks.com/images/cricket/players/22/22.png",
    "Ashton Agar": "https://cdn.sportmonks.com/images/cricket/players/23/23.png",
    "Brendan Doggett": "https://cdn.sportmonks.com/images/cricket/players/24/24.png",
    "Aaron Finch": "https://cdn.sportmonks.com/images/cricket/players/25/25.png",
    "Travis Head": "https://cdn.sportmonks.com/images/cricket/players/26/26.png",
    "Jon Holland": "https://cdn.sportmonks.com/images/cricket/players/27/27.png",
    "Usman Khawaja": "https://cdn.sportmonks.com/images/cricket/players/28/28.png",
    "Marnus Labuschagne": "https://cdn.sportmonks.com/images/cricket/players/29/29.png",
    "Nathan Lyon": "https://cdn.sportmonks.com/images/cricket/players/30/30.png",
    "Mitchell Marsh": "https://cdn.sportmonks.com/images/cricket/players/31/31.png",
    "Shaun Marsh": "https://cdn.sportmonks.com/images/cricket/players/0/32.png",
    "Michael Neser": "https://cdn.sportmonks.com/images/cricket/players/1/33.png",
    "Matt Renshaw": "https://cdn.sportmonks.com/images/cricket/players/2/34.png",
    "Peter Siddle": "https://cdn.sportmonks.com/images/cricket/players/3/35.png",
    "Mitchell Starc": "https://cdn.sportmonks.com/images/cricket/players/4/36.png",
    "Alex Carey": "https://cdn.sportmonks.com/images/cricket/players/5/37.png",
    "Nathan Coulter-Nile": "https://cdn.sportmonks.com/images/cricket/players/6/38.png",
    "Chris Lynn": "https://cdn.sportmonks.com/images/cricket/players/7/39.png",
    "Glenn Maxwell": "https://cdn.sportmonks.com/images/cricket/players/8/40.png",
    "D'Arcy Short": "https://cdn.sportmonks.com/images/cricket/players/9/41.png",
    "Billy Stanlake": "https://cdn.sportmonks.com/images/cricket/players/10/42.png",
    "Andrew Tye": "https://cdn.sportmonks.com/images/cricket/players/11/43.png",
    "Adam Zampa": "https://cdn.sportmonks.com/images/cricket/players/12/44.png",
    "Ben McDermott": "https://cdn.sportmonks.com/images/cricket/players/13/45.png",
    "Virat Kohli": "https://cdn.sportmonks.com/images/cricket/players/14/46.png",
    "Lokesh Rahul": "https://cdn.sportmonks.com/images/cricket/players/15/47.png",
    "Prithvi Shaw": "https://cdn.sportmonks.com/images/cricket/players/16/48.png",
    "Mayank Agarwal": "https://cdn.sportmonks.com/images/cricket/players/17/49.png",
    "Cheteshwar Pujara": "https://cdn.sportmonks.com/images/cricket/players/18/50.png",
    "Ajinkya Rahane": "https://cdn.sportmonks.com/images/cricket/players/19/51.png",
    "Hanuma Vihari": "https://cdn.sportmonks.com/images/cricket/players/20/52.png",
    "Rishabh Pant": "https://cdn.sportmonks.com/images/cricket/players/21/53.png",
    "Ravichandran Ashwin": "https://cdn.sportmonks.com/images/cricket/players/22/54.png",
    "Ravindra Jadeja": "https://cdn.sportmonks.com/images/cricket/players/23/55.png",
    "Kuldeep Yadav": "https://cdn.sportmonks.com/images/cricket/players/24/56.png",
    "Mohammed Shami": "https://cdn.sportmonks.com/images/cricket/players/25/57.png",
    "Umesh Yadav": "https://cdn.sportmonks.com/images/cricket/players/26/58.png",
    "Mohammed Siraj": "https://cdn.sportmonks.com/images/cricket/players/27/59.png",
    "Shardul Thakur": "https://cdn.sportmonks.com/images/cricket/players/28/60.png",
    "Jean-Paul Duminy": "https://cdn.sportmonks.com/images/cricket/players/29/61.png",
    "Reeza Hendricks": "https://cdn.sportmonks.com/images/cricket/players/30/62.png",
    "Imran Tahir": "https://cdn.sportmonks.com/images/cricket/players/31/63.png",
    "Christiaan Jonker": "https://cdn.sportmonks.com/images/cricket/players/0/64.png",
    "Heinrich Klaasen": "https://cdn.sportmonks.com/images/cricket/players/1/65.png",
    "Aiden Markram": "https://cdn.sportmonks.com/images/cricket/players/2/66.png",
    "Lungi Ngidi": "https://cdn.sportmonks.com/images/cricket/players/4/68.png",
    "Andile Phehlukwayo": "https://cdn.sportmonks.com/images/cricket/players/5/69.png",
    "Kagiso Rabada": "https://cdn.sportmonks.com/images/cricket/players/6/70.png",
    "Tabraiz Shamsi": "https://cdn.sportmonks.com/images/cricket/players/7/71.png",
    "Dale Steyn": "https://cdn.sportmonks.com/images/cricket/players/8/72.png",
    "Khaya Zondo": "https://cdn.sportmonks.com/images/cricket/players/9/73.png",
    "Dean Elgar": "https://cdn.sportmonks.com/images/cricket/players/10/74.png",
    "Faf du Plessis": "https://cdn.sportmonks.com/images/cricket/players/11/75.png",
    "Junior Dala": "https://cdn.sportmonks.com/images/cricket/players/12/76.png",
    "Quinton de Kock": "https://cdn.sportmonks.com/images/cricket/players/13/77.png",
    "David Miller": "https://cdn.sportmonks.com/images/cricket/players/15/79.png",
    "Dane Paterson": "https://cdn.sportmonks.com/images/cricket/players/16/80.png",
    "Gihahn Cloete": "https://cdn.sportmonks.com/images/cricket/players/17/81.png",
    "Rassie van der Dussen": "https://cdn.sportmonks.com/images/cricket/players/18/82.png",
    "Hamilton Masakadza": "https://cdn.sportmonks.com/images/cricket/players/19/83.png",
    "Solomon Mire": "https://cdn.sportmonks.com/images/cricket/players/20/84.png",
    "Craig Ervine": "https://cdn.sportmonks.com/images/cricket/players/21/85.png",
    "Brendan Taylor": "https://cdn.sportmonks.com/images/cricket/players/22/86.png",
    "Peter Moor": "https://cdn.sportmonks.com/images/cricket/players/23/87.png",
    "Elton Chigumbura": "https://cdn.sportmonks.com/images/cricket/players/24/88.png",
    "Donald Tiripano": "https://cdn.sportmonks.com/images/cricket/players/25/89.png",
    "Kyle Jarvis": "https://cdn.sportmonks.com/images/cricket/players/26/90.png",
    "Brandon Mavuta": "https://cdn.sportmonks.com/images/cricket/players/27/91.png",
    "Richard Ngarava": "https://cdn.sportmonks.com/images/cricket/players/28/92.png",
    "Tinashe Kamunhukamwe": "https://cdn.sportmonks.com/images/cricket/players/29/93.png",
    "Wellington Masakadza": "https://cdn.sportmonks.com/images/cricket/players/30/94.png",
    "Ryan Murray": "https://cdn.sportmonks.com/images/cricket/players/31/95.png",
    "Tendai Chatara": "https://cdn.sportmonks.com/images/cricket/players/0/96.png",
    "Neville Madziva": "https://cdn.sportmonks.com/images/cricket/players/1/97.png",
    "Chris Mpofu": "https://cdn.sportmonks.com/images/cricket/players/2/98.png",
    "Tarisai Musakanda": "https://cdn.sportmonks.com/images/cricket/players/3/99.png",
    "Jason Holder": "https://cdn.sportmonks.com/images/cricket/players/4/100.png",
    "Sunil Ambris": "https://cdn.sportmonks.com/images/cricket/players/5/101.png",
    "Devendra Bishoo": "https://cdn.sportmonks.com/images/cricket/players/6/102.png",
    "Kraigg Brathwaite": "https://cdn.sportmonks.com/images/cricket/players/7/103.png",
}

# Name variations mapping (database name -> sportmonks name)
name_mapping = {
    "KL Rahul": "Lokesh Rahul",
    "Mohammad Shami": "Mohammed Shami",
}

# Connect to database
conn = sqlite3.connect('cricketers.db')
c = conn.cursor()

# Get all cricketers from database
c.execute("SELECT name FROM cricketers ORDER BY name")
db_cricketers = [row[0] for row in c.fetchall()]

print("🔍 Matching cricketers with Sportmonks images...\n")

updated = 0
missing = []

for db_name in db_cricketers:
    # Check direct match
    if db_name in sportmonks_images:
        url = sportmonks_images[db_name]
        c.execute("UPDATE cricketers SET image_url = ? WHERE name = ?", (url, db_name))
        updated += 1
        print(f"✅ {db_name}")
    # Check name mapping
    elif db_name in name_mapping and name_mapping[db_name] in sportmonks_images:
        url = sportmonks_images[name_mapping[db_name]]
        c.execute("UPDATE cricketers SET image_url = ? WHERE name = ?", (url, db_name))
        updated += 1
        print(f"✅ {db_name} (mapped from {name_mapping[db_name]})")
    else:
        missing.append(db_name)
        print(f"⚠️  {db_name} - NOT FOUND")

conn.commit()
conn.close()

print(f"\n{'='*60}")
print(f"📊 SUMMARY:")
print(f"  ✅ Updated with Sportmonks images: {updated}/113")
print(f"  ⚠️  Missing images: {len(missing)}/113")

if missing:
    print(f"\n❌ CRICKETERS WITHOUT IMAGES ({len(missing)}):")
    for i, name in enumerate(missing, 1):
        print(f"  {i}. {name}")

print(f"\n🎉 Database updated!")
