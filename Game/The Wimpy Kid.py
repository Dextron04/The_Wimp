import time

choice_a = ["A", "a"]
choice_b = ["B", "b"]
choice_c = ["C", "c"]
choice_Y = ["Y", "y", "yes"]
choice_N = ["N", "n", "no"]
choice_D = ["D", "d"]
choice_E = ["E", "e"]
choice_f = ["F", "f"]
special_name = "Tushin Kulshreshtha"
friend_name = ["Moksh Wadhwa", "Garvit Shukla", "garvit", "om", "nanu", "Om", "Garvit", "Moksh", "moksh","MOKSH", "GARVIT"]
bff_name = ["Shukla", "shukla"]
bff_2_name = ["Chacha", "chacha"]

run = True

required = "\n Use only A, B, C and D only."

good = 0
bad = 0
money = 100
password = "GameByTushin"


print("Before the game please tell me a bit about yourself :)")
name = input("Your name is: ")
age = input("Your age is: ")
if name in special_name:
    time.sleep(3)
    print("Welcome Sir!")
    time.sleep(2)
    print("Thanks for making the game!")
    time.sleep(2)
elif name in bff_name:
    print("Aur madarchod shukla aa gaye yaha gaand marane?")
    time.sleep(4)
    print("Ab aa hi gaye ho beta toh khel hi lo")
    time.sleep(5)
elif name in bff_2_name:
    print("Aur bhoisdiwale chacha yaha kaha se ana ho gaya tera?")
    time.sleep(3)
    print("Chal ab aa hi gya hai toh gaand mara le yaha")
    time.sleep(4)
elif name:
    print("Welcome to the game friend!!!")
elif name in friend_name:
    time.sleep(2)
    print("Aur chutiye yaha kaha se aagaye?")
    time.sleep(1)
    print("Mili nahi kya?")
    time.sleep(2)
    print("Tujhe ye chalana kabse aa gaya bsdk!")
    time.sleep(3)
    print("Chal ab aa hi gaya hai toh khel le")
else:
    print("Error!")
def player_info():
    print("Please tell me a bit about yourself :)")
    time.sleep(3)
    print("Your name is:",input(" "))
    print("Your age is:",input(" "))

def player_status():
    print("Your name is ", name)
    print("Your age is ", age,'Years')
    print("Here is your player stat(Good, Bad, Money):-")
    print("Good", "=", good)
    print("Bad", "=", bad)
    print("Money", "=", money,'$')
    time.sleep(3)
    print("Restarting Game in 5 seconds....")
    time.sleep(5)


def intro():
    print('''\n 
                                                                                              
     ████████╗██╗░░░██╗░██████╗██╗░░██╗██╗███╗░░██╗  ██╗░░██╗  ██╗███╗░░██╗░█████╗░░░░                                                
     ╚══██╔══╝██║░░░██║██╔════╝██║░░██║██║████╗░██║  ██║░██╔╝  ██║████╗░██║██╔══██╗░░░                                                
     ░░░██║░░░██║░░░██║╚█████╗░███████║██║██╔██╗██║  █████═╝░  ██║██╔██╗██║██║░░╚═╝░░░                                                 
     ░░░██║░░░██║░░░██║░╚═══██╗██╔══██║██║██║╚████║  ██╔═██╗░  ██║██║╚████║██║░░██╗░░░                                                 
     ░░░██║░░░╚██████╔╝██████╔╝██║░░██║██║██║░╚███║  ██║░╚██╗  ██║██║░╚███║╚█████╔╝██╗                                                 
     ░░░╚═╝░░░░╚═════╝░╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝  ╚═╝░░╚═╝  ╚═╝╚═╝░░╚══╝░╚════╝░╚═╝                                                 
                                                                                                     
                                                                                              ''')
    time.sleep(3)
    print('''
       
            
            █▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█▄─▄▄─█▄─▀█▄─▄█─▄─▄─█─▄▄▄▄█████████████                           
            ██─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─██─▄█▀██─█▄▀─████─███▄▄▄▄─█░░██░░██░░██    
            ▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▀▄▄▀▀▄▄▀▀                                                       
                                                                   
                                                                    
                                                                      
                                                                      
                                                                                ''')
    time.sleep(4)
    print('''
              
          █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
          █░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░░░████░░░░░░██████████░░░░░░█░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░█     
          █░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀░░██████████░░▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█     
          █░░░░░░▄▀░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░████░░▄▀░░██████████░░▄▀░░█░░░░▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█     
          █████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░████████████░░▄▀░░██████████░░▄▀░░███░░▄▀░░███░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█     
          █████░░▄▀░░█████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░████░░▄▀░░██░░░░░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█     
          █████░░▄▀░░█████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀░░██░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█     
          █████░░▄▀░░█████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░████░░▄▀░░██░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░░░░░██░░▄▀░░█░░▄▀░░░░░░░░░░█     
          █████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░████████████░░▄▀░░░░░░▄▀░░░░░░▄▀░░███░░▄▀░░███░░▄▀░░██████████░░▄▀░░█░░▄▀░░█████████                
          █████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░████░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░░░▄▀░░░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░█████████                                                   
          █████░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░█████████                                                      
          █████░░░░░░█████░░░░░░██░░░░░░█░░░░░░░░░░░░░░████░░░░░░██░░░░░░██░░░░░░█░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░█████████                                                                                
          █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████                                                                                
                                                                                                                                     ''')
    print("Game Starting in 5 seconds.....")



