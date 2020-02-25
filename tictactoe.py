# I am Prerak Patel and my student number is 000736376, I have created this
# program all by myself and I haven't shared with anyone. My professor name
# is Tiffany,Antopolski

def board(place):

    print("\t\t\t\t" + place[0] + "  |  " + place[1]+ "  |  " + place[2])
    print("\t\t\t      " + "-"*17)
    print("\t\t\t\t" + place[3] + "  |  " + place[4]+ "  |  " + place[5])
    print("\t\t\t      " + "-"*17)
    print("\t\t\t\t" + place[6] + "  |  " + place[7]+ "  |  " + place[8])

def wins_O(place):
    if (place[0] == place[1] == place[2] or place[3] == place[4] == place[5] \
        or place[6] == place[7] == place[8] or place[0] == place[4] == place[8] \
        or place[2] == place[4] == place[6] or place[0] == place[3] == place[6] \
        or place[1] == place[4] == place[7] or place[2] == place[5] == place[8]):
        return True
    else:
        return False

def wins_X(place):
    if (place[0] == place[1] == place[2] or place[3] == place[4] == place[5] \
        or place[6] == place[7] == place[8] or place[0] == place[4] == place[8] \
        or place[2] == place[4] == place[6] or place[0] == place[3] == place[6] \
        or place[1] == place[4] == place[7] or place[2] == place[5] == place[8]):
        return True
    else:
        return False
    
def draw(place,count):
    if count == 9 :
        for variable in range(0,8,1):
            if place[variable] in ("O","X"):
                return True
            else:
                return False
        
first_player = input("Please enter the name of the first name : ")
second_player = input("Please enter  the name of the second name : ")

print("\nFirst chance is given to them whose first alphabet of the name is \
coming first in a-z.")

players = [first_player,second_player]

players.sort()

print("\nFirst chance is of " + \
      players[0] + "\nSecond chance is of " + players[1] + ".")

print(players[0] + " is O and " + players[1] + " is X.")
print("\n\n\t\t   Here is your board to play tic tac toe game\n\n")
place = ["1","2","3","4","5","6","7","8","9"]
chance = players[0]
board(place)
count = 0

while wins_O(place) != True and wins_X(place) != True and draw(place,count) != True:
    if chance == players[0]:
        place_in_board = int(input(players[0] + " chance to play select any number in between 1-9 : "))
        place_in_board = place_in_board - 1
        if place[place_in_board] in ["O","X"]:
            print("Please try another place these already used")
        else:
            place[place_in_board] = "O"
        chance = players[1]
        board(place)

    elif chance == players[1]:
        place_in_board = int(input(players[1] + " chance to play select any number in between 1-9 : "))
        place_in_board = place_in_board - 1
        if place[place_in_board] in ["O","X"]:
            print("Please try another place these already used")
        else:
            place[place_in_board] = "X"
        chance = players[0]
        board(place)

    count += 1

if wins_O(place) == True:
    print("Congratulations " + players[0] + " you won.")

elif wins_X(place) == True:
    print("Congratulations " + players[1] + " you won.")

elif draw(place,count) == True:
    print("Match draw")


