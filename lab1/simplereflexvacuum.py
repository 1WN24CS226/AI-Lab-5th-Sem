Rooms = {'A': 'Dirty', 'B': 'Clean'}
curr_room = "A"
while Rooms['A'] != "Clean" or Rooms['B'] != "Clean":
    if Rooms[curr_room] == "Dirty":
        print("Cleaning Room "+curr_room)
        Rooms[curr_room] = "Clean"
    else:
        print("Room is Clean")

        if curr_room == "A":
            curr_room = "B"
        elif curr_room == "B":
            curr_room = "A"
print("Both Rooms Clean")