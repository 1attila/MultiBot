import discord
from discord import Color

Colors = ['teal',
'dark_teal',
'brand_green',
'green',
'dark_green',
'blue',
'dark_blue',
'purple',
'dark_purple',
'magenta',
'dark_magenta',
'gold',
'dark_gold',
'orange',
'dark_orange',
'brand_red',
'red',
'dark_red',
'lighter_grey',
'dark_grey',
'light_grey',
'darker_grey',
'og_burple',
'greyple',
'dark_theme',
'fuchsia',
'yellow'
]
Dcolors = [Color.teal(),
Color.dark_teal(),
Color.brand_green(),
Color.green(),
Color.dark_green(),
Color.blue(),
Color.dark_blue(),
Color.purple(),
Color.dark_purple(),
Color.magenta(),
Color.dark_magenta(),
Color.gold(),
Color.dark_gold(),
Color.orange(),
Color.dark_orange(),
Color.brand_red(),
Color.red(),
Color.dark_red(),
Color.lighter_gray(),
Color.dark_gray(),
Color.light_gray(),
Color.darker_grey(),
Color.og_blurple(),
Color.greyple(),
Color.dark_theme(),
Color.fuchsia(),
Color.yellow()
]

def Get(Color:str):

    for color in range(len(Colors)):
        if Colors[color] == Color:
            
            return Dcolors[color]