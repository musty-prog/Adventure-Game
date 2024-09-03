# Game with two stories from solo leveling and nano machine
import random

print("You are now Jin Runcandel, the youngest son of Runcandel, the land’s most prestigious swordsman family. You need to help him.")
FirstTask = int(input("You need to find the person who tried to kill you when you were young. Your goal is to kill him.\nNow, what will you do?\n1) Tell your father (Chiron Runcandel), the strongest in the game\n2) Train and get stronger\n3) Ask your sister for help\nChoose a number 1-3: "))

if FirstTask == 1:
    print("Your Dad was very disappointed in you, didn't help, and you got disowned by him.")
elif FirstTask == 3:
    print("Your sister tried to help you but couldn't find enough evidence and got assassinated.")
elif FirstTask == 2:
    Training = int(input("Yes, you shouldn't ask anyone for help since everyone is for themselves, and you are in a place full of darkness.\nYou went to the training area and started training. You found you had dark mana and the power of a fallen king. That king appeared in front of you and told you to go downstairs.\nWhat will you do?\n1) Listen to him\n2) Ignore him and keep training: "))

    if Training == 1:
        Gaston = int(input('After going downstairs, you found a hidden old sword. When you picked it up, you realized you are not only a swordsman but a magical-swordsman.\nAfter training for two years and improving your skills with the help of your sister, you went to the info sellers to find out who tried to kill you. They gave you the name of one of the nine stars (Bubare Gaston).\nAfter going back home, you found Bubare Gaston as a guest in your family house.\nHow would you act?\n1) Attack him\n2) Test his level\n3) Pretend you\'re weak: '))

        if Gaston == 3:
            ivt = int(input('Since you pretended to be weak, Gaston\'s son fought you, and you almost killed him. Gaston and his son are left, and now he is trying to kill you by any means possible. He invited you to his house.\nWhat will you do?\n1) Go\n2) Apologize: '))

            if ivt == 1:
                print("You went to his house, and from the start, the guards started attacking you. You defeated them easily and went to Gaston's room to fight him, and he started using his killing instincts.")

                fight = int(input('What will you do?\n1) Escape\n2) Fight: '))

                if fight == 2:
                    Myhp = 100
                    Npchp = 100

                    while Myhp > 0 and Npchp > 0:
                        MyAction = int(input('1) Attack\n2) Block\n3) Heal\nChoose 1-3: '))
                        NpAction = random.randint(1, 3)

                        if MyAction == 1:  # Player attacks
                            if NpAction == 1:  # NPC attacks
                                Npchp -= 20
                                Myhp -= 20
                                print(f"Both attacked! Your HP: {Myhp}, NPC's HP: {Npchp}")
                            elif NpAction == 2:  # NPC blocks
                                Npchp -= 10
                                print(f"You attacked, but NPC blocked! Your HP: {Myhp}, NPC's HP: {Npchp}")
                            elif NpAction == 3:  # NPC heals
                                Npchp -= 20
                                Npchp += 10
                                print(f"You attacked while NPC healed! Your HP: {Myhp}, NPC's HP: {Npchp}")

                        elif MyAction == 2:  # Player blocks
                            if NpAction == 1:  # NPC attacks
                                Myhp -= 10
                                print(f"NPC attacked while you blocked! Your HP: {Myhp}, NPC's HP: {Npchp}")
                            else:
                                print(f"Both blocked or healed! Your HP: {Myhp}, NPC's HP: {Npchp}")

                        elif MyAction == 3:  # Player heals
                            if NpAction == 1:  # NPC attacks
                                Myhp += 10
                                Myhp -= 20
                                print(f"You tried to heal, but NPC attacked! Your HP: {Myhp}, NPC's HP: {Npchp}")
                            elif NpAction == 2:  # NPC blocks
                                Myhp += 10
                                print(f"You healed, NPC blocked! Your HP: {Myhp}, NPC's HP: {Npchp}")
                            elif NpAction == 3:  # NPC heals
                                Myhp += 10
                                Npchp += 10
                                print(f"Both healed! Your HP: {Myhp}, NPC's HP: {Npchp}")

                        # Check if the game should end
                        if Myhp <= 0:
                            print("You lost!")
                            break
                        elif Npchp <= 0:
                            print("You won!")
                            break
                else:
                    print("You escaped, but your enemy is still out there.")
            else:
                print("You apologized, but Gaston didn't forgive you. The tension remains.")
        else:
            print("Wrong Choice")
else:
    print('Wrong input')
