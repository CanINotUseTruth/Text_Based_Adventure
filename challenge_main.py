### 21 / 01 / 2021
### Toby Rutherford
### Text-Based Adventure Game

# --------------------------------------------------------------- Imports ---------------------------------------------------------------
import time
import sys
from random import randrange

# ---------------------------------------------------------------- Start ----------------------------------------------------------------

print("\n>>>>>>>>> Survival of Mt. Kosciuszco <<<<<<<<<<")
time.sleep(2)
name = input("\nEnter your name: ")
print("")

# ----------------------------------------------------------- Story-Functions -----------------------------------------------------------

# 1.0 - Story Start - Choice
def Start():
    ''' 1.0 '''
    text = ("\n\nFade to black..."
            "\n\nBlinding lights pierce through your closed eyes shocking you into consciousness."
            " A sharp pain engulfs your senses." 
            "\nYou open your eyes to see a ridge about fifteen meters tall."
            " Covered in snow it had blended in with the rest of the mountain below." 
            "\nYou finally assess yourself to find the source of the excruciating pain."
            " Your arm seems to have taken the brunt of the fall, blood gushing from multiple gashes."
            "\nYou rip a portion of your undershirt and wrap it around your arm tight to stop the bleeding."
            " Mt Kosciuszko is quite remote being at least 5 kilometers from any settlement."
            "\nBut with an injured arm and the sun going down after losing time to lost consciousness things are getting dire.")

    # Letter by Letter Typing - Start
    Typing(text)

    while True:
        # Start Decision Input
        time.sleep(1)
        text = ("\n\nWhat will you do?")

        Typing(text)

        time.sleep(1.5)
        print("\n\n1. Attempt to go back up the mountain and get your bearings.")
        time.sleep(1.5)
        print("2. Climb down the mountain and attempt to reach the rendez-vous point.")
        time.sleep(1.5)
        print("3. Wait for someone to come find you as the pain is unbearable.")
        time.sleep(1.5)
        istart = input("\nEnter Here: ")

        while True:
            if istart == '1':
                Up()
            elif istart == '2':
                Down()
            elif istart == '3':
                Wait()
            elif istart == 'q':
                StandardQuit()
            else:
                print("\nInvalid input..."
                    "\n\nTry again...")
                break

# 1.1 - Up Mountain - Risky - From 1.0
def Up():
    ''' 1.1 '''
    text = ("\nYou struggle back up the mountain managing to find a rocky path clear of snow."
            " Sitting at the highest point you can manage you fashion a flag out of your ski pole and bright red gaiter."
            "\nThe ski patrols do a round every afternoon in the helicopter to check the mountains more obscure slopes."
            " Hoping that the flag will help them spot you, you look around to see that your far from anywhere you recognize."
            "\nIt's a gamble to wait up here with the sun getting low, but now it's the only chance you have."
            "\n\nDoes the patrol find you:")

    # Letter by Letter Typing - Up
    Typing(text)

    # Start Decision Input
    time.sleep(1)
    print("\n\nChance of being found: 40%")
    time.sleep(1)
    print("Chance of being stranded: 60%")

    # Random chance for moving on
    chance = str(randrange(1, 11, 1))
    ichance = int(chance)
    if ichance <= 4:
        HeliFound()
    elif ichance >= 5:
        SnowDeath()
    else:
        ErrorQuit()
        
# 1.2 - Down Mountain - Guaranteed Continue - From 1.0
def Down():
    ''' 1.2 '''
    text = ("\nYou stumble down the slope using every bit of energy you can muster."
            "After seemingly endless hours of pushing forward you come across a path. It must be the summit trail!"
            "\nYou have a chance, people use this track constantly even in the winter time to reach the mountain's top."
            "You continue down the path, in the distance you see a black figure appear."
            "\nYou can't make it out but assume it is a hiker, as you get closer you notice it is actually a saddled horse."
            "This might be your saving grace, if it is tamed.")

    # Letter by Letter Typing - Down
    Typing(text)

    while True:
        time.sleep(1)
        text = ("\n\nWhat will you do?")

        Typing(text)

        time.sleep(1.5)
        print("\n\n1. Approach the horse and attempt to mount it.")
        time.sleep(1.5)
        print("2. Avoid the horse as it could be potentially dangerous.")
        time.sleep(1.5)
        ihorse = input("\nEnter Here: ")

        while True:
            if ihorse == '1':
                AppHorse()
            elif ihorse == '2':
                AvHorse()
            elif ihorse == 'q':
                StandardQuit()
            else:
                print("\nInvalid input..."
                    "\n\nTry again...")
                break

# 1.3 - Wait - Fail - From 1.0
def Wait():
    ''' 1.3 '''
    text = ("\nYou pray that someone comes looking for you."
            "You wait for hours..."
            "\n\nIt begins to snow and you finally realise...")

    # Letter by Letter Typing - Up
    Typing(text)

    SnowDeath()
    
# 2.1 - Snowy Death - Game Over - From 1.1
def SnowDeath():
    ''' 2.1 '''
    text = ("\nTime has run out..."
            "\n\nThe sun has begun to go down and noone ever found you."
            " The cold slowly starts to inch into your clothes clasping at every part of you it can grab."
            "\nThis is the end you can feel yourself begin to knock on death's door."
            " You feel your extremities begin to freeze over as you lose conciousness for the last time.")

    # Letter by Letter Typing - Snow Death
    Typing(text)

    GameOver()