def end():
    print('''
    
     ████████╗██╗░░░██╗░██████╗██╗░░██╗██╗███╗░░██╗  ██╗░░██╗  ██╗███╗░░██╗░█████╗░░░░                                                
     ╚══██╔══╝██║░░░██║██╔════╝██║░░██║██║████╗░██║  ██║░██╔╝  ██║████╗░██║██╔══██╗░░░                                                
     ░░░██║░░░██║░░░██║╚█████╗░███████║██║██╔██╗██║  █████═╝░  ██║██╔██╗██║██║░░╚═╝░░░                                                 
     ░░░██║░░░██║░░░██║░╚═══██╗██╔══██║██║██║╚████║  ██╔═██╗░  ██║██║╚████║██║░░██╗░░░                                                 
     ░░░██║░░░╚██████╔╝██████╔╝██║░░██║██║██║░╚███║  ██║░╚██╗  ██║██║░╚███║╚█████╔╝██╗                                                 
     ░░░╚═╝░░░░╚═════╝░╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝  ╚═╝░░╚═╝  ╚═╝╚═╝░░╚══╝░╚════╝░╚═╝  
     
     
                                       THANKS FOR PLAYING!              
                                                                                        ''')


def game_start():
    global good
    global bad
    global money
    global age
    global name
    global run
    print("\nYou're a boy from a small family your name is greg.")
    time.sleep(2)
    print("You live with your parents and 2 brothers one is young and the other is little")
    time.sleep(2)
    print("\nOne day you encounter that. you have located a small treasure map in your big brother's bed room")
    time.sleep(2)
    print("What will you do next? : ")
    time.sleep(2)
    print('''
    A. Look inside the map
    B. Ignore it.
    C. Tell your Mom
    D. Status and Restart
    E. Status
    F. Quit''')
    choice = input("=> ")
    if choice in choice_a:
        option_map()
    elif choice in choice_b:
        time.sleep(2)
        print("You ignore the map and your life continues without any adventure.")
        time.sleep(2)
        print("End 1")
        end()
    elif choice in choice_c:
        option_mom()
    elif choice in choice_D:
        time.sleep(2)
        print("Showing your player stat")
        time.sleep(2)
        print("Warning! This will restart the game.")
        time.sleep(3)
        player_status()
    elif choice in choice_E:
        print("Here is your current status:-")
        time.sleep(2)
        print("Good", "=", good)
        time.sleep(2)
        print("Bad", "=", bad)
        time.sleep(2)
        print("Money", "=", money,"$")
        print("Resuming game in 5 seconds....")
        time.sleep(5)
        game_start()
    elif choice in choice_f:
        end()
        time.sleep(3)
        run = False
    else:
        print("Invalid Input")
        time.sleep(2)
        print(required)
        game_start()
def option_mom():
    global good
    global bad
    global money
    global name
    global age
    global run
    print("\nYou take the map with you to show it to your mom")
    print("She takes the map from you and keeps it with her")
    print("She orders you to eat your food to get it")
    print("Will you obey it or not?")
    print("Yes or No")
    choice = input("=> ")
    time.sleep(1)
    good = +5
    if choice in choice_Y:
        good = +5
        print("You're a good kid!")
        time.sleep(2)
        good_son()
    elif choice in choice_N:
         bad = +10
         time.sleep(1)
         print("You should listen to your mom.")
         time.sleep(1)
         end()
    else:
        print("Invalid Input")
        game_start()
def good_son():
    global good
    global bad
    global money
    global name
    global age
    global run
    print("\nYou happily obey your mother's command and in return she gives you back the map.")
    print("Along with that you receive 50")
    money = +50
    map_part3()
