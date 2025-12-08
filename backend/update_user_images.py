import sqlite3

# Your updated cricketer images
cricketers = {
    "MS Dhoni": "https://upload.wikimedia.org/wikipedia/commons/d/d5/MS_Dhoni_%28Prabhav_%2723_-_RiGI_2023%29.jpg",
    "Sachin Tendulkar": "https://upload.wikimedia.org/wikipedia/commons/2/25/Sachin_Tendulkar_at_MRF_Promotion_Event.jpg",
    "Virat Kohli": "https://upload.wikimedia.org/wikipedia/commons/9/9b/Virat_Kohli_in_PMO_New_Delhi.jpg",
    "Rohit Sharma": "https://upload.wikimedia.org/wikipedia/commons/1/1e/Prime_Minister_Of_Bharat_Shri_Narendra_Damodardas_Modi_with_Shri_Rohit_Gurunath_Sharma%28Cropped%29.jpg",
    "Jasprit Bumrah": "https://upload.wikimedia.org/wikipedia/commons/0/02/Jasprit_Bumrah_in_PMO_New_Delhi.jpg",
    "Ravichandran Ashwin": "https://upload.wikimedia.org/wikipedia/commons/d/da/The_Minister_of_State_for_Youth_Affairs_and_Sports_conffering_the_Arjuna_Award_on_cricketer_Ravichandran_Ashwin.jpg",
    "Ricky Ponting": "https://upload.wikimedia.org/wikipedia/commons/4/49/Ricky_Ponting_2015.jpg",
    "Pat Cummins": "https://upload.wikimedia.org/wikipedia/commons/6/69/Pat_Cummins_fielding_Ashes_2021_%28cropped%29.jpg",
    "Steve Smith": "https://upload.wikimedia.org/wikipedia/commons/1/1b/STEVE_SMITH_%2811705303043%29.jpg",
    "Mitchell Starc": "https://upload.wikimedia.org/wikipedia/commons/3/38/Mitchell_Starc_2023.jpg",
    "Shane Warne": "https://upload.wikimedia.org/wikipedia/commons/f/ff/Shane_Warne_February_2015.jpg",
    "Adam Gilchrist": "https://upload.wikimedia.org/wikipedia/commons/1/1f/Adam_Gilchrist_of_Australia_%28cropped%29.jpg",
    "Steve Waugh": "https://upload.wikimedia.org/wikipedia/commons/8/82/SRWaugh.png",
    "David Warner": "https://upload.wikimedia.org/wikipedia/commons/2/2c/DAVID_WARNER_%2811704782453%29.jpg",
    "Glenn Maxwell": "https://upload.wikimedia.org/wikipedia/commons/4/43/Glenn_Maxwell_3.jpg",
    "Cameron Green": "https://upload.wikimedia.org/wikipedia/commons/b/b4/Cameron_Green_fielding_Boxing_Day_2022_%28cropped%29.jpg",
    "Joe Root": "https://upload.wikimedia.org/wikipedia/commons/f/f7/Joe_Root_HIP1487_%28cropped%29.jpg",
    "Ben Stokes": "https://upload.wikimedia.org/wikipedia/commons/3/3e/BEN_STOKES_%2811704787023%29_%28cropped%29.jpg",
    "Hardik Pandya": "https://upload.wikimedia.org/wikipedia/commons/f/fc/Hardik_Pandya_in_PMO_New_Delhi.jpg",
    "Shubman Gill": "https://goyahills.com/wp-content/uploads/2025/03/Shubman-Gill.jpg",
    "Abhishek Sharma": "https://goyahills.com/wp-content/uploads/2025/03/Abhishek-Sharma.png",
    "Alastair Cook": "https://upload.wikimedia.org/wikipedia/commons/c/c7/Alastair_Cook_vs_Upminster_CC.jpg",
    "Jos Buttler": "https://upload.wikimedia.org/wikipedia/commons/0/01/Jos_Buttler_in_2023.jpg",
    "Andrew Strauss": "https://upload.wikimedia.org/wikipedia/commons/6/62/Andrew_Strauss.JPG",
    "Don Bradman": "https://upload.wikimedia.org/wikipedia/commons/d/d8/Don_Bradman_1930.jpg",
    "Jason Roy": "https://upload.wikimedia.org/wikipedia/commons/e/ed/Jason_Roy_with_the_Sydney_Sixers.jpg",
    "James Anderson": "https://upload.wikimedia.org/wikipedia/commons/e/e5/JIMMY_ANDERSON.jpg",
    "Stuart Broad": "https://upload.wikimedia.org/wikipedia/commons/4/45/Stuart_broad.jpg",
    "AB de Villiers": "https://upload.wikimedia.org/wikipedia/commons/e/e0/AB_de_villiers_%28cropped%29.jpg",
    "Dale Steyn": "https://media.crictracker.com/media/featureimage/2019/12/Dale-Steyn-picture.jpg",
    "Dewald Brevis": "https://www.gettyimages.in/detail/news-photo/dewald-brevis-of-south-africa-celebrates-after-reaching-his-news-photo/2229695971",
    "Kagiso Rabada": "https://www.astrosage.com/celebrity-horoscope/img/Kagiso-Rabada-horoscope.jpg",
    "Jonty Rhodes": "https://upload.wikimedia.org/wikipedia/commons/9/9b/JONTY_RHODES.jpg",
    "Quinton de Kock": "https://upload.wikimedia.org/wikipedia/commons/6/67/QUINTON_DE_KOCK_%2815681398316%29.jpg",
    "Kuldeep Yadav": "https://upload.wikimedia.org/wikipedia/commons/9/91/Kuldeep_Yadav_in_PMO_New_Delhi.jpg",
    "Kane Williamson": "https://upload.wikimedia.org/wikipedia/commons/2/2a/Kane_Williamson_in_2019.jpg",
    "Ross Taylor": "https://upload.wikimedia.org/wikipedia/commons/0/0e/Ross_Taylor_CNZM_%28cropped%29.jpg",
    "Rachin Ravindra": "https://akm-img-a-in.tosshub.com/indiatoday/images/story/202410/rachin-ravindra.jpg",
    "Tim Southee": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Tim_Southee_ONZM_%28cropped%29.jpg",
    "Chris Gayle": "https://upload.wikimedia.org/wikipedia/commons/f/f8/Two_views_of_Chris_Gayle_%2848020785077%29.jpg",
    "Brian Lara": "https://upload.wikimedia.org/wikipedia/commons/9/92/Brian_Lara_at_2012_Mumbai_Marathon_pre_bash.jpg",
    "Curtly Ambrose": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Curtly_Ambrose.jpg/400px-Curtly_Ambrose.jpg",
    "Carlos Brathwaite": "https://upload.wikimedia.org/wikipedia/commons/2/20/Carlos_Brathwaite.jpg",
    "Babar Azam": "https://upload.wikimedia.org/wikipedia/commons/4/43/Babar_azam_2023.jpg",
    "Shoaib Akhtar": "https://upload.wikimedia.org/wikipedia/commons/0/02/Khizer_Ahmed_and_mentor_Shoaib_Akhtar_%28cropped%29.jpg",
    "Wasim Akram": "https://upload.wikimedia.org/wikipedia/commons/f/f4/Wasim-akram-gesf-2018-7878.jpg",
    "Mohammad Rizwan": "https://upload.wikimedia.org/wikipedia/commons/a/af/M_Rizwan.jpg",
    "Shahid Afridi": "https://upload.wikimedia.org/wikipedia/commons/1/13/Shahid_Afridi_in_2017_%283x4_cropped%29.jpg",
    "Shaheen Afridi": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Shaheen_Afridi.jpg/400px-Shaheen_Afridi.jpg",
    "Kapil Dev": "https://upload.wikimedia.org/wikipedia/commons/8/88/Kapil_Dev_at_Equation_sports_auction_%283x4_cropped%29.jpg",
    "Sunil Gavaskar": "https://upload.wikimedia.org/wikipedia/commons/e/ed/Sunny_Gavaskar_Sahara.jpg",
    "Sourav Ganguly": "https://upload.wikimedia.org/wikipedia/commons/e/e8/Sourav_Ganguly_closeup.jpg",
    "Rahul Dravid": "https://upload.wikimedia.org/wikipedia/commons/1/17/Rahul_Dravid_in_2024.jpg",
    "Rashid Khan": "https://upload.wikimedia.org/wikipedia/commons/7/71/Rashid_Khan.jpg",
    "Lasith Malinga": "https://upload.wikimedia.org/wikipedia/commons/2/26/Lasith_Malinga_tossing_a_cricket_ball_at_practice.jpg",
    "Kumar Sangakkara": "https://upload.wikimedia.org/wikipedia/commons/b/bd/Kumar_Sangakkara_bat_in_hand.JPG",
    "Mahela Jayawardene": "https://upload.wikimedia.org/wikipedia/commons/f/f7/Mahela_Jayawardene_3.JPG"
}

# Connect to database
conn = sqlite3.connect('cricketers.db')
c = conn.cursor()

print("🔄 Updating cricketer images...\n")

updated = 0
not_found = []

for name, url in cricketers.items():
    # Check if cricketer exists in database
    c.execute("SELECT COUNT(*) FROM cricketers WHERE name = ?", (name,))
    exists = c.fetchone()[0]
    
    if exists:
        c.execute("UPDATE cricketers SET image_url = ? WHERE name = ?", (url, name))
        updated += 1
        print(f"✅ {name}")
    else:
        not_found.append(name)
        print(f"⚠️  {name} - Not in database")

conn.commit()
conn.close()

print(f"\n{'='*60}")
print(f"📊 SUMMARY:")
print(f"  ✅ Updated: {updated}/{len(cricketers)}")
print(f"  ⚠️  Not found in DB: {len(not_found)}/{len(cricketers)}")

if not_found:
    print(f"\n❌ Cricketers not in database:")
    for name in not_found:
        print(f"    - {name}")

print(f"\n🎉 Database updated successfully!")
