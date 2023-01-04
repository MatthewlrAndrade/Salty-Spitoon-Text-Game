from time import sleep
from numpy import random

print('''"Hello, what's your name?"''')
username = input("Enter name: ")

if username == "69":
    print("nice")
    exit()

if username == "Peter Griffin":
    print('''You say, "Hey Lois, I'm in a text-based Spongebob game!"''')
    sleep(2)

print('You are trying to enter the Salty Spitoon to prove to your friend {} that you are tough.' .format(username[::-1]))
sleep(3.5)
print('The bouncer, Reg, says, "Welcome to the Salty Spitoon {}. How tough are ya?"' .format(username))
sleep(3)
response1dict = {
    "I ate a bowl of nails for breakfast!" : "1",
    "*You glance at his MOM tattoo.*" : "2",
    "You got a new bottle of ketchup?" : "3",
    "*Choose your own response.*" : "4"
    }
print(" ")
print(response1dict)

response1_1 = 'You say, "I ate a bowl of nails for breakfast!"'
response1_2 = 'You glance at his MOM tattoo.'
response1_3 = 'You say, "You got a new bottle of ketchup?"'

response1 = input("Select a number that corresponds with an option to choose that option: ")

if response1 == "1":
    print(response1_1)
    sleep(1.5)
    print('Reg says, "Yeah so?"')
    sleep(1.5)
    response1_1dict = {
        "With milk" : "1",
        "Without any milk" : "2"
        }
    print(" ")
    print(response1_1dict)

    response1_1_a = 'You say, "With milk"'
    response1_1_b = 'You say, "Without any milk"'

    response1_1 = input("Select your response: ")
    if response1_1 == "1":
            print('Reg says, "Only cowards eat bowls of nails with milk. {}, you belong over in that place over there!"' .format(username))
            sleep(2.5)
            print('''You reply, "Weenie Hut Junior's?"''')
            sleep(1.5)
            print('Reg sternly commands, "Yeah, now scram!"')
            sleep(1)
            print('You have reached the CRY OVER DRANK MILK ENDING!')
    if response1_1 == "2":
            print('Reg politely says, "Oh, go right this way! Sorry to have kept you waiting."')
            sleep(1.5)
            print('You have successfully infiltrated the Salty Spitoon!')

if response1 == "2":
    print(response1_2)

    response1_2dict = {
        "*You compliment him on his tattoo*" : "1",
        "*You forcibly rip off the tattoo (and skin) from his body*" : "2"
        }
    print(" ")
    print(response1_2dict)

    response1_2_a = "You compliment him on his tattoo."
    response1_2_b = "You forcibly rip off the tattoo (and skin) from his body."
    response1_2 = input("Select your response: ")
    if response1_2 == "1":
            compliment = input("What will you say about Reg's tattoo? ")
            print('''You bashfully say, "{}!"''' .format(compliment))
            sleep(2 + len(compliment)/20)
            print('''Reg, who is blushing, says, "What are you saying {}?" Then he sharply says, "Are you coming on to me? That's disgusting! I will personally punt you across the street"''' .format(username))
            sleep(4)
            print('''You says quizzically, "You mean to Weenie Hut Junior's?"''')
            sleep(1.5)
            print('Reg, preparing for the kick of the lifetime, replies, "Yeah, now prepare to be launched into orbit!"')
            sleep(2)
            print('You have reached the {} BUT BALL ENDING!' .format(username.upper()))
    if response1_2 == "2":
            print(response1_2_b)
            sleep(1.75)
            print('You say, "You got any more tattoos!?"')
            sleep(1.5)
            print('''Reg fearfully replies, "Uh no, that won't be necessary. Go right on ahead."''')
            sleep(2)
            print('You have successfully infiltrated the Salty Spitoon!')