# 2.2 - Heli Found - Choice - From 1.1
def HeliFound():
    ''' 2.2 '''
    text = ("\nYou've been found!"
            "\n\nA helicopter's rotary blades whirr and a moment later it banked around the mountain into view."
            " It lands nearby and two paramedics jump out, rushing to your side."
            "\nThey inspect your injured arm, you've lost a lot of blood."
            " You hear them discussing a hospital and it's distance."
            "\nThey turn to you and one of them says:"
            "\n\n<< Son we are going to need to do a field blood tranfusion... Do you know you're blood type? >>"
            "\n<< I don't know. >> You rasp as your eyes grow heavy."
            "\n<< What's your name? We might be able to find you in our system. >> He asked, hurriedly, seeing you slowly go to sleep.")
    
    # Letter by Letter Typing - Heli Found
    Typing(text)
    
    # Name input must match game original to continue
    name_input = input("\nEnter your name: ")

    if name_input == name:
        HeliSurvive()
    elif name_input == 'q':
        StandardQuit()
    else:
        HeliDeath()

# 2.3 AppHorse - Win - From 1.2
def AppHorse():
    ''' 2.3 '''
    text = ("\nAs you approach the horse it backs up apprehensively."
            "You speak softly to the horse to keep it calm."
            "\n\n<< It's okay. It's okay. >> You repeat over and over."
            "\n\nYou reach out and pat the horse on it's neck, it doesn't pull away."
            "This is a good sign so with your good hand and big effort you pull yourself into the saddle."
            "\nAs soon as you grab the reins the horse shoots off down the path."
            "You hold on for dear life. Closing your eyes as the cold winds whip around you."
            "\nThe horse carries you back to Smiggin's Hole, it seemed like it took no time at all."
            "There skiiers and patrols get you inside their station and onsite paramedics are able to assess and stablize you as you drift into unconciousness again.")

    Typing(text)

    Win()


# 2.4 AvHorse - Game Over - From
def AvHorse():
    ''' 2.4 '''
    text = ("\nYou avoid the horse thinking it's too risky."
            "But as you stumble through the snow losing every last drop of energy, you realise...")

    Typing(text)

    SnowDeath()

# 3.1 - HeliDeath - Game Over - From 2.2
def HeliDeath():
    ''' 3.1 '''
    text = ("\nUnable to quickly test your blood type or look your name up in any medical records, the paramedics watch helplessly."
             "\nThey attempt to rush you to hospital however you die from bloodloss in transit.")

    # Letter by Letter Typing - Heli Death
    Typing(text)
    
    GameOver()

# 3.2 - HeliSurvive - WIN - From 2.2
def HeliSurvive():
    ''' 3.2 '''
    text = ("\nYou whisper..."
               " My name is " + name + "."
               "\n\nYou were able to provide them with your name before passing out."
               " You wake up groggy in a hospital bed."
               "\nDoctors and nurses are around you checking many machines and contraptions."
               "They notice you have been aroused."
               "\n\n<< Ahh, you've finally come around " + name + ". >> Says one of the doctors."
               "\n<< You're lucky you survived, the paramedics say you were a bit of a hero yourself though. >>")

    # Letter by Letter Typing - Heli Survive
    Typing(text)

    Win()


# ----------------------------------------------------------- Other-Functions -----------------------------------------------------------

# Letter by Letter typing function for text specified
def Typing(text):
    ''' Controls letter by letter typing '''
    type_text = text
    for c in type_text:
        sys.stdout.write(c)
        sys.stdout.flush()
        seconds = "0." + str(randrange(1, 2, 1))
        seconds = float(seconds)
        time.sleep(seconds)

# Function to call to Quit or Continue (Start Again)
def GameOver():
    ''' Signals loss of Game '''
    text = ("\n\nGame Over...")

    # Letter by Letter Typing - Game Over
    Typing(text)
    # Start Again or Quit Input
    go_choice = input("\nWould you like to start again? 'Yes' or 'No'"
                      "\n\nEnter Here: ")

    # If statement that controls restart or quit
    if go_choice == 'Yes':
        Start()
    elif go_choice == 'No':
        StandardQuit()
    else:
        InvalidChoice()

# Quits game for invalid choices
def InvalidChoice():
    ''' Quits game due to invalid choice '''
    print("\nYou have not entered a valid choice..."
          "\n\nQuitting program...")

    exit()

# Quits game if there is an error in certain functions
def ErrorQuit():
    ''' Quits game due to errors '''
    print("\nError occured..."
          "\n\nQuitting program...")
    
    exit()

# Quits game if called upon by player with 'q'
def StandardQuit():
    ''' Quits game due to player input '''
    print("\nYou have selected to quit..."
          "\n\nQuitting program...")
    
    exit()

# Function to let player know they have beaten the game
def Win():
    ''' Completes game with WIN '''
    text = ("\nYou have survived! Congratulations, you are the hero to your own story." 
            "\nYou overcome the challenges and saved yourself (With a bit of help here and there)"
            "\n\nVirtual high-fives all round!")
    
    # Letter by Letter Typing - Win
    Typing(text)

    Credits()

def Credits():
    ''' Plays credits '''
    text = ("\nCredits..."
            "\n\nDeveloper: Me"
            "\nStory-Writer: Myself"
            "\nExecutive Producer: I"
            "\nHero: You"
            "\n\nThankyou for playing..."
            "\n\n :)")
    
    # Letter by Letter Typing - Credits
    Typing(text)
    


# ------------------------------------------------------------- Initializer -------------------------------------------------------------

# Start Call
if __name__ == "__main__":
    Start()