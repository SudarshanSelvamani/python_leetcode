import pygame
import random
from pygame import mixer
# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# set a background
background = pygame.image.load("back1.png").convert()

# bullet sound
bullet_sound = mixer.Sound("Laser2.wav")

# enemy explosion
enemy_sound = mixer.Sound("bomb.wav")

# background music
SONG_END = pygame.USEREVENT + 1
_songs = ["Steamtech-Mayhem.mp3", "Dystopic-Factory.mp3", "Blazing-Stars.mp3"]
_currently_playing_song = None


def play_a_different_song():
    global _currently_playing_song, _songs
    next_song = random.choice(_songs)
    while next_song == _currently_playing_song:
        next_song = random.choice(_songs)
    _currently_playing_song = next_song
    mixer.music.set_endevent(SONG_END)
    mixer.music.load(next_song)
    mixer.music.play()


    # mixer.music.play(-1)
play_a_different_song()

# create the title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("launch.png")
pygame.display.set_icon(icon)
player_img = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 480
playerX_change = 0

enemy_img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5

for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load("spaceship_enemy.png"))
    enemyX.append(random.randrange(1, 736))
    enemyY.append(random.randrange(2, 100))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

# ready state means you can't see the bullet
# fire if the bullet is currently moving
bullet_img = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 3
bullet_state = "ready"
no_of_bullets = 10


# score
score_value = 0
font = pygame.font.Font('Minecraft.ttf', 15)
font2 = pygame.font.Font('Minecraft.ttf', 40)

textX = 10
textY = 10


def show_score(x, y):
    score = font.render("Score : "+str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
    num_bullets = font.render("Ammo : "+str(no_of_bullets),True,(255,255,255))
    screen.blit(num_bullets,(700,10))


def game_over():
    over_text = font2.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (275, 250))


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x+25, y+1))


def iscollision(enemyX, enemyY, bulletX, bulletY):
    if (((bulletX-enemyX)**2)+((bulletY-enemyY)**2))**(1/2) <= 37:
        return True
    return False


running = True
i = 0


# game loop which keeps game running indefinitely so the window does not close down
while running:
    # screen.fill((26, 0, 51))

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == SONG_END:
            play_a_different_song()

        # if key stroke is pressed update it in pygame.event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5

            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5

            if event.key == pygame.K_SPACE and bullet_state == "ready" and no_of_bullets > 0:
                # Get the current x coordinate of the player
                no_of_bullets -= 1
                bullet_sound.play()
                bulletX = playerX
                fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:

                playerX_change = 0
    # checking for boundaries for spaceship so that it does not go over
    playerX += playerX_change
    if playerX < 1:
        playerX = 1
    if playerX > 735:
        playerX = 735

    # enemy movement

    for i in range(num_of_enemies):

        # Game over
        if enemyY[i] > 450 or no_of_bullets == 0:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] < 1:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        if enemyX[i] > 735:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            enemy_sound.play()
            no_of_bullets += 1
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randrange(1, 736)
            enemyY[i] = random.randrange(2, 100)

        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
     

    player(playerX, playerY)
    show_score(textX, textY)

    pygame.display.update()