def option_map():
    global good
    global bad
    global money
    global name
    global age
    global run
    print("\nYou slowly take out the map you found out in your brother's bed")
    time.sleep(2)
    print("While looking inside it you found out that this is a treasure map and can make you really rich")
    time.sleep(2)
    print("Suddenly your mom calls you for dinner. Will you? ")
    time.sleep(1)
    print('''
    A. Listen to your mom and go for dinner.
    B. ignore your mom
    C. Hide the map in your room.
    D. Status and Restart
    E. Status''')
    choice = input("=> ")
    if choice in choice_a:
        option_mom()
    elif choice in choice_b:
        print("\nYou ignored your mom and kept doing your work")
        time.sleep(2)
        print("\nBad levels increased")
        bad = +10
        print("\nBad", "=", bad)
        time.sleep(2)
        bad_start()
    elif choice in choice_c:
        print("\nYou quickly rush towards your room to hide it-")
        time.sleep(2)
        print("After reaching your room you hide it inside your closet,")
        time.sleep(2)
        print("Then you rush downstairs for dinner")
        good = +10
        time.sleep(2)
        print("Good levels Increased!")
        print("Good", "=", good)
        option_dinner()
    elif choice in choice_D:
        print("Showing your player stat")
        print("Warning! This will restart the game.")
        time.sleep(3)
        player_status()
    elif choice in choice_E:
        print("Here is your current status:-")
        time.sleep(2)
        print("Good", "=", good)
        time.sleep(2)
        print("Bad", "=", bad)
        time.sleep(2)
        print("Money", "=", money,"$")
        print("Resuming game in 5 seconds....")
        time.sleep(5)
        option_map()
    elif choice in choice_f:
        time.sleep(3)
        print("Quitting the game in 5 seconds.....")
        time.sleep(6)
        end()
        run = False
    else:
        print("Invalid Input")
        print(required)
        game_start()
def option_dinner():
    global good
    global bad
    global money
    global name
    global age
    print("She provides you with the food which you don't like")
    time.sleep(2)
    print("Will you eat it or not?")
    time.sleep(2)
    print('''
    Yes
    No''')
    choice = input("=> ")
    if choice in choice_Y:
        print("You tried to eat the food which you didn't like,")
        print("You felt sick  :(")
        time.sleep(2)
        print(".")
        time.sleep(2)
        print(".")
        time.sleep(2)
        print(".")
        time.sleep(2)
        print(".")
        time.sleep(2)
        print(".")
        time.sleep(2)
        print("You vomited all out of your mouth")
        time.sleep(2)
        print("You accidentally ate your dogs food ")
        time.sleep(2)
        print("Try to be more careful with what you eat")
        time.sleep(2)
        print("Restarting game in 5 seconds....")
        time.sleep(5)
        game_start()
    elif choice in choice_N:
        print("You deny the to eat the food in front of you,")
        print("Your mother laughs and says that the food in front of you is dog food")
        print('She provides you with Hot peperoni pizza......Yum!')
        time.sleep(2)
        good = +5
        time.sleep(1)
        print("Good levels increased!")
        map_part2()
    else:
        print("Invalid Input")
        print(required)
        game_start()
def map_part2():
    global good
    global bad
    global money
    global age
    global name
    global run
    print("After eating your food you rush towards your room along with the map")
    print('Suddenly your big brother steps in and says "Why are you in such a hurry?"')
    print("What will you do?")
    print('''
    A. Tackle him and make a run for your room
    B. Give a suitable reason
    C. Tell him mom has made his favourite dish for dinner
    D. Status and Restart
    E. Status
    F. Quit''')
    choice = input("=> ")
    if choice in choice_a:
        print("\nYou look down and bash towards your brother's stomach")
        print("He took damage from your attack and fell down")
        time.sleep(2)
        print("System: 'Well that was very rude of you'")
        bad = +5
        time.sleep(2)
        print("Bad Increased.")
        print("You arrived in your room successfully!")
        map_room()
    elif choice in choice_b:
        print("\nYou tell your brother that mom has made his favourite dish for dinner")
        time.sleep(2)
        print("System: 'Genius you've just had your dinner'")
        time.sleep(2)
        print("Your calls you a skunk")
        time.sleep(1)
        print('Snatches out the map out of your sneaky hands')
        time.sleep(1)
        print("and warns you not to come in his room again")
        time.sleep(2)
        print("System: NO MAP!")
        time.sleep(2)
        print("System:NO GAME!")
        time.sleep(2)
        print("GAME OVER GENIUS!")
        intro()
        time.sleep(15.5)
        game_start()
    elif choice in choice_c:
        print("\nYou try to give a suitable reason to your brother")
        print("System: Well your brother is as dumb as a donkey")
        print("System: There is nothing which is reasonable for him")
        print("You receive a beat up from him")
        print("He snatches the map from your hand")
        time.sleep(2)
        print("GAME                                                OVER!")
        end()
    elif choice in choice_D:
        print("Showing your player stat")
        print("Warning! This will restart the game.")
        time.sleep(3)
        player_status()
    elif choice in choice_E:
        print("Here is your current status:-")
        time.sleep(2)
        print("Good", "=", good)
        time.sleep(2)
        print("Bad", "=", bad)
        time.sleep(2)
        print("Money", "=", money,"$")
        print("Resuming game in 5 seconds....")
        time.sleep(5)
        map_part2()
    elif choice in choice_f:
        time.sleep(3)
        print("Quitting game in 5 seconds.......")
        time.sleep(6)
        end()
        time.sleep(3)
        run = False
    else:
        print("Invalid Input")
        print(required)
        game_start()
