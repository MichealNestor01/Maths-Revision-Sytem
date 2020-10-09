# This file contains classes that create the game part of this project
from programModules import *  # I use all of the imports and some of the functions from this file
import pygame as pygame
from PIL import Image
from random import shuffle

# this is a pygame sprite class for the player, the character that the user controls
class playerClass(pygame.sprite.Sprite):
    def __init__(self, selectedStyle, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.playerWidth = int(self.WIDTH / 10)
        self.playerHeight = int(self.HEIGHT * (7 / 30))
        self.playerSpeedX = 6
        self.playerSpeedY = 5
        pygame.sprite.Sprite.__init__(self)
        # The following data is parsed from the main menu, it points to the file location of the
        # sprite that the user selected, each sprite has 12 images which are used to animate the sprite
        walkforward = selectedStyle[0]
        walkbackwards = selectedStyle[1]
        walkleft = selectedStyle[2]
        walkright = selectedStyle[3]
        self.playerWalkingTowards1 = pygame.image.load(path.join(walkforward, "1.png"))
        self.playerWalkingTowards2 = pygame.image.load(path.join(walkforward, "2.png"))
        self.playerWalkingTowards3 = pygame.image.load(path.join(walkforward, "3.png"))
        self.playerWalkingAway1 = pygame.image.load(path.join(walkbackwards, "1.png"))
        self.playerWalkingAway2 = pygame.image.load(path.join(walkbackwards, "2.png"))
        self.playerWalkingAway3 = pygame.image.load(path.join(walkbackwards, "3.png"))
        self.playerWalkingLeft1 = pygame.image.load(path.join(walkleft, "1.png"))
        self.playerWalkingLeft2 = pygame.image.load(path.join(walkleft, "2.png"))
        self.playerWalkingLeft3 = pygame.image.load(path.join(walkleft, "3.png"))
        self.playerWalkingRight1 = pygame.image.load(path.join(walkright, "1.png"))
        self.playerWalkingRight2 = pygame.image.load(path.join(walkright, "2.png"))
        self.playerWalkingRight3 = pygame.image.load(path.join(walkright, "3.png"))
        # the inital image of the sprite is playerWalkingTowards1
        self.image = pygame.transform.scale(
            self.playerWalkingTowards1, (self.playerWidth, self.playerHeight)
        )
        # colour key gives the sprite a transparent background
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = int(self.WIDTH / 2)
        self.rect.bottom = int(self.HEIGHT / 2)
        self.speedx = 0
        self.movementTick = 0  # movement tick indicates when a movement starts, eg when a user clicks A, W, S or D
        # state indicates teh direction of the sprite, (left=3, right=4, forwards=1, backwards=2, static=0) when static the sprite retains the direction that it was last moving in
        self.state = 0
        # skip tick will stop the player moving when set to true, it is used for collisions
        self.skipTick = False

    # get y just returns the y position of the sprite
    def getY(self):
        return self.rect.bottom

    # update detects movement keypresses and adjusts the 'speed' of the sprite which will change the direction of movement
    def update(self, tick):
        # if speedx and speedy is 0 then the player will not move
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            # as the positive spead means move right negative will move left
            self.speedx = -self.playerSpeedX
            if (
                self.state != 3
            ):  # registers when a player starts to press a, sets the movement tick, and sets the state to moving left (3)
                self.movementTick = tick
                self.state = 3
        elif keystate[pygame.K_d]:
            self.speedx = self.playerSpeedX
            if (
                self.state != 4
            ):  # registers when a player starts to press d, sets the movement tick, and sets the state to moving right (4)
                self.movementTick = tick
                self.state = 4
        elif keystate[pygame.K_w]:
            self.speedy = -self.playerSpeedY
            if self.state != 2:
                # registers when a player starts to press w, sets the movement tick, and sets the state to moving away (2)
                self.movementTick = tick
                self.state = 2
        elif keystate[pygame.K_s]:
            self.speedy = self.playerSpeedY
            if self.state != 1:
                # registers when a player starts to press s, sets the movement tick, and sets the state to moving forwards (1)
                self.movementTick = tick
                self.state = 1
        else:  # if no key is being presed, this will make the sprite static while retaining the last direction of movement
            if self.state == 1:
                self.image = pygame.transform.scale(
                    self.playerWalkingTowards1, (self.playerWidth, self.playerHeight)
                )
                self.state = 0
            elif self.state == 2:
                self.image = pygame.transform.scale(
                    self.playerWalkingAway1, (self.playerWidth, self.playerHeight)
                )
                self.state = 0
            elif self.state == 3:
                self.image = pygame.transform.scale(
                    self.playerWalkingLeft1, (self.playerWidth, self.playerHeight)
                )
                self.state = 0
            elif self.state == 4:
                self.image = pygame.transform.scale(
                    self.playerWalkingRight1, (self.playerWidth, self.playerHeight)
                )
                self.state = 0
        # if skip tick is false then the player is moved
        if self.skipTick == False:
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            # These selection statements stop the player from walking off of the screen
            if self.rect.x < 0:
                self.rect.x = 0
            elif self.rect.x > self.WIDTH - self.playerWidth:
                self.rect.x = self.WIDTH - self.playerWidth
            if self.rect.x > 540:
                if self.rect.x < 640:
                    if self.rect.y < 30:
                        self.rect.y = 30
                    elif self.rect.y > self.HEIGHT - self.playerHeight:
                        self.rect.y = self.HEIGHT - self.playerHeight
                else:
                    if self.rect.y < 50:
                        self.rect.y = 50
                    elif self.rect.y > self.HEIGHT - self.playerHeight:
                        self.rect.y = self.HEIGHT - self.playerHeight
            else:
                if self.rect.y < 50:
                    self.rect.y = 50
                elif self.rect.y > self.HEIGHT - self.playerHeight:
                    self.rect.y = self.HEIGHT - self.playerHeight
        # using the difference between the movement tick and current tick these selection statements decide what picture should be showing for the sprite
        # this creates the movement animation:
        if self.state == 1:
            # tick is the tick the game is currently on and movement tick is the tick that the player started moving
            use = tick - self.movementTick
            # by making the animation dependant on the difference, the animation will start when the user starts moving, this makes
            # for a consistent player expreience, this changes the image displayed to  the user every fifth of a second roughly
            if use % 48 == 0:
                self.image = pygame.transform.scale(
                    self.playerWalkingTowards2, (self.playerWidth, self.playerHeight)
                )
            elif use % 24 == 0:
                self.image = pygame.transform.scale(
                    self.playerWalkingTowards3, (self.playerWidth, self.playerHeight)
                )
            elif use % 12 == 0:
                self.image = pygame.transform.scale(
                    self.playerWalkingTowards1, (self.playerWidth, self.playerHeight)
                )
        if self.state == 2:
            use = tick - self.movementTick
            if use % 48 == 0:
                self.image = pygame.transform.scale(
                    self.playerWalkingAway2, (self.playerWidth, self.playerHeight)
                )
            elif use % 24 == 0:
                self.image = pygame.transform.scale(
                    self.playerWalkingAway3, (self.playerWidth, self.playerHeight)
                )
            elif use % 12 == 0:
                self.image = pygame.transform.scale(
                    self.playerWalkingAway1, (self.playerWidth, self.playerHeight)
                )
        if self.state == 3:
            use = tick - self.movementTick
            if use % 48 == 0:
                self.image = pygame.transform.scale(
                    self.playerWalkingLeft2, (self.playerWidth, self.playerHeight)
                )
            elif use % 24 == 0:
                self.image = pygame.transform.scale(
                    self.playerWalkingLeft3, (self.playerWidth, self.playerHeight)
                )
            elif use % 12 == 0:
                self.image = pygame.transform.scale(
                    self.playerWalkingLeft1, (self.playerWidth, self.playerHeight)
                )
        if self.state == 4:
            use = tick - self.movementTick
            if use % 48 == 0:
                self.image = pygame.transform.scale(
                    self.playerWalkingRight2, (self.playerWidth, self.playerHeight)
                )
            elif use % 24 == 0:
                self.image = pygame.transform.scale(
                    self.playerWalkingRight3, (self.playerWidth, self.playerHeight)
                )
            elif use % 12 == 0:
                self.image = pygame.transform.scale(
                    self.playerWalkingRight1, (self.playerWidth, self.playerHeight)
                )


# Class for the teachers, the entities that the user interacts with while playing the game
class teacherClass(pygame.sprite.Sprite):
    def __init__(
        self, direction, width, height, dialogueFunction, dialogueArguments=0, level=1
    ):
        # this constructor is quite complex as this class is used to make 3 different entities
        # dialoge arguments and function are used to store the windows that pop up when a user interacts with a teacher
        self.dialogueArguments = dialogueArguments
        self.dialogueFunction = dialogueFunction
        self.WIDTH = width
        self.HEIGHT = height
        self.spriteWidth = int(self.WIDTH / 10)
        self.spriteHeight = int(self.HEIGHT * (7 / 30))
        pygame.sprite.Sprite.__init__(self)
        spritesFolder = "./gameResources/images/enemies"
        if direction == 1 or direction == 2:
            image = pygame.image.load(f"{spritesFolder}/enemy{str(direction)}.png")
        else:
            image = pygame.image.load(f"{spritesFolder}/level{str(level)}.png")
        self.image = pygame.transform.scale(
            image, (self.spriteWidth, self.spriteHeight)
        )
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        # the direction the teacher is facing dictates where on the screen it is placed
        if direction == 1:
            self.rect.centerx = int(self.WIDTH * (8 / 10))
            self.rect.bottom = int(self.HEIGHT * (2 / 3))
        elif direction == 2:
            self.rect.centerx = int(self.WIDTH * (2 / 10))
            self.rect.bottom = int(self.HEIGHT * (2 / 3))
        else:
            self.rect.centerx = int(self.WIDTH / 2)
            self.rect.y = 20
        self.imageOriginal = image
        # shadow is another sprite object that apears when the player is above the teaceher object's
        # y value, it creates the ilusion of depth with the player being able to walk infront of and behind the teachers
        self.shadow = ""

    # run dialoge runs teh speicific dialogue window attatched to the teacher in the constructor
    def runDialogue(self):
        if self.dialogueArguments == 0:
            return self.dialogueFunction()
        else:
            return self.dialogueFunction(self.dialogueArguments)

    # as it is a game sprite it is updated each tick but nothing needs to happen here
    def update(self, tick):
        pass

    # update shadow checks the height of the player and either hides the shadow or shows the shadow
    def updateShadow(self, y):
        if y > (self.HEIGHT * (2 / 3)) + 4:
            self.shadow.hide()
        else:
            self.shadow.show()


# Class for teacher shadow that allows for depth
class teacherShadow(pygame.sprite.Sprite):
    def __init__(self, image, x, y, spriteWidth, spriteHeight):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (spriteWidth, spriteHeight))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.y = y
        self.disable = False

    # to hide the shadow it was easiest to teleport the sprite off screen
    def hide(self):
        if self.disable == False:
            self.rect.bottom = 2000

    def show(self):
        if self.disable == False:
            self.rect.bottom = self.y

    def update(self, tick):
        pass


