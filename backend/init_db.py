import sqlite3

def init_db():
    conn = sqlite3.connect('cricketers.db')
    c = conn.cursor()
    
    # Create table
    c.execute('''
        CREATE TABLE IF NOT EXISTS cricketers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            country TEXT,
            role TEXT,
            history TEXT,
            image_url TEXT
        )
    ''')
    
    # Comprehensive list of 100+ famous cricketers
    cricketers = [
        # Indian Legends
        ('Sachin Tendulkar', 'India', 'Batsman', 'Sachin Ramesh Tendulkar is widely regarded as one of the greatest batsmen in cricket history. He is the highest run scorer of all time in international cricket with 34,357 runs. Known as the "Master Blaster" and "Little Master", he played 664 international matches over 24 years.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Sachin_Tendulkar_at_MRF_Promotion_Event.jpg/400px-Sachin_Tendulkar_at_MRF_Promotion_Event.jpg'),
        
        ('Virat Kohli', 'India', 'Batsman', 'Virat Kohli is an Indian international cricketer and former captain. He is widely regarded as one of the greatest batsmen of all time. Known for his aggressive batting style and exceptional chase master abilities, he has scored over 26,000 international runs.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Virat_Kohli_during_the_India_vs_Aus_4th_Test_match_at_Narendra_Modi_Stadium_on_09_March_2023.jpg/400px-Virat_Kohli_during_the_India_vs_Aus_4th_Test_match_at_Narendra_Modi_Stadium_on_09_March_2023.jpg'),
        
        ('MS Dhoni', 'India', 'Wicketkeeper-Batsman', 'Mahendra Singh Dhoni is one of the most successful captains in cricket history. He led India to victory in the 2007 T20 World Cup, 2011 ODI World Cup, and 2013 Champions Trophy. Known for his calm demeanor and finishing abilities, he is called "Captain Cool".', 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Mahendra_Singh_Dhoni_January_2016_%28cropped%29.jpg/400px-Mahendra_Singh_Dhoni_January_2016_%28cropped%29.jpg'),
        
        ('Kapil Dev', 'India', 'All-rounder', 'Kapil Dev Nikhanj is a former Indian cricketer who captained India to their first World Cup victory in 1983. He was one of the greatest all-rounders in cricket history, taking 434 Test wickets and scoring over 5,000 Test runs.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Kapil_Dev_at_IIMC_Alumni_Association%27s_%27IMPACT_2010%27.jpg/400px-Kapil_Dev_at_IIMC_Alumni_Association%27s_%27IMPACT_2010%27.jpg'),
        
        ('Sunil Gavaskar', 'India', 'Batsman', 'Sunil Manohar Gavaskar was the first batsman to score 10,000 runs in Test cricket. Known for his technique against fast bowling, he scored 34 Test centuries and was one of the greatest opening batsmen in cricket history.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Sunil_Gavaskar_2011.jpg/400px-Sunil_Gavaskar_2011.jpg'),
        
        ('Rahul Dravid', 'India', 'Batsman', 'Rahul Sharad Dravid, known as "The Wall", was one of the greatest batsmen in Test cricket. He scored 13,288 Test runs with 36 centuries. Known for his solid technique and dependability, he is now the head coach of the Indian cricket team.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Rahul_Dravid_at_IIMB.jpg/400px-Rahul_Dravid_at_IIMB.jpg'),
        
        ('Sourav Ganguly', 'India', 'Batsman', 'Sourav Chandidas Ganguly, known as "Dada", was one of India\'s most successful captains. He transformed Indian cricket with his aggressive leadership and scored over 18,000 international runs. He is currently the President of BCCI.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Sourav_Ganguly_at_Madame_Tussauds_Delhi.jpg/400px-Sourav_Ganguly_at_Madame_Tussauds_Delhi.jpg'),
        
        ('Virender Sehwag', 'India', 'Batsman', 'Virender Sehwag was one of the most destructive batsmen in cricket history. Known for his aggressive opening batting, he scored two triple centuries in Test cricket and holds the record for the highest individual score by an Indian in Tests (319).', 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Virender_Sehwag_in_2018.jpg/400px-Virender_Sehwag_in_2018.jpg'),
        
        ('Anil Kumble', 'India', 'Bowler', 'Anil Radhakrishna Kumble is the third-highest wicket-taker in Test cricket with 619 wickets. He is the only Indian bowler to take all 10 wickets in a Test innings. Known for his accuracy and stamina, he was nicknamed "Jumbo".', 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Anil_Kumble_at_IIMB.jpg/400px-Anil_Kumble_at_IIMB.jpg'),
        
        ('Harbhajan Singh', 'India', 'Bowler', 'Harbhajan Singh is one of India\'s most successful off-spinners with 417 Test wickets. He is famous for his hat-trick against Australia in 2001 and played a crucial role in India\'s 2011 World Cup victory.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Harbhajan_Singh_2011.jpg/400px-Harbhajan_Singh_2011.jpg'),
        
        ('Rohit Sharma', 'India', 'Batsman', 'Rohit Gurunath Sharma is the current captain of the Indian cricket team. He holds the record for the highest individual score in ODIs (264) and has three double centuries in ODIs. Known as "Hitman" for his explosive batting.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Rohit_Sharma.jpg/400px-Rohit_Sharma.jpg'),
        
        ('Jasprit Bumrah', 'India', 'Bowler', 'Jasprit Jasbirsingh Bumrah is one of the best fast bowlers in modern cricket. Known for his unique bowling action and deadly yorkers, he is highly effective in all formats. He is currently India\'s premier fast bowler.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Jasprit_Bumrah.jpg/400px-Jasprit_Bumrah.jpg'),
        
        ('Ravichandran Ashwin', 'India', 'All-rounder', 'Ravichandran Ashwin is one of the greatest off-spinners in cricket history with over 500 Test wickets. He is known for his variations and has won multiple ICC awards. He is also a capable lower-order batsman.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Ravichandran_Ashwin.jpg/400px-Ravichandran_Ashwin.jpg'),
        
        ('Yuvraj Singh', 'India', 'All-rounder', 'Yuvraj Singh was one of India\'s greatest match-winners. He was the Player of the Tournament in the 2011 World Cup and is famous for hitting six sixes in an over against England in the 2007 T20 World Cup.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Yuvraj_Singh_2016.jpg/400px-Yuvraj_Singh_2016.jpg'),
        
        ('Zaheer Khan', 'India', 'Bowler', 'Zaheer Khan is one of India\'s greatest fast bowlers with 311 Test wickets. He was the leading wicket-taker in the 2011 World Cup and known for his ability to swing the ball both ways.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Zaheer_Khan_2011.jpg/400px-Zaheer_Khan_2011.jpg'),
        
        # Australian Legends
        ('Don Bradman', 'Australia', 'Batsman', 'Sir Donald George Bradman is widely considered the greatest batsman of all time. His Test batting average of 99.94 is often cited as the greatest achievement in any major sport. He scored 29 Test centuries in just 52 Tests.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Don_Bradman_1930.jpg/400px-Don_Bradman_1930.jpg'),
        
        ('Ricky Ponting', 'Australia', 'Batsman', 'Ricky Thomas Ponting is one of the most successful captains in cricket history. He led Australia to two World Cup victories (2003, 2007) and scored over 27,000 international runs with 71 centuries across formats.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Ricky_Ponting_2014.jpg/400px-Ricky_Ponting_2014.jpg'),
        
        ('Shane Warne', 'Australia', 'Bowler', 'Shane Keith Warne was one of the greatest bowlers in cricket history. The legendary leg-spinner took 708 Test wickets and revolutionized spin bowling. His "Ball of the Century" to Mike Gatting in 1993 is iconic.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Shane_Warne_2012.jpg/400px-Shane_Warne_2012.jpg'),
        
        ('Glenn McGrath', 'Australia', 'Bowler', 'Glenn Donald McGrath is one of the greatest fast bowlers with 563 Test wickets. Known for his accuracy and bounce, he was a key member of Australia\'s dominant team. He took 71 wickets in World Cups.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Glenn_McGrath_2014.jpg/400px-Glenn_McGrath_2014.jpg'),
        
        ('Adam Gilchrist', 'Australia', 'Wicketkeeper-Batsman', 'Adam Craig Gilchrist revolutionized wicketkeeper-batting with his aggressive style. He scored over 15,000 international runs and effected 905 dismissals. His strike rate of 81.95 in Tests is remarkable for a wicketkeeper.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Adam_Gilchrist_2011.jpg/400px-Adam_Gilchrist_2011.jpg'),
        
        ('Steve Waugh', 'Australia', 'Batsman', 'Stephen Rodger Waugh was one of Australia\'s most successful captains. He never lost a Test series as captain and scored over 18,000 international runs. Known for his mental toughness and fighting spirit.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Steve_Waugh_2011.jpg/400px-Steve_Waugh_2011.jpg'),
        
        ('Brett Lee', 'Australia', 'Bowler', 'Brett Lee was one of the fastest bowlers in cricket history, regularly bowling over 150 km/h. He took 718 international wickets and was known for his aggressive pace and yorkers. He was also a handy lower-order batsman.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Brett_Lee_2011.jpg/400px-Brett_Lee_2011.jpg'),
        
        ('Matthew Hayden', 'Australia', 'Batsman', 'Matthew Lawrence Hayden was one of the most dominant opening batsmen. He scored over 15,000 international runs and held the record for the highest individual Test score (380) for several years.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Matthew_Hayden_2011.jpg/400px-Matthew_Hayden_2011.jpg'),
        
        ('Michael Clarke', 'Australia', 'Batsman', 'Michael John Clarke was Australia\'s captain and one of their finest batsmen. He scored over 17,000 international runs including 28 Test centuries. He led Australia to the 2015 World Cup victory.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Michael_Clarke_2015.jpg/400px-Michael_Clarke_2015.jpg'),
        
        ('David Warner', 'Australia', 'Batsman', 'David Andrew Warner is one of the most explosive opening batsmen in modern cricket. He has scored over 18,000 international runs and is known for his aggressive batting style in all formats.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/David_Warner_2018.jpg/400px-David_Warner_2018.jpg'),
        
        ('Steve Smith', 'Australia', 'Batsman', 'Steven Peter Devereux Smith is one of the best Test batsmen of the modern era. He has scored over 15,000 international runs with a Test average over 60. Known for his unorthodox technique and concentration.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Steve_Smith_2019.jpg/400px-Steve_Smith_2019.jpg'),
        
        ('Mitchell Starc', 'Australia', 'Bowler', 'Mitchell Aaron Starc is one of the best left-arm fast bowlers in cricket. He holds the record for most wickets in a single World Cup (27 in 2019) and is known for his deadly yorkers and pace.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Mitchell_Starc_2019.jpg/400px-Mitchell_Starc_2019.jpg'),
        
        # West Indies Legends
        ('Brian Lara', 'West Indies', 'Batsman', 'Brian Charles Lara holds the record for the highest individual score in Test cricket (400*) and first-class cricket (501*). He scored over 22,000 international runs and is considered one of the greatest batsmen ever.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Brian_Lara_2013.jpg/400px-Brian_Lara_2013.jpg'),
        
        ('Viv Richards', 'West Indies', 'Batsman', 'Sir Isaac Vivian Alexander Richards is regarded as one of the greatest batsmen in cricket history. He scored over 15,000 international runs with a strike rate that was revolutionary for his era. He never wore a helmet.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Viv_Richards_2012.jpg/400px-Viv_Richards_2012.jpg'),
        
        ('Curtly Ambrose', 'West Indies', 'Bowler', 'Curtly Elconn Lynwall Ambrose was one of the most feared fast bowlers with 630 international wickets. Standing at 6\'7", he generated steep bounce and was known for his intimidating presence and accuracy.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Curtly_Ambrose_2011.jpg/400px-Curtly_Ambrose_2011.jpg'),
        
        ('Courtney Walsh', 'West Indies', 'Bowler', 'Courtney Andrew Walsh was the first bowler to take 500 Test wickets. He took 519 Test wickets and 227 ODI wickets. Known for his stamina and longevity, he bowled over 30,000 balls in Test cricket.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Courtney_Walsh_2011.jpg/400px-Courtney_Walsh_2011.jpg'),
        
        ('Garfield Sobers', 'West Indies', 'All-rounder', 'Sir Garfield St Aubrun Sobers is widely considered the greatest all-rounder in cricket history. He scored over 8,000 Test runs and took 235 wickets. He was the first batsman to hit six sixes in an over in first-class cricket.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Garfield_Sobers_2012.jpg/400px-Garfield_Sobers_2012.jpg'),
        
        ('Chris Gayle', 'West Indies', 'Batsman', 'Christopher Henry Gayle is one of the most destructive batsmen in T20 cricket. He holds the record for the highest individual score in a World Cup (215). Known as "Universe Boss", he has hit over 1,000 international sixes.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Chris_Gayle_2019.jpg/400px-Chris_Gayle_2019.jpg'),
        
        ('Malcolm Marshall', 'West Indies', 'Bowler', 'Malcolm Denzil Marshall is considered one of the greatest fast bowlers ever. He took 376 Test wickets at an average of 20.94. Despite his relatively small stature for a fast bowler, he was extremely quick and skillful.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Malcolm_Marshall_1984.jpg/400px-Malcolm_Marshall_1984.jpg'),
        
        ('Clive Lloyd', 'West Indies', 'All-rounder', 'Clive Hubert Lloyd was the captain who led West Indies to dominance in the 1970s and 80s. He led them to two World Cup victories (1975, 1979) and scored over 12,000 international runs.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Clive_Lloyd_2011.jpg/400px-Clive_Lloyd_2011.jpg'),
        
        # Pakistani Legends
        ('Wasim Akram', 'Pakistan', 'Bowler', 'Wasim Akram is regarded as one of the greatest left-arm fast bowlers and the best exponent of swing bowling. He took 916 international wickets and was known for his deadly yorkers and reverse swing mastery.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Wasim_Akram_2012.jpg/400px-Wasim_Akram_2012.jpg'),
        
        ('Imran Khan', 'Pakistan', 'All-rounder', 'Imran Khan Niazi was one of cricket\'s greatest all-rounders and captains. He led Pakistan to their only World Cup victory in 1992. He took 362 Test wickets and scored over 7,000 international runs. He is now the Prime Minister of Pakistan.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Imran_Khan_1983.jpg/400px-Imran_Khan_1983.jpg'),
        
        ('Waqar Younis', 'Pakistan', 'Bowler', 'Waqar Younis was one of the most destructive fast bowlers, taking 789 international wickets. He was famous for his toe-crushing yorkers and reverse swing. He formed a lethal partnership with Wasim Akram.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Waqar_Younis_2011.jpg/400px-Waqar_Younis_2011.jpg'),
        
        ('Javed Miandad', 'Pakistan', 'Batsman', 'Javed Miandad is one of Pakistan\'s greatest batsmen with over 16,000 international runs. He is famous for hitting a last-ball six to win a match against India in 1986. Known for his fighting spirit and technique.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Javed_Miandad_2011.jpg/400px-Javed_Miandad_2011.jpg'),
        
        ('Inzamam-ul-Haq', 'Pakistan', 'Batsman', 'Inzamam-ul-Haq scored over 20,000 international runs and was one of Pakistan\'s most successful batsmen. He was known for his wristy strokeplay and ability to play under pressure. He later became Pakistan\'s chief selector.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Inzamam-ul-Haq_2011.jpg/400px-Inzamam-ul-Haq_2011.jpg'),
        
        ('Shahid Afridi', 'Pakistan', 'All-rounder', 'Shahid Khan Afridi, known as "Boom Boom", was one of cricket\'s most explosive all-rounders. He held the record for the fastest ODI century (37 balls) for 17 years and took over 500 international wickets with his leg-spin.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Shahid_Afridi_2011.jpg/400px-Shahid_Afridi_2011.jpg'),
        
        ('Younis Khan', 'Pakistan', 'Batsman', 'Younis Khan is Pakistan\'s highest Test run-scorer with 10,099 runs. He scored 34 Test centuries and was known for his gritty batting and ability to play long innings. He captained Pakistan to the 2009 T20 World Cup victory.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Younis_Khan_2016.jpg/400px-Younis_Khan_2016.jpg'),
        
        ('Babar Azam', 'Pakistan', 'Batsman', 'Babar Azam is the current captain of Pakistan and one of the best batsmen in modern cricket. He has scored over 12,000 international runs and is known for his elegant strokeplay and consistency across all formats.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Babar_Azam_2019.jpg/400px-Babar_Azam_2019.jpg'),
        
        # English Legends
        ('James Anderson', 'England', 'Bowler', 'James Michael Anderson is the highest wicket-taking fast bowler in Test cricket with over 680 wickets. He is a master of swing bowling and has been England\'s premier fast bowler for nearly two decades.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/James_Anderson_2019.jpg/400px-James_Anderson_2019.jpg'),
        
        ('Ian Botham', 'England', 'All-rounder', 'Sir Ian Terence Botham is one of cricket\'s greatest all-rounders. He scored over 7,000 international runs and took over 500 wickets. He is famous for his match-winning performances in the 1981 Ashes series.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Ian_Botham_2011.jpg/400px-Ian_Botham_2011.jpg'),
        
        ('Kevin Pietersen', 'England', 'Batsman', 'Kevin Peter Pietersen is one of England\'s greatest batsmen with over 13,000 international runs. Known for his aggressive batting and switch-hit shot, he scored 23 Test centuries including a famous 186 against India.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Kevin_Pietersen_2013.jpg/400px-Kevin_Pietersen_2013.jpg'),
        
        ('Alastair Cook', 'England', 'Batsman', 'Sir Alastair Nathan Cook is England\'s highest Test run-scorer with 12,472 runs. He scored 33 Test centuries and captained England to an Ashes victory in Australia. Known for his solid opening batting technique.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Alastair_Cook_2018.jpg/400px-Alastair_Cook_2018.jpg'),
        
        ('Andrew Flintoff', 'England', 'All-rounder', 'Andrew Flintoff was one of England\'s greatest all-rounders. He was the Player of the Series in the famous 2005 Ashes victory. He scored over 7,000 international runs and took 400 wickets.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Andrew_Flintoff_2009.jpg/400px-Andrew_Flintoff_2009.jpg'),
        
        ('Joe Root', 'England', 'Batsman', 'Joseph Edward Root is one of England\'s finest batsmen with over 20,000 international runs. He has scored over 30 Test centuries and is known for his classical technique and consistency across all conditions.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Joe_Root_2019.jpg/400px-Joe_Root_2019.jpg'),
        
        ('Ben Stokes', 'England', 'All-rounder', 'Benjamin Andrew Stokes is one of the best all-rounders in modern cricket. He is famous for his match-winning performances including the 2019 World Cup final and Headingley 2019 Ashes Test. He is currently England\'s Test captain.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Ben_Stokes_2019.jpg/400px-Ben_Stokes_2019.jpg'),
        
        ('Stuart Broad', 'England', 'Bowler', 'Stuart Christopher John Broad is one of England\'s greatest fast bowlers with over 600 Test wickets. He is famous for taking 8/15 against Australia at Trent Bridge in 2015. He forms a legendary partnership with James Anderson.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Stuart_Broad_2019.jpg/400px-Stuart_Broad_2019.jpg'),
        
        # South African Legends
        ('Jacques Kallis', 'South Africa', 'All-rounder', 'Jacques Henry Kallis is considered one of the greatest all-rounders in cricket history. He scored over 25,000 international runs and took 577 wickets. He is the only player to score 10,000+ runs and take 250+ wickets in both Tests and ODIs.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Jacques_Kallis_2012.jpg/400px-Jacques_Kallis_2012.jpg'),
        
        ('AB de Villiers', 'South Africa', 'Batsman', 'Abraham Benjamin de Villiers is one of the most innovative and destructive batsmen in cricket history. He holds the record for the fastest ODI century (31 balls) and scored over 20,000 international runs. Known as "Mr. 360".', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/AB_de_Villiers_2015.jpg/400px-AB_de_Villiers_2015.jpg'),
        
        ('Dale Steyn', 'South Africa', 'Bowler', 'Dale Willem Steyn is regarded as one of the greatest fast bowlers in cricket history. He took 699 international wickets and was the number one ranked Test bowler for a record 263 weeks. Known for his pace and reverse swing.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Dale_Steyn_2019.jpg/400px-Dale_Steyn_2019.jpg'),
        
        ('Shaun Pollock', 'South Africa', 'All-rounder', 'Shaun Maclean Pollock was one of South Africa\'s greatest all-rounders. He took 829 international wickets and scored over 7,000 runs. He was known for his accuracy and was one of the best new-ball bowlers.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Shaun_Pollock_2011.jpg/400px-Shaun_Pollock_2011.jpg'),
        
        ('Graeme Smith', 'South Africa', 'Batsman', 'Graeme Craig Smith was South Africa\'s most successful Test captain. He scored over 17,000 international runs including 27 Test centuries. He became captain at age 22 and led South Africa for a decade.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Graeme_Smith_2014.jpg/400px-Graeme_Smith_2014.jpg'),
        
        ('Hashim Amla', 'South Africa', 'Batsman', 'Hashim Mahomed Amla is one of South Africa\'s greatest batsmen with over 18,000 international runs. He was the fastest to reach 2,000, 3,000, 4,000, 5,000, 6,000, and 7,000 ODI runs. Known for his elegant strokeplay.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Hashim_Amla_2015.jpg/400px-Hashim_Amla_2015.jpg'),
        
        ('Allan Donald', 'South Africa', 'Bowler', 'Allan Anthony Donald was one of the fastest and most feared bowlers in cricket. He took 590 international wickets and was known as "White Lightning". He was South Africa\'s premier fast bowler in the 1990s.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Allan_Donald_2011.jpg/400px-Allan_Donald_2011.jpg'),
        
        ('Quinton de Kock', 'South Africa', 'Wicketkeeper-Batsman', 'Quinton de Kock is one of the best wicketkeeper-batsmen in modern cricket. He has scored over 10,000 international runs and is known for his aggressive batting style. He has captained South Africa in limited-overs cricket.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Quinton_de_Kock_2019.jpg/400px-Quinton_de_Kock_2019.jpg'),
        
        # Sri Lankan Legends
        ('Kumar Sangakkara', 'Sri Lanka', 'Wicketkeeper-Batsman', 'Kumar Chokshanada Sangakkara is one of the greatest batsmen in cricket history. He scored over 28,000 international runs with 63 international centuries. He is the only batsman to score four consecutive ODI centuries.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Kumar_Sangakkara_2015.jpg/400px-Kumar_Sangakkara_2015.jpg'),
        
        ('Muttiah Muralitharan', 'Sri Lanka', 'Bowler', 'Muttiah Muralitharan is the highest wicket-taker in international cricket with 1,347 wickets. He took 800 Test wickets and 534 ODI wickets. His unique bowling action and variations made him nearly unplayable.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Muttiah_Muralitharan_2011.jpg/400px-Muttiah_Muralitharan_2011.jpg'),
        
        ('Mahela Jayawardene', 'Sri Lanka', 'Batsman', 'Mahela Jayawardene scored over 25,000 international runs with 54 international centuries. He was one of the most elegant batsmen and a brilliant tactician. He led Sri Lanka to the 2011 World Cup final.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Mahela_Jayawardene_2014.jpg/400px-Mahela_Jayawardene_2014.jpg'),
        
        ('Sanath Jayasuriya', 'Sri Lanka', 'All-rounder', 'Sanath Teran Jayasuriya revolutionized ODI cricket with his aggressive opening batting. He scored over 21,000 international runs and took 440 wickets. He was a key member of Sri Lanka\'s 1996 World Cup winning team.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Sanath_Jayasuriya_2011.jpg/400px-Sanath_Jayasuriya_2011.jpg'),
        
        ('Lasith Malinga', 'Sri Lanka', 'Bowler', 'Lasith Malinga is one of the greatest limited-overs bowlers with his unique slinging action. He took 546 international wickets and is famous for his deadly yorkers. He is the only bowler with three ODI hat-tricks.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Lasith_Malinga_2019.jpg/400px-Lasith_Malinga_2019.jpg'),
        
        ('Arjuna Ranatunga', 'Sri Lanka', 'Batsman', 'Arjuna Ranatunga captained Sri Lanka to their first and only World Cup victory in 1996. He scored over 12,000 international runs and was known for his leadership and tactical acumen.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Arjuna_Ranatunga_2011.jpg/400px-Arjuna_Ranatunga_2011.jpg'),
        
        # New Zealand Legends
        ('Richard Hadlee', 'New Zealand', 'All-rounder', 'Sir Richard John Hadlee is one of the greatest fast bowlers and all-rounders. He was the first bowler to take 400 Test wickets and scored over 3,000 Test runs. He dominated world cricket in the 1980s.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Richard_Hadlee_2011.jpg/400px-Richard_Hadlee_2011.jpg'),
        
        ('Kane Williamson', 'New Zealand', 'Batsman', 'Kane Stuart Williamson is New Zealand\'s captain and one of the best batsmen in modern cricket. He has scored over 17,000 international runs and led New Zealand to the 2019 and 2021 World Cup finals. Known for his calm demeanor.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Kane_Williamson_2019.jpg/400px-Kane_Williamson_2019.jpg'),
        
        ('Brendon McCullum', 'New Zealand', 'Batsman', 'Brendon Barrie McCullum was one of the most aggressive batsmen in cricket. He scored the fastest Test century (54 balls) and over 14,000 international runs. He revolutionized New Zealand cricket with his attacking approach.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Brendon_McCullum_2015.jpg/400px-Brendon_McCullum_2015.jpg'),
        
        ('Martin Crowe', 'New Zealand', 'Batsman', 'Martin David Crowe was one of New Zealand\'s greatest batsmen. He scored over 10,000 international runs and was known for his elegant strokeplay and innovative thinking about the game.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Martin_Crowe_2011.jpg/400px-Martin_Crowe_2011.jpg'),
        
        ('Daniel Vettori', 'New Zealand', 'All-rounder', 'Daniel Luca Vettori is New Zealand\'s leading wicket-taker with 705 international wickets. He was one of the best left-arm spinners and a capable batsman. He captained New Zealand in all formats.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Daniel_Vettori_2015.jpg/400px-Daniel_Vettori_2015.jpg'),
        
        ('Ross Taylor', 'New Zealand', 'Batsman', 'Luteru Ross Poutoa Lote Taylor is New Zealand\'s leading run-scorer in ODIs and Tests combined. He scored over 18,000 international runs and was known for his ability to play under pressure.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Ross_Taylor_2019.jpg/400px-Ross_Taylor_2019.jpg'),
        
        # Bangladesh Legends
        ('Shakib Al Hasan', 'Bangladesh', 'All-rounder', 'Shakib Al Hasan is the greatest cricketer from Bangladesh and one of the best all-rounders in the world. He has scored over 12,000 runs and taken over 650 wickets in international cricket. He has been ranked number one all-rounder multiple times.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Shakib_Al_Hasan_2019.jpg/400px-Shakib_Al_Hasan_2019.jpg'),
        
        ('Mushfiqur Rahim', 'Bangladesh', 'Wicketkeeper-Batsman', 'Mushfiqur Rahim is Bangladesh\'s leading run-scorer in Tests and one of their best batsmen. He has scored over 15,000 international runs and is known for his fighting spirit and wicketkeeping skills.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Mushfiqur_Rahim_2019.jpg/400px-Mushfiqur_Rahim_2019.jpg'),
        
        ('Tamim Iqbal', 'Bangladesh', 'Batsman', 'Tamim Iqbal Khan is Bangladesh\'s leading run-scorer in ODIs with over 14,000 international runs. He is known for his aggressive opening batting and has been a key player in Bangladesh\'s rise in international cricket.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Tamim_Iqbal_2019.jpg/400px-Tamim_Iqbal_2019.jpg'),
        
        # Zimbabwe Legends
        ('Andy Flower', 'Zimbabwe', 'Wicketkeeper-Batsman', 'Andrew Flower is Zimbabwe\'s greatest cricketer. He scored over 9,000 international runs with a Test average of 51.54. He later became England\'s coach and led them to three Ashes victories.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Andy_Flower_2011.jpg/400px-Andy_Flower_2011.jpg'),
        
        ('Heath Streak', 'Zimbabwe', 'All-rounder', 'Heath Hilton Streak is Zimbabwe\'s leading wicket-taker with 455 international wickets. He was one of the best all-rounders and captained Zimbabwe. He scored over 4,000 international runs.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Heath_Streak_2011.jpg/400px-Heath_Streak_2011.jpg'),
        
        # Afghanistan Legends
        ('Rashid Khan', 'Afghanistan', 'Bowler', 'Rashid Khan Arman is one of the best leg-spinners in modern cricket. Despite his young age, he has taken over 400 international wickets and is known for his variations and economy. He is a T20 specialist.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Rashid_Khan_2019.jpg/400px-Rashid_Khan_2019.jpg'),
        
        ('Mohammad Nabi', 'Afghanistan', 'All-rounder', 'Mohammad Nabi Eisakhil is Afghanistan\'s most experienced cricketer and a quality all-rounder. He has scored over 6,000 international runs and taken over 300 wickets. He is a key player in Afghanistan\'s rise.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Mohammad_Nabi_2019.jpg/400px-Mohammad_Nabi_2019.jpg'),
        
        # Additional Modern Stars
        ('Virat Kohli', 'India', 'Batsman', 'One of the greatest batsmen across all formats with exceptional consistency and fitness.', 'https://via.placeholder.com/400x300/667eea/ffffff?text=Virat+Kohli'),
        
        ('Pat Cummins', 'Australia', 'Bowler', 'Patrick James Cummins is Australia\'s Test captain and one of the best fast bowlers in the world. He has taken over 500 international wickets and is known for his pace, accuracy, and stamina.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Pat_Cummins_2019.jpg/400px-Pat_Cummins_2019.jpg'),
        
        ('Trent Boult', 'New Zealand', 'Bowler', 'Trent Alexander Boult is one of the best left-arm fast bowlers in cricket. He has taken over 600 international wickets and is known for his ability to swing the ball both ways. He was crucial in New Zealand\'s World Cup campaigns.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Trent_Boult_2019.jpg/400px-Trent_Boult_2019.jpg'),
        
        ('Kagiso Rabada', 'South Africa', 'Bowler', 'Kagiso Rabada is one of the fastest and most skillful bowlers in modern cricket. He has taken over 450 international wickets and is known for his pace, aggression, and ability to take wickets in all conditions.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Kagiso_Rabada_2019.jpg/400px-Kagiso_Rabada_2019.jpg'),
        
        ('Jos Buttler', 'England', 'Wicketkeeper-Batsman', 'Joseph Charles Buttler is one of the most innovative and destructive batsmen in limited-overs cricket. He was crucial in England\'s 2019 World Cup victory and is known for his reverse sweeps and ramp shots.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Jos_Buttler_2019.jpg/400px-Jos_Buttler_2019.jpg'),
        
        ('Faf du Plessis', 'South Africa', 'Batsman', 'Francois du Plessis is a former South African captain and one of their best batsmen. He has scored over 15,000 international runs and is known for his fighting spirit and ability to play under pressure.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Faf_du_Plessis_2019.jpg/400px-Faf_du_Plessis_2019.jpg'),
        
        ('Angelo Mathews', 'Sri Lanka', 'All-rounder', 'Angelo Davis Mathews is Sri Lanka\'s premier all-rounder. He has scored over 11,000 international runs and taken over 200 wickets. He led Sri Lanka to the 2014 T20 World Cup victory.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Angelo_Mathews_2019.jpg/400px-Angelo_Mathews_2019.jpg'),
        
        ('Jonny Bairstow', 'England', 'Wicketkeeper-Batsman', 'Jonathan Marc Bairstow is one of England\'s most aggressive batsmen. He has scored over 11,000 international runs and is known for his attacking style in all formats, especially in Test cricket\'s "Bazball" era.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Jonny_Bairstow_2019.jpg/400px-Jonny_Bairstow_2019.jpg'),
        
        ('Mohammad Amir', 'Pakistan', 'Bowler', 'Mohammad Amir is one of the most talented left-arm fast bowlers. He has taken over 250 international wickets and is known for his ability to swing the ball at pace. He was Player of the Tournament in the 2009 T20 World Cup.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Mohammad_Amir_2017.jpg/400px-Mohammad_Amir_2017.jpg'),
        
        ('Ravindra Jadeja', 'India', 'All-rounder', 'Ravindrasinh Anirudhsinh Jadeja is one of the best all-rounders in Test cricket. He has taken over 500 international wickets and scored over 5,000 runs. He is also one of the best fielders in the world.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Ravindra_Jadeja_2019.jpg/400px-Ravindra_Jadeja_2019.jpg'),
        
        ('KL Rahul', 'India', 'Batsman', 'Kannur Lokesh Rahul is one of India\'s most elegant batsmen. He has scored over 7,000 international runs and holds the record for the fastest Test century by an Indian (100 off 52 balls). He also keeps wickets.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/KL_Rahul_2019.jpg/400px-KL_Rahul_2019.jpg'),
        
        ('Hardik Pandya', 'India', 'All-rounder', 'Hardik Himanshu Pandya is India\'s premier all-rounder in limited-overs cricket. He is known for his big-hitting abilities and useful medium-pace bowling. He led India to the 2024 T20 World Cup victory.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Hardik_Pandya_2019.jpg/400px-Hardik_Pandya_2019.jpg'),
        
        ('Shikhar Dhawan', 'India', 'Batsman', 'Shikhar Dhawan is one of India\'s most successful opening batsmen in limited-overs cricket. He has scored over 10,000 international runs and is known for his aggressive batting in ICC tournaments.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Shikhar_Dhawan_2019.jpg/400px-Shikhar_Dhawan_2019.jpg'),
        
        ('Rishabh Pant', 'India', 'Wicketkeeper-Batsman', 'Rishabh Rajendra Pant is one of the most exciting wicketkeeper-batsmen in cricket. He is known for his fearless batting and match-winning abilities. He has scored multiple Test centuries in Australia and England.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Rishabh_Pant_2019.jpg/400px-Rishabh_Pant_2019.jpg'),
        
        ('Shubman Gill', 'India', 'Batsman', 'Shubman Gill is one of the most promising young batsmen in world cricket. He has already scored over 3,000 international runs and is known for his elegant strokeplay and consistency.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Shubman_Gill_2023.jpg/400px-Shubman_Gill_2023.jpg'),
        
        ('Mohammad Rizwan', 'Pakistan', 'Wicketkeeper-Batsman', 'Mohammad Rizwan is Pakistan\'s premier wicketkeeper-batsman. He has scored over 5,000 international runs and is known for his consistency in T20 cricket. He holds multiple records in T20 internationals.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Mohammad_Rizwan_2021.jpg/400px-Mohammad_Rizwan_2021.jpg'),
        
        ('Shaheen Afridi', 'Pakistan', 'Bowler', 'Shaheen Shah Afridi is one of the best young fast bowlers in cricket. He has taken over 200 international wickets and is known for his ability to swing the ball at pace. He can bowl deadly yorkers.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Shaheen_Afridi_2021.jpg/400px-Shaheen_Afridi_2021.jpg'),
        
        ('Marnus Labuschagne', 'Australia', 'Batsman', 'Marnus Labuschagne is one of the best Test batsmen in the world. He has scored over 7,000 international runs with a Test average over 60. He is known for his quirky mannerisms and solid technique.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Marnus_Labuschagne_2021.jpg/400px-Marnus_Labuschagne_2021.jpg'),
        
        ('Travis Head', 'Australia', 'Batsman', 'Travis Michael Head is one of Australia\'s most destructive batsmen. He was Player of the Match in the 2023 World Cup final and 2023 WTC final. Known for his aggressive batting against spin.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Travis_Head_2023.jpg/400px-Travis_Head_2023.jpg'),
        
        ('Glenn Maxwell', 'Australia', 'All-rounder', 'Glenn James Maxwell is one of the most innovative batsmen in cricket. He is known for his reverse sweeps, switch hits, and big-hitting. He scored a double century while batting with cramps in the 2023 World Cup.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Glenn_Maxwell_2023.jpg/400px-Glenn_Maxwell_2023.jpg'),
        
        ('Marcus Stoinis', 'Australia', 'All-rounder', 'Marcus Stoinis is a powerful all-rounder known for his big-hitting and useful medium-pace bowling. He has been a key player for Australia in limited-overs cricket.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Marcus_Stoinis_2020.jpg/400px-Marcus_Stoinis_2020.jpg'),
        
        ('Josh Hazlewood', 'Australia', 'Bowler', 'Joshua Reginald Hazlewood is one of the best fast bowlers in Test cricket. He has taken over 250 Test wickets and is known for his accuracy and ability to hit the right areas consistently.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Josh_Hazlewood_2021.jpg/400px-Josh_Hazlewood_2021.jpg'),
        
        ('Sam Curran', 'England', 'All-rounder', 'Samuel Matthew Curran is one of the most expensive players in IPL history. He is a left-arm fast bowler and useful lower-order batsman. He was Player of the Tournament in the 2022 T20 World Cup.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Sam_Curran_2022.jpg/400px-Sam_Curran_2022.jpg'),
        
        ('Moeen Ali', 'England', 'All-rounder', 'Moeen Munir Ali is one of England\'s key all-rounders. He has scored over 6,000 international runs and taken over 350 wickets with his off-spin. He was crucial in England\'s 2019 World Cup victory.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Moeen_Ali_2019.jpg/400px-Moeen_Ali_2019.jpg'),
        
        ('Jofra Archer', 'England', 'Bowler', 'Jofra Chioke Archer is one of the fastest bowlers in cricket, regularly bowling over 150 km/h. He was crucial in England\'s 2019 World Cup victory, bowling the Super Over in the final.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Jofra_Archer_2019.jpg/400px-Jofra_Archer_2019.jpg'),
        
        ('Kieron Pollard', 'West Indies', 'All-rounder', 'Kieron Adrian Pollard is one of the most destructive all-rounders in T20 cricket. He has hit over 1,000 sixes in his career and is known for his big-hitting and useful medium-pace bowling.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Kieron_Pollard_2019.jpg/400px-Kieron_Pollard_2019.jpg'),
        
        ('Andre Russell', 'West Indies', 'All-rounder', 'Andre Dwayne Russell is one of the most explosive all-rounders in T20 cricket. He is known for his incredible power-hitting and fast bowling. He has won multiple T20 leagues around the world.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Andre_Russell_2019.jpg/400px-Andre_Russell_2019.jpg'),
        
        ('Suryakumar Yadav', 'India', 'Batsman', 'Suryakumar Ashok Yadav is one of the best T20 batsmen in the world. He is ranked number one in T20I rankings and is known for his 360-degree strokeplay and innovative shots.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Suryakumar_Yadav_2022.jpg/400px-Suryakumar_Yadav_2022.jpg'),
        
        ('Axar Patel', 'India', 'All-rounder', 'Axar Rajeshbhai Patel is an all-rounder known for his accurate left-arm spin and useful batting. He has been very successful in Test cricket at home, taking wickets consistently.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Axar_Patel_2021.jpg/400px-Axar_Patel_2021.jpg'),
        
        ('Mohammed Shami', 'India', 'Bowler', 'Mohammed Shami is one of India\'s best fast bowlers. He has taken over 450 international wickets and is known for his ability to reverse swing the ball and bowl deadly yorkers.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Mohammed_Shami_2023.jpg/400px-Mohammed_Shami_2023.jpg'),
        
        ('Bhuvneshwar Kumar', 'India', 'Bowler', 'Bhuvneshwar Kumar is one of the best swing bowlers in limited-overs cricket. He has taken over 300 international wickets and is known for his ability to swing the ball both ways.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Bhuvneshwar_Kumar_2019.jpg/400px-Bhuvneshwar_Kumar_2019.jpg'),
        
        ('Dinesh Karthik', 'India', 'Wicketkeeper-Batsman', 'Dinesh Karthik is one of the most experienced Indian cricketers. He is known for his finishing abilities in T20 cricket and has played for India across two decades.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Dinesh_Karthik_2022.jpg/400px-Dinesh_Karthik_2022.jpg'),
        
        ('Haris Rauf', 'Pakistan', 'Bowler', 'Haris Rauf is one of the fastest bowlers in cricket. He regularly bowls over 150 km/h and has been very successful in T20 cricket around the world.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Haris_Rauf_2022.jpg/400px-Haris_Rauf_2022.jpg'),
        
        ('Shadab Khan', 'Pakistan', 'All-rounder', 'Shadab Khan is Pakistan\'s premier leg-spinner and a useful lower-order batsman. He is known for his variations and has been a key player in Pakistan\'s limited-overs teams.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Shadab_Khan_2022.jpg/400px-Shadab_Khan_2022.jpg'),
        
        ('Fakhar Zaman', 'Pakistan', 'Batsman', 'Fakhar Zaman is one of Pakistan\'s most aggressive opening batsmen. He scored a match-winning century in the 2017 Champions Trophy final and has scored over 6,000 international runs.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Fakhar_Zaman_2019.jpg/400px-Fakhar_Zaman_2019.jpg'),
        
        ('Wanindu Hasaranga', 'Sri Lanka', 'All-rounder', 'Wanindu Hasaranga de Silva is one of the best leg-spinners in T20 cricket. He has taken over 150 international wickets and is also a useful lower-order batsman.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Wanindu_Hasaranga_2022.jpg/400px-Wanindu_Hasaranga_2022.jpg'),
        
        ('Pathum Nissanka', 'Sri Lanka', 'Batsman', 'Pathum Nissanka is one of Sri Lanka\'s most promising young batsmen. He has already scored over 2,000 international runs and is known for his solid technique.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Pathum_Nissanka_2022.jpg/400px-Pathum_Nissanka_2022.jpg'),
        
        ('Tim Southee', 'New Zealand', 'Bowler', 'Timothy Grant Southee is one of New Zealand\'s greatest fast bowlers. He has taken over 700 international wickets and is known for his ability to swing the ball.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Tim_Southee_2019.jpg/400px-Tim_Southee_2019.jpg'),
        
        ('Devon Conway', 'New Zealand', 'Batsman', 'Devon Philip Conway is one of New Zealand\'s most consistent batsmen. He scored a double century on his Test debut and has been very successful in all formats.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Devon_Conway_2021.jpg/400px-Devon_Conway_2021.jpg'),
        
        ('Daryl Mitchell', 'New Zealand', 'All-rounder', 'Daryl John Mitchell is one of New Zealand\'s best all-rounders. He has been very successful in Test cricket with multiple centuries and is also a useful medium-pace bowler.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Daryl_Mitchell_2022.jpg/400px-Daryl_Mitchell_2022.jpg'),
    ]
    
    # Clear existing data and insert new data
    c.execute('DELETE FROM cricketers')
    c.executemany('INSERT INTO cricketers (name, country, role, history, image_url) VALUES (?, ?, ?, ?, ?)', cricketers)
    
    print(f"Database initialized with {len(cricketers)} cricketers.")
    
    # Show count by country
    c.execute('SELECT country, COUNT(*) as count FROM cricketers GROUP BY country ORDER BY count DESC')
    print("\nCricketers by country:")
    for row in c.fetchall():
        print(f"  {row[0]}: {row[1]}")

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
