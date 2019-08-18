$ import images.rpy

# Declare characters used by this game.
define nar = Character('::Intercom::', color="#b1a9a9")
define ts = Character('Sally', color="#f60c0c")
define jm = Character('James', color="#f5920d")
define nrs = Character('Nurse', color="#ffffff")
define sns = Character('Sensei', color="#8808c4")
define mky = Character('Michael', color="819bd3")
define bos = Character('Boss', color="070001")
define nta = Character('Anita', color="7e0ce9")
define wine = Character('Wine', color="7F0000")
define dmnta = Character('Demon', color="FF0000")
define anjm = Character('Angel', color="E6BF15")

# The game starts here.
label start:
    # declare variables
    
    $ Hangover = False

    $ nurseVisits = 0

    # for Sensei
    $ SNSamore = 0
    $ SNShate = 0
    $ SNSannoy = 0
    $ SNSagape = 0

    # for Tsundere Sally
    $ TSamore = 0
    $ TShate = 0
    $ TSannoy = 0
    $ TSagape = 0    

    # for Senpai James
    $ JMamore = 0
    $ JMhate = 0
    $ JMannoy = 0
    $ JMagape = 0
    
    # for Michael Yuren
    $ MKamore = 0
    $ MKhate = 0
    $ MKannoy = 0
    $ MKagape = 0
    $ MKnumber = False
    
    # for Anita G. Kirai
    $ AKamore = 0
    $ AKhate = 0
    $ AKannoy = 0
    $ AKagape = 0
    
    play music "GameSong.ogg"
    # debug menu
    # jump nextDay

        
    scene school:
        xalign 1.0
        linear 3.0 xalign 0.0
    
    nar "Welcome, new students to The University!"
    nar "Please report to your homeroom to check in"
    nar "Guides are available to those who get lost. Just look for the students wearing red ribbons!"
    jump SallyIntro
    
    label SallyIntro:
        scene cYard
        show Sally with dissolve:
            xalign 0.5 yalign 1.0
            linear 2.0 xalign 0.2
            
        ts "You must be a new student from the looks of you!"
        hide Sally
        show SallyHa
        ts "All new students have that dumb expression."
        hide SallyHa
        show Sally with dissolve:
            xalign 0.75 yalign 1.0
        ts "Anyway, my name is {color=#f60c0c}Sally{/color}, and I will be your babysitt-er your guide. The library is that way."
        hide Sally
        show SallyL:
            xalign 0.25 yalign 1.0
        ts "The dorms are that way."
        hide SallyL
        show SallyHa
        ts "And any idiot knows you use {color=#fb0009}right-click{/color} or {color=#fb0009}Esc{/color} to get to the game menu. From there you can save your progress or manage your preferences like music volume."
        hide SallyHa
        show Sally with dissolve:
            xalign 0.75 yalign 1.0
            linear 4.0 xalign 0.25 yalign 0.75
        ts "Here's my number so you can annoy me with your basic-ass questions. Please know that if I don't respond right away it is because I'm ignoring you. Do you get it or should I explain it again more slowly?"
        menu:
            "I get it, geez! Fuck off! (annoyed)":
                jump SallyBlush
            
            "Hey, I totally get it. I'm not like these babies. I toured the campus last summer. Nice shoes, by the way. (flirtatious)":
                jump SallyYeah
                
            "Could... could you explain more about the game menu? (timid)":
                jump SallyUgh
                
        label SallyBlush:
            hide Sally
            show SallyHa:
                xalign 0.5 yalign 1.0
                linear 4.5 xalign 1.0
            ts "Haaaaaaaaaaa.... well ok. Here's my messenger ID. I'll see you around."
            $ TSamore + 1
            $ TSagape - 1
            jump hallway
            
            
        label SallyYeah:
            hide Sally
            show SallyL:
                xalign 0.5 yalign 1.0
                linear 4.0 xalign 0.5 yalign 0.5
            $ TSagape - 1
            $ TSamore + 1
            ts "Really?... Well I'll be keeping my eye on you. Here's my number. Text me if you need anything."
            hide SallyL
            show Sally:
                xalign 0.5 yalign 0.5
            ts "Also, yes, these shoes are killer."
            jump hallway
            
        label SallyUgh:
            hide Sally
            show SallyAngryFlash
            ts "Ugggghhhhhhh.....{w}...{w}...{w}..."
            hide SallyAngryFlash
            show SallyHa
            ts "I guess that's the job I volunteered for..."
            $ TSannoy + 1
            $ TShate - 1
            jump explainMenu
            
            
        label explainMenu:
            scene RPmn with dissolve
            ts "When you {color=#fb0009}right click{/color} your mouse or press the {color=#fb0009}Esc{/color} key, you open the game menu."
            show SallyCl with dissolve
            ts "You can save your game progress in one of the save slots."
            show pointUp with dissolve:
                xalign 0.15 yalign 0.25
            ts "here"
            hide pointUp with dissolve
            hide SallyCl
            show SallyCl:
                xalign 0.5 yalign 1.0
                linear 3.0 xalign 0.25
            ts "And you can change your in-game preferences...."
            show pointRt with dissolve:
                xalign 0.67 yalign 0.8
            ts "here"
            scene PFmn with dissolve
            ts "This is what the preferences menu looks like, but you can also just see it for yourself by {color=#fb0009}right click{/color}ing your mouse or pressing the {color=#fb0009}Esc{/color} key."
            ts "Right now."
            ts "You could have done it yourself all this time, but I guess you like to have things explained to you in simple terms."
            show SallyCl with dissolve
            ts "It's funny. When I started at this school they made me fill out an application to prove I was smart. I guess they just let anyone in now."
            hide SallyCl
            show Sally at left
            ts "Anyway, if you need help, this is my messenger ID. I'll see you around campus. Hopefully from really far away."
            jump hallway
    
             
        label hallway:
            scene blkgrnd with dissolve
            "You find the building where your homeroom class is supposed to be."
            scene hallway with dissolve
            show James with dissolve
            jm "Oh, hi. Are you a first year? It's ok. I'll help you out."
            hide James
            show JamesR
            jm "My name is {color=#f5920d}James{/color}. This is my second year, but I've worked here in custodial since highschool, so I know my way around pretty well."
            hide JamesR
            show JamesYm
            jm "I'm not technically an official guide, but I can help you find where you're going. Here's my number. Feel free to text me."
            hide JamesYm
            show JamesYmR
            jm "Where are you headed now?"
            
            menu:
                "Um, I'm, um... *faint*":
                    jump nurse1
                "I'm headed to homeroom. I know it's in this building, but now I'm lost... Can you please help me? (endearing)":
                    jump jm2homeroom
                "I know where I'm going, thank you. (curt)":
                    jump homeroom
                    
        label nurse1:
            $ JMagape += 1
            $ nurseVisits += 1
            scene Clinic with Fade(0.1, 0.0, 0.5, color="#ffffff")
            show Nurse with dissolve
            nrs "Oooh my. What a spill you took. You're none the worse for wear, though."
            hide Nurse
            show NurseR
            nrs "We'll get you fixed right up, and on your way to homeroom."
            jump homeroom
            
        label jm2homeroom:
            $ JMamore += 1
            scene ClassDay
            show James with dissolve
            jm "Here's your homeroom class. Oh, hey. This is my homeroom too this year."
            hide James
            show JamesR at left
            jm "They like to combine first and second years in the same homeroom so the first years don't get too lost."
            hide JamesR
            show James
            jm "Don't worry. I was the lost one last year."
            hide James
            show JamesR at right
            jm "Oh, here comes Sensei."
            jump sensei1
            
        label homeroom:
            $ JMannoy += 1
            scene ClassDay
            "Congratulations. You made it to your first class without making any friends."
            jump sensei1
            
        label sensei1:
            scene ClassFront with dissolve
            show SenseiR with dissolve
            sns "Hello, class! Welcome to your first day of homeroom at The University."
            hide SenseiR
            show SenseiL
            sns "We have a lot of new students this year. Second years, show of hands!"
            hide SenseiL with dissolve
            show SallyGr at left with dissolve
            show JamesR at right with dissolve
            hide SallyGr with dissolve
            hide JamesR with dissolve
            show SenseiL at right with dissolve
            sns "Alright, first years. Those students are your lifelines, but be gentle with them. Remember that next year you'll be the lifeline."
            hide SenseiL
            show SenseiR
            sns "Second years, if you need a lifeline at any time this semester, you can look to me, ok?"
            hide SenseiR with dissolve
            show Sally with dissolve
            hide Sally
            show Sally:
                xalign 0.5 yalign 1.0
                linear 2.0 xalign 0.8
            show James with dissolve:
                xalign 0.5 yalign 1.0
                linear 2.0 xalign 0.15
            "Class:" "THANK YOU SENSEI!!!"
            hide James
            hide Sally
            show SenseiR with dissolve
            sns "I'm passing out syllabi now. Please take one and pass it to the person behind you."
            hide SenseiR with dissolve
            jump meet_mikey
            
        label meet_mikey:
            scene ClassFront with dissolve
            show MikYL with dissolve
            mky "H... here's the syllabus. Oh, hi. You, you're... hello..."
            hide MikYL
            show MikYR:
                xalign 0.5 yalign 1.0
                linear 1.5 xalign 0.9
            mky "My name is Michael. I'm a first year too. I guess we have homeroom together..."
            menu:
                "Thanks! You're really... dot dot dot... yourself... *flirtatious*":
                    $ MKamore += 1
                    jump MikeyLunch
                "Just pass me the form, nerd.":
                    $ MKhate += 1
                    jump noMikeyLunch
                "Oh hey, thanks. Cool, let's be friends.":
                    $ MKagape += 1
                    jump MikeyLunch
                    
        label MikeyLunch:
            scene blkgrnd
            "You have the next period free and decide to take lunch."
            scene Lunchroom
            "You are feeling very independent and grown up."
            show MikYL:
                xalign 0.1 yalign 1.0
                linear 1.0 xalign 0.5
            mky "Oh hi! Funny running into you in the lunchroom! Ha Ha Ha!"
            menu:
                "Michael, hi! Yes, please sit with me!":
                    $ MKamore += 1
                    jump MikeConvo
                "Oh, hello. You're Nathan from homeroom, aren't you? Want to sit with me?":
                    $ MKannoy += 1
                    jump MikeConvo2
                "I don't talk to strangers...":
                    $ MKamore += 1
                    hide MikYL
                    show MikYL:
                        xalign 0.5 yalign 1.0
                        linear 2.5 xalign 1.5
                    mky "Oh, um, I'll see you tomorrow I guess..."
                    jump work1
                    
        label noMikeyLunch:
            scene blkgrnd
            "You have the next period free and decide to take lunch."
            scene Lunchroom
            "You are feeling very grown up and independent."
            show AnitaR:
                xpos -0.5 ypos 0.0
                linear 3.5 xpos 1.5
            "Woah, who was that?"
            hide AnitaR with dissolve
            jump work1
            
        label MikeConvo:
            scene Lunchroom
            show MikYR at left
            mky "What a coincidence that we both decided to eat lunch at the same time, HA HA!"
            menu:
                "Most people eat lunch in the middle of the day, right?":
                    $ MKannoy += 1
                "I know! I'm so glad to see your familiar face again. To be honest I'm kind of nervous about living away from home.":
                    $ MKamore += 1
                "It's not a coincidence. Our class got out at 12:30 and I assume we both have more classes later. Do you think the sun being up in the daytime is a coincidence too? *then take a sip of your iced tea*":
                    $ MKhate += 1
            
            hide MikYR
            show MikYL at right
            mky "You know, something about you really reminds me of my mother..."
            menu:
                "Oh wow, I am honored. There is nothing more important than family.":
                    $ MKamore += 1
                "Dude, that is a super weird thing to say to a person you just met today.":
                    $ MKhate += 1
                "Isn't the weather really nice today?":
                    $ MKannoy += 1
                    
            play sound "Bell.ogg"
            mky "Oh no, my next class is about to start. Here is my number. Text me!"
            $ MKnumber = True
            hide MikYL
            show MikYL at right:
                linear 2.0 xpos -1.5
            jump work1
            
        label MikeConvo2:
            scene Lunchroom
            show MikYR at left
            mky "Actually it's Michael."
            hide MikYR
            show MikYL at right
            mky "Actually, my mom called me Mickey. She... she's dead now..."
            menu:
                "Ok man, you can sit here, geez. You are bumming me out on my first day.":
                    $ MKannoy += 1
                "Oh, sorry. Sorry about your mom. Mickey...":
                    $ MKamore += 1
                "Good god, Nathan, I did not ask for your whole life story. You can sit here. I have to go anyway.":
                    $ MKhate += 1
                    jump work1
                
            mky "Sorry to drop that. I always thought my first day away from boarding school would be with my dad."
            mky "I haven't seen him since mom's funeral. I was 11."
            menu:
                "I hope you are able to reconnect with him.":
                    $ MKannoy += 1
                "That bastard abandoned you...":
                    $ MKamore += 1
                "Holy crap, your life is depressing. I have to get out of here.":
                    $ MKhate += 1
                    jump work1
            play sound "Bell.ogg"
            mky "Oh no, my next class is about to start. Here is my number. Text me!"
            $ MKnumber = True
            hide MikYL
            show MikYL at right:
                linear 2.0 xpos -1.5
            jump work1
            
        label work1:
            scene Work with dissolve
            show BossR with dissolve
            bos "Why hello! Welcome to your first day at the Snak-Kun kiosk."
            hide BossR
            show BossL at left
            bos "All you gotta do, mang, is sell these cute stickers and erasers and like there's snacks and stuff too. Don't even worry about it. People love this stuff. Just, ching-ching that register."
            hide BossL with dissolve
            "So you work"
            show James at right with dissolve
            pause 0.5
            hide James with dissolve
            "Some friends show up"
            show SallyHa at left with dissolve
            pause 0.5
            hide SallyHa
            "And some other people who know you show up."
            "and then{w} she showed up..."
            show AnitaR with dissolve
            nta "Do you have any cute cat erasers?..."
            menu:
                "We have... we... have... cat... Will you marry me?":
                    $ AKhate += 1
                    jump AKhate
                "I cannot control my brain right now help":
                    $ AKannoy += 1
                    jump AKannoy
                "Please be impressed by how composed I am right now. Erasers are over there.":
                    $ AKagape += 1
                    jump AKagape
                    
                    
        label AKhate:
            scene Work
            show AnRageR
            nta "WHAT THE HELL? I DON'T EVEN KNOW YOU! UGH!"
            hide AnRageR
            show AnitaL:
                xpos 0.5 ypos 0.0
                linear 2 xpos 0.0
            "Wow, that was inappropriate."
            jump home_night
            
        label AKannoy:
            scene Work
            show AnitaL
            nta "Hm, I will definitely alert the school nurse right after you ring up these cute cat erasers."
            hide AnitaL
            show AnitaR:
                xpos 0.5 ypos 0.0
                linear 4.0 xpos 1.5
            jump nurse2
            
        label nurse2:
            $ nurseVisits += 1
            scene Clinic with Fade(0.1, 0.0, 0.5, color="#ffffff")
            show Nurse with dissolve
            nrs "Oooh my. Are you aenemic? Is that really a thing? Hm. Well I got what I need fro- er, you seem to be ok now."
            hide Nurse
            show NurseR
            nrs "Ha haaaaaaa... well, off you go. See you next time!"
            jump home_night
            
        label AKagape:
            scene Work
            show AnitaR
            nta "Oh yes. That is very impressive. Um, I like the orange stripey cat erasers so..."
            nta "so please sell me them."
            jump home_night
            
        label home_night:
            scene blkgrnd with dissolve
            "{color=#006699}Yay! You did it! Celebrate!{/color}"
            scene Bedroom with dissolve
            show wine with dissolve:
                xpos 0.7 ypos 0.6
                linear 4.0 xpos 0.0
            wine "What a neat first day of school. I bet you'll never forget that, right? It's probably only going to get less exciting from here. Get ready to settle into a boring old routine."
            hide wine
            show wine:
                xpos 0.0 ypos 0.6
                linear 3.0 ypos 0.3
            wine "You know what's a good idea? Sending flirty texts to people you just met!"
            # hide wine with dissolve
            "{color=#006699}Wine's right. Get out your phone.{/color}"
            show phone:
                xpos 0.5 ypos 1.5
                linear 3.5 xpos 0.5 ypos 0.3
            if MKnumber:
                menu:
                    "Text James: 'Hey bae, what's up?'":
                        jump TextJames
                    "Text Sally: 'Man, you know what I hate? Everything. Wanna get drinks?'":
                        jump TextSally
                    "Text Anita: 'Hey, I have a limited edition Hello Kitty lunchbox with thermos...'":
                        jump TextAnita
                    "Text Mickey: 'Hey sexy trash, want to get in my dumpster?'":
                        jump TextMickey
            else:
                menu:
                    "Text James: 'Hey bae, what's up?'":
                        jump TextJames
                    "Text Sally: 'Man, you know what I hate? Everything. Wanna get drinks?'":
                        jump TextSally
                    "Text Anita: 'Hey, I have a limited edition Hello Kitty lunchbox with thermos...'":
                        jump TextAnita
                    
            label TextJames:
                show James at left:
                    alpha 0.3
                jm "Oh hi, it's you. I'm doing good. How are you?"
                menu:
                    "I'm just unwinding before bed. Hey, do you want to go for coffee before class tomorrow?":
                        $ JMagape += 1
                        jump JamesDate
                    "I was just laying around in my pajamas and was wondering if you wanted to come take them off.":
                        $ JMannoy += 1
                        jump nextDay
                    "*get nervous and don't respond*":
                        $ JMannoy += 1
                        jump nextDay
                                
            label TextSally:
                show Sally at right:
                    alpha 0.3
                ts "Ha haaaa, I totally get you. I was about to go to bed, but yeah. Let's make some bad decisions."
                menu:
                    "Oh, uh, I didn't mean right now. Even the club waits until Tuesday to go up.":
                        $ TSannoy += 1
                        jump nextDay
                    "Hell to the yeah, grrrl! Let me get my shoes on.":
                        $ TSamore += 1
                        jump SallyDate
                    "*drink more wine alone and fall asleep in your own bed*":
                        $ TShate += 1
                        jump nextDay
                                
            label TextAnita:
                show AnitaR:
                    alpha 0.3
                nta "I don't believe you, pervert. Did you get my messenger ID out of the customer database at your work?"
                menu:
                    "You're right. I was just lonely. I'm sorry.":
                        $ AKannoy += 1
                    "Will you be my friend if I buy you a Hello Kitty lunchbox, though?":
                        $ AKagape += 1
                    "No, um, new phone, who dis?":
                        $ AKhate += 1
                        
                nta "Whatever. Don't text me again."
                if AKagape >= 1:
                    nta "I'll see you at Snak-Kun tomorrow."
                    jump nextDay
                else:
                    jump nextDay

            label TextMickey:
                show MikYL at right:
                    alpha 0.5
                mky "What? I don't understand. I am sexy trash? What dumpster do you mean? Hello?"
                menu:
                    "Geez you are awkward. Why don't you come over, and I'll top you like an ice cream sundae?":
                        $ MKamore += 1
                    "Oh my gosh. I may have had too much wine to be texting. I am sorry.":
                        $ MKannoy += 1
                    "Nevermind. I will see you tomorrow.":
                        $ MKhate += 1
                    
                mky "I am so confused..."
                jump nextDay
                
            label JamesDate:
                $ JManita = False
                $ JMannoyed = False
                $ JMinsecure = False
                scene blkgrnd with dissolve
                "The next morning, you meet James for coffee."
                scene coffeeshop with dissolve
                show James with dissolve
                jm "Oh hi! I'm glad you made it."
                jm "So how do you feel about living at the school so far? Did you make any friends?"
                menu:
                    "I've met some people, but I can't remember their names when I'm talking to you...":
                        $ JMannoy += 1
                        $ JMannoyed = True
                    "I've met a Sally and a Mickey and... *sigh* Anita...":
                        $ JMagape += 1
                        $ JManita = True
                    "I've met a few people, but I'm pretty sure everyone hates me. I'm really terrible in social situations.":
                        $ JMamore += 1
                        
                hide James
                show JamesR
                if JManita:
                    jm "Wow, she sounds really nice. And you got her number? Well, hey, I'm rooting for you."
                elif JMannoyed:
                    jm "Ha ha! Well... Oh man. Look at the time. My class is starting soon. It's been really fun.!"
                else:
                    jm "Hey, no. I think you're really great. Anyone else with half a brain would think so too."
                
                scene coffeeshop with hpunch
                show James with vpunch
                hide James
                show JamesR
                jm "Oh no. This is sooner than Sensei predicted."
                hide JamesR
                show James
                jm "You stay here, ok? Try to hide."
                hide James with zoomout
                scene blkgrnd with dissolve
                jump JamesANbattle
                
            label SallyDate:
                $ SallyAnnoy = False
                $ SallyHeart = False
                $ SallyFuckU = False
                $ Hangover = False
                scene blkgrnd with dissolve
                ts "Meet me at {color=#561567}Club la Club.{/color}"
                scene ClubLaClub:
                    xpos 0.0
                    linear 0.1 xpos -0.1
                    xpos 0.0
                    pause 0.5
                    repeat
                play music "ClubMusic.ogg"
                show Sally with dissolve
                ts "OH HEY! YOU MADE IT!"
                menu:
                    "WHAT?":
                        $ TSannoy += 1
                        $ SallyAnnoy = True
                    "I'LL GET US DRINKS!":
                        $ TSamore += 1
                        $ SallyHeart = True
                    "YOU SHOULD GET US DRINKS!":
                        $ TShate += 1
                hide Sally
                show SallyL at right
                if SallyAnnoy:
                    ts "I SAID! Fuck nevermind. I'll get us drinks."
                elif SallyHeart:
                    ts "OH HELL YEAH! HOOK IT UP!"
                    $ Hangover = True
                else:
                    ts "ACTUALLY I'LL JUST GET DRINKS FROM ONE OF THESE RANDOS! SEE YOU TOMORROW!"
                    jump nextDay
                if SallyAnnoy:
                    hide SallyL with dissolve
                    "{color=#006699}What a good and smart thing to do on your first day of University."
                    "Maybe she'll touch your butt and then after you're expelled for being an idiot you can console yourself with the memory of having your butt touched.{/color}"
                    
                else:
                    hide SallyL with dissolve
                    "{color=#006699}Yes, awesome. Stay up late drinking before your second day of school. This is a choice a smart person makes.{/color}"
                    show Bartender with dissolve
                    "{color=#006699}Two of whatever will get me kicked out of school fastest, doc.{/color}"
                    hide Bartender with dissolve
                
                show SallyHa with dissolve
                ts "Sweet, let's get blitzed!"
                    
                menu:
                    "Maybe I'll just have one..":
                        $ TShate += 1
                    "YEAH! LET'S DO SHOTS OFF EACH OTHER!":
                        $ TSagape += 1
                        $ Hangover = True
                    "SWEET! I'VE GOT THE NEXT ROUND!":
                        $ TSamore = 1
                        $ Hangover = True
                scene blkgrnd with dissolve
                "And so you club the night away..."
                jump nextDay
                
            label JamesANbattle:
                play music "battlemusic.ogg"
                scene sidewalk
                show batAnR with dissolve:
                    xalign 0.5 yalign 1.0
                pause 0.5
                hide batAnR
                show batAnR:
                    xalign 0.5 yalign 1.0
                    linear 1.5 xalign 0.10 yalign 0.6
                show batJmR with dissolve
                pause 0.5
                hide batJmR
                show batJmR:
                    xalign 0.5 yalign 1.0
                    linear 1.5 xalign 0.9 yalign 0.75
                anjm "So, you finally show your true form. I always knew it was you. I could just never prove it."
                dmnta "YOU'LL NEVER WIN!"
                hide batAnR
                show batAnR with hpunch:
                    xalign 0.10 yalign 0.6
                show m50:
                    xalign 0.75 yalign 0.6
                    linear 1.5 yalign 0.35
                hide m50 with dissolve
                anjm "ARGH!"
                hide batJmR
                show batJmL:
                    xalign 0.8 yalign 0.75
                    linear 1.0 xalign 0.8 yalign 0.1
                anjm "DEMON! DIIIIIIIE!"
                hide batJmL
                show batJmL with hpunch:
                    xalign 0.8 yalign 0.75
                show m50:
                    xalign 0.1 yalign 0.6
                    linear 1.5 xalign 0.1 yalign 0.35
                hide m50 with dissolve
                dmnta "RRRRRAAAAAAAHHHHGGG!"
                if JMannoy > AKannoy:
                    dmnta "That's it. I'm ending this!"
                    hide batAnR
                    show batAnR:
                        xalign 0.10 yalign 0.6
                        linear 1.5 xalign 0.10 yalign 0.1
                    pause 1.0
                    hide batAnR
                    show batAnL:
                        xalign 0.10 yalign 0.1
                        linear 0.1 xalign 0.75 yalign 0.75
                    hide batJmL
                    show batJmL:
                        xalign 0.8 yalign 0.75
                        linear 1.0 xalign 1.0
                    show m666:
                        xalign 0.75 yalign 0.6
                        linear 1.5 yalign 0.35
                    hide m666 with dissolve
                    hide batJmL with dissolve
                    dmnta "Now... where is that little pretty one?..."
                    jump kidnapped
                else:
                    dmnta "Fuck you, teacher's pet! This isn't over"
                    hide batAnR
                    show batAnR:
                        xalign 0.10 yalign 0.6
                        linear 1.0 xalign -0.5 yalign 0.6
                jump nextDay
                
            
            label nextDay:
                play music "GameSong.ogg"
                scene ClassDim
                if Hangover:
                    "oh my god my head why"
                show MikYL at right with dissolve
                mky "Oh, hi classmate! It's good to see you again!"
                if Hangover:
                    menu:
                        "Holy crap your voice is loud.":
                            $ MKannoy += 1
                        "Oh... yeah... jeez. Good to see you too.":
                            $ MKamore += 1
                        "*throw up in your backpack*":
                            $ MKagape += 1
                else:
                    menu:
                        "Have we met?":
                            $ MKhate += 1
                        "Hey friend! it's good to see you too!":
                            $ MKamore += 1
                        "Sham-bam, bamina to you, sir.":
                            $ MKagape += 1
                mky "Ooooh yeah. Ha. yeah..."
                hide MikYL
                show MikYR at right:
                    linear 2.5 xalign -0.5
                scene ClassFront
                show SenseiR with dissolve
                sns "Good morning class, and welcome to day 2 of the new school year."
                hide SenseiR
                show SenseiL:
                    xalign 0.5 yalign 1.0
                    linear 1.5 xalign 0.25 yalign 1.0
                sns "Has everyone had a good morning so far?"
                hide SenseiL with dissolve
                show Sally at right with dissolve
                show JamesYm at left with dissolve
                "class" "Yes sensei!"
                hide Sally with dissolve
                hide JamesYm with dissolve
                show SenseiR with dissolve
                sns "So! It has come to my attention that one of you is The Chosen One, ha ha!"
                sns "You."
                show SenseiBig
                hide SenseiR
                sns "It's you."
                menu:
                    "Um... what?":
                        $ SNSannoy += 1
                    "I KNEW IT!":
                        $ SNSagape += 1
                    "Yeah, I know. Your mom told me last night. Wait, maybe she said the 'hosin' one.":
                        $ SNShate
                hide SenseiBig with dissolve
                show SenseiL at left with dissolve
                sns "Nevermind that. The time has come for you to choose a side."
                hide SenseiL with dissolve
                show Sally at left with dissolve
                show JamesYm at right with dissolve
                "class" "CHOOSE!"
                hide Sally with dissolve
                hide JamesYm with dissolve
                show SenseiR at right with dissolve
                sns "Will you be the savior of the Earth or the Lord of the Moon?"
                sns "You can't have both, and either choice will destroy the other."
                hide SenseiR
                show SenseiL
                sns "What will it be?!?"
                show SenseiBig
                hide SenseiL
                sns "CHOOSE!"
                menu:
                    "What the hell is happening!?! I thought this was a dating sim!":
                        $ SNSagape += 1
                        jump escape
                    "Oh man. Oh jeez. Um... moon! For destruction? Because I don't live there?":
                        $ SNSannoy += 1
                        jump nope
                    "I choose the moon! Destroy the Earth! It is too full of trash.":
                        $ SNSamore += 1
                        jump YAYsensei
                        
            label escape:
                scene blkgrnd with dissolve
                "You run"
                scene hallway
                "You escape the school."
                scene school with dissolve
                "You escape the campus."
                scene country with dissolve
                "You escape the city."
                scene cottage with dissolve
                "You find a quaint little cottage out in the hills."
                "You enter into the most boring, heteronormative relationship since Paris and Helen of Troy."
                "This is the worst ending, just so you know."
                "And, like, you could have died before this."
                "You should envy your dead alternate-self."
                "Because that version of you had an adventure."
                jump credits
                
            label kidnapped:
                scene blkgrnd
                "This is the kidnapped label."
                jump credits
            
            label YAYsensei:
                "this is the YAYsensei label"
                jump credits
            
            label nope:
                "this is the {color=ff0000}nope{/color} label"
                jump credits
                
            label credits:
                scene blkgrnd
                "This is the credits, but I haven't made the credits yet."
                "Chris Brown A.K.A. Yeti Detective did the story and coding."
                "Teigan Hockman A.K.A. Telephonoscope will do the art."
                "Jordan Horne A.K.A. A Fucking Hipster will do the music."
                
                                                                                    
    return