# class for the ok button that the user can click, it was changed to a talk button, in development but I have not changed the class name
class OkButton(pygame.sprite.Sprite):
    def __init__(self, place, width, height):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("./gameResources/images/buttons/talkButton.png")
        self.image = pygame.transform.scale(image, (378, 84))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = int(width / 2)
        self.rect.bottom = int(height + 200)
        self.height = height

    def update(self, tick):
        pass

    # again to hide and show objects it was easiest to teleoprt the srpite off and onto screen
    def show(self):
        self.rect.bottom = int(self.height - 20)

    def hide(self):
        self.rect.bottom = int(self.height + 200)


# the class for the leave button that the user can click
class LeaveButton(pygame.sprite.Sprite):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("./gameResources/images/buttons/leaveButton.png")
        self.image = pygame.transform.scale(image, (284, 63))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 150
        self.rect.bottom = 70

    # the leave button is static and present through the whole game so there isnt need for methods that update it
    def update(self, tick):
        pass

    def select(self):
        pass


# game isntance is the class that manages all the sprites and runs the game
class gameInstance:
    def __init__(self, style, mode, topic, playerName):
        # the constructor takes data from the main loop to create either the revision mode or the game mode
        self.playerName = playerName
        self.mode = mode
        self.style = style
        self.topic = topic
        self.action = 0
        self.currentUser = ""
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.FPS = 60
        self.levelBackground = "./gameResources/images/levels/level1.png"
        # when game instance is called the game is ran, so all I need to do in the main loop is type gameInstance() and give the correct
        # parameters the game will just run
        self.gamePrep()  # game prep creates all of the sprites and necessary variables for the game
        self.runTime()  # run time runs the game itself

    # game prep is necessary to define all of the sprites and create sprite groups that are necessary for run time
    def gamePrep(self):
        # pygame.init() initialises pygame and makes sure I can create the pygame objects
        pygame.init()
        # set camption gives prospective pygame windows the given title
        pygame.display.set_caption("Maths Revision System")
        # background is the background that was defined in the constructor, I plan to allow the user to choose this in the end product
        background = pygame.image.load(self.levelBackground)
        # I need to transform the background and get a rect so it can be displayed
        self.background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
        self.background_rect = self.background.get_rect()
        # screen is the window where the game will be displayed
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        # clock is the pygame clock that manages the frame rates, my self.tick is independant of this. I found that a simpler tick
        # system is what I prefered
        self.clock = pygame.time.Clock()
        # game sprites includes all of the sprites on screens
        self.game_sprites = pygame.sprite.Group()
        # teacher sprites is a group of all the teacher sprites
        teacher_sprites = pygame.sprite.Group()
        # self.player is the the player sprite
        self.player = playerClass(self.style, self.WIDTH, self.HEIGHT)
        # depending on the mode there is a different layout of teachers with different interactions with the player
        # the fourth argument the teacher object takes is a qtWindow that I am using as dialoge boxes
        if self.mode == "game":
            self.teacherOne = teacherClass(
                1, self.WIDTH, self.HEIGHT, self.topicTipsDialogue
            )
            self.teacherTwo = teacherClass(
                2, self.WIDTH, self.HEIGHT, self.warmupQuestionsWindow
            )
            self.teacherThree = teacherClass(
                3, self.WIDTH, self.HEIGHT, self.gameQuestionsWindow
            )
        else:
            self.teacherOne = teacherClass(
                1, self.WIDTH, self.HEIGHT, self.lessonsWindow, 1
            )
            self.teacherTwo = teacherClass(
                2, self.WIDTH, self.HEIGHT, self.lessonsWindow, 2
            )
            self.teacherThree = teacherClass(
                3, self.WIDTH, self.HEIGHT, self.topicTipsDialogue
            )
        # teachers is an array that stores all of the teacher sprites
        self.teachers = [self.teacherTwo, self.teacherOne, self.teacherThree]
        # this loop sets up all of the teacher's shadows
        for teacher in self.teachers:
            teacher.shadow = teacherShadow(
                teacher.imageOriginal,
                teacher.rect.centerx,
                teacher.rect.bottom,
                teacher.spriteWidth,
                teacher.spriteHeight,
            )
        # talk button pops up when the user is close enough to a teacher to interact with them
        self.talkButton = OkButton(3.5, self.WIDTH, self.HEIGHT)
        # leave button is just a static button at the top left of the screen that the user can click to end the game
        self.leaveButton = LeaveButton(self.WIDTH, self.HEIGHT)
        # sprites is all of the sprites created, it is used to add all of these to the game sprites group
        sprites = [
            self.teacherOne,
            self.teacherTwo,
            self.teacherThree,
            self.player,
            self.teacherOne.shadow,
            self.teacherTwo.shadow,
            self.teacherThree.shadow,
            self.talkButton,
            self.leaveButton,
        ]
        for item in sprites:
            self.game_sprites.add(item)
        # the third teacher does not need a shadow so it gets dissabled
        self.teacherThree.shadow.hide()
        self.teacherThree.shadow.disable = True
        font = pygame.font.Font(None, 250)
        # win text and loose text is for if you either win or loose the game
        self.winText = font.render("You Won!", True, pygame.Color("White"))
        self.looseText = font.render("You Lost!", True, pygame.Color("White"))
        self.winTextRect = (
            int((self.WIDTH / 2) - (self.winText.get_width() / 2)),
            int((self.HEIGHT / 2) - (self.winText.get_height() / 2)) - 100,
        )
        self.looseTextRect = (
            int((self.WIDTH / 2) - (self.looseText.get_width() / 2)),
            int((self.HEIGHT / 2) - (self.looseText.get_height() / 2)) - 100,
        )

    # run time is a subroutine that actually generates the game window and draws all of the sprites onto it.
    def runTime(self):
        running = True
        tick = 0
        showText = False
        animationSwitch = True
        while running:
            tick += 1
            self.clock.tick(self.FPS)
            self.player.skipTick = False
            # this loop checks to see if the player has colided with one of the teachers
            for teacher in self.teachers:
                collision = self.playerTeacherCollision(teacher)
                if collision == "collision":
                    selectedTeacher = teacher
                    break
            # this loop checks to see if any of the buttons on screen have been clicked
            # and then runs the relevant subroutines
            for event in pygame.event.get():
                if (
                    event.type == pygame.QUIT
                ):  # this occours if the user clicks the red x
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    # if talk has been pressed then the dialogue which is linked to the teacher that the player is closest to is ran
                    if self.talkButton.rect.collidepoint(pygame.mouse.get_pos()):
                        while True:
                            action = selectedTeacher.runDialogue()
                            # depending on the action that is returned from the function either:
                            if action == "break":
                                # nothing will happen
                                break
                            elif action[0] == "loose" or action[0] == "win":
                                # the win / loss screen will show
                                showText = action[0]
                                self.talkButton.hide()
                                break
                            else:
                                # or an image will be displayed to the user, an example of this would be the worked examples for the lesson
                                self.displayImage(action[0], action[1])
                    elif self.leaveButton.rect.collidepoint(pygame.mouse.get_pos()):
                        leave = self.leaveMethod()
                        if leave == "leave":
                            running = False
            # this loop updates the 'shadows' of the teachers, which allows the illusion of depth as the player is running around
            for item in self.teachers:
                item.updateShadow(self.player.getY())
            # if the game has not ended then when a user walks up to a teacher then a talk button will pop up
            if showText == False:
                # skip tick is true when a player walks up to a teacher and collides with the hitbox
                if self.player.skipTick == True:
                    self.talkButton.show()
                else:
                    self.talkButton.hide()
            # all of the game sprites are updated and drawn onto the screen
            self.game_sprites.update(tick)
            self.screen.blit(self.background, self.background_rect)
            self.game_sprites.draw(self.screen)
            # when the game is finished then these statistics pop up on screen
            if showText != False:
                if showText == "win":
                    self.screen.blit(self.winText, self.winTextRect)
                else:
                    self.screen.blit(self.looseText, self.looseTextRect)
                font = pygame.font.Font(None, 50)
                easyStats = font.render(
                    f"Easy Questions: {action[1]} correct", True, pygame.Color("White"),
                )
                mediumStats = font.render(
                    f"Medium Questions: {action[2]} correct",
                    True,
                    pygame.Color("White"),
                )
                hardStats = font.render(
                    f"Hard Questions: {action[3]} correct", True, pygame.Color("White"),
                )
                easyStatsRect = (
                    int((self.WIDTH / 2) - (easyStats.get_width() / 2)),
                    int((self.HEIGHT / 2) - (easyStats.get_height() / 2)),
                )
                mediumStatsRect = (
                    int((self.WIDTH / 2) - (mediumStats.get_width() / 2)),
                    int((self.HEIGHT / 2) - (mediumStats.get_height() / 2)) + 50,
                )
                hardStatsRect = (
                    int((self.WIDTH / 2) - (hardStats.get_width() / 2)),
                    int((self.HEIGHT / 2) - (hardStats.get_height() / 2)) + 100,
                )
                self.screen.blit(easyStats, easyStatsRect)
                self.screen.blit(mediumStats, mediumStatsRect)
                self.screen.blit(hardStats, hardStatsRect)
                leaveText = font.render(
                    "To return to the main menu press the leave button!",
                    True,
                    pygame.Color("White"),
                )
                leaveTextRect = (
                    int((self.WIDTH / 2) - (leaveText.get_width() / 2)),
                    int((self.HEIGHT / 2) - (leaveText.get_height() / 2)) + 150,
                )
                if tick % 30 == 0:
                    animationSwitch = not animationSwitch
                if animationSwitch == True:
                    self.screen.blit(leaveText, leaveTextRect)
            pygame.display.flip()
        # when the loop is broken close pygame
        pygame.quit()

    def playerTeacherCollision(self, teacher):
        tBottom = teacher.rect.bottom
        tLeft = teacher.rect.left
        tRight = teacher.rect.right
        pBottom = self.player.rect.bottom
        pLeft = self.player.rect.left
        pRight = self.player.rect.right
        # head on collisions the hit boxes dont line up so we have to do the +25/+30 maths on it to work
        if (pBottom > tBottom - 20) and (pBottom < tBottom + 20):
            if (
                (pRight > tLeft + 25)
                and (pRight < tLeft + 30)
                and ((self.player.state == 4) or (self.player.state == 0))
            ):
                self.player.skipTick = True
            elif (
                (pLeft > tRight - 30)
                and (pLeft < tRight - 25)
                and ((self.player.state == 3) or (self.player.state == 0))
            ):
                self.player.skipTick = True
        # top -> down collisions
        if (
            (pBottom > tBottom - 20)
            and (pBottom < tBottom)
            and (pRight > tLeft + 30)
            and (pLeft < tRight - 25)
            and ((self.player.state == 1) or (self.player.state == 0))
        ):
            self.player.skipTick = True
        # top -> up collisions
        if (
            (pBottom < tBottom + 20)
            and (pBottom > tBottom)
            and (pRight > tLeft + 30)
            and (pLeft < tRight - 25)
            and ((self.player.state == 2) or (self.player.state == 0))
        ):
            self.player.skipTick = True
        # skipTick is set to true if a collision has occoured, it will stop the player moving into the teacher.
        if self.player.skipTick == True:
            return "collision"
        else:
            return "noCollision"

    # this subroutine is linked to the leave button and allows a user to leave the game at any time
    def leaveMethod(self):
        app = QtWidgets.QApplication(sys.argv)
        # first there is a yes no box pop up to make sure that the user actually wants to close the game
        answer = yesNoBox(
            f"Leave {self.mode} mode",
            "Are you sure you want to leave, if you say ok you will be returned to the main menu.",
        )
        QtWidgets.qApp.quit()
        if answer == 1024:
            return "leave"

    # below are the functions that are used to call tbhe dialogue box windows that show up if you talk to a teacher:
    # all of the windows adapt to the given topic.

    # The possibilities:
    # Revision mode:
    #   Teacher1 = lessons part 1
    #   Teacher2 = lessons part 2
    #   Teacher3 = topic tips
    # Game mode:
    #   Teacher1 = practice question
    #   Teacher2 = topic tips
    #   Teacher3 = game questions
    def topicTipsDialogue(self):
        app = QtWidgets.QApplication(sys.argv)
        topicTipsWindow = QtWidgets.QMainWindow()
        ui = Ui_topicTipsWindow(self.topic)
        ui.setupUi(topicTipsWindow)
        topicTipsWindow.show()
        app.exec_()
        return "break"

    def lessonsWindow(self, part):
        # part refrences whether to show the first part of the lessons or the second
        app = QtWidgets.QApplication(sys.argv)
        lessonsWindow = QtWidgets.QMainWindow()
        ui = Ui_lessonsWindow(self.topic, part)
        ui.setupUi(lessonsWindow)
        lessonsWindow.show()
        app.exec_()
        return ui.action

    def warmupQuestionsWindow(self):
        app = QtWidgets.QApplication(sys.argv)
        warmupQuestionWindow = QtWidgets.QMainWindow()
        ui = Ui_warmupQuestionWindow(self.topic)
        ui.setupUi(warmupQuestionWindow)
        warmupQuestionWindow.show()
        app.exec_()
        return ui.action

    def gameQuestionsWindow(self):
        app = QtWidgets.QApplication(sys.argv)
        questionWindow = QtWidgets.QMainWindow()
        ui = Ui_questionWindow(self.topic, self.style[0], self.playerName)
        ui.setupUi(questionWindow)
        questionWindow.show()
        app.exec_()
        return ui.action

    # display image is a simple interface that jsut displays an image to the user
    def displayImage(self, image, title):
        app = QtWidgets.QApplication(sys.argv)
        imageDisplay = QtWidgets.QFrame()
        ui = Ui_imageDisplay()
        ui.setupUi(imageDisplay, image, title)
        imageDisplay.show()
        app.exec_()


