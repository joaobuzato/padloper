import json

# json loads // json dumps

game_map = json.loads(open('map.json').read())

print(game_map.get("screen"))
screen = game_map.get("screen")
screen_txt = f"from turtle import Screen\n" \
             f"screen = Screen()\n" \
             f"screen.setup(width={screen.get('width')}, height={screen.get('height')})\n" \
             f"screen.title('{game_map.get('name')}')\n" \
             f"screen.exitonclick()"
file = open("screen.py", "w")
file.write(screen_txt)
file.close()