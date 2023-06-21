from ursina import *
import random

app = Ursina()

# Load the player texture
player_texture = load_texture("image/cam.png")

player = Button(
    parent=scene,
    model='cube',
    texture=player_texture,
    color=color.white,
    position=(0, 3, -2000),
    scale=(5, 3, 10),
    collider='box'
)

camera.z = -15
camera.add_script(SmoothFollow(target=player, offset=(0, 5, -30)))
road_texture = load_texture("image/road.png")
road = Entity(model='plane', texture=road_texture, scale=(50, 10, 1e6))

bullet = Entity(model='sphere')
rows = [-15, -10, -5, 0, 5, 10, 15]

# Load textures for median_r and median_l
median_texture = load_texture("image/median.png")

median_r = Entity(model='cube', collider='box', position=(25, 2, 0), scale=(5, 10, 1e6), texture=median_texture)
median_l = Entity(model='cube', collider='box', position=(-25, 2, 0), scale=(5, 10, 1e6), texture=median_texture)

score_board = Text(text=str(0), scale=5, x=-0.85, y=0.45)
speed = 200
enemy_scale = 8
elapsed_time = 0

enemy_textures = [
    'image/skibidi_toilet.png',
    'image/skibidi_toilet1.png',
    'image/skibidi_toilet3.png',
    # Add more enemy textures here
]

def update():
    global elapsed_time

    player.z += time.dt * speed
    elapsed_time += time.dt
    score = int(elapsed_time)
    score_board.text = str(score)

    if held_keys['d']:
        player.x += time.dt * 25
    if held_keys['a']:
        player.x -= time.dt * 25
    if held_keys['w']:
        player.z += time.dt * 1000

    if player.intersects().hit or median_r.intersects().hit or median_l.intersects().hit:
        destroy(player)

def increase_enemy_scale():
    global enemy_scale

    enemy_scale += 1

    for enemy in scene.entities:
        if isinstance(enemy, Button):
            enemy.scale = (enemy_scale, enemy_scale, enemy_scale)

window.fullscreen = True

# Add the sky image
sky = Sky(texture='image/sky.png')

for i in range(0, 100000, 100):
    enemy_texture = random.choice(enemy_textures)
    enemy = Button(
        parent=scene,
        model='quad',
        texture=enemy_texture,
        collider='box',
        position=(random.choice(rows), 6, i),
        color=color.white,
        highlight_color=color.gray
    )
    enemy.scale = (enemy_scale, enemy_scale, enemy_scale)

def play_background_music():
    # Play the background song in a loop
    background_music = Audio('Music/skibidi-bop-yes-yes.mp3', loop=True)  # Replace with the actual path to your song file
    background_music.play()

# Delay the start of the music by 2 seconds
invoke(play_background_music, delay=2)

app.run()
