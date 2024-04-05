# Egyptian Escapades


# import necessary modules
import pygame
from pygame.locals import *
import random
import os

# initialize pygame
pygame.init()


# initialize sounds
coin_sound = pygame.mixer.Sound(os.path.join(
    "../EE-SOUND", "coin.wav"))
collision_sound = pygame.mixer.Sound(
    os.path.join("../EE-SOUND", "collision.wav"))
jump_slide_sound = pygame.mixer.Sound(
    os.path.join("../EE-SOUND", "jump-slide.wav"))
end_sound = pygame.mixer.Sound(os.path.join(
    "../EE-SOUND", "death.wav"))


# set size of game window
SIZE = WIDTH, HEIGHT = 800, 600


# initialize game window
screen = pygame.display.set_mode(SIZE)
# set window title
pygame.display.set_caption("Egyptian Escapades")


# load background image
background_image = pygame.image.load(os.path.join(
    "../EE-SPRITES", "background.png")).convert()
# set x position for 1st and 2nd background images
background_x_pos = 0
# while first background is displayed, 2nd background in hidden
background2_x_pos = int(background_image.get_width())

# create lists to hold the images of the main character
run_images = []
jump_images = []

# load jump images into the list
for image_no in range(1, 8):
    jump_images.append(pygame.image.load(os.path.join(
        "../EE-SPRITES", str(image_no) + ".png")))

# load run images into list
for image_no in range(8, 16):
    run_images.append(pygame.image.load(os.path.join(
        "../EE-SPRITES", str(image_no) + ".png")))

# load slide images into list
slide_images = [
    pygame.image.load(os.path.join(
        "../EE-SPRITES", "S1.png")),
    pygame.image.load(os.path.join(
        "../EE-SPRITES", "S2.png")),
    pygame.image.load(os.path.join(
        "../EE-SPRITES", "S2.png")),
    pygame.image.load(os.path.join(
        "../EE-SPRITES", "S2.png")),
    pygame.image.load(os.path.join(
        "../EE-SPRITES", "S2.png")),
    pygame.image.load(os.path.join(
        "../EE-SPRITES", "S2.png")),
    pygame.image.load(os.path.join(
        "../EE-SPRITES", "S2.png")),
    pygame.image.load(os.path.join(
        "../EE-SPRITES", "S2.png")),
    pygame.image.load(os.path.join(
        "../EE-SPRITES", "S3.png")),
    pygame.image.load(os.path.join(
        "../EE-SPRITES", "S4.png")),
    pygame.image.load(os.path.join(
        "../EE-SPRITES", "S5.png")),
]

# load fall image into list
fall_image = pygame.image.load(os.path.join(
    "../EE-SPRITES", "0.png"))

# define the path taken by the character while jumping - a parabola path
jumpPixelMovements = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4]


# load saw images
saw_images = [
    pygame.image.load(os.path.join(
        "../EE-SPRITES", "SAW0.png")),
    pygame.image.load(os.path.join(
        "../EE-SPRITES", "SAW1.png")),
    pygame.image.load(os.path.join(
        "../EE-SPRITES", "SAW2.png")),
    pygame.image.load(os.path.join(
        "../EE-SPRITES", "SAW3.png")),
]


# load spike image
spike_image = pygame.image.load(os.path.join(
    "../EE-SPRITES", "spike.png"))


# load sphinx image
sphinx_image = pygame.image.load(os.path.join(
    "../EE-SPRITES", "sphinx.png"))

# load cactus image
cactus_image = pygame.image.load(os.path.join(
    "../EE-SPRITES", "cactus.png"))


# create list to hold images
coin_images = []
# load coin images
for image_no in range(0, 7):
    coin_images.append(pygame.image.load(os.path.join(
        "../EE-SPRITES", "coin" + str(image_no) + ".PNG")))

# load arrow image
arrow_image = pygame.image.load(os.path.join(
    "../EE-SPRITES", "arrow.png"))


# create list to hold bird images
bird_images = []
# load images
for image_no in range(0, 9):
    bird_images.append(pygame.image.load(os.path.join(
        "../EE-SPRITES", "bird" + str(image_no) + ".png")))


# set some colour values
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