def bad_start():
    global good
    global bad
    global money
    global name
    global age
    global run
    print("After Ignoring your mom you took a peak inside the map,")
    time.sleep(1)
    print("You find out that the map which you're holding is actually a map of historic importance,")
    time.sleep(2)
    print("behind its back its written tissue")
    time.sleep(2)
    print("System: Your brother thought it to be a tissue I wonder what he was up to with this?")
    time.sleep(1)
    print("Suddenly you hear footsteps coming upstairs")
    print("What will you do?")
    print('''
    A. Make a run for your room and tricking mom
    B. Hide under your brother's bed
    C. Throw the map
    D. Status and restart
    E. Status
    F. Quit''')
    choice = input("=> ")
    if choice in choice_a:
        print("System: Well tricking your mom is bad :(")
        print("You sneak out of your mom escaping from your mother's eye")
        print("Your mom searched and called your name a few times")
        print("You didn't listen and rushed to your room")
        print("While rushing inside your room")
        if bad > 10:
            print("You dropped a few coins while going in")
        else:
            print("You strained your ankle")
            print("Bad level increased")
            bad = + 10
        map_room()
    elif choice in choice_b:
        print("\nYou hid under your brother's bed")
        print("System: Well that's one disgusting smell!")
        print("You weren't able to manage the smell and pass out")
        time.sleep(2)
        print("System: So that was it for you ",name)
        if name in friend_name:
            time.sleep(4)
            print("\nMujhe pata tha tere se nahi hoga bhen ke lode")
            time.sleep(4)
            print("Ab jaake kahi aur gaand mara")
            time.sleep(5)
            end()
        else:
            print("\nSorry you couldn't make")
            time.sleep(2)
            print("Hope you do it next time")
            time.sleep(2)
            print("or I'll find someone worthy")
            end()
    elif choice in choice_c:
        if name in friend_name:
            print("You threw the map out of the")
            time.sleep(2)
            print("Tushin: SHabash bhen ke lode aapse yahi umeed thi hume ab aap jaake mar jaiye")
            time.sleep(3)
            end()
        else:
            print("You threw the map out of the nearby window")
            time.sleep(3)
            print("System: Really?......Graet choice champ, Your quest is over.")
            time.sleep(3)
            print("System: Well at least you tried ")
            time.sleep(3)
            end()
    elif choice in choice_D:
        print("Showing your player stat")
        print("Warning! This will restart the game.")
        time.sleep(3)
        player_status()
    elif choice in choice_E:
        print("Here is your current status:-")
        time.sleep(2)
        print("Good", "=", good)
        time.sleep(2)
        print("Bad", "=", bad)
        time.sleep(2)
        print("Money", "=", money, "$")
        print("Resuming game in 5 seconds....")
        time.sleep(5)
        map_part2()
    elif choice in choice_f:
        time.sleep(3)
        print("Quitting game in 5 seconds.........")
        time.sleep(6)
        end()
        time.sleep(3)
        end()
    else:
        print("Invalid Input")
        print(required)
        game_start()
def map_part3():
    global good
    global bad
    global money
    global name
    global age
    global run
    print("After obeying your mother you have a clear way to your room")
    time.sleep(2)
    print("You rush towards your room")
    time.sleep(3)
    map_room()

def map_room():
    global good
    global bad
    global money
    global age
    global name
    global run
    print("\nYou are successfully inside your room and holding a map of historic importance")
    print("Good levels =", good)
    if good > 20:
        time.sleep(3)
        print("\nCongratulations! You are good enough to continue the game")
        time.sleep(2)
        print("2nd Part of the game will be provided to you on the website")
        time.sleep(2)
        print("Don't forget to use the given key provided in the end for the next part")
        time.sleep(2)
        print("Generating code........")
        time.sleep(5)
        print("Here's your code: HYGAME@2020")
        end()
    else:
        print("\nsorry you aren't good enough to continue this game please try a different ending :(")
        time.sleep(2)
        print("Quitting game....")
        time.sleep(3)
        end()

print("\nPlease provide the password which was given to you")
input_password = input("=> ")
if input_password in password:
    print("Thanks!!")
    time.sleep(2)
    intro()
    time.sleep(15.5)
    game_start()
else:
    print("Incorrect Password!")
    time.sleep(2)
    end()


