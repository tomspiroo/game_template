# Game_v1
Early development game

# To do:
Check out Tiled do make new levels, Im assuming that the Tiled app generates the images needed as well as the csv files for where each level of the floor is (walkable pathing, obstacles, grass, enemies, player)

CSV for objects seems fucked for the object indexing and placement, inconsistent throughout the level, when make own levels make sure everything is alright

Move all asseted to their own folder 'assets' for easy file manipulation and to make the folderspace look clean, WILL NEED TO CHANGE PATHING IN CODE IF YOU ARE TO DO THIS

Attacking while moving was not permitted in the tutorial, will have to fix this later so that you can attack and move at the same time, to do so go to 'player.py' in the function 'keyboard_input' and change the function's global 'if' statement to not hold all the inputs while attacking, instead add that conditional to the attack and magic keys only since there does need to be a cooldown of the weapons and magic attacks

When attack button and a move button is pressed at the saeme time there seems to be a bug where the character doesnt take the 'no movement when attacking' policy properly. This might eventually get changed since the attacking while moving might not be a mechanism I want but at the minute when attacking while moving the animation for the weapon does not move with the character, leaving it in the place of spawn until it is destroyed.

Currently (20/07/2024) the animate function in both the player and enemy are the same even though the bloke said theyre different? can put into Entity if they remain the same 

# Final game ideas - Title: The Garden?:
Gameplay:
- NPCs are randomly encountered within stages  of the run and will occupy a place at the beginning of the level and will stay there in that save, 'unlocking' them and their assistance. 

NPCs:
- Dog NPC, main companion and will be the first NPC the character finds along the runs, might spawn with him. Potentially: Eventually a demon steals the dog and turns him into cerebros (3-headed dog) to fight as a boss, knocking him out and making the dog rememebr you to take back to the launch area. Then you will have to find a way to cure him (defeat the demon who stole him?)
- Eventually the player will encounter an 'builder' who will be able to make room for late game NPCs and upgrading the launch stage
- A priest that offers blessings, he has alzheimers and cant remmeber his name or the charatcer each time you meet him in the launch room and he will roam since he lost his way due to his mental illness, thus giving blessings along the run rather than help at the start (maybe initial blessing). The dialogue box will give you randomised options as to what his name will be for the run since he cant remember. At late stages of the game there will be an option for 'not a priest' or then he turns into a demon saying 'thats right im somthing else completely' or something like that and will spawn devils for a boss fight
- Miner can give access to underground areas via bombs/shovel/pickaxe

Debug:
- impleemnt a report/record bug fucntion while game is in alpha in the pause menu, will probabl consist of adding to a .txt file where logs can be made

Enemies:
- See NPCs for some potential boss ideas
- assassin blinking enemy that blinks behind character, delayed heavy attack, then runs from main character. Could be a boss assassin, maybe from a 'league of assassins' type shit.