# Game_v1
Early development game

# To do:
Check out Tiled do make new levels, Im assuming that the Tiled app generates the images needed as well as the csv files for where each level of the floor is (walkable pathing, obstacles, grass, enemies, player)

CSV for objects seems fucked for the object indexing and placement, inconsistent throughout the level, when make own levels make sure everything is alright

Move all asseted to their own folder 'assets' for easy file manipulation and to make the folderspace look clean, WILL NEED TO CHANGE PATHING IN CODE IF YOU ARE TO DO THIS

Attacking while moving was not permitted in the tutorial, will have to fix this later so that you can attack and move at the same time, to do so go to 'player.py' in the function 'keyboard_input' and change the function's global 'if' statement to not hold all the inputs while attacking, instead add that conditional to the attack and magic keys only since there does need to be a cooldown of the weapons and magic attacks