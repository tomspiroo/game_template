# game setup
WIDTH    = 1280 
HEIGTH   = 720
FPS      = 60
TILESIZE = 64
 
# UI
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colours
WATER_COLOUR = '#71ddee'
UI_BG_COLOUR = '#222222'
UI_BOARDER_COLOUR = '#111111'
TEXT_COLOUR = '#EEEEEE'

# UI colours
HEALTH_COLOUR = 'red'
ENERGY_COLOUR = 'blue'
UI_BOARDER_COLOUR_ACTIVE = 'gold'


# weapons 
weapon_data = {
    'sword':    {'cooldown': 100,   'damage': 15,   'graphic': '../graphics/weapons/sword/full.png'},
    'lance':    {'cooldown': 400,   'damage': 30,   'graphic': '../graphics/weapons/lance/full.png'},
    'axe':      {'cooldown': 300,   'damage': 20,   'graphic': '../graphics/weapons/axe/full.png'},
    'rapier':   {'cooldown': 50,    'damage': 8,    'graphic': '../graphics/weapons/rapier/full.png'},
    'sai':      {'cooldown': 80,    'damage': 10,   'graphic': '../graphics/weapons/sai/full.png'},
} 

# magic
magic_data = {
    'flame':    {'strength': 5,  'cost': 20, 'graphic': '../graphics/particles/flame/fire.png'},
    'heal':     {'strength': 20, 'cost': 10, 'graphic': '../graphics/particles/heal/heal.png'},
}

# enemy
monster_data = {
    'squid':    {'health':100,  'exp': 100, 'damage': 20,   'attack_type': 'slash',         'attack_sound': '../audio/attack/shash.wav'},
    'raccoon':  {'health':300,  'exp': 250, 'damage': 40,   'attack_type': 'claw',          'attack_sound': '../audio/attack/claw.wav'},
    'spirit':   {'health':100,  'exp': 110, 'damage': 8,    'attack_type': 'thunder',       'attack_sound': '../audio/attack/fireball.wav'},
    'bamboo':   {'health':70,   'exp': 120, 'damage': 6,    'attack_type': 'leaf_attack',   'attack_sound': '../audio/attack/shash.wav'},
}