# the topic tips window is very simple, it is a window that scales to the size
# of a given image that has a button that closes the window
class Ui_topicTipsWindow(object):
    def __init__(self, topic):
        self.topic = topic

    def setupUi(self, topicTipsWindow):
        imageSrc = f"./gameResources/Topics/{self.topic}/TopicTips/tips.png"
        image = Image.open(imageSrc)
        width, height = image.size
        topicTipsWindow.setObjectName("topicTipsWindow")
        topicTipsWindow.resize(width + 20, height + 130)
        topicTipsWindow.setMinimumSize(QtCore.QSize(width + 20, height + 130))
        topicTipsWindow.setMaximumSize(QtCore.QSize(width + 20, height + 130))
        topicTipsWindow.setStyleSheet(
            "QMainWindow {\n"
            "    background: royalBlue;\n"
            "}\n"
            "QPushButton {\n"
            "    color: black;\n"
            "    background: rgb(179, 102, 255);\n"
            "}"
        )
        self.centralwidget = QtWidgets.QWidget(topicTipsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, width + 20, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tipsPictureLabel = QtWidgets.QLabel(self.centralwidget)
        self.tipsPictureLabel.setGeometry(QtCore.QRect(10, 60, width, height))
        self.tipsPictureLabel.setPixmap(QtGui.QPixmap(imageSrc))
        self.tipsPictureLabel.setScaledContents(True)
        self.tipsPictureLabel.setObjectName("tipsPictureLabel")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(10, 70 + height, 281, 51))
        font.setPointSize(15)
        self.okButton.setFont(font)
        self.okButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.okButton.setObjectName("okButton")
        topicTipsWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(topicTipsWindow)
        QtCore.QMetaObject.connectSlotsByName(topicTipsWindow)
        self.okButton.clicked.connect(self.quitMethod)

    def retranslateUi(self, topicTipsWindow):
        _translate = QtCore.QCoreApplication.translate
        topicTipsWindow.setWindowTitle(
            _translate("topicTipsWindow", "Topic Tips Window")
        )
        self.titleLabel.setText(_translate("topicTipsWindow", f"Tips for {self.topic}"))
        self.okButton.setText(_translate("topicTipsWindow", "OK"))

    # topic tips only has one button, an ok button that closes the window
    def quitMethod(self):
        QtWidgets.qApp.quit()


