import time
import sys
import winsound
import pyaudio
import wave
import threading



crow = "audio/crow.wav"
butler = "audio/butler.wav"
horror = "audio/horror.wav"
cry = "audio/cry.wav"
happy =  "audio/happy.wav"
murder = "audio/murder.wav"
vampire = "audio/vampire.wav"
behind = "audio/behind.wav"


def play_again():
    while True:
        play_again = input("Do you want to play again? (yes or no)").lower()
        if play_again == "yes":
            print("Starting a new game...")
            time.sleep(3)
            start_game()
            thread = threading.Thread(target=play_music, args=(filename,))
            thread.start() # repeat the music
        elif play_again == "no":
            print("Thanks for playing! Goodbye.")
            time.sleep(1)
            sys.exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            play_again()



def play_music(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(chunk)

    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(chunk)

    stream.stop_stream()
    stream.close()

    p.terminate()

filename = horror
thread = threading.Thread(target=play_music, args=(filename,))
thread.start()


def start_game():
    player_choice = ""
    player_choice2 = ""
    player_choice3 = ""
    player_choice4 = ""
    player_choice5 = ""
    player_choice6 = ""
    player_choice7 = ""
    player_choice8 = ""
    player_choice9 = ""
    player_choice10 = ""
    choices = ["Tent", "tent", "Walk", "walk", "ignore", "Ignore", "explore", "Explore", "Upstairs", "upstairs", "Downstairs", "downstairs", "Inside", "inside",
               "seduce", "Seduce", "Explain", "explain", "talk", "Talk", "silent", "Silent", "accept", "Accept", "decline", "Decline", "back", "Back", "kiss", "Kiss"]
    while player_choice == "":
        player_choice = input(
            "Hello stranger, you're lost in a forest and it's getting dark. You can set up a tent or keep on walking. (pick between tent/walk)")
        if player_choice not in choices:
            print("This is not a valid choice! Pick something else.")
            player_choice = ""
            print(player_choice)
        if player_choice.lower() == "walk":
            print("Just pick tent bro pls. It will lead to the same thing anyway")
        if player_choice.lower() == "tent":
            print("You set up the tent and went to sleep.")
            time.sleep(3)
            print("The morning came and you decided to keep exploring.")
            time.sleep(3)
            while player_choice2 == "":
                player_choice2 = input(
                    "After exploring for a long. Long time, you see this big mansion. Will you ignore the mansion and explore something else or explore the mansion? (pick between ignore/explore)")
                if player_choice2 not in choices:
                    print("This is not a valid choice! Pick something else.")
                    player_choice2 = ""
                if player_choice2.lower() == "ignore":
                    time.sleep(1)
                    print(
                        "It was way too foggy and dark to keep exploring. A swarm of dnagerous crows killed you. 'Crow Ending'")
                    winsound.PlaySound(crow, winsound.SND_FILENAME)
                if player_choice2.lower() == "explore":
                    print(
                        "You see that the door is opened, you're way too curious. So you go inside.")
                    time.sleep(3)
                    while player_choice3 == "":
                        player_choice3 = input(
                            "You're inside the mansion, but you don't see any people. Infront of you are stairs that lead to downstairs. What are you going to do? Stay upstairs and explore the place, or go downstairs and explore the place? (pick between upstairs/downstairs)")
                        if player_choice3 not in choices:
                            print("This is not a valid choice! Pick something else.")
                            player_choice3 = ""
                        if player_choice3.lower() == "downstairs":
                            time.sleep(3)
                            print(
                                "Oh no! You bumped into this butler and got kicked out. 'Kicked Out! Ending.'")
                            winsound.PlaySound(butler, winsound.SND_FILENAME)
                        if player_choice3.lower() == "upstairs":
                            while player_choice4 == "":
                                player_choice4 = input(
                                    "Upstairs, you find another door. What are you going to do? Open the door and go inside, or go downstairs? (pick between inside/downstairs)")
                                if player_choice4 not in choices:
                                    print(
                                        "This is not a valid choice! Pick something else.")
                                    player_choice4 = ""
                                if player_choice4.lower() == "downstairs":
                                    time.sleep(3)
                                    print(
                                        "Oh no! You bumped into this butler and got kicked out. 'Kicked Out! Ending.'")
                                    winsound.PlaySound(butler, winsound.SND_FILENAME)
                                if player_choice4.lower() == "inside":
                                    while player_choice5 == "":
                                        player_choice5 = input(
                                            "You open the door and take a look inside, your eyes widen from seeing a handsome young man sittons on a sofa. He speaks up calmly, 'Hello there, what brings you here?' What are you going to do? Seduce him, or give him an explanation? (pick between seduce/explain)")
                                        if player_choice5 not in choices:
                                            print(
                                                "This is not a valid choice! Pick something else.")
                                            player_choice5 = ""
                                        if player_choice5.lower() == "seduce":
                                            while player_choice8 == "":
                                                player_choice8 = input(
                                                    "You walk closer to him and he gets up. Suddenly he leans in but doesn't kiss you. What are you going to do? Back up, or kiss him? (pick between back/kiss)")
                                                if player_choice8 not in choices:
                                                    print(
                                                        "This is not a valid choice! Pick something else.")
                                                    player_choice8 = ""
                                                if player_choice8.lower() == "kiss":
                                                    print(
                                                        "Uh Oh! The man didn't trust you and tricked you into thinking he was going to kiss you. Instead of kissing you, he bit your neck and sucked your blood. 'Vamp Ending'")
                                                    winsound.PlaySound(vampire, winsound.SND_FILENAME)
                                                if player_choice8.lower() == "back":
                                                    time.sleep(2)
                                                    print(
                                                        "He stares at you with a slight smirk appearing on his pale face. 'Take a seat' he says as his penis is hard. You obey him and take a seat next to him")
                                                    time.sleep(1)
                                                    while player_choice9 == "":
                                                        player_choice9 = input(
                                                            "The heavy silence in the room is making it akward for you. His deep stare isn't it making it any better. What are you going to do? Start a conversation with him, or stay silent? (pick between talk/silent)")
                                                        if player_choice9 not in choices:
                                                            print(
                                                                "This is not a valid choice! Pick something else.")
                                                            player_choice9 = ""
                                                        if player_choice9.lower() == "silent":
                                                            time.sleep(1)
                                                            print(
                                                                "The man clears his throat and suddenly gets up to grab something.")
                                                            time.sleep(2)
                                                            print(
                                                                "He quickly turned around and stabbed you with the knife he grabbed. He didn't trust you and became impatient, so his only option was ending you. 'Time's Up Ending'")
                                                            winsound.PlaySound(behind, winsound.SND_FILENAME)

                                                            time.sleep(2)

                                                            winsound.PlaySound(murder, winsound.SND_FILENAME)
                                                        if player_choice9.lower() == "talk":
                                                            while player_choice10 == "":
                                                                player_choice10 = input(
                                                                    "After having a nice conversation with the man, he offers you a glass of wine. What are you going to do? Accept it, or decline it? (pick between accept/decline)")
                                                                if player_choice10 not in choices:
                                                                    print(
                                                                        "This is not a valid choice! Pick something else.")
                                                                    player_choice10 = ""
                                                                if player_choice10.lower() == "accept":
                                                                    print(
                                                                        "The man is happy you accepted his drink. 'Cheers!' He said.")
                                                                    time.sleep(
                                                                        1)
                                                                    print(
                                                                        "After a whole night of talking with the gorgeous man, he offered you to stay so that you could go home safely the next morning. He loved your company! 'Euphoria Ending' ")
                                                                    winsound.PlaySound(happy, winsound.SND_FILENAME)
                                                        if player_choice10.lower() == "decline":
                                                            time.sleep(1)
                                                            print(
                                                                "Oh, the man didn't think you were going to decline his offer. It made him upset :( 'Blue Side Ending'")
                                                            winsound.PlaySound(cry, winsound.SND_FILENAME)
                                        if player_choice5.lower() == "explain":
                                            print("You explain...")
                                            time.sleep(2)
                                            print(
                                                "He stares at you with a slight smirk appearing on his pale face. 'Take a seat' he says as his p**is is hard. You obey him and take a seat next to him")
                                            time.sleep(1)
                                            while player_choice6 == "":
                                                player_choice6 = input(
                                                    "The heavy silence in the room is making it akward for you. His deep stare isn't it making it any better. What are you going to do? Start a conversation with him, or stay silent? (pick between talk/silent)")
                                                if player_choice6 not in choices:
                                                    print(
                                                        "This is not a valid choice! Pick something else.")
                                                    player_choice6 = ""
                                                if player_choice6.lower() == "silent":
                                                    time.sleep(1)
                                                    print(
                                                        "The man clears his throat and suddenly gets up to grab something.")
                                                    time.sleep(2)
                                                    print(
                                                        "He quickly turned around and stabbed you with the knife he grabbed. He didn't trust you and became impatient, so his only option was ending you. 'Time's Up Ending'")
                                                    winsound.PlaySound(behind, winsound.SND_FILENAME)
                                                    time.sleep(1)
                                                    winsound.PlaySound(murder, winsound.SND_FILENAME)
                                                if player_choice6.lower() == "talk":
                                                    while player_choice7 == "":
                                                        player_choice7 = input(
                                                            "After having a nice conversation with the man, he offers you a glass of wine. What are you going to do? Accept it, or decline it? (pick between accept/decline)")
                                                        if player_choice7 not in choices:
                                                            print(
                                                                "This is not a valid choice! Pick something else.")
                                                            player_choice7 = ""
                                                        if player_choice7.lower() == "accept":
                                                            print(
                                                                "The man is happy you accepted his drink. 'Cheers!' He said.")
                                                            time.sleep(1)
                                                            print(
                                                                "After a whole night of talking with the gorgeous man, he offered you to stay so that you could go home safely the next morning. He loved your company! 'Euphoria Ending' ")
                                                            winsound.PlaySound(happy, winsound.SND_FILENAME)
                                                        if player_choice7.lower() == "decline":
                                                            time.sleep(1)
                                                            print(
                                                                "Oh, the man didn't think you were going to decline his offer. It made him upset :( 'Blue Side Ending'")
                                                            winsound.PlaySound(cry, winsound.SND_FILENAME)
                                                            

start_game()
play_again()

