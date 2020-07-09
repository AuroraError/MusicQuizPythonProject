import random
import time
import sys

def leaderboard():
    print ("\n")
    print ("Check out the leaderboard")
    f = open('H_Highscore.txt', 'r')
    leaderboard = [line.replace('\n','') for line in f.readlines()]
    for i in leaderboard:
        print(i)
    f.close()
    time.sleep(10)
    sys.exit()

credentials = {"Jeff" : "1234", "Alex" : "2468"}
success = False
for i in range(3):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if (credentials.get(username) == password):
        print("login succeeded")
        success = True
        break
    else:
        print("login failed")
if not success:
    print("\nYour login failures have reached maximum, please try again in 10 minutes!")
    quit()

points = 0

while True:

    with open("songlist.txt", "r") as songs_file:
        with open("artistlist.txt", "r") as artists_file:
            songs_and_artists = [(song.rstrip('\n'), artist.rstrip('\n'))
                                for (song, artist) in zip(songs_file, artists_file)]

    random_song, random_artist = random.choice(songs_and_artists)
    songs_intials = "".join(item[0].upper() for item in random_song.split())


    print("The songs' initials are", songs_intials, "and the name of the artist is", random_artist)

    nb_tries_left = 3
    guess = input("Guess the name of the song! ")
    nb_tries_left -= 1

    finished = False
    while not finished:
        answer_found = (guess == random_song)
        if not answer_found:
            guess = input("Nope! Try again! ")
            nb_tries_left -= 1

        finished = (answer_found or nb_tries_left <= 0) 

    if answer_found:
        points = points + 1
        print ("Points = ", points)
        print ("Well done!")
    else:
        print ("Sorry, you've had two chances. Come back soon!")
        user = str(input("Enter a name to save your highscore: "))
        file = open ("H_Highscore.txt", "a")
        file.write("\n")
        file.write(user)
        file.write(",")
        file.write(str(points))
        file.write("pts")
        file.write("\n")
        file.close()
        time.sleep(0.5)
        leaderboard()
        sys.exit()
        quit()