# lessons window shows lessons for a given topic
class Ui_lessonsWindow(object):
    def __init__(self, topic, part):
        # this constructor selects the specific lessons that the window will show
        self.action = "break"
        self.topic = topic
        # the number of lessons in this topic is sourced from the database and stored in lessonsNumber
        topicData = databaseAccess(f"SELECT * FROM tblTopics")
        lessonsNumber = 0
        for record in topicData:
            if record[1] == topic:
                lessonsNumber = record[2]
                break
        self.part = part
        self.lessonsArray = []
        # since there area two teachers that show lessons, each one will show one half of them, this is
        # indicated by 'part'
        self.breakPoint = lessonsNumber // 2
        # this loop filters the lessons so that you only have the half of the lessons you want
        for i in range(lessonsNumber):
            if part == 1:
                if i + 1 <= self.breakPoint:
                    self.lessonsArray.append(i + 1)
            else:
                if i + 1 > self.breakPoint:
                    self.lessonsArray.append(i + 1)
        # each of the lessons is on a png file along with a worked example to go with the lesson
        self.lessonsImages = []
        self.workedExampleImages = []
        for i in self.lessonsArray:
            self.lessonsImages.append(
                f"./gameResources/Topics/{topic}/Lessons/lesson{i}.png"
            )
            self.workedExampleImages.append(
                f"./gameResources/Topics/{topic}/Lessons/lesson{i}WE.png"
            )

    def setupUi(self, lessonsWindow):
        self.images = []
        # here I am using PIL that I imported at the top to convert all of the images into a PIL object
        # with this I could easily get the width and the height of each image
        for image in self.lessonsImages:
            self.images.append(Image.open(image))
        self.imageLabelWidgets = []
        self.workedExampleButtons = []
        self.tabs = []
        width, height = self.images[0].size
        self.lessonsWindow = lessonsWindow
        self.lessonsWindow.resize(width + 30, height + 230)
        self.lessonsWindow.setMinimumSize(QtCore.QSize(width + 30, height + 230))
        self.lessonsWindow.setMaximumSize(QtCore.QSize(width + 30, height + 230))
        self.lessonsWindow.setStyleSheet(
            "QPushButton {\n"
            "    color: black;\n"
            "    background: rgb(179, 102, 255);\n"
            "}\n"
            "QMainWindow {\n"
            "    background: royalBlue;\n"
            "}\n"
            "QTabBar::tab {\n"
            "    background: rgb(201, 162, 255);\n"
            "    border: 2px solid black;\n"
            "    border-top-left-radius: 4px;\n"
            "    border-top-right-radius: 4px;\n"
            "    padding: 0px;\n"
            "    height: 20px;\n"
            "    width: 100px; \n"
            "    padding-bottom: 1px;\n"
            "    border-bottom: none;\n"
            "}\n"
            "\n"
            "QTabBar::tab:hover {\n"
            "    background: rgb(179, 102, 255);\n"
            "}\n"
            "\n"
            "QTabBar::tab:selected {\n"
            "    background: rgb(179, 102, 255);\n"
            "}\n"
            "QTabWidget::pane {\n"
            "    border: 2px solid black;\n"
            "}"
        )
        self.centralwidget = QtWidgets.QWidget(self.lessonsWindow)
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, width + 30, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(15, 60, width, height + 95))
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        # Each lesson tab is given the correct image and sized around the size of the lesson image
        for i in range(len(self.lessonsArray)):
            lessonTab = QtWidgets.QWidget()
            lessonTab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            lessonPicture = QtWidgets.QLabel(lessonTab)
            lessonPicture.setGeometry(QtCore.QRect(0, 0, width, height))
            lessonPicture.setPixmap(QtGui.QPixmap(self.lessonsImages[i]))
            workedExampleButton = QtWidgets.QPushButton(lessonTab)
            workedExampleButton.setGeometry(QtCore.QRect(10, height + 10, 291, 50))
            font.setPointSize(15)
            workedExampleButton.setFont(font)
            workedExampleButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.imageLabelWidgets.append(lessonPicture)
            self.workedExampleButtons.append(workedExampleButton)
            self.tabs.append(lessonTab)
            self.tabWidget.addTab(lessonTab, "")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(15, height + 165, width, 50))
        self.okButton.setFont(font)
        self.okButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lessonsWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(self.lessonsWindow)
        QtCore.QMetaObject.connectSlotsByName(self.lessonsWindow)
        # when the current tab is changed the the whole window will need to be resized around the image of the new lesson
        self.tabWidget.currentChanged.connect(self.updateSizing)
        self.okButton.clicked.connect(self.quitMethod)
        for button in self.workedExampleButtons:
            button.clicked.connect(self.workedExampleMethod)

    def retranslateUi(self, lessonsWindow):
        _translate = QtCore.QCoreApplication.translate
        self.lessonsWindow.setWindowTitle(_translate("lessonsWindow", "Lessons window"))
        self.titleLabel.setText(
            _translate("lessonsWindow", f"{self.topic} lessons part {self.part}")
        )
        for i in range(len(self.lessonsArray)):
            self.workedExampleButtons[i].setText(
                _translate("lessonsWindow", "See worked example")
            )
            self.tabWidget.setTabText(
                self.tabWidget.indexOf(self.tabs[i]),
                _translate("lessonsWindow", f"Lesson {self.lessonsArray[i]}"),
            )
        self.okButton.setText(_translate("lessonsWindow", "OK"))

    # worked example method closes the current window and causes the display image window to open, displaying the worked example
    def workedExampleMethod(self):
        index = self.tabWidget.currentIndex()
        image = self.workedExampleImages[index]
        self.action = [image, "worked example"]
        QtWidgets.qApp.quit()

    # update sizing is triggered every time that a user switches lesson tab, it resizes the window around the image that is currently
    # being show, this makes for a consistent experience between topics and lessons
    def updateSizing(self):
        image = self.images[self.tabWidget.currentIndex()]
        width, height = image.size
        self.lessonsWindow.resize(width + 30, height + 230)
        self.lessonsWindow.setMinimumSize(QtCore.QSize(width + 30, height + 230))
        self.lessonsWindow.setMaximumSize(QtCore.QSize(width + 30, height + 230))
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, width + 30, 61))
        self.tabWidget.setGeometry(QtCore.QRect(15, 60, width, height + 95))
        for label in self.imageLabelWidgets:
            # resizing labels keeps the text inside them cenetered
            label.setGeometry(QtCore.QRect(0, 0, width, height))
        for button in self.workedExampleButtons:
            button.setGeometry(QtCore.QRect(10, height + 10, 291, 50))
        self.okButton.setGeometry(QtCore.QRect(15, height + 165, width, 50))

    def quitMethod(self):
        QtWidgets.qApp.quit()


