#Space Invaders
import turtle
import os
import math
import random

#Screen setup
screen = turtle.Screen()
screen.setup(460, 420)
screen.bgpic('SpaceinvadersBG.gif')

#Instructions Turtle
intro_pen = turtle.Turtle()
intro_pen.circle(15,)
intro_pen.hideturtle()
intro_pen.color('lime')
intro_pen.penup()
intro_pen.setposition(0, 20)
instructions = 'Instructions: Use the Left and Right arrow keys to move'
instructions2 = 'Space to shoot, Dont let the aliens touch you!'
intro_pen.write('Welcome to Space Escape',
                False,
                align='center',
                font=('Arial', 15, 'normal'))
intro_pen.setposition(0, 0)
intro_pen.write(instructions,
                False,
                align='center',
                font=('Arial', 8, 'normal'))
intro_pen.setposition(0, -20)
intro_pen.write(instructions2,
                False,
                align='center',
                font=('Arial', 8, 'normal'))
start = input('Press enter to start')

#Setup screen
intro_pen.clear()

#Border Turtle
border_pen = turtle.Turtle()
border_pen.hideturtle()
border_pen.speed(1)
border_pen.color("lime")
border_pen.penup()
border_pen.setposition(-190, -190)
border_pen.pendown()
border_pen.pensize(3)
#Drawing Border
for side in range(4):
  border_pen.fd(380)
  border_pen.lt(90)

#Score turtle
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('lime')
score_pen.penup()
score_pen.setposition(-165, 165)
scorestring = 'Score: ' + str(score)
score_pen.write(scorestring, False, align='Left', font=('Arial', 10, 'normal'))
score_pen.hideturtle()

#Player turtle
player = turtle.Turtle()
player.color('lime')
screen.register_shape('invader.gif')
player.shape('invader.gif')
player.penup()
player.setheading(180)
player.speed(10)
player.setposition(0, -150)

'''
Enemy Turtle
enemy = turtle.Turtle()
enemy.hideturtle()
'''
#Difficulty setting
difficulty = 'None'
while difficulty != 'hard' or difficulty != 'easy':
  difficulty = input(
    'What difficulty would you like?\nHard: 3 enemies, Fast speed, high rate of shooting\nEasy: 2 enemies, Slow speed, slow rate of shooting\n'
  ).lower()
  if difficulty == 'hard':
    enemyspeed = 3
    number_of_enemies = 3
    shootingRate = 20
    break
  elif difficulty == 'easy':
    enemyspeed = 2
    number_of_enemies = 2
    shootingRate = 30
    break
  else:
    print('Please enter Hard or Easy')

#Create list of enemies
enemies = []

#Add enemies to list
for i in range(number_of_enemies):
  #Create enemy
  enemies.append(turtle.Turtle())

for enemy in enemies:
  enemy.speed(0)
  screen.register_shape('player.gif')
  screen.register_shape('playerUp.gif')
  enemy.shape('player.gif')
  enemy.setheading(90)
  #Dont want enemy to draw
  enemy.penup()
  x = random.randint(-165, 165)
  y = 150
  enemy.setposition(x, y)

#Bullet Turtle
bullet = turtle.Turtle()
bullet.color('lime')
bullet.penup()
bullet.speed(0)
bullet.setheading(270)
bullet.setposition(0, -250)
bullet.hideturtle()
bulletspeed = 40

#Bullet States
#Ready - ready to fire
#Fire - bullet is firing
bulletstate = 'ready'
upOrDown = True
#Player Controls
playerspeed = 10


#Left and right functions
def move_left():
  x = player.xcor()
  #Subtract current position by player speed
  x -= playerspeed
  #Boundary Check
  if x < -165:
    x = -165
  player.setx(x)


def move_right():
  x = player.xcor()
  x += playerspeed
  if x > 165:
    x = 165
  player.setx(x)

def move_up():
  y = player.ycor()
  y += playerspeed
  if y > 165:
    y = 165
  player.sety(y)

def move_down():
  y = player.ycor()
  y -= playerspeed
  if y < -165:
    y = -165
  player.sety(y)

#Bullet firing function
def fire_bullet(enemy):
  global bulletstate
  global upOrDown
  if bulletstate == 'ready':
    if enemy.ycor()>0:
      #Set bullet right above player
      x = enemy.xcor()
      y = enemy.ycor() - 20
      bullet.setposition(x, y)
      bullet.seth(270)
      bulletstate = 'fire'
      bullet.showturtle()
      return True
    else:
      x = enemy.xcor()
      y = enemy.ycor() + 20
      bullet.setposition(x, y)
      bullet.seth(90)
      bulletstate = 'fire'
      bullet.showturtle()
      return False
  else:
    return upOrDown


#Collision detection
def isCollision(t1, t2):
  #Distance equation d = sqrt((x1-x2)^2 + (y1-y2)^2)
  distance = math.sqrt(
    math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
  if distance < 40:
    return True
  else:
    return False


#Key Bindings
screen.listen()
#When left is pressed call move_left function
screen.onkey(move_left, 'Left')
#When right is pressed call move_right function
screen.onkey(move_right, "Right")
#When right is pressed call move up function
screen.onkey(move_up, "Up")
#When right is pressed call move up function
screen.onkey(move_down, "Down")
#When space is pressed call fire_bullet function
# screen.onkey(fire_bullet, 'space')


Gameover = False
#Main Game Code
while Gameover == False:

  for enemy in enemies:
    #Move enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    #Boundary Check for enemy
    if enemy.xcor() > 165:
      #Move to the another border when enemy reaches edge
      enemy.setx(-165)
      # enemyspeed *= -1
    if enemy.xcor() < -165:
      enemy.setx(165)
      # enemyspeed *= -1
    # if enemy.ycor() < -160:
    #   x = random.randint(-165, 165)
    #   y = random.randint(50, 150)
    #   enemy.setposition(x, y)

      #Check Collision between player and enemy
    if isCollision(player, enemy):
      #Reset enemy
      y = enemy.ycor()
      x = random.randint(-165, 165)
      y *= -1
      enemy.setposition(x, y)
      if y<0:
        enemy.shape('playerUp.gif')
      else:
        enemy.shape('player.gif')
      #update score
      score += 10
      scorestring = 'Score: ' + str(score)
      score_pen.clear()
      score_pen.write(scorestring,
                      False,
                      align='Left',
                      font=('Arial', 8, 'normal'))

    #Check Collision between player and bullet
    if isCollision(player, bullet):
      #Hide both player,bullet and enemy and instigate game over
      player.hideturtle()
      #Reset bullet
      bullet.hideturtle()
      bulletstate = 'ready'
      bullet.setposition(0, -250)
      bullet.hideturtle()
      for enemy in enemies:
        enemy.hideturtle()
      #Instigate gameover
      border_pen.penup()
      border_pen.setposition(0, 0)
      border_pen.write('GAMEOVER',
                       move=False,
                       align='center',
                       font=('Arial', 25, 'normal'))
      print('Gameover')
      Gameover = True
    
    #Shoot player
    i = random.randint(0,shootingRate)
    if i==0:
      upOrDown = fire_bullet(enemy)


  #Move Bullet
  if upOrDown and bulletstate == 'fire':
    y = bullet.ycor()
    y -= bulletspeed
    bullet.sety(y)
  elif not(upOrDown) and bulletstate == 'fire':
    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)

  if bullet.ycor() < -170 or bullet.ycor() > 170:
    bulletstate = 'ready'
    bullet.hideturtle()

print('Score: ' + str(score))
delay = input("Press enter to exit game")
