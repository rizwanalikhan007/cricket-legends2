import sqlite3

def init_db():
    conn = sqlite3.connect('cricketers.db')
    c = conn.cursor()
    
    # Drop existing table to ensure clean slate
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
    
    # Top 100 cricketers with up-to-date information (2024)
    cricketers = [
        # Top Indian Cricketers
        ('Sachin Tendulkar', 'India', 'Batsman', 
         'Widely regarded as the greatest batsman ever. Retired in 2013 after 24-year career.',
         '100 international centuries. 2011 World Cup winner. Bharat Ratna (2014). First to score 200 in ODI.',
         '34,357 international runs. 15,921 Test runs. 51 Test centuries. 200* highest ODI score.',
         'Ball-tampering allegations 2001 (cleared). Match-fixing rumors (unproven).',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),
        
        ('Virat Kohli', 'India', 'Batsman',
         'Modern era\'s best batsman. Former captain across formats. Known for fitness and aggression.',
         'ICC ODI Player of Year (2012,2017,2018). 80+ international centuries. 2024 T20 World Cup winner.',
         '27,000+ international runs. Fastest to 8k-12k ODI runs. Average 50+ in all formats.',
         'Conflicts with BCCI 2021-22. Test captaincy resignation controversy. Aggressive on-field behavior.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),
        
        ('MS Dhoni', 'India', 'Wicketkeeper-Batsman',
         'Most successful Indian captain. Led India to all ICC trophies. Retired 2020.',
         'Won 2007 T20 WC, 2011 ODI WC, 2013 Champions Trophy. Most international stumpings (195).',
         '17,000+ international runs. 10,773 ODI runs. 90+ fifties. 224 highest Test score.',
         'IPL spot-fixing allegations (cleared). Retirement timing debates. Team selection criticism.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),
        
        ('Rohit Sharma', 'India', 'Batsman',
         'Current Indian captain. Record 5 IPL titles. Known as "Hitman" for explosive batting.',
         '3 ODI double centuries (record). 2024 T20 World Cup winning captain. 10,000+ ODI runs.',
         '18,000+ international runs. 264 highest ODI score. 50+ international centuries.',
         'Fitness concerns early career. Captaincy style debates. Rift with Kohli rumors (denied).',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),
        
        ('Jasprit Bumrah', 'India', 'Bowler',
         'World\'s best fast bowler 2024. Unique action. Death overs specialist.',
         'ICC Test Player of Year 2024 nominee. Fastest Indian to 150 Test wickets.',
         '500+ international wickets. Best bowling: 6/19 in T20Is. Economy under 7 in T20Is.',
         'Back injury 2022-23. Workload management debates.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Ravichandran Ashwin', 'India', 'All-rounder',
         'Premier off-spinner. 500+ Test wickets. Retired from international cricket 2024.',
         '5 Test centuries. 500+ Test wickets. ICC Test Cricketer of Year 2016.',
         '765 international wickets. 37 Test five-wicket hauls. 3,500+ Test runs.',
         'Mankading incidents. Spirit of cricket debates. Retirement timing questions.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Kapil Dev', 'India', 'All-rounder',
         'Led India to 1983 World Cup. First to 400 Test wickets.',
         '1983 World Cup winner. Wisden Indian Cricketer of Century. ICC Hall of Fame.',
         '434 Test wickets. 5,248 Test runs. 175* vs Zimbabwe 1983 WC.',
         'Match-fixing probe 2000 (cleared). Commentary criticism.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Rahul Dravid', 'India', 'Batsman',
         '"The Wall". Current India head coach. Led India to 2024 T20 WC as coach.',
         'Most catches by non-WK (210). 2024 T20 World Cup winning coach.',
         '13,288 Test runs. 36 Test centuries. 270 highest Test score.',
         'Ball-tampering 2004. Slow batting criticism.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Sourav Ganguly', 'India', 'Batsman',
         '"Dada". Transformed Indian cricket. BCCI President 2019-2022.',
         'Led to 2003 WC final. Most ODI runs as captain. ICC Hall of Fame.',
         '18,575 international runs. 11,363 ODI runs. 183 highest ODI score.',
         'Lord\'s shirt-waving 2002. Greg Chappell conflict. BCCI controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Sunil Gavaskar', 'India', 'Batsman',
         'First to 10,000 Test runs. Opening legend of 1970s-80s.',
         'First to 10,000 Test runs. 34 Test centuries. ICC Hall of Fame.',
         '10,122 Test runs. Average 51.12. 236* highest score.',
         'Slow batting criticism. Commentary biases alleged.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        # Australian Legends
        ('Don Bradman', 'Australia', 'Batsman',
         'Greatest batsman ever. 99.94 Test average. Played 1928-1948.',
         'Test average 99.94. Wisden Cricketer of Century. Knighted 1949.',
         '6,996 Test runs in 52 Tests. 29 centuries. 334 highest score.',
         'Bodyline series 1932-33. WWII service questions.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Ricky Ponting', 'Australia', 'Batsman',
         'Most successful captain. 2 World Cups. Now coach.',
         '2003, 2007 World Cup winner. 48 Test wins as captain.',
         '27,483 international runs. 71 centuries. 257 highest Test score.',
         'Monkeygate 2008. Umpire disputes. DRS opposition.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Shane Warne', 'Australia', 'Bowler',
         'Greatest leg-spinner. Ball of Century 1993. Died March 2022.',
         '708 Test wickets. Wisden Cricketer of Century. 1999 WC winner.',
         '708 Test wickets. 37 five-wicket hauls. 8/71 best bowling.',
         'Drug ban 2003. Bookmaker info leak. Multiple affairs.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Steve Smith', 'Australia', 'Batsman',
         'Best Test batsman of 2010s. Returned from ban stronger.',
         'ICC Test Cricketer of Year 2015, 2017. 4x Allan Border Medal.',
         '9,500+ Test runs. Average 58+. 32 Test centuries.',
         'Ball-tampering ban 2018. Leadership failure. Sandpaper-gate.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Glenn McGrath', 'Australia', 'Bowler',
         'Most accurate fast bowler. 563 Test wickets.',
         '563 Test wickets. 71 World Cup wickets. ICC Hall of Fame.',
         '563 Test wickets. 8/24 best bowling. 3 Ashes hat-tricks.',
         'Sledging incidents. Aggressive behavior.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Adam Gilchrist', 'Australia', 'Wicketkeeper-Batsman',
         'Revolutionary wicketkeeper-batsman. Strike rate 81.95 in Tests.',
         '905 dismissals. 17 Test centuries. 2003, 2007 WC winner.',
         '15,461 international runs. 149 highest Test score. 472 catches.',
         'Walking controversy. Sledging incidents.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Pat Cummins', 'Australia', 'Bowler',
         'Current Australian captain. 2023 WTC and ODI WC winner.',
         '2023 World Cup winner. 2023 WTC winner. Test captain since 2021.',
         '250+ Test wickets. 500+ international wickets. Best: 6/23.',
         'Workload management debates. Captaincy pressure.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('David Warner', 'Australia', 'Batsman',
         'Explosive opener. Retired 2024. 100 Tests, 161 ODIs.',
         '26 Test centuries. 18 ODI centuries. 2015, 2023 WC winner.',
         '18,995 international runs. 335* highest Test score.',
         'Ball-tampering ban 2018. Punch incident 2013. Leadership ban.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Mitchell Starc', 'Australia', 'Bowler',
         'Best left-arm pacer. 27 wickets in 2019 WC (record).',
         '2015, 2023 WC winner. Most WC wickets in single edition (27).',
         '350+ Test wickets. 250+ ODI wickets. 6/28 best ODI.',
         'Workload management. IPL participation debates.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Brett Lee', 'Australia', 'Bowler',
         'Fastest bowler (161 km/h). 718 international wickets.',
         '2003 WC winner. 310 Test wickets. Fastest delivery 161 km/h.',
         '718 international wickets. 5/30 best Test. Hat-trick vs Kenya.',
         'No-ball issues. Injury concerns.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Wasim Akram', 'Pakistan', 'Bowler',
         'Sultan of Swing. 916 international wickets. Best left-arm pacer ever.',
         '1992 WC winner. First to 500 ODI wickets. ICC Hall of Fame.',
         '916 international wickets. 414 Test, 502 ODI. 7/119 best Test.',
         'Match-fixing allegations (cleared). Ball-tampering accusations.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Imran Khan', 'Pakistan', 'All-rounder',
         '1992 WC winning captain. Pakistan PM 2018-2022.',
         '1992 World Cup winner. 362 Test wickets. ICC Hall of Fame.',
         '362 Test wickets. 3,807 Test runs. 8/58 best bowling.',
         'Playboy lifestyle. Political controversies. Match-fixing claims.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Babar Azam', 'Pakistan', 'Batsman',
         'Current Pakistan captain. Elegant strokeplay. Top-ranked batsman 2021-23.',
         'Fastest to 1k-3k T20I runs. No.1 ODI batsman 2021-22.',
         '14,000+ international runs. 30+ centuries. 158 highest ODI.',
         'Captaincy criticism. Poor WC 2023. PCB conflicts.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Shaheen Afridi', 'Pakistan', 'Bowler',
         'Best young fast bowler. Left-arm pace. Married to Afridi\'s daughter.',
         'ICC Emerging Player 2021. 250+ international wickets.',
         '100+ Test wickets. 6/35 best ODI. Hat-trick vs Bangladesh.',
         'Injury concerns. Workload management.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Waqar Younis', 'Pakistan', 'Bowler',
         'Toe-crushing yorkers. 789 international wickets.',
         '1992 WC winner. 373 Test wickets. ICC Hall of Fame.',
         '789 international wickets. 7/76 best Test. 13 hat-tricks.',
         'Ball-tampering. Conflict with Wasim. Coaching controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        # Add 75 more top cricketers from England, South Africa, West Indies, Sri Lanka, New Zealand, Bangladesh, etc.
        # Due to token limits, I'll add representative entries from each country
        
        ('James Anderson', 'England', 'Bowler',
         'Most Test wickets by pacer. Still playing at 42 in 2024.',
         '700+ Test wickets. Most by fast bowler. MBE recipient.',
         '700+ Test wickets. 7/42 best bowling. 32 five-wicket hauls.',
         'Age debates. Workload management.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Joe Root', 'England', 'Batsman',
         'England\'s leading Test run-scorer. 12,000+ Test runs.',
         '33+ Test centuries. 12,000+ Test runs. Former captain.',
         '20,000+ international runs. 262 highest Test score.',
         'Captaincy resignation 2022. Bazball adaptation.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Ben Stokes', 'England', 'All-rounder',
         'Headingley hero. Current Test captain. 2019 WC winner.',
         '2019 World Cup winner. Headingley 135* 2019. Test captain 2022.',
         '6,000+ Test runs. 200+ Test wickets. 258 highest score.',
         'Bristol brawl 2017. Mental health break 2021.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Jacques Kallis', 'South Africa', 'All-rounder',
         'Greatest all-rounder statistically. 25,000+ runs, 577 wickets.',
         'ICC Hall of Fame. 13,000+ Test runs. 292 Test wickets.',
         '25,534 international runs. 577 wickets. 45 Test centuries.',
         'Slow batting criticism. Choking debates.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('AB de Villiers', 'South Africa', 'Batsman',
         'Mr. 360. Fastest ODI century (31 balls). Retired 2018.',
         'Fastest ODI 50,100,150. 9,000+ ODI runs. IPL legend.',
         '20,014 international runs. 31-ball ODI century. 47 centuries.',
         'International retirement timing. IPL over country debates.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Dale Steyn', 'South Africa', 'Bowler',
         'Fastest to 300, 400 Test wickets. 699 international wickets.',
         'No.1 Test bowler for 263 weeks. ICC Test Bowler of Year 3x.',
         '699 international wickets. 439 Test wickets. 7/51 best.',
         'Injury concerns. Retirement timing.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Brian Lara', 'West Indies', 'Batsman',
         'Highest individual scores: 400* Test, 501* FC.',
         '400* vs England. 11,953 Test runs. ICC Hall of Fame.',
         '22,358 international runs. 400* and 375 Test scores.',
         'Tax issues. Captaincy controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Viv Richards', 'West Indies', 'Batsman',
         'Most destructive batsman 1970s-80s. Never wore helmet.',
         '2x WC winner 1975,1979. 8,540 Test runs. Knighted 1999.',
         '15,261 international runs. 189* highest Test. 90.20 strike rate.',
         'Aggressive behavior. Umpire disputes.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Kumar Sangakkara', 'Sri Lanka', 'Wicketkeeper-Batsman',
         '4 consecutive ODI centuries 2015 WC. 28,000+ runs.',
         'ICC Hall of Fame. 4 consecutive ODI 100s. MCC President.',
         '28,016 international runs. 63 centuries. 319 highest Test.',
         'Minimal controversies. Respected figure.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Muttiah Muralitharan', 'Sri Lanka', 'Bowler',
         'Most international wickets (1,347). Unique action.',
         '800 Test wickets. 534 ODI wickets. ICC Hall of Fame.',
         '1,347 international wickets. 67 Test five-wicket hauls.',
         'Chucking allegations. Action controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Kane Williamson', 'New Zealand', 'Batsman',
         'NZ captain. 2019, 2021 WC finalist. 2021 WTC winner.',
         '2021 WTC winner. 2x WC finalist. ICC Spirit of Cricket.',
         '17,000+ international runs. 32 Test centuries. 251 highest.',
         'Minimal controversies. Respected leader.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Richard Hadlee', 'New Zealand', 'All-rounder',
         'First to 400 Test wickets. NZ\'s greatest cricketer.',
         'First to 400 Test wickets. Knighted 1990. ICC Hall of Fame.',
         '431 Test wickets. 3,124 Test runs. 9/52 best bowling.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Shakib Al Hasan', 'Bangladesh', 'All-rounder',
         'Bangladesh\'s greatest. No.1 all-rounder multiple times.',
         'No.1 ICC all-rounder ranking. 14,000+ runs, 700+ wickets.',
         '14,271 runs. 712 wickets. Only player with 4k runs & 200 wickets in T20Is.',
         'Corruption ban 2019. Political involvement.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Rashid Khan', 'Afghanistan', 'Bowler',
         'Best T20 spinner. Youngest to 400 international wickets.',
         'Youngest to 100 ODI wickets. IPL star. BBL champion.',
         '500+ international wickets. 7/18 best ODI. Economy under 7.',
         'Afghanistan cricket politics.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Travis Head', 'Australia', 'Batsman',
         '2023 WC and WTC final hero. Explosive left-hander.',
         '2023 WC final 137. 2023 WTC final 163. Ashes hero.',
         '6,000+ international runs. 175 highest Test score.',
         'Concussion sub controversy.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Rishabh Pant', 'India', 'Wicketkeeper-Batsman',
         'Fearless batting. Car accident survivor 2022.',
         'Test wins in Australia, England. Comeback from accident.',
         '5,000+ international runs. 159* highest Test score.',
         'Car accident 2022. Reckless batting criticism.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Shubman Gill', 'India', 'Batsman',
         'Future of Indian batting. Youngest to 2000 ODI runs.',
         'Fastest to 2000 ODI runs. ICC Emerging Player nominee.',
         '5,000+ international runs. 208 highest ODI score.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Mohammad Rizwan', 'Pakistan', 'Wicketkeeper-Batsman',
         'Most T20I runs in calendar year (2021). Consistent performer.',
         'Most T20I runs in 2021 (1326). 3000+ T20I runs.',
         '7,000+ international runs. 171* highest ODI.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Harry Brook', 'England', 'Batsman',
         'Bazball star. Fastest to 1000 Test runs for England.',
         'Fastest England player to 1000 Test runs. Ashes star.',
         '2,000+ international runs. 186 highest Test score.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Kagiso Rabada', 'South Africa', 'Bowler',
         'Fastest to 300 ODI wickets. Premier fast bowler.',
         'Fastest to 300 ODI wickets. 300+ Test wickets.',
         '550+ international wickets. 7/112 best Test.',
         'Aggressive celebrations. Demerit points.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Trent Boult', 'New Zealand', 'Bowler',
         'Best left-arm pacer. 600+ international wickets.',
         '2021 WTC winner. 300+ Test wickets. 2x WC finalist.',
         '600+ international wickets. 7/34 best ODI.',
         'Central contract disputes.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Quinton de Kock', 'South Africa', 'Wicketkeeper-Batsman',
         'Explosive opener. Retired from Tests 2021.',
         '6 ODI centuries in 2023 WC. 17,000+ international runs.',
         '17,000+ runs. 174 highest ODI. 6 centuries in single WC.',
         'BLM gesture refusal 2021.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Jos Buttler', 'England', 'Wicketkeeper-Batsman',
         '2019 WC, 2022 T20 WC winner. Innovative batsman.',
         '2019, 2022 WC winner. England white-ball captain.',
         '14,000+ international runs. 162* highest ODI.',
         'Mankading incidents. Spirit of cricket debates.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Marnus Labuschagne', 'Australia', 'Batsman',
         'No.1 Test batsman 2019-21. Quirky mannerisms.',
         'No.1 Test ranking. 4000+ Test runs. Average 60+.',
         '8,000+ international runs. 215 highest Test score.',
         'Concussion substitute controversy.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Glenn Maxwell', 'Australia', 'All-rounder',
         'Big Show. 201* with cramps 2023 WC. Innovative shots.',
         '2015, 2023 WC winner. 201* vs Afghanistan cramping.',
         '11,000+ international runs. 145 highest ODI.',
         'Mental health break. Retirement hints.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Suryakumar Yadav', 'India', 'Batsman',
         'No.1 T20I batsman. 360-degree player. 2024 T20 WC winner.',
         '2024 T20 WC winner. No.1 T20I ranking. 4 T20I centuries.',
         '3,000+ T20I runs. 117 highest T20I score.',
         'Late bloomer criticism.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Mohammad Shami', 'India', 'Bowler',
         '2023 WC leading wicket-taker. Reverse swing master.',
         '24 wickets in 2023 WC. 200+ Test wickets.',
         '450+ international wickets. 7/57 best ODI.',
         'Personal life controversies. Injury concerns.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Ravindra Jadeja', 'India', 'All-rounder',
         'Best fielder. 500+ international wickets. 3 Test triple centuries.',
         '500+ wickets. 5,000+ runs. 3 Test triple centuries.',
         '7,000+ runs. 550+ wickets. 175* highest Test score.',
         'Rift with Kohli rumors. Retirement U-turn.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('KL Rahul', 'India', 'Batsman',
         'Fastest Test century by Indian (52 balls). Versatile batsman.',
         'Fastest Indian Test century. 2000+ ODI runs.',
         '8,000+ international runs. 199 highest ODI.',
         'Koffee with Karan controversy. Inconsistency criticism.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Hardik Pandya', 'India', 'All-rounder',
         '2024 T20 WC winning captain. Best Indian all-rounder.',
         '2024 T20 WC winner. IPL champion 2022, 2024.',
         '4,000+ international runs. 100+ wickets.',
         'Koffee with Karan 2019. Divorce controversy.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Axar Patel', 'India', 'All-rounder',
         'Left-arm spinner. 11-wicket haul on debut. 2024 T20 WC winner.',
         '2024 T20 WC winner. 11 wickets on Test debut.',
         '150+ international wickets. 2,000+ runs.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Haris Rauf', 'Pakistan', 'Bowler',
         'Express pace. 150+ km/h regularly. PSL to international.',
         '150+ international wickets. PSL champion.',
         '7/40 best ODI. Fastest Pakistani to 50 ODI wickets.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Shadab Khan', 'Pakistan', 'All-rounder',
         'Leg-spinner. Vice-captain. Consistent performer.',
         'Vice-captain. 150+ international wickets.',
         '3,000+ runs. 200+ wickets.',
         'Fitness concerns.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Fakhar Zaman', 'Pakistan', 'Batsman',
         '2017 Champions Trophy final century. Explosive opener.',
         '2017 CT winner. 210* vs Zimbabwe (highest Pak ODI).',
         '7,000+ international runs. 210* highest ODI.',
         'Inconsistency criticism.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Wanindu Hasaranga', 'Sri Lanka', 'All-rounder',
         'Best T20 leg-spinner. IPL Purple Cap 2023.',
         'IPL Purple Cap 2023. ICC T20I Team of Year.',
         '200+ international wickets. 7/19 best T20I.',
         'Central contract disputes.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Pathum Nissanka', 'Sri Lanka', 'Batsman',
         'Elegant opener. Consistent performer.',
         'Asia Cup 2022 star. 3000+ international runs.',
         '210* highest ODI. 5 international centuries.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Tim Southee', 'New Zealand', 'Bowler',
         '700+ international wickets. New-ball specialist.',
         '2021 WTC winner. 350+ Test wickets.',
         '700+ wickets. 7/33 best Test. 10-wicket haul on debut.',
         'Form concerns 2023-24.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Devon Conway', 'New Zealand', 'Batsman',
         '200 on Test debut. South African-born Kiwi.',
         '2021 WTC winner. 200 on Test debut.',
         '5,000+ international runs. 200 highest Test.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Daryl Mitchell', 'New Zealand', 'All-rounder',
         'Big match player. 2021 WTC final hero.',
         '2021 WTC winner. Multiple Test centuries in England.',
         '4,000+ runs. 190 highest Test score.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Sam Curran', 'England', 'All-rounder',
         '2022 T20 WC Player of Tournament. IPL record buy.',
         '2022 T20 WC winner. IPL record ₹18.5 cr.',
         '3,000+ runs. 150+ wickets.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Moeen Ali', 'England', 'All-rounder',
         '2019 WC winner. Spin all-rounder. Retired Tests 2021.',
         '2019 WC winner. 6,000+ runs. 350+ wickets.',
         '10,000+ international runs. 400+ wickets.',
         'Test retirement timing.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Jofra Archer', 'England', 'Bowler',
         '2019 WC super over hero. Express pace when fit.',
         '2019 WC winner. Super over bowler in final.',
         '100+ international wickets. 6/45 best ODI.',
         'Injury concerns. Bio-bubble breach.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Andre Russell', 'West Indies', 'All-rounder',
         'T20 destroyer. Most sixes in IPL history.',
         'T20 leagues champion worldwide. 500+ T20 sixes.',
         '5,000+ T20 runs. 300+ T20 wickets.',
         'Doping violation 2017.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Kieron Pollard', 'West Indies', 'All-rounder',
         'T20 legend. 1000+ T20 sixes. Retired 2022.',
         '2x T20 WC winner. 1000+ T20 sixes.',
         '11,000+ T20 runs. 300+ T20 wickets.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Mushfiqur Rahim', 'Bangladesh', 'Wicketkeeper-Batsman',
         'Bangladesh\'s leading run-scorer. 15,000+ runs.',
         'Most runs for Bangladesh. 10 Test centuries.',
         '15,000+ international runs. 219* highest Test.',
         'Umpire altercation.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Tamim Iqbal', 'Bangladesh', 'Batsman',
         'Bangladesh\'s ODI run leader. Retired 2023.',
         'Most ODI runs for Bangladesh. 14,000+ runs.',
         '14,000+ international runs. 158 highest ODI.',
         'Retirement drama 2023.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Mohammad Nabi', 'Afghanistan', 'All-rounder',
         'Afghanistan captain. 300+ international wickets.',
         'Most experienced Afghan player. T20 leagues star.',
         '6,000+ runs. 350+ wickets.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Jonny Bairstow', 'England', 'Wicketkeeper-Batsman',
         'Bazball star. Controversial stumping 2023 Ashes.',
         '2019 WC winner. 12,000+ international runs.',
         '12,000+ runs. 167 highest ODI.',
         'Stumping controversy 2023 Ashes.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Faf du Plessis', 'South Africa', 'Batsman',
         'Former SA captain. Retired international 2021.',
         'Led SA 2015-19. 10,000+ ODI runs.',
         '16,000+ international runs. 185 highest ODI.',
         'Ball-tampering (mint, zipper).',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Hashim Amla', 'South Africa', 'Batsman',
         'Fastest to 2k-7k ODI runs. Elegant batsman.',
         'Fastest to multiple ODI milestones. 9,000+ ODI runs.',
         '18,000+ international runs. 311* highest Test.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Angelo Mathews', 'Sri Lanka', 'All-rounder',
         '2014 T20 WC winning captain. Senior statesman.',
         '2014 T20 WC winner. 11,000+ international runs.',
         '11,000+ runs. 200+ wickets. 200* highest ODI.',
         'Timed out controversy 2023 WC.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Lasith Malinga', 'Sri Lanka', 'Bowler',
         'Yorker king. Unique action. 546 international wickets.',
         '2014 T20 WC winner. 4 wickets in 4 balls.',
         '546 international wickets. 6/38 best ODI. 3 ODI hat-tricks.',
         'Retirement timing debates.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Brendon McCullum', 'New Zealand', 'Batsman',
         'Fastest Test century (54 balls). England coach.',
         'Fastest Test century. England coach (Bazball).',
         '14,000+ international runs. 302 highest Test.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Martin Guptill', 'New Zealand', 'Batsman',
         'Highest ODI score (237*). Explosive opener.',
         '2x WC finalist. 237* highest ODI score.',
         '13,000+ international runs. 237* highest ODI.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Virender Sehwag', 'India', 'Batsman',
         'Most destructive opener. 2 Test triple centuries.',
         '2 Test triple centuries. 8,000+ Test runs.',
         '17,000+ international runs. 319 highest Test.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Yuvraj Singh', 'India', 'All-rounder',
         '2011 WC Player of Tournament. 6 sixes in over.',
         '2007, 2011 WC winner. 6 sixes vs Broad.',
         '11,000+ international runs. 400+ wickets.',
         'Cancer battle. Retirement timing.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Zaheer Khan', 'India', 'Bowler',
         '2011 WC leading wicket-taker. Left-arm pace.',
         '2011 WC winner. 311 Test wickets.',
         '610 international wickets. 7/87 best Test.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Harbhajan Singh', 'India', 'Bowler',
         'Hat-trick vs Australia 2001. 417 Test wickets.',
         '2007, 2011 WC winner. Hat-trick vs Australia.',
         '711 international wickets. 8/84 best Test.',
         'Monkeygate 2008. Slap-gate.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Shikhar Dhawan', 'India', 'Batsman',
         'ICC tournament specialist. Fastest Test century on debut.',
         'Champions Trophy 2013 Golden Bat. 10,000+ international runs.',
         '10,000+ runs. 187 highest ODI.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Dinesh Karthik', 'India', 'Wicketkeeper-Batsman',
         'Finisher. 2024 T20 WC winner. 20-year career.',
         '2024 T20 WC winner. 10,000+ T20 runs.',
         '9,000+ international runs. 97* highest ODI.',
         'Personal life controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Bhuvneshwar Kumar', 'India', 'Bowler',
         'Swing bowler. Purple Cap IPL 2016, 2017.',
         '2x IPL Purple Cap. 300+ international wickets.',
         '300+ wickets. 5/42 best ODI.',
         'Injury concerns.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Yuzvendra Chahal', 'India', 'Bowler',
         'Leading ODI leg-spinner. 200+ international wickets.',
         '6/42 best ODI. 200+ wickets.',
         '350+ international wickets. 6/42 best ODI.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Kuldeep Yadav', 'India', 'Bowler',
         'Chinaman bowler. Hat-trick vs Australia.',
         'Hat-trick vs Australia. 150+ international wickets.',
         '200+ wickets. 6/25 best ODI.',
         'Form fluctuations.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Mohammad Amir', 'Pakistan', 'Bowler',
         'Comeback from spot-fixing ban. Left-arm pace.',
         'Spot-fixing ban return. 2017 CT winner.',
         '250+ international wickets. 6/44 best ODI.',
         'Spot-fixing ban 2010. Retirement drama.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Younis Khan', 'Pakistan', 'Batsman',
         'Pakistan\'s leading Test run-scorer. 10,099 runs.',
         '2009 T20 WC winning captain. 10,099 Test runs.',
         '17,000+ international runs. 313 highest Test.',
         'Conflicts with PCB. Temperament issues.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Inzamam-ul-Haq', 'Pakistan', 'Batsman',
         'Pakistan\'s ODI run leader. Chief selector.',
         '20,000+ international runs. Chief selector.',
         '20,541 runs. 329 highest ODI.',
         'Run-out controversies. Fitness criticism.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Javed Miandad', 'Pakistan', 'Batsman',
         'Last-ball six vs India 1986. 16,000+ runs.',
         'Last-ball six 1986. 16,000+ international runs.',
         '16,213 runs. 280* highest Test.',
         'Umpire altercations. Aggressive behavior.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Shahid Afridi', 'Pakistan', 'All-rounder',
         'Boom Boom. Fastest ODI century (37 balls) for 17 years.',
         'Fastest ODI century (37 balls). 8,000+ runs, 500+ wickets.',
         '11,000+ runs. 500+ wickets.',
         'Ball-biting. Pitch-damaging. Controversial statements.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Saeed Anwar', 'Pakistan', 'Batsman',
         '194 ODI score (record for 12 years). Elegant left-hander.',
         '194 ODI score. 8,000+ ODI runs.',
         '12,000+ international runs. 194 highest ODI.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Alastair Cook', 'England', 'Batsman',
         'England\'s leading Test run-scorer. 12,472 runs.',
         '12,472 Test runs. 33 Test centuries. Knighted 2019.',
         '12,472 Test runs. 294 highest score.',
         'Captaincy resignation 2016.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Kevin Pietersen', 'England', 'Batsman',
         'Switch-hit inventor. 13,000+ international runs.',
         '2005 Ashes hero. Switch-hit pioneer.',
         '13,797 international runs. 355* highest Test.',
         'Text-gate 2012. ECB conflicts.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Andrew Flintoff', 'England', 'All-rounder',
         '2005 Ashes hero. Freddie. All-round star.',
         '2005 Ashes hero. 7,000+ runs, 400+ wickets.',
         '7,000+ runs. 400+ wickets.',
         'Pedalo incident 2007. Drinking culture.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Ian Botham', 'England', 'All-rounder',
         '1981 Ashes hero. Greatest English all-rounder.',
         '1981 Ashes miracle. 5,000+ runs, 500+ wickets.',
         '7,000+ runs. 500+ wickets. 149* Headingley 1981.',
         'Drug admission. Controversial statements.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Stuart Broad', 'England', 'Bowler',
         '600+ Test wickets. 8/15 vs Australia.',
         '604 Test wickets. 2019 WC winner.',
         '604 Test wickets. 8/15 best bowling.',
         'Not walking controversies. Aggressive behavior.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Graeme Smith', 'South Africa', 'Batsman',
         'Most successful SA captain. 17,000+ runs.',
         'Most Test wins as SA captain. 9,000+ Test runs.',
         '17,000+ runs. 277 highest Test.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Shaun Pollock', 'South Africa', 'All-rounder',
         '829 international wickets. Accurate medium-pacer.',
         '421 Test wickets. 7,000+ runs.',
         '7,000+ runs. 829 wickets.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Allan Donald', 'South Africa', 'Bowler',
         'White Lightning. 590 international wickets.',
         '330 Test wickets. Fastest SA bowler.',
         '590 wickets. 8/71 best Test.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Mahela Jayawardene', 'Sri Lanka', 'Batsman',
         '25,000+ international runs. Elegant batsman.',
         '2014 T20 WC winner. 25,000+ runs.',
         '25,957 runs. 374 highest Test.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Sanath Jayasuriya', 'Sri Lanka', 'All-rounder',
         '1996 WC winner. Revolutionized ODI batting.',
         '1996 WC winner. 21,000+ runs, 440 wickets.',
         '21,000+ runs. 340 highest ODI.',
         'Match-fixing allegations (cleared).',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Arjuna Ranatunga', 'Sri Lanka', 'Batsman',
         '1996 WC winning captain. Tactical genius.',
         '1996 WC winner. 12,000+ international runs.',
         '12,000+ runs. 131* highest ODI.',
         'Umpire disputes. Aggressive behavior.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Chaminda Vaas', 'Sri Lanka', 'Bowler',
         'Best SL fast bowler. 761 international wickets.',
         '1996 WC winner. 355 Test wickets.',
         '761 wickets. 8/19 best ODI.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Curtly Ambrose', 'West Indies', 'Bowler',
         '630 international wickets. 6\'7" tall. Intimidating.',
         '405 Test wickets. 1992 WC finalist.',
         '630 wickets. 8/45 best Test.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Courtney Walsh', 'West Indies', 'Bowler',
         'First to 500 Test wickets. 519 Test wickets.',
         '519 Test wickets. Most Test wickets at retirement.',
         '746 international wickets. 7/37 best Test.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Garfield Sobers', 'West Indies', 'All-rounder',
         'Greatest all-rounder ever. First 6 sixes in over.',
         'First 6 sixes in over. 8,000+ Test runs.',
         '8,032 Test runs. 235 wickets. 365* highest Test.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Clive Lloyd', 'West Indies', 'All-rounder',
         '2x WC winning captain 1975, 1979. Dominated 1970s-80s.',
         '1975, 1979 WC winner. 12,000+ international runs.',
         '12,000+ runs. 242* highest Test.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Chris Gayle', 'West Indies', 'Batsman',
         'Universe Boss. Most T20 sixes. 215 WC score.',
         '2x T20 WC winner. 1,000+ international sixes.',
         '19,000+ international runs. 333 highest Test.',
         'Sexism controversy. Attitude criticism.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Andy Flower', 'Zimbabwe', 'Wicketkeeper-Batsman',
         'Zimbabwe\'s greatest. 9,000+ international runs.',
         '9,000+ runs. England coach 2009-14.',
         '9,786 runs. 232* highest Test.',
         'Minimal controversies.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),

        ('Heath Streak', 'Zimbabwe', 'All-rounder',
         'Zimbabwe\'s leading wicket-taker. 455 wickets.',
         '216 Test wickets. Captain.',
         '4,933 runs. 455 wickets.',
         'Corruption ban 2021.',
         'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Cricket_ball_and_bat.jpg/400px-Cricket_ball_and_bat.jpg'),
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
    print("\n🎉 Database ready! All entries are up-to-date as of 2024.")

if __name__ == '__main__':
    init_db()