if response1 == "3":
    print(response1_3)
    sleep(1)
    print('Reg indifferently says, "Sure."')

    response1_3dict = {
        "*You fail to open the ketchup bottle*" : "1",
        "*You smash Reg over the head with the glass ketchup bottle*" : "2"
        }
    sleep(1.5)
    print(" ")
    print(response1_3dict)

    response1_3_a = "You fail to open the ketchup bottle."
    response1_3_b = "You smash Reg over the head with the glass ketchup bottle."
    response1_3 = input("Select your response: ")
    if response1_3 == "1":
            print(response1_3_a)
            sleep(1)
            print('''Reg angrily commands, "Get outta here. This place is too tough for you {}!"''' .format(username))
            sleep(2)
            print('''Fill in the following 2 blank statements without capitalizing any letters (unless they are names) or using ending punctuation (periods, exclamation marks, question  marks, etc...).''')
            response1_3_a_a = input('''"I'll have you know I _______  " (an action) ''')
            response1_3_a_b = input('''and I only ______!" (something that you did/something that happened to you as a result of the last action) ''')
            print('''You quickly retort, "Too tough for me!? I'll have you know I {} and I only {}!"''' .format(response1_3_a_a, response1_3_a_b))
            sleep(3 + len(response1_3_a_a)/30 + len(response1_3_a_a)/30)
            print('''Reg calmingly says, "Listen {}. I think you'd be more comfortable over at that place."''' .format(username))
            sleep(2.5)
            print('''You, indignantly reply, "Are you saying I belong in Weenie Hut Junior's!?"''')
            sleep(2.25)
            print('''Reg, realizing his mistake, says, "Oh no, I was pointing at that place next to it."''')
            sleep(2)
            print('''Incensed at the notion, you say, "SUPER Weenie Hut Junior's!?"''')
            sleep(2)
            print('''Reg commands, "Yeah kid, unless you're man enough to fight me!"''')
            response1_3_adict = {
                "*You choose to fight Reg*" : "1",
                "*You decide to go to Weenie Hut Junior's*" : "2"
                }
            sleep(1.5)
            print(" ")
            print(response1_3_adict)

            response1_3_a_a_a = "You choose to fight Reg."
            response1_3_a_a_b = "You decide to go to Weenie Hut Junior's."

            response1_3_c = input("Select your response: ")
            if response1_3_c == "1":
                print(response1_3_a_a_a)
                sleep(1)
                print('''Reg says, "Alright {}, you asked for this. I really didn't want to have to fight you but here we are."''' .format(username))
                sleep(2)

                i1 = len(input("Pick your move: "))
                print("{} damage dealt" .format(i1))

                if i1 < 142069 or i1 > 142069:
                    print('''Reg says, "Is that all you got {}? You really are a weenie!"''' .format(username))
                    sleep(2.5)
                    print('''Reg pleads, "Listen {}, since I'm such a nice guy I won't attack you if you turn around and go to Weenie Hut Junior's! This is your last chance, what will you do?"''' .format(username))
                    sleep(4)
                    Regchoicedict = {
                        "Leave and go to Weenie Hut Junior's" : "1",
                        "Continue the fight with Reg." : "2"
                        }
                    print(" ")
                    print(Regchoicedict)

                    Regchoice = input("Which will you choose? ")
                    if Regchoice == "1":
                        print('''You decide to leave and go to Weenie Hut Junior's because you realize you can't take on Reg.''')
                        sleep(2)
                        print('''Reg says, "Smart move {}, I didn't want to hafta end up hurting you, so go back to where you belong!"''' .format(username))
                        sleep(2)
                        print('''You have reached the {} HAS BECOME THE WEENIE GOD ENDING!''' .format(username.upper()))

                    if Regchoice == "2":
                        print('''You foolishly stay to fight Reg.''')
                        sleep(1.5)
                        print('''Reg says condescendingly, "{}, {}, {}! I thought you were so much smarter than that. For shame."''' .format(username, username, username))
                        sleep(3)
                        print('''Reg punches you in the gut so hard that you start puking and then he body slams your face.''')
                        sleep(2.5)
                        print('''You are barely holding onto consciousness.''')
                        sleep(1.5)
                        print('''Reg looks at you and says, "Well {}, any last words?"''' .format(username))
                        sleep(2.5)
                        lastwords = input("What will your last words be? ")
                        print('''Reg looks down at you and says, "'{}' Huh. I've never heard anything crazier than that in my life. Goodbye {}."''' .format(lastwords, username))
                        sleep(3 + len(lastwords)/20)
                        print('''Reg does a cannonball right onto your head.''')
                        sleep(1.5)
                        print('''You have died.''')

                else:
                    print('''You have successfully murdered Reg and are now free to enter the Salty Spitoon!''')
                    sleep(2)
                    print('''You have reached the {} YOU ARE DEFINITELY A MURDERER ENDING!''' .format(username.upper()))


            if response1_3_c == "2":
                print(response1_3_a_a_b)
                sleep(1.5)
                print('''You have reached the SUPER WEENIE ENDING!''')

    if response1_3 == "2":
            print(response1_3_b)
            sleep(1.5)
            print('''You used enough force to shatter the bottle on his head and knock him unconscious. Now no one can stop you from going into the Salty Spitoon!''')
            sleep(3.5)
            print("You have reached the {}, YOU MAY BE A MURDERER ENDING!" .format(username.upper()))