# questions window creates the interface where the user is tested on their knowlege of the selected topic
# the player battles against the teacher to answer 6 multiple choice questions, further more both player and teacher have
# 500 health that is visible on the top of the screen, of the 6 questions there are 2 easy, 2 medium and 2 hard
# Easy Question:
#   player answers wrong: they take 250 damage
#   player answers correct: the teacher takes 100 damage
# Medium Questions:
#   player answers wrong: they take 200 damage
#   players answer correct: the teacher takes 150 damage
# Hard Questions:
#   player answers wrong: they take 150 damage
#   player answers correct: the teacher takes 200 damage
class Ui_questionWindow(object):
    def __init__(self, topic, imageFolder, playerName):

        # player name and image are both used for the player's health bar
        self.playerUsername = playerName
        self.playerImage = f".{imageFolder[45:59]}.png"
        self.action = "break"
        self.index = 0
        self.topic = topic
        # theses correct variables stores how many of each question the user got correct
        self.easyCorrect = 0
        self.mediumCorrect = 0
        self.hardCorrect = 0
        # questions stores all of the questions that are going to be used
        self.questions = []
        # since we need 2 of each type of question its easiest to separate by difficulty
        easyQuestions = []
        mediumQuestions = []
        hardQuestions = []
        topicRecords = databaseAccess(f"SELECT * FROM tblTopics")
        for record in topicRecords:
            if record[1] == topic:
                topicId = record[0]
                break
        # the database is searched for all questions that are in the current topic
        questionRecords = databaseAccess("SELECT * FROM tblQuestions")
        for question in questionRecords:
            if question[0] == topicId and question[1] == 1:
                if question[4] == "1":
                    easyQuestions.append(
                        Question(question[2], "Easy", self.topic, question[3])
                    )
                elif question[4] == "2":
                    mediumQuestions.append(
                        Question(question[2], "Medium", self.topic, question[3])
                    )
                else:
                    hardQuestions.append(
                        Question(question[2], "Hard", self.topic, question[3])
                    )
        # the next lines shuffle the order of all of the questions in the easy medium and hard question arrays
        shuffle(easyQuestions)
        shuffle(mediumQuestions)
        shuffle(hardQuestions)
        # then two random easy, medium and hard questions are addded to the questions array
        self.questions.append(easyQuestions.pop(0))
        self.questions.append(easyQuestions.pop(0))
        self.questions.append(mediumQuestions.pop(0))
        self.questions.append(mediumQuestions.pop(0))
        self.questions.append(hardQuestions.pop(0))
        self.questions.append(hardQuestions.pop(0))

    def setupUi(self, questionWindow):
        # unlike the lessons window the questions window does not use a tab widget to sparate the questions, instead it uses a
        # single window with images that are swapped, since all the images are the same size there is no need for window resizing
        questionWindow.setObjectName("questionWindow")
        questionWindow.resize(800, 590)
        questionWindow.setMinimumSize(QtCore.QSize(800, 590))
        questionWindow.setMaximumSize(QtCore.QSize(800, 590))
        questionWindow.setStyleSheet(
            "QMainWindow {\n"
            "    background: royalBlue;\n"
            "}\n"
            "QPushButton {\n"
            "    color: black;\n"
            "    background: rgb(179, 102, 255);\n"
            "}\n"
            "\n"
            "QComboBox {\n"
            "    background: rgba(0, 0, 0, 0);\n"
            "    border-width: 2px;    \n"
            "    border-style: solid;\n"
            "    border-color: black;\n"
            "}\n"
            "QComboBox QAbstractItemView {\n"
            "    selection-background-color: rgba(0,212,255,1);\n"
            "    color: black;\n"
            "    background-color: rgb(220, 240, 255);\n"
            "}"
        )
        self.centralwidget = QtWidgets.QWidget(questionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.teacherPicture = QtWidgets.QLabel(self.centralwidget)
        self.teacherPicture.setGeometry(QtCore.QRect(10, 10, 120, 120))
        self.teacherPicture.setStyleSheet(
            "background: white;\n" "border-style: solid;\n" "border-width: 3px;\n" ""
        )
        self.teacherPicture.setPixmap(QtGui.QPixmap("./images/teacher.png"))
        self.teacherPicture.setScaledContents(True)
        self.teacherPicture.setObjectName("teacherPicture")
        self.playerPicture = QtWidgets.QLabel(self.centralwidget)
        self.playerPicture.setGeometry(QtCore.QRect(670, 10, 120, 120))
        self.playerPicture.setStyleSheet(
            "background: white;\n" "border-style: solid;\n" "border-width: 3px;\n" ""
        )
        self.playerPicture.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.SaintHelena)
        )
        self.playerPicture.setMidLineWidth(0)
        self.playerPicture.setPixmap(QtGui.QPixmap(self.playerImage))
        self.playerPicture.setScaledContents(True)
        self.playerPicture.setObjectName("playerPicture")
        self.teacherLine = QtWidgets.QFrame(self.centralwidget)
        self.teacherLine.setGeometry(QtCore.QRect(130, 20, 505, 40))
        self.teacherLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.teacherLine.setLineWidth(40)
        self.teacherLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.teacherLine.setObjectName("teacherLine")
        self.playerLine = QtWidgets.QFrame(self.centralwidget)
        self.playerLine.setGeometry(QtCore.QRect(165, 80, 505, 40))
        self.playerLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.playerLine.setLineWidth(40)
        self.playerLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.playerLine.setObjectName("playerLine")
        self.playerHealth = QtWidgets.QLabel(self.centralwidget)
        self.playerHealth.setGeometry(QtCore.QRect(170, 85, 500, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.playerHealth.setFont(font)
        self.playerHealth.setStyleSheet("background: lime;")
        self.playerHealth.setObjectName("playerHealth")
        self.teacherHealth = QtWidgets.QLabel(self.centralwidget)
        self.teacherHealth.setGeometry(QtCore.QRect(130, 25, 500, 30))
        self.teacherHealth.setStyleSheet("background: lime;")
        self.teacherHealth.setObjectName("teacherHealth")
        self.playerName = QtWidgets.QLabel(self.centralwidget)
        self.playerName.setGeometry(QtCore.QRect(170, 85, 500, 30))
        self.playerName.setFont(font)
        self.playerName.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.playerName.setObjectName("playerName")
        self.teacherName = QtWidgets.QLabel(self.centralwidget)
        self.teacherName.setGeometry(QtCore.QRect(130, 25, 500, 30))
        self.teacherName.setFont(font)
        self.teacherName.setObjectName("teacherName")
        self.playerRedBar = QtWidgets.QLabel(self.centralwidget)
        self.playerRedBar.setGeometry(QtCore.QRect(170, 85, 500, 30))
        self.playerRedBar.setFont(font)
        self.playerRedBar.setStyleSheet("background: red;")
        self.playerRedBar.setObjectName("playerRedBar")
        self.teacherRedLine = QtWidgets.QLabel(self.centralwidget)
        self.teacherRedLine.setGeometry(QtCore.QRect(130, 25, 500, 30))
        self.teacherRedLine.setStyleSheet("background: red;")
        self.teacherRedLine.setObjectName("teacherRedLine")
        self.difficultyLabel = QtWidgets.QLabel(self.centralwidget)
        self.difficultyLabel.setGeometry(QtCore.QRect(10, 140, 211, 31))
        font.setPointSize(14)
        self.difficultyLabel.setFont(font)
        self.difficultyLabel.setObjectName("difficultyLabel")
        self.previousQuestionButton = QtWidgets.QPushButton(self.centralwidget)
        self.previousQuestionButton.setGeometry(QtCore.QRect(10, 530, 131, 51))
        font.setPointSize(15)
        self.previousQuestionButton.setFont(font)
        self.previousQuestionButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.previousQuestionButton.setObjectName("previousQuestionButton")
        self.nextQuestionButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextQuestionButton.setGeometry(QtCore.QRect(660, 530, 131, 51))
        self.nextQuestionButton.setFont(font)
        self.nextQuestionButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextQuestionButton.setObjectName("nextQuestionButton")
        self.submitAnswerButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitAnswerButton.setGeometry(QtCore.QRect(160, 530, 481, 51))
        self.submitAnswerButton.setFont(font)
        self.submitAnswerButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submitAnswerButton.setObjectName("submitAnswerButton")
        self.questionPicture = QtWidgets.QLabel(self.centralwidget)
        self.questionPicture.setGeometry(QtCore.QRect(10, 170, 781, 191))
        self.questionPicture.setPixmap(QtGui.QPixmap(self.questions[0].question))
        self.questionPicture.setScaledContents(True)
        self.questionPicture.setObjectName("questionPicture")
        self.questionNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.questionNumberLabel.setGeometry(QtCore.QRect(610, 140, 181, 31))
        font.setPointSize(14)
        self.questionNumberLabel.setFont(font)
        self.questionNumberLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.questionNumberLabel.setObjectName("questionNumberLabel")
        self.answerPicture = QtWidgets.QLabel(self.centralwidget)
        self.answerPicture.setGeometry(QtCore.QRect(10, 370, 781, 111))
        self.answerPicture.setPixmap(QtGui.QPixmap(self.questions[0].answer))
        self.answerPicture.setScaledContents(True)
        self.answerPicture.setObjectName("answerPicture")
        self.chooseAnswerLabel = QtWidgets.QLabel(self.centralwidget)
        self.chooseAnswerLabel.setGeometry(QtCore.QRect(10, 490, 221, 31))
        self.chooseAnswerLabel.setFont(font)
        self.chooseAnswerLabel.setObjectName("chooseAnswerLabel")
        self.answerSelect = QtWidgets.QComboBox(self.centralwidget)
        self.answerSelect.setGeometry(QtCore.QRect(220, 490, 81, 31))
        self.answerSelect.setFont(font)
        self.answerSelect.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.answerSelect.setEditable(False)
        self.answerSelect.setObjectName("answerSelect")
        for i in range(5):
            self.answerSelect.addItem("")
        self.teacherPicture.raise_()
        self.playerPicture.raise_()
        self.teacherLine.raise_()
        self.playerLine.raise_()
        self.playerRedBar.raise_()
        self.playerHealth.raise_()
        self.playerName.raise_()
        self.teacherRedLine.raise_()
        self.teacherHealth.raise_()
        self.teacherName.raise_()
        self.difficultyLabel.raise_()
        self.previousQuestionButton.raise_()
        self.nextQuestionButton.raise_()
        self.submitAnswerButton.raise_()
        self.questionPicture.raise_()
        self.questionNumberLabel.raise_()
        self.answerPicture.raise_()
        self.chooseAnswerLabel.raise_()
        self.answerSelect.raise_()
        questionWindow.setCentralWidget(self.centralwidget)
        self.previousQuestionButton.clicked.connect(self.previousMethod)
        self.nextQuestionButton.clicked.connect(self.nextMethod)
        self.submitAnswerButton.clicked.connect(self.answerMethod)
        self.retranslateUi(questionWindow)
        QtCore.QMetaObject.connectSlotsByName(questionWindow)

    def retranslateUi(self, questionWindow):
        _translate = QtCore.QCoreApplication.translate
        questionWindow.setWindowTitle(_translate("questionWindow", "Question Window"))
        self.playerName.setText(_translate("questionWindow", f"{self.playerUsername}"))
        self.teacherName.setText(_translate("questionWindow", "Teacher"))
        self.difficultyLabel.setText(_translate("questionWindow", "Difficulty: Easy"))
        self.previousQuestionButton.setText(_translate("questionWindow", "< Previous"))
        self.nextQuestionButton.setText(_translate("questionWindow", "Next >"))
        self.submitAnswerButton.setText(_translate("questionWindow", "Submit Answer"))
        self.questionNumberLabel.setText(_translate("questionWindow", "Question 1/6"))
        self.chooseAnswerLabel.setText(
            _translate("questionWindow", "Choose an answer:")
        )
        self.answerSelect.setItemText(0, _translate("questionWindow", "A"))
        self.answerSelect.setItemText(1, _translate("questionWindow", "B"))
        self.answerSelect.setItemText(2, _translate("questionWindow", "C"))
        self.answerSelect.setItemText(3, _translate("questionWindow", "D"))
        self.answerSelect.setItemText(4, _translate("questionWindow", "E"))

    # previouse and next are similar methods they just both change the index and then update the interface with the update ui function
    def previousMethod(self):
        self.index = self.index - 1
        self.updateUi()

    def nextMethod(self):
        self.index = self.index + 1
        self.updateUi()

    def updateUi(self):
        # it first checks if the index has over or underflowed and adjusts accordingly
        if self.index == -1:
            self.index = 5
        elif self.index == 6:
            self.index = 0
        # the easy, medium and hard questions are always in the same place in the questions array so if the index is 0 or 1 then the difficulty
        # label is set to easy, 2 or 3 and the difficulty lable is set to medium and 4 or 5 and the difficulty label is set to hard
        if self.index == 0 or self.index == 1:
            self.difficultyLabel.setText("Difficulty: Easy")
        elif self.index == 2 or self.index == 3:
            self.difficultyLabel.setText("Difficulty: Medium")
        else:
            self.difficultyLabel.setText("Difficulty: Hard")
        # then the question number label is updated
        self.questionNumberLabel.setText(f"Question {self.index + 1}/6")
        # finaly the question and possile answer images are updated
        self.questionPicture.setPixmap(
            QtGui.QPixmap(self.questions[self.index].question)
        )
        self.answerPicture.setPixmap(QtGui.QPixmap(self.questions[self.index].answer))

    # answer method is called when the user tries to answer one of the questions
    def answerMethod(self):
        # 1, 2 and 3 refrence the damage given to teacher if a question is answered correctly
        # 4, 5 and 6 refrence the damage given to player if a question is answered incorrectly
        damageValues = {
            "Easy": 100,
            "Medium": 150,
            "Hard": 200,
            "playerEasy": 250,
            "playerMedium": 200,
            "playerHard": 150,
        }
        question = self.questions[self.index]
        answered = False
        # if the questions has been answered before then it can't be answered again
        if question.answered == True:
            answered = True
            messageBox(
                "Question already answered!",
                "Sorry you can not answer the same question twice",
                "error",
            )
        if answered == False:
            # the current question is set to have being answered so it cant be answered again
            self.questions[self.index].answered = True
            # the correct answer and the user's answers are compared
            correctAnswer = question.correctAnswer
            userAnswer = self.answerSelect.currentText()
            if userAnswer == correctAnswer:
                # if it is corect then the damage is done to the teacher and the correct count for the specific difficulty is updated
                damage = damageValues[question.difficulty]
                if question.difficulty == "Easy":
                    self.easyCorrect += 1
                elif question.difficulty == "Medium":
                    self.mediumCorrect += 1
                else:
                    self.hardCorrect += 1
                # the damage to the teacher is calculated and the teaher's health bar is resized
                teacherHealth = self.teacherHealth.frameGeometry().width() - damage
                messageBox(
                    "Correct answer!",
                    f"Well done {correctAnswer} was the correct answer and you did {damage} damage to the teacher!",
                )
                self.teacherHealth.resize(
                    ((teacherHealth)), self.teacherHealth.frameGeometry().height(),
                )
                # if the teacher's health is less than or equal to 0 then it the player has won, in this case action is updated and
                # the window is closed
                if teacherHealth <= 0:
                    self.action = [
                        "win",
                        self.easyCorrect,
                        self.mediumCorrect,
                        self.hardCorrect,
                    ]
                    QtWidgets.qApp.quit()
            else:
                # if the answer is wrong then damage is taken from the player health
                damage = damageValues[f"player{question.difficulty}"]
                playerHealth = self.playerHealth.frameGeometry().width() - damage
                messageBox(
                    "Wrong answer.",
                    f"Unfortunately {userAnswer} is not correct, {correctAnswer} was the correct answer and so you took {damage} damage!",
                )
                # the player health bar is then resized
                self.playerHealth.setGeometry(
                    QtCore.QRect(170 + (500 - playerHealth), 85, playerHealth, 30)
                )
                # if the player health is less than 0 then the player has lost and so action is updated and the window is closed
                if playerHealth <= 0:
                    self.action = [
                        "loose",
                        self.easyCorrect,
                        self.mediumCorrect,
                        self.hardCorrect,
                    ]
                    QtWidgets.qApp.quit()


# The warmup questions window is a simplified version of the game questions window, it has the same basic structure,
# 6 randomly selected. multiple choice questions, 2 medium, 2 easy and 2 hard however with these questions you can
# check hints to help you answer them, also there are no health bars as you are just practicing
class Ui_warmupQuestionWindow(object):
    def __init__(self, topic):
        # index refers to the current question being viewed
        self.index = 0
        # these count give the users stats at the end
        self.correctCount = 0
        self.answerCount = 0
        self.action = "break"
        self.topic = topic
        self.questions = []
        easyQuestions = []
        mediumQuestions = []
        hardQuestions = []
        # questions are taken from the database and the filtered by topic and difficulty into the three question arrays above
        topicRecords = databaseAccess(f"SELECT * FROM tblTopics")
        for record in topicRecords:
            if record[1] == topic:
                topicId = record[0]
                break
        questionRecords = databaseAccess("SELECT * FROM tblQuestions")
        for question in questionRecords:
            if question[0] == topicId and question[1] == 0:
                if question[4] == "1":
                    easyQuestions.append(
                        WarmupQuestion(question[2], "Easy", self.topic, question[3])
                    )
                elif question[4] == "2":
                    mediumQuestions.append(
                        WarmupQuestion(question[2], "Medium", self.topic, question[3])
                    )
                else:
                    hardQuestions.append(
                        WarmupQuestion(question[2], "Hard", self.topic, question[3])
                    )
        # The following lines randomly choose 6 questions, 2 easy 2 medium and 2 hard difficulty
        shuffle(easyQuestions)
        shuffle(mediumQuestions)
        shuffle(hardQuestions)
        self.questions.append(easyQuestions.pop(0))
        self.questions.append(easyQuestions.pop(0))
        self.questions.append(mediumQuestions.pop(0))
        self.questions.append(mediumQuestions.pop(0))
        self.questions.append(hardQuestions.pop(0))
        self.questions.append(hardQuestions.pop(0))

    def setupUi(self, warmupQuestionWindow):
        warmupQuestionWindow.setObjectName("warmupQuestionWindow")
        warmupQuestionWindow.resize(800, 468)
        warmupQuestionWindow.setMinimumSize(QtCore.QSize(800, 468))
        warmupQuestionWindow.setMaximumSize(QtCore.QSize(800, 468))
        warmupQuestionWindow.setStyleSheet(
            "QMainWindow {\n"
            "    background: royalBlue;\n"
            "}\n"
            "QPushButton {\n"
            "    color: black;\n"
            "    background: rgb(179, 102, 255);\n"
            "}QComboBox {\n"
            "    background: rgba(0, 0, 0, 0);\n"
            "    border-width: 2px;    \n"
            "    border-style: solid;\n"
            "    border-color: black;\n"
            "}\n"
            "QComboBox QAbstractItemView {\n"
            "    selection-background-color: rgba(0,212,255,1);\n"
            "    color: black;\n"
            "    background-color: rgb(220, 240, 255);\n"
            "}"
        )
        self.centralwidget = QtWidgets.QWidget(warmupQuestionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.difficultyLabel = QtWidgets.QLabel(self.centralwidget)
        self.difficultyLabel.setGeometry(QtCore.QRect(10, 10, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.difficultyLabel.setFont(font)
        self.difficultyLabel.setObjectName("difficultyLabel")
        self.previousQuestionButton = QtWidgets.QPushButton(self.centralwidget)
        self.previousQuestionButton.setGeometry(QtCore.QRect(10, 410, 131, 51))
        font.setPointSize(15)
        self.previousQuestionButton.setFont(font)
        self.previousQuestionButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        self.previousQuestionButton.setObjectName("previousQuestionButton")
        self.nextQuestionButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextQuestionButton.setGeometry(QtCore.QRect(660, 410, 131, 51))
        self.nextQuestionButton.setFont(font)
        self.nextQuestionButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextQuestionButton.setObjectName("nextQuestionButton")
        self.submitAnswerButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitAnswerButton.setGeometry(QtCore.QRect(160, 410, 481, 51))
        self.submitAnswerButton.setFont(font)
        self.submitAnswerButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submitAnswerButton.setObjectName("submitAnswerButton")
        self.getHintButton = QtWidgets.QPushButton(self.centralwidget)
        self.getHintButton.setGeometry(QtCore.QRect(320, 370, 131, 31))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.getHintButton.setFont(font)
        self.getHintButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.getHintButton.setObjectName("getHintButton")
        self.questionNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.questionNumberLabel.setGeometry(QtCore.QRect(590, 10, 201, 31))
        font.setBold(True)
        font.setWeight(75)
        self.questionNumberLabel.setFont(font)
        self.questionNumberLabel.setObjectName("questionNumberLabel")
        self.chooseAnswerLabel = QtWidgets.QLabel(self.centralwidget)
        self.chooseAnswerLabel.setGeometry(QtCore.QRect(10, 370, 221, 31))
        self.chooseAnswerLabel.setFont(font)
        self.chooseAnswerLabel.setObjectName("chooseAnswerLabel")
        self.answerSelect = QtWidgets.QComboBox(self.centralwidget)
        self.answerSelect.setGeometry(QtCore.QRect(230, 370, 81, 31))
        font.setPointSize(14)
        self.answerSelect.setFont(font)
        self.answerSelect.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.answerSelect.setEditable(False)
        self.answerSelect.setObjectName("answerSelect")
        for i in range(5):
            self.answerSelect.addItem("")
        self.questionPicture = QtWidgets.QLabel(self.centralwidget)
        self.questionPicture.setGeometry(QtCore.QRect(10, 40, 781, 191))
        self.questionPicture.setPixmap(QtGui.QPixmap(self.questions[0].question))
        self.questionPicture.setScaledContents(True)
        self.questionPicture.setObjectName("questionPicture")
        self.answerPicture = QtWidgets.QLabel(self.centralwidget)
        self.answerPicture.setGeometry(QtCore.QRect(10, 250, 781, 111))
        self.answerPicture.setPixmap(QtGui.QPixmap(self.questions[0].answer))
        self.answerPicture.setScaledContents(True)
        warmupQuestionWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(warmupQuestionWindow)
        QtCore.QMetaObject.connectSlotsByName(warmupQuestionWindow)
        self.getHintButton.clicked.connect(self.hintMethod)
        self.previousQuestionButton.clicked.connect(self.previousMethod)
        self.nextQuestionButton.clicked.connect(self.nextMethod)
        self.submitAnswerButton.clicked.connect(self.answerMethod)

    def retranslateUi(self, warmupQuestionWindow):
        _translate = QtCore.QCoreApplication.translate
        warmupQuestionWindow.setWindowTitle(
            _translate("warmupQuestionWindow", "Warmup Questions")
        )
        self.difficultyLabel.setText(
            _translate("warmupQuestionWindow", "Difficulty: Easy")
        )
        self.previousQuestionButton.setText(
            _translate("warmupQuestionWindow", "< Previous")
        )
        self.nextQuestionButton.setText(_translate("warmupQuestionWindow", "Next >"))
        self.submitAnswerButton.setText(
            _translate("warmupQuestionWindow", "Submit Answer")
        )
        self.getHintButton.setText(_translate("warmupQuestionWindow", "Get Hint"))
        self.questionNumberLabel.setText(
            _translate("warmupQuestionWindow", f"Question {self.index + 1}/6")
        )
        self.chooseAnswerLabel.setText(
            _translate("warmupQuestionWindow", "Choose an answer:")
        )
        self.answerSelect.setItemText(0, _translate("warmupQuestionWindow", "A"))
        self.answerSelect.setItemText(1, _translate("warmupQuestionWindow", "B"))
        self.answerSelect.setItemText(2, _translate("warmupQuestionWindow", "C"))
        self.answerSelect.setItemText(3, _translate("warmupQuestionWindow", "D"))
        self.answerSelect.setItemText(4, _translate("warmupQuestionWindow", "E"))

    # hint method updates action and closes the winodw, this will trigger a display image window with the image of the hint
    def hintMethod(self):
        self.action = [
            self.questions[self.index].hint,
            f"Hint for question {self.index + 1}",
        ]
        QtWidgets.qApp.quit()

    # previous and next update the index and then call the update ui method
    def previousMethod(self):
        self.index = self.index - 1
        self.updateUi()

    def nextMethod(self):
        self.index = self.index + 1
        self.updateUi()

    # update ui changes the question and answer images as well as a couple of labels
    def updateUi(self):
        # first index is checked for over or underflow
        if self.index == -1:
            self.index = 5
        elif self.index == 6:
            self.index = 0
        # then depending on the current difficulty the difficulty label is updated
        if self.index == 0 or self.index == 1:
            self.difficultyLabel.setText("Difficulty: Easy")
        elif self.index == 2 or self.index == 3:
            self.difficultyLabel.setText("Difficulty: Medium")
        else:
            self.difficultyLabel.setText("Difficulty: Hard")
        # update the question number label using the undex
        self.questionNumberLabel.setText(f"Question {self.index + 1}/6")
        # update the question picture
        self.questionPicture.setPixmap(
            QtGui.QPixmap(self.questions[self.index].question)
        )
        # update the answer picture
        self.answerPicture.setPixmap(QtGui.QPixmap(self.questions[self.index].answer))

    # answer method is triggered when the user clicks the submit button
    def answerMethod(self):
        # question is the object for the question the user just tried to run
        question = self.questions[self.index]
        answered = False
        # first it is checked that the user has not already answered this question
        if question.answered == True:
            answered = True
            messageBox(
                "Question already answered!",
                "Sorry you can not answer the same question twice",
                "error",
            )
        # if this question has not been answered:
        if answered == False:
            # set the question's answered attribute to true
            self.questions[self.index].answered = True
            # check if the user has answered the question correct
            correctAnswer = question.correctAnswer
            userAnswer = self.answerSelect.currentText()
            if userAnswer == correctAnswer:
                messageBox(
                    "Correct answer!",
                    f"Well done {correctAnswer} was the correct answer",
                )
                self.correctCount += 1
            else:
                messageBox(
                    "Wrong answer.",
                    f"Unfortunately {userAnswer} is not correct, {correctAnswer} was the correct answer.",
                )
            # increment the answer count and chekck if all of the questions have beeen answered
            self.answerCount += 1
            if self.answerCount == 6:
                messageBox(
                    "Warmup completed",
                    f"You have given an answer to all of the warmup questions and you got {self.correctCount} correct",
                )
                QtWidgets.qApp.quit()


# display image is a simple interface that displays a given image and a window title, it has no methods, it is just a frame.
class Ui_imageDisplay(object):
    def setupUi(self, imageDisplay, imageToDisplay, title):
        self.title = title
        image = Image.open(imageToDisplay)
        width, height = image.size
        # each time it is created the window is sized around the image
        imageDisplay.resize(width, height)
        imageDisplay.setMinimumSize(QtCore.QSize(width, height))
        imageDisplay.setMaximumSize(QtCore.QSize(width, height))
        self.imageLabel = QtWidgets.QLabel(imageDisplay)
        self.imageLabel.setGeometry(QtCore.QRect(0, 0, width, height))
        self.imageLabel.setPixmap(QtGui.QPixmap(imageToDisplay))
        self.imageLabel.setScaledContents(False)
        self.imageLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.imageLabel.setObjectName("imageLabel")
        self.retranslateUi(imageDisplay)
        QtCore.QMetaObject.connectSlotsByName(imageDisplay)

    def retranslateUi(self, imageDisplay):
        _translate = QtCore.QCoreApplication.translate
        imageDisplay.setWindowTitle(_translate("imageDisplay", f"{self.title}"))


# the question class and warmup question class are used by the game and warmup questions windows
# every question that is asked of the player has its own object which stores the correct answer, an image which
# has possible answers, a bool which stores whether the question has been answered and the difficulty of the question
class Question:
    def __init__(self, index, difficulty, topic, correctAnswer):
        self.answered = False
        self.correctAnswer = correctAnswer
        self.question = (
            f"./gameResources/Topics/{topic}/GameQuestions/question{index}.png"
        )
        self.answer = f"./gameResources/Topics/{topic}/GameQuestions/answers{index}.png"
        self.difficulty = difficulty


# the warmup question class is similar a child of the question class as it is shares the same attributes however it also has an attatched hint
class WarmupQuestion(Question):
    def __init__(self, index, difficulty, topic, correctAnswer):
        super().__init__(index, difficulty, topic, correctAnswer)
        self.hint = f"./gameResources/Topics/{topic}/warmupQuestions/hint{index}.png"

