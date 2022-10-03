import json

# json loads // json dumps

game_map = json.loads(open('map.json').read())

print(game_map.get("screen"))
screen = game_map.get("screen")
screen_txt = f""" 
from turtle import Screen
screen = Screen()
screen.setup(width={screen.get('width')}, height={screen.get('height')})
screen.title('{game_map.get('name')}')
screen.exitonclick()
"""
file = open("src/screen.py", "w")
file.write(screen_txt)
file.close()