if response1 == "4":
    response4_1 = input('''What will you say to Reg? ''')
    print('''Reg says, "Did I heard you correctly, did you really say '{}?' I've never been so insulted in my life!"''' .format(response4_1))
    sleep(3 + len(response4_1)/20)
    print('''You say, "Oh yeah, I really meant that."''')
    sleep(2)
    print('''Reg responds, "Well if that is so, I will engage thee in a duel {}."''' .format(username))
    sleep(2.9)
    print(" ")
    print('''Challenger Reg approaches!''')
    sleep(1.75)
    print(' ')
    print('''Reg says, "Alright {}, since I'm so nice, you will get to make the first move!"''' .format(username))
    sleep(1)
    RegHealth = 500
    HP = 150
    Turn = 1

    while RegHealth > 0 or HP > 0:
        sleep(2)
        print(' ')
        print('''{} HP = {}''' .format(username, HP))
        sleep(1)

        Areset = 1

        Attack1_input = input("What will your move be? ")

        if Turn == 1:
            Item = 1
            Warn = 1

        if Attack1_input == "ITEM" and Item == 1 and HP <= 100 and HP > 0:
            print('''You ate the Krabby Patty! 50 HP restored!''')
            HP = HP + 50
            Item = 0
            Areset = 0
        elif Attack1_input == "ITEM" and Item == 1 and HP > 100:
            print('''You cannot restore HP until you have less than 100 HP.''')
            Item = 1
            continue
        elif Attack1_input == "ITEM" and Item <= 0 :
            print('''You have already consumed the Krabby Patty.''')
            Item = 0
            continue
        else:
            pass

        Attack1 = list(Attack1_input)
        Attack_stat = len(Attack1[0:50])
        RNG = random.multinomial(n=1, pvals = [899/1000, 100/1000, 1/1000])
        if RNG[1] == 1 and Areset == 1:
            Random_Damage = Attack_stat + random.randint(40, 50)
            print('''A critical hit!''')
            print('''{} damage dealt!''' .format(Random_Damage))
        if RNG[0] == 1 and Areset == 1:
            Random_Damage = Attack_stat + random.randint(10, 30)
            print('''{} damage dealt!''' .format(Random_Damage))
        if RNG[2] == 1 and Areset == 1:
            Random_Damage = RegHealth
            print('''It's a one-hit  KO!''')

        RegHealth = RegHealth - Random_Damage
        
        if RegHealth <= 0:
            sleep(1)
            print(' ')
            print('''You have beat Reg! You are free to enter the Salty Spitoon!''')
            sleep(2)
            print('''You have reached the SUCCESSFUL ASSASSINATION ENDING!''')
            break


        sleep(1)
        print(' ')
        print('''It's Reg's turn.''')
        sleep(1)
        print('''Reg attacks!''')
        RNG = random.multinomial(n=1, pvals = [800/1000, 165/1000, 25/1000, 10/1000])
        if RNG[1] == 1:
            Random_Damage_r = random.randint(60, 75)
            print('''A critical hit!''')
            print('''{} damage dealt!''' .format(Random_Damage_r))
        if RNG[0] == 1:
            Random_Damage_r = random.randint(10, 30)
            print('''{} damage dealt!''' .format(Random_Damage_r))
        if RNG[2] == 1:
            Random_Damage_r = HP
            print('''It's a one-hit KO!''')
        if RNG[3] == 1:
            RegHealth = 600
            Random_Damage_r = 0
            print('''Reg heals himself back to full.''')
            
        HP = HP - Random_Damage_r
            
        if HP <= 0:
            sleep(1)
            print(' ')
            print('''You have been defeated by Reg...''')
            sleep(1.5)
            print('''Reg gloats by saying, "Tough luck {}, always knew you were a bit weak!''' .format(username))
            sleep(2)
            print('''Game Over!''')
            break

        Turn = Turn + 1
        print(" ")
        print('''Turn {}''' .format(Turn))

        if HP <= 50 and HP > 0 and Warn == 1 and Item == 1:
            print(" ")
            print('''"Here's some divine intervention! I put a Krabby Patty in your Item box if you need it! Open it up by typing 'ITEM' on your next turn!" Good luck getting into the Salty Spitoon!''')
            sleep(6)
            Warn = 0
            continue
                
if response1 == "5":
    print('''Reg looks at you and realizes that he has been wasting his life as a bouncer and decides to live out his dream as a ballerina.''')
    print('''You have reached the REG REDISCOVERY ENDING!''')

if response1 == "69":
    print('''Reg cautions, "Look kid, we ain't doing that!''')

if response1 == "420":
    print('''Wait, if we're underwater, how can we...''')
                