# initialize some fonts to display scores, etc
SCORE_FONT = pygame.font.Font(
    "/usr/share/fonts/abattis-cantarell-fonts/Cantarell-Regular.otf", 30)
END_SCREEN_FONT = pygame.font.Font(
    "/usr/share/fonts/abattis-cantarell-fonts/Cantarell-Regular.otf", 50)
START_TITLE = pygame.font.Font(
    "/usr/share/fonts/abattis-cantarell-fonts/Cantarell-Regular.otf", 80)
START_DIRECTIONS = pygame.font.Font(
    "/usr/share/fonts/abattis-cantarell-fonts/Cantarell-Regular.otf", 30)
FEATURE_FONT = pygame.font.Font(
    "/usr/share/fonts/abattis-cantarell-fonts/Cantarell-Regular.otf", 20)


# set hitboxes to true or false
enable_hitbox = True
# set sound to true or false
enable_sound = True


# initialize the clock which controls the speed of the game
clock = pygame.time.Clock()


# create a Player class which will become our main character
class Player():

    # initialize object with x and y coordinates, width and height of character
    def __init__(self, x_pos, y_pos, width, height):

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        # define if character is jumping or falling or ducking, etc
        self.is_jumping = False
        self.is_sliding = False
        self.is_sliding_up = False
        self.is_falling = False
        # define character's run slide and jump counts - allows us to time the characters movements
        self.run_count = 0
        self.slide_count = 0
        self.jump_count = 0
        # define health number of player
        self.health_count = 4

    # define function to draw the main character

    def draw_player(self, screen):

        # check if main character is falling
        if self.is_falling:
            # define the hitbox or redbox
            self.hitbox = (int(self.x_pos), int(self.y_pos + 35),
                           self.width - 8, self.height - 35)
            # draw or blit(Block Transfer) onto game window(screen)
            screen.blit(fall_image,
                        (int(self.x_pos), int(self.y_pos + 30)))

        # check if main character is jumping
        elif self.is_jumping:

            # subtract values from y position according to previous list
            self.y_pos -= jumpPixelMovements[self.jump_count] * 1.2

            # cycle through all jumping images and draw them on the game window
            screen.blit(
                jump_images[self.jump_count // 18], (int(self.x_pos), int(self.y_pos)))
            # increment jump count
            self.jump_count += 1

            # if jump count is greater than the length of list which defines parabola
            if self.jump_count > 124:

                # reset jump count to 0, set jumping value to False, and reset to run count to start running again
                self.jump_count = 0
                self.is_jumping = False
                self.run_count = 0

            # define hitbox or redbox for jumping
            self.hitbox = (int(self.x_pos + 4), int(self.y_pos),
                           self.width - 24, self.height - 10)

        # check if player is ducking or sliding
        elif self.is_sliding or self.is_sliding_up:

            # stage 1 : player is starting to duck
            if self.slide_count < 20:
                self.y_pos += 1
                self.hitbox = (int(self.x_pos + 4), int(self.y_pos),
                               self.width - 24, self.height - 10)

            # stage 2 : player is lying down
            elif self.slide_count > 20 and self.slide_count < 80:
                self.hitbox = (int(self.x_pos), int(self.y_pos + 3),
                               self.width - 8, self.height - 35)

            # stage 3 : player is coming back up
            elif self.slide_count == 80:
                self.y_pos -= 19
                self.is_sliding = False
                self.is_sliding_up = True

            # stage 4 : player is back to normal running position
            if self.slide_count >= 110:
                self.slide_count = 0
                self.is_sliding_up = False
                self.run_count = 0
                self.hitbox = (int(self.x_pos + 4), int(self.y_pos),
                               self.width - 24, self.height - 10)

            # draw or blit player images from our slide list of images
            screen.blit(
                slide_images[self.slide_count // 10], (int(self.x_pos), int(self.y_pos)))
            # increment sliding count by 1
            self.slide_count += 1

        # default movement of character is running. So if running:
        else:

            # check if run count exceeds the limit
            if self.run_count > 42:
                self.run_count = 0

            # draw character onto the screen
            screen.blit(run_images[self.run_count // 6],
                        (int(self.x_pos), int(self.y_pos)))

            # increment running count
            self.run_count += 1
            self.hitbox = (int(self.x_pos + 4), int(self.y_pos),
                           self.width - 24, self.height - 13)

        # if hitbox or redbox is enabled then draw it also
        if enable_hitbox:
            pygame.draw.rect(screen, RED, self.hitbox, 2)

        # draw healthbars
        pygame.draw.rect(
            screen, RED, (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(
            screen, GREEN, (self.hitbox[0], self.hitbox[1] - 20, 50 - (50 - (50 * self.health_count // 4)), 10))


# define class Blade
class Blade():

    def __init__(self, x_pos, y_pos, width, height):

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.hitbox = (x_pos, y_pos, width, height)
        # initialize saw count as 0
        self.saw_count = 0

    # draw function
    def draw(self, screen):

        # define hitbox of saw
        self.hitbox = (int(self.x_pos + 10), int(self.y_pos + 10),
                       self.width - 20, self.height - 10)

        # check if saw count is greater than limit, if yes : reset it to 0
        if self.saw_count >= 8:
            self.saw_count = 0

        # draw saw images on screen after shrinking or transforming it into suitable size
        screen.blit(pygame.transform.scale(saw_images[self.saw_count // 2], (64, 64)),
                    (int(self.x_pos), int(self.y_pos)))
        # increment saw count by 1
        self.saw_count += 1

        # if hitbox is enabled draw it
        if enable_hitbox:
            pygame.draw.rect(screen, RED, self.hitbox, 2)

    # check it player collides with saw

    def collide(self, otherRect):

        # if player's hitbox is within obstacle's hitbox, then return True
        if Rect(self.hitbox).colliderect(Rect(otherRect.hitbox)):
            return True
        else:
            return False


# define class Wedge while inheriting Blade class
class Wedge(Blade):

    # draw image and hitbox
    def draw(self, screen):

        self.hitbox = (int(self.x_pos + 5), int(self.y_pos), 25, 175)
        screen.blit(spike_image, (int(self.x_pos), int(self.y_pos)))

        if enable_hitbox:
            pygame.draw.rect(screen, RED, self.hitbox, 2)


# define class Statue - inherits Blade class
class Statue(Blade):

    # draw image and hitbox
    def draw(self, screen):

        self.hitbox = (int(self.x_pos + 5), int(self.y_pos + 5), 50, 66)
        screen.blit(pygame.transform.scale(sphinx_image,
                                           (60, 76)), (int(self.x_pos), int(self.y_pos)))

        if enable_hitbox:
            pygame.draw.rect(screen, RED, self.hitbox, 2)


# define class Cactus - inherits Blade class
class Cactus(Blade):

    # draw image and hitbox
    def draw(self, screen):

        self.hitbox = (int(self.x_pos + 5), int(self.y_pos + 5), 55, 80)
        screen.blit(pygame.transform.scale(cactus_image,
                                           (60, 90)), (int(self.x_pos), int(self.y_pos)))

        if enable_hitbox:
            pygame.draw.rect(screen, RED, self.hitbox, 2)


class Arrow(Blade):

    # draw image and hitbox
    def draw(self, screen):

        self.hitbox = (int(self.x_pos), int(self.y_pos), 100, 17)
        screen.blit(pygame.transform.scale(arrow_image,
                                           (100, 17)), (int(self.x_pos), int(self.y_pos)))

        if enable_hitbox:
            pygame.draw.rect(screen, RED, self.hitbox, 2)


# define Bird class
class Bird():

    # initialize coordinates, height, width and bird count
    def __init__(self, x_pos, y_pos, width, height):

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.hitbox = (x_pos, y_pos, width, height)
        self.bird_count = 0

    # draw images and hitbox

    def draw(self, screen):

        self.hitbox = (int(self.x_pos + 5), int(self.y_pos), 65, 75)
        if self.bird_count >= 45:
            self.bird_count = 0

        screen.blit(pygame.transform.scale(bird_images[self.bird_count // 5], (80, 80)),
                    (int(self.x_pos), int(self.y_pos)))

        # increment bird count by 1
        self.bird_count += 1

        if enable_hitbox:
            pygame.draw.rect(screen, RED, self.hitbox, 2)

    def collide(self, otherRect):

        if Rect(self.hitbox).colliderect(Rect(otherRect.hitbox)):
            return True
        else:
            return False


# define class Coin
class Coin():

    # initialize properties
    def __init__(self, x_pos, y_pos, width, height):

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.hitbox = (x_pos, y_pos, width, height)
        self.coin_count = 0

    # draw images and hitbox(optional)
    def draw(self, screen):

        self.hitbox = (int(self.x_pos), int(self.y_pos), 40, 40)
        if self.coin_count >= 35:
            self.coin_count = 0

        screen.blit(pygame.transform.scale(coin_images[self.coin_count // 5], (40, 40)),
                    (int(self.x_pos), int(self.y_pos)))

        self.coin_count += 1
        # if user wants hitbox for coins, uncomment next 2 lines
        """if enable_hitbox:
            pygame.draw.rect(screen, RED, self.hitbox, 2)"""

    def collide(self, otherRect):

        if Rect(self.hitbox).colliderect(Rect(otherRect.hitbox)):
            return True
        else:
            return False


# define function to return high scores from previous game plays
def getHighScore():

    # open file and read score
    high_score_file = open(
        "../EE-CODE/high_scores.txt", "r")
    previous_score = high_score_file.readlines()
    high_score = previous_score[0]

    # check if current score is greater than high score
    if int(current_score + coin_score) > int(high_score):

        # close and open file in write mode and write current score to it
        high_score_file.close()
        high_score_file = open(
            "../EE-CODE/high_scores.txt", "w")
        high_score_file.write(str(int(current_score + coin_score)))
        high_score_file.close()

        return str(int(current_score + coin_score))

    else:
        return high_score


# define function to draw end screen
def drawEndWindow():

    # set global variables so that they can changed inside function also
    global has_collided, delay_after_death, obstacles, current_score, coin_score, FPS, play_end_sound

    # after player dies and end screen is displayed, reset variables to original state so that the game can restart properly
    has_collided = False
    delay_after_death = 0
    obstacles = []
    player.is_falling = False

    # variable to check if end screen program is running
    end_screen_run = True

    # while end screen run is True
    while end_screen_run:

        # get events that are occuring
        for event in pygame.event.get():

            # if event is QUIT event, then exit loop
            if event.type == QUIT:
                end_screen_run = False
                pygame.quit()

            # if event is mouse click, restart game
            if event.type == KEYDOWN:

                if event.key == K_p:
                    end_screen_run = False

        # draw background image
        screen.blit(background_image, (0, 0))

        # define and load certain fonts for display
        high_score = END_SCREEN_FONT.render(
            "High Score : " + str(getHighScore()), True, BLACK)
        present_score = END_SCREEN_FONT.render(
            "Current Score : " + str(int(current_score + coin_score)), True, BLACK)
        play_game = START_DIRECTIONS.render(
            "Press 'p' to play again", True, BLACK)

        # display text
        screen.blit(
            high_score, (int(WIDTH // 2 - high_score.get_width() // 2), 150))
        screen.blit(present_score,
                    (int(WIDTH // 2 - present_score.get_width() // 2), 250))
        screen.blit(
            play_game, (int(WIDTH // 2 - play_game.get_width() // 2), 350))

        # update game window
        pygame.display.update()

    # reset game speed and scores and health
    FPS = 60
    current_score = 0
    coin_score = 0
    player.health_count = 4
    play_end_sound = True


# define function to draw the start window
def drawStartWindow():

    # define global variables
    global enable_hitbox, enable_sound

    # set while loop to true and run
    start_screen_run = True

    while start_screen_run:

        # get events
        for event in pygame.event.get():

            if event.type == QUIT:
                start_screen_run = False
                pygame.quit()

            if event.type == KEYDOWN:

                # if 'p' is pressed, then play game
                if event.key == K_p:
                    start_screen_run = False

                # if 'k' is pressed, toggle hitbox
                if event.key == K_h:
                    enable_hitbox = not(enable_hitbox)

                # if 's' is pressed, toggle sound
                if event.key == K_s:
                    enable_sound = not(enable_sound)

        # check status of hitbox and sound
        if enable_hitbox:
            hitbox_status = "On"
        else:
            hitbox_status = "Off"

        if enable_sound:
            sound_status = "On"
        else:
            sound_status = "Off"

        # draw background
        screen.blit(background_image, (0, 0))

        # render text
        title = START_TITLE.render("Egyptian Escapades", True, BLACK)
        play_game = START_DIRECTIONS.render("Press 'p' to play", True, BLACK)
        toggle_hitbox = START_DIRECTIONS.render(
            "Press 'h' to toggle hitbox", True, BLACK)
        hitbox_status_display = FEATURE_FONT.render(
            "Hitbox: " + hitbox_status, True, WHITE)
        play_sound = START_DIRECTIONS.render(
            "Press 's' to toggle sound", True, BLACK)
        toggle_pause = START_DIRECTIONS.render(
            "Press 'k' to pause", True, BLACK)
        sound_status_display = FEATURE_FONT.render(
            "Sound: " + sound_status, True, WHITE)

        # draw text
        screen.blit(title, (int(WIDTH // 2 - title.get_width() // 2), 30))
        screen.blit(
            play_game, (int(WIDTH // 2 - play_game.get_width() // 2), 400))
        screen.blit(toggle_hitbox,
                    (int(WIDTH // 2 - toggle_hitbox.get_width() // 2), 430))
        screen.blit(play_sound,
                    (int(WIDTH // 2 - play_sound.get_width() // 2), 460))
        screen.blit(toggle_pause,
                    (int(WIDTH // 2 - toggle_pause.get_width() // 2), 490))
        screen.blit(hitbox_status_display, (25, 10))
        screen.blit(sound_status_display, (160, 10))

        # update display
        pygame.display.update()


# define function to pause game
def drawPauseWindow():

    # set global variables
    global pause_status

    pause_is_running = True

    while pause_is_running:

        # render text
        paused_text = START_TITLE.render("PAUSED", True, BLACK)

        # draw text
        screen.blit(
            paused_text, (int(WIDTH // 2 - paused_text.get_width() // 2), 200))

        # get events
        for event in pygame.event.get():

            if event.type == KEYDOWN:

                # if 'k' is pressed, unpause
                if event.key == K_k:
                    pause_is_running = False
                    pause_status = False

            if event.type == QUIT:

                pause_is_running = False
                pause_status = False
                pygame.quit()
                exit()

        # update display
        pygame.display.update()


# define function to draw everything
def drawMainWindow():

    # draw 2 background images, one after another
    screen.blit(background_image, (int(background_x_pos), 0))
    screen.blit(background_image, (int(background2_x_pos), 0))

    # draw main character
    player.draw_player(screen)

    # draw all obstacles
    for obstacle in obstacles:
        obstacle.draw(screen)

    # check status of hitbox and sound
    if enable_hitbox:
        hitbox_status = "On"
    else:
        hitbox_status = "Off"

    if enable_sound:
        sound_status = "On"
    else:
        sound_status = "Off"

    # draw score, hitbox status, and sound status at top right of game window
    screen_font = SCORE_FONT.render(
        "Score: " + str(int(current_score + coin_score)), True, WHITE)
    hitbox_status_display = FEATURE_FONT.render(
        "Hitbox: " + hitbox_status, True, WHITE)
    sound_status_display = FEATURE_FONT.render(
        "Sound: " + sound_status, True, WHITE)

    screen.blit(screen_font, (620, 10))
    screen.blit(hitbox_status_display, (25, 10))
    screen.blit(sound_status_display, (160, 10))

    # update display
    pygame.display.update()


# create an event that will trigger every 2s to 3s to add obstacles
ADD_OBSTACLE = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_OBSTACLE, random.randrange(2000, 3000))

# create an event to increase speed of the game every 500ms
INCREASE_FPS = pygame.USEREVENT + 1
pygame.time.set_timer(INCREASE_FPS, 500)


# set speed of game
FPS = 60


# create variable to hold score due to coin collections
coin_score = 0
# create variable to hold score due to time played
current_score = 0


# create player object from Player class
player = Player(200, 390, 64, 64)


# set varible to check if program is running
program_is_running = True

# variable to control pause window
pause_status = False


# set variable to count delays after player dies
delay_after_death = 0
# set variable to check if player has collided
has_collided = False
# check speed of game when player has collided
player_fall_speed = 0


# create list to hold obstacles
obstacles = []

# variable to check if player has collided or not
previous_collide = False

# variable to check if we need to play end screen sound
play_end_sound = True


# call function to draw start window
drawStartWindow()

# main game loop
while program_is_running:

    # check pause status and if true, draw pause window
    if pause_status:
        drawPauseWindow()

    # reset FPS if it becomes unplayable
    if FPS >= 150:
        FPS = 60

    # set score based on game speed
    current_score = FPS // 5 - 12

    # if player's health is less than or equal to zero
    if player.health_count <= 0:

        # set player falling to True so that player dies
        player.is_falling = True
        # set has collided to True so that delay starts for 1s
        has_collided = True

        # set fall speed to actual game speed
        player_fall_speed = FPS

        # if sound in enabled
        if enable_sound:
            # if we want to play end sound
            if play_end_sound:
                # play sound
                pygame.mixer.Sound.play(end_sound)
                # set to False
                play_end_sound = False

    # check if player has collided with obstacle
    if has_collided:
        # increase delay time by 1
        delay_after_death += 1

        # wait for 1s until delay equals game speed
        if delay_after_death > player_fall_speed:
            # call function to show end screen
            drawEndWindow()

    # for obstacle in list
    for obstacle in obstacles:

        # if obstacle is NOT Coin
        if str(obstacle)[10: 14] != "Coin" and str(obstacle)[10: 15] != "Arrow":

            # if obstacle has collided with player
            if obstacle.collide(player):

                # check if we have collided before, if not
                if previous_collide is False:
                    # play sound
                    if enable_sound:
                        pygame.mixer.Sound.play(collision_sound)

                    # check if player's health is greater than zero
                    if player.health_count > 0:
                        # if yes, decrease health number by 1
                        player.health_count -= 1

                    # set variable to True, because we have collided now
                    previous_collide = True

                # remember with which obstacle we collided
                previous_obstacle = obstacle

            # check if we have collided before, if yes:
            if previous_collide is True:

                # check if we have passed the obstacle with which we had collided before, if yes:
                if player.hitbox[0] > previous_obstacle.hitbox[0] + previous_obstacle.hitbox[2]:
                    # reset variable
                    previous_collide = False

            # move obstacle at same speed as background image
            obstacle.x_pos -= 1.5

        # if obstacle is coin
        elif str(obstacle)[10: 14] == "Coin":

            # if coin has collided with player
            if obstacle.collide(player):
                # play sound
                if enable_sound:
                    pygame.mixer.Sound.play(coin_sound)

                # increase coin score by 10
                coin_score += 10
                # remove coin from obstacles list so that it is not drawn
                obstacles.pop(obstacles.index(obstacle))

            # move obstacle at same speed as background image
            obstacle.x_pos -= 1.5

        elif str(obstacle)[10: 15] == "Arrow":

            # if obstacle has collided with player
            if obstacle.collide(player):

                # check if we have collided before, if not
                if previous_collide is False:
                    # play sound
                    if enable_sound:
                        pygame.mixer.Sound.play(collision_sound)

                    # check if player's health is greater than zero
                    if player.health_count > 0:
                        # if yes, decrease health number by 1
                        player.health_count -= 1

                    # set variable to True, because we have collided now
                    previous_collide = True

                # remember with which obstacle we collided
                previous_obstacle = obstacle

            # check if we have collided before, if yes:
            if previous_collide is True:

                # check if we have passed the obstacle with which we had collided before, if yes:
                if player.hitbox[0] > previous_obstacle.hitbox[0] + previous_obstacle.hitbox[2]:
                    # reset variable
                    previous_collide = False

            # move obstacle at same speed as background image
            obstacle.x_pos -= 5

        # if obstacle goes out of screen, then don't draw it
        if obstacle.x_pos < background_image.get_width() * -1:
            obstacles.pop(obstacles.index(obstacle))

    # change background location peridiocally so that player appears to move
    background_x_pos -= 1.5
    background2_x_pos -= 1.5

    # if background images go offscreen, then set them back to original locations
    if background_x_pos < background_image.get_width() * -1:
        background_x_pos = background_image.get_width()

    if background2_x_pos < background_image.get_width() * -1:
        background2_x_pos = background_image.get_width()

    # check events
    for event in pygame.event.get():

        # if event is QUIT, then exit
        if event.type == QUIT:
            program_is_running = False

        # if event is to increase speed, then increment speed
        if event.type == INCREASE_FPS:
            FPS += 0.5

        if event.type == KEYDOWN:

            # toggle hitbox, sound, and pause
            if event.key == K_h:
                enable_hitbox = not(enable_hitbox)

            if event.key == K_s:
                enable_sound = not(enable_sound)

            if event.key == K_k:
                pause_status = not(pause_status)

        # if event is to add obstacles
        if event.type == ADD_OBSTACLE:

            # generate random numbers
            random_no = random.randrange(0, 26)

            # based on random numbers generated, append obstacles or coins to obstacle list
            if random_no == 0:
                obstacles.append(Blade(810, 385, 64, 64))
            elif random_no == 1:
                obstacles.append(Wedge(810, 220, 41, 190))
            elif random_no == 2:
                obstacles.append(Statue(810, 375, 60, 76))
            elif random_no == 3:
                obstacles.append(
                    Bird(810, random.choice([320, 100, 200]), 80, 80))
            elif random_no == 4:
                obstacles.append(Coin(810, 385, 40, 40))
                obstacles.append(Coin(860, 385, 40, 40))
            elif random_no == 5:
                obstacles.append(Coin(810, 385, 40, 40))
                obstacles.append(Coin(870, 385, 40, 40))
            elif random_no == 6:
                obstacles.append(Coin(810, 290, 40, 40))
                obstacles.append(Coin(890, 385, 40, 40))
            elif random_no == 7:
                obstacles.append(Coin(810, 290, 40, 40))
                obstacles.append(Coin(900, 290, 40, 40))
            elif random_no == 8:
                obstacles.append(Coin(810, 290, 40, 40))
                obstacles.append(Coin(890, 385, 40, 40))
            if random_no == 9:
                obstacles.append(Blade(810, 385, 64, 64))
            elif random_no == 10:
                obstacles.append(Wedge(810, 220, 41, 190))
            elif random_no == 11:
                obstacles.append(Statue(810, 375, 60, 76))
            if random_no == 12:
                obstacles.append(Blade(810, 385, 64, 64))
            elif random_no == 13:
                obstacles.append(Wedge(810, 220, 41, 190))
            elif random_no == 14:
                obstacles.append(Statue(810, 375, 60, 76))
            elif random_no == 15:
                obstacles.append(Arrow(810, 380, 100, 17))
            elif random_no == 16:
                obstacles.append(Arrow(810, 380, 100, 17))
            elif random_no == 17:
                obstacles.append(Arrow(810, 380, 100, 17))
            elif random_no == 18:
                obstacles.append(Arrow(810, 380, 100, 17))
            elif random_no == 19:
                obstacles.append(Arrow(810, 380, 100, 17))
            elif random_no == 20:
                obstacles.append(Arrow(810, 380, 100, 17))
            elif random_no == 21:
                obstacles.append(Cactus(810, 360, 60, 90))
            elif random_no == 22:
                obstacles.append(Cactus(810, 360, 60, 90))
            elif random_no == 23:
                obstacles.append(Cactus(810, 360, 60, 90))
            elif random_no == 24:
                obstacles.append(Cactus(810, 360, 60, 90))
            elif random_no == 25:
                obstacles.append(Cactus(810, 360, 60, 90))

    # if player is not dead
    if player.is_falling is False:
        # get all keys that are pressed while playing the game
        pressed_keys = pygame.key.get_pressed()

    # check if down arrow is pressed
    if pressed_keys[K_DOWN]:

        # check if we are already sliding, if not then set sliding to True
        if not(player.is_sliding):
            player.is_sliding = True

            if enable_sound:
                pygame.mixer.Sound.play(jump_slide_sound)

    # check if spacebar or up arrow is pressed, and set jumping to True
    if pressed_keys[K_SPACE] or pressed_keys[K_UP]:

        if not(player.is_jumping):
            player.is_jumping = True

            if enable_sound:
                pygame.mixer.Sound.play(jump_slide_sound)

    # call function to draw window each time and update display
    drawMainWindow()

    # set game speed with Clock
    clock.tick(FPS)

# after game is done, quit module
pygame.quit()
