import sqlite3

def init_db():
    conn = sqlite3.connect('cricketers.db')
    c = conn.cursor()
    
    # Drop existing table to recreate with better data
    c.execute('DROP TABLE IF EXISTS cricketers')
    
    # Create table with enhanced schema
    c.execute('''
        CREATE TABLE cricketers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            country TEXT,
            role TEXT,
            history TEXT,
            achievements TEXT,
            records TEXT,
            controversies TEXT,
            image_url TEXT
        )
    ''')
    
    # Comprehensive list with detailed information
    cricketers = [
        # Indian Legends
        (
            'Sachin Tendulkar', 
            'India', 
            'Batsman', 
            'Sachin Ramesh Tendulkar is widely regarded as one of the greatest batsmen in cricket history. Born on April 24, 1973, he made his Test debut at age 16. Over a 24-year career, he became the highest run scorer in international cricket. Known as the "Master Blaster" and "Little Master", he was a complete batsman who could dominate any bowling attack.',
            'First player to score 100 international centuries (51 Test, 49 ODI). Only player to score 200 runs in an ODI. Played 6 World Cups (1992-2011). Won 2011 World Cup. Received Bharat Ratna (India\'s highest civilian award) in 2014. ICC Cricket Hall of Fame inductee.',
            'Most runs in international cricket: 34,357 runs. Most runs in Test cricket: 15,921. Most runs in ODI cricket: 18,426. Most centuries in international cricket: 100. Highest individual score in ODI: 200* vs South Africa. 51 Test centuries, 49 ODI centuries.',
            'Ball-tampering allegations in 2001 (cleared). Involved in match-fixing allegations (never proven). Criticized for not speaking against corruption. Toes-gate controversy with Mike Denness in 2001.',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Sachin_Tendulkar_at_MRF_Promotion_Event.jpg/400px-Sachin_Tendulkar_at_MRF_Promotion_Event.jpg'
        ),
        
        (
            'Virat Kohli', 
            'India', 
            'Batsman', 
            'Virat Kohli is an Indian international cricketer and former captain. Born on November 5, 1988, he is widely regarded as one of the best batsmen of the modern era. Known for his aggressive batting style, exceptional fitness, and chase master abilities. He revolutionized Indian cricket with his fitness standards and aggressive approach.',
            'ICC ODI Player of the Year (2012, 2017, 2018). Wisden Leading Cricketer (2016, 2017, 2018). Fastest to 8,000, 9,000, 10,000, 11,000, and 12,000 ODI runs. Led India to number 1 Test ranking. Won U19 World Cup as captain in 2008.',
            '80+ international centuries across formats. Fastest to reach multiple ODI milestones. Average over 50 in all three formats. 27,000+ international runs. Best ODI average among players with 5000+ runs (58+). 70+ Test centuries. Highest individual score: 254* in Tests.',
            'Altercation with Gautam Gambhir in IPL. Controversial send-offs and aggressive behavior. Criticized for poor Test performances in England. Resignation as Test captain controversy in 2022. Conflicts with BCCI over player selection.',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Virat_Kohli_during_the_India_vs_Aus_4th_Test_match_at_Narendra_Modi_Stadium_on_09_March_2023.jpg/400px-Virat_Kohli_during_the_India_vs_Aus_4th_Test_match_at_Narendra_Modi_Stadium_on_09_March_2023.jpg'
        ),
        
        (
            'MS Dhoni', 
            'India', 
            'Wicketkeeper-Batsman', 
            'Mahendra Singh Dhoni is one of the most successful captains in cricket history. Born on July 7, 1981, he is known for his calm demeanor under pressure, earning him the nickname "Captain Cool". He transformed Indian cricket with his leadership and finishing abilities. Retired from international cricket in 2020 but continues in IPL.',
            'Only captain to win all three ICC trophies: T20 World Cup (2007), ODI World Cup (2011), Champions Trophy (2013). Led India to No.1 Test ranking. Most successful Indian captain with 110 ODI wins. ICC ODI Team of the Year captain multiple times. Padma Bhushan and Padma Shri recipient.',
            'Most international stumpings: 195. Most dismissals as wicketkeeper-captain. Most runs in successful ODI chases. Most sixes in ODI cricket by an Indian. 10,000+ ODI runs. 90+ international fifties. Highest score: 224 in Tests.',
            'Retirement timing controversies. Criticized for slow batting in T20s. Conflict with Greg Chappell. Alleged involvement in IPL spot-fixing (cleared). Criticism over team selection decisions.',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Mahendra_Singh_Dhoni_January_2016_%28cropped%29.jpg/400px-Mahendra_Singh_Dhoni_January_2016_%28cropped%29.jpg'
        ),
        
        (
            'Kapil Dev', 
            'India', 
            'All-rounder', 
            'Kapil Dev Nikhanj is a former Indian cricketer who captained India to their first World Cup victory in 1983. Born on January 6, 1959, he was one of the greatest all-rounders in cricket history. Known for his aggressive batting and fast bowling. He inspired a generation of Indian cricketers.',
            'Led India to 1983 World Cup victory. First player to take 400 Test wickets. Wisden Indian Cricketer of the Century. ICC Cricket Hall of Fame inductee. Padma Shri and Padma Bhushan recipient.',
            '434 Test wickets (first to reach 400). 5,248 Test runs with 8 centuries. Best bowling: 9/83. Famous 175* vs Zimbabwe in 1983 World Cup. 687 international wickets. All-round double of 5000 runs and 400 wickets in Tests.',
            'Match-fixing allegations in 2000 (cleared). Conflict with Mohammad Azharuddin. Criticized for poor commentary. Involvement in cricket administration controversies.',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Kapil_Dev_at_IIMC_Alumni_Association%27s_%27IMPACT_2010%27.jpg/400px-Kapil_Dev_at_IIMC_Alumni_Association%27s_%27IMPACT_2010%27.jpg'
        ),
        
        (
            'Rahul Dravid', 
            'India', 
            'Batsman', 
            'Rahul Sharad Dravid, known as "The Wall", was one of the greatest batsmen in Test cricket. Born on January 11, 1973, he was known for his solid technique, dependability, and ability to play long innings. He is currently the head coach of the Indian cricket team and has mentored young talent successfully.',
            'ICC Test Player of the Year (2004). Wisden Cricketer of the Year (2000). Most catches by a non-wicketkeeper in Tests (210). Led India to historic Test series wins abroad. U19 and India A coach. Current India head coach.',
            '13,288 Test runs with 36 centuries. 10,889 ODI runs. 210 catches in Tests (most by non-wicketkeeper). Most balls faced in Test cricket. 270 in Tests (highest score). Only player to score century in all 10 Test playing nations.',
            'Slow over-rate fines. Criticized for slow batting in ODIs. Ball-tampering incident (2004). Conflict with Greg Chappell during coaching tenure.',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Rahul_Dravid_at_IIMB.jpg/400px-Rahul_Dravid_at_IIMB.jpg'
        ),
        
        (
            'Sourav Ganguly', 
            'India', 
            'Batsman', 
            'Sourav Chandidas Ganguly, known as "Dada", was one of India\'s most successful captains. Born on July 8, 1972, he transformed Indian cricket with his aggressive leadership. He backed young players and made India a competitive force abroad. Currently serves as BCCI President.',
            'Led India to 2003 World Cup final. Joint-fastest to 9,000 ODI runs. Most ODI runs as captain. Led India to historic Test series wins in Pakistan and England. ICC Cricket Hall of Fame. Current BCCI President.',
            '18,575 international runs. 38 international centuries. 11,363 ODI runs. 7,212 Test runs. Highest ODI score: 183. Most successful Indian ODI captain. 100 ODI wickets.',
            'Lord\'s shirt-waving incident (2002). Match-fixing allegations (cleared). Conflict with Greg Chappell. Criticized for favoritism. BCCI presidency controversies.',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Sourav_Ganguly_at_Madame_Tussauds_Delhi.jpg/400px-Sourav_Ganguly_at_Madame_Tussauds_Delhi.jpg'
        ),
        
        # Australian Legends
        (
            'Don Bradman', 
            'Australia', 
            'Batsman', 
            'Sir Donald George Bradman is widely considered the greatest batsman of all time. Born on August 27, 1908, his Test batting average of 99.94 is often cited as the greatest achievement in any major sport. He dominated cricket in the 1930s and 1940s. His records remain unmatched even today.',
            'Test batting average of 99.94 (highest ever). Australian Cricket Hall of Fame. ICC Cricket Hall of Fame. Wisden Cricketer of the Century. Knighted in 1949. Australian of the Year.',
            '99.94 Test average (6,996 runs in 52 Tests). 29 Test centuries in 52 Tests. Highest Test score: 334. 12 double centuries in Tests. Scored century every 3 innings. 974 runs in 1930 Ashes series.',
            'Bodyline series controversy (1932-33). Accused of being too focused on statistics. Criticized for not serving in WWII. Administrative controversies in later years.',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Don_Bradman_1930.jpg/400px-Don_Bradman_1930.jpg'
        ),
        
        (
            'Ricky Ponting', 
            'Australia', 
            'Batsman', 
            'Ricky Thomas Ponting is one of the most successful captains in cricket history. Born on December 19, 1974, he led Australia to two World Cup victories (2003, 2007). Known for his aggressive batting and brilliant fielding. He scored over 27,000 international runs with 71 centuries across formats.',
            'Led Australia to 2003 and 2007 World Cup victories. ICC Cricketer of the Year (2006, 2007). Most successful Test captain (48 wins). Allan Border Medal winner (4 times). ICC Cricket Hall of Fame.',
            '27,483 international runs. 71 international centuries (41 Test, 30 ODI). 13,378 Test runs. 13,704 ODI runs. Highest Test score: 257. Most catches in Tests (196). 100+ Test matches as captain.',
            'Monkeygate scandal (2008). Aggressive behavior and umpire disputes. DRS opposition controversy. Criticized for poor sportsmanship at times.',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Ricky_Ponting_2014.jpg/400px-Ricky_Ponting_2014.jpg'
        ),
        
        (
            'Shane Warne', 
            'Australia', 
            'Bowler', 
            'Shane Keith Warne was one of the greatest bowlers in cricket history. Born on September 13, 1969, the legendary leg-spinner took 708 Test wickets and revolutionized spin bowling. His "Ball of the Century" to Mike Gatting in 1993 is iconic. He passed away on March 4, 2022, leaving an indelible mark on cricket.',
            'Second-highest Test wicket-taker (708). Wisden Leading Cricketer (1997, 2004). Wisden Cricketer of the Century (one of five). ICC Cricket Hall of Fame. Won 1999 World Cup.',
            '708 Test wickets (second-most all-time). 293 ODI wickets. 1,001 international wickets. Best bowling: 8/71 in Tests. Hat-trick in Tests and ODIs. Ball of the Century (1993). 37 five-wicket hauls in Tests.',
            'Drug ban (2003). Multiple extramarital affairs. Banned for passing information to bookmaker. Criticized for lifestyle choices. Feud with Steve Waugh.',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Shane_Warne_2012.jpg/400px-Shane_Warne_2012.jpg'
        ),
        
        (
            'Steve Smith', 
            'Australia', 
            'Batsman', 
            'Steven Peter Devereux Smith is one of the best Test batsmen of the modern era. Born on June 2, 1989, he has scored over 15,000 international runs with a Test average over 60. Known for his unorthodox technique and exceptional concentration. Former Australian captain who returned after ball-tampering ban.',
            'ICC Test Cricketer of the Year (2015, 2017). Allan Border Medal (4 times). Fastest Australian to 7,000 Test runs. Led Australia to 2015 World Cup final. Youngest Australian Test captain in 100+ years.',
            '9,000+ Test runs with average over 60. 32 Test centuries. Fastest to 7,000 Test runs for Australia. Highest Test score: 239. Three consecutive Ashes centuries (2019). 8,000+ ODI runs.',
            'Ball-tampering scandal (2018) - banned for 12 months. Stripped of captaincy. Criticized for leadership failure. Booed by crowds after return. Concussion substitute controversy.',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Steve_Smith_2019.jpg/400px-Steve_Smith_2019.jpg'
        ),
        
        # Pakistani Legends
        (
            'Wasim Akram', 
            'Pakistan', 
            'Bowler', 
            'Wasim Akram is regarded as one of the greatest left-arm fast bowlers and the best exponent of swing bowling. Born on June 3, 1966, he took 916 international wickets. Known for his deadly yorkers and reverse swing mastery. He was a key member of Pakistan\'s 1992 World Cup winning team.',
            'Won 1992 World Cup. ICC Cricket Hall of Fame. Wisden Cricketer of the Year (1993). First bowler to take 500 ODI wickets. Pakistan\'s greatest bowler.',
            '916 international wickets (414 Test, 502 ODI). Most ODI wickets at retirement. Best bowling: 7/119 in Tests. Hat-tricks in both Tests and ODIs. 3,000+ international runs. Two hat-tricks in ODIs.',
            'Match-fixing allegations (cleared). Accused of ball-tampering. Conflict with Waqar Younis. Criticized for poor captaincy. Drug smuggling allegations (cleared).',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Wasim_Akram_2012.jpg/400px-Wasim_Akram_2012.jpg'
        ),
        
        (
            'Imran Khan', 
            'Pakistan', 
            'All-rounder', 
            'Imran Khan Niazi was one of cricket\'s greatest all-rounders and captains. Born on October 5, 1952, he led Pakistan to their only World Cup victory in 1992. He took 362 Test wickets and scored over 7,000 international runs. He is currently serving as the Prime Minister of Pakistan.',
            'Led Pakistan to 1992 World Cup victory. ICC Cricket Hall of Fame. Wisden Cricketer of the Year (1983). Built Shaukat Khanum Cancer Hospital. Prime Minister of Pakistan (2018-2022).',
            '362 Test wickets. 3,807 Test runs with 6 centuries. All-round double in Tests. Best bowling: 8/58. Highest score: 136. 126 ODI wickets. Never lost a Test series as captain.',
            'Playboy lifestyle criticism. Multiple marriages. Political controversies as PM. Accused of match-fixing (never proven). Conflict with cricket board.',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Imran_Khan_1983.jpg/400px-Imran_Khan_1983.jpg'
        ),
        
        (
            'Babar Azam', 
            'Pakistan', 
            'Batsman', 
            'Babar Azam is the current captain of Pakistan and one of the best batsmen in modern cricket. Born on October 15, 1994, he has scored over 12,000 international runs. Known for his elegant strokeplay and consistency across all formats. He is ranked among the top batsmen in all three formats.',
            'Fastest to 1,000, 2,000, 3,000 T20I runs. ICC ODI Cricketer of the Year (2022). Fastest Asian to 14 ODI centuries. Number 1 ranked ODI batsman. Captain of Pakistan in all formats.',
            '12,000+ international runs. 30+ international centuries. Fastest to multiple T20I milestones. Average over 50 in ODIs and T20Is. Highest ODI score: 158. 3,000+ T20I runs.',
            'Criticized for defensive captaincy. Poor World Cup 2023 performance. Conflict with PCB over selection. Accused of favoritism. Pressure of captaincy affecting form.',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Babar_Azam_2019.jpg/400px-Babar_Azam_2019.jpg'
        ),
        
        # Add more cricketers with similar detailed information...
        # (Continuing with other legends)
    ]
    
    # Insert data
    try:
        c.executemany('''
            INSERT INTO cricketers (name, country, role, history, achievements, records, controversies, image_url) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', cricketers)
        
        print(f"✅ Database initialized with {len(cricketers)} cricketers.")
        
        # Show count by country
        c.execute('SELECT country, COUNT(*) as count FROM cricketers GROUP BY country ORDER BY count DESC')
        print("\n📊 Cricketers by country:")
        for row in c.fetchall():
            print(f"  {row[0]}: {row[1]}")
            
        # Check for duplicates
        c.execute('SELECT name, COUNT(*) as count FROM cricketers GROUP BY name HAVING count > 1')
        duplicates = c.fetchall()
        if duplicates:
            print("\n⚠️  Duplicate entries found:")
            for row in duplicates:
                print(f"  {row[0]}: {row[1]} entries")
        else:
            print("\n✅ No duplicate entries found!")
            
    except sqlite3.IntegrityError as e:
        print(f"❌ Error: Duplicate entry detected - {e}")
        conn.rollback()
        return

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
