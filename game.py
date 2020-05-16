{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pygame 1.9.6\n",
      "Hello from the pygame community. https://www.pygame.org/contribute.html\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\DELL-\\Anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py:3304: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "import pygame\n",
    "import sys\n",
    "\n",
    "pygame.init()\n",
    "size = width,height = 320,240\n",
    "screen = pygame.display.set_mode(size)\n",
    "color = (0, 0, 0)\n",
    "ball = pygame.image.load('ball2.png')\n",
    "ballrect = ball.get_rect()\n",
    "\n",
    "speed = [5, 5]\n",
    "while True:\n",
    "    for event in pygame.event.get():\n",
    "        if event.type == pygame.QUIT:\n",
    "            sys.exit()\n",
    "    ballrect = ballrect.move(speed)\n",
    "    if ballrect.left < 0 or ballrect.right > width:\n",
    "        speed[0] = -speed[0]/2\n",
    "    if ballrect.top < 0 or ballrect.bottom > height:\n",
    "        speed[1] = -speed[1]/2\n",
    "        \n",
    "    screen.fill(color)\n",
    "    screen.blit(ball,ballrect)\n",
    "    pygame.display.flip()\n",
    "            \n",
    "pygame.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-1-c7cfc84bc2ed>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-1-c7cfc84bc2ed>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    pip3 install pygame\u001b[0m\n\u001b[1;37m               ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "pip3 install pygame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-4-0a0fc7a77e37>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-4-0a0fc7a77e37>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    pip3 install numpy\u001b[0m\n\u001b[1;37m               ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "pip3 install numpy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'function' object is not subscriptable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-7-57c5af30b2f5>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msort\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: 'function' object is not subscriptable"
     ]
    }
   ],
   "source": [
    "np.sort[0,1,2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'pygame'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-8-671b35b41eba>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mpygame\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'pygame'"
     ]
    }
   ],
   "source": [
    "import pygame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pygame\n",
    "import sys\n",
    "import random\n",
    "import os\n",
    "import time\n",
    "\n",
    "class Bird(object):\n",
    "    def __init__(self):\n",
    "        self.birdRect = pygame.Rect(65,50,50,50)\n",
    "        self.birdStatus = [pygame.image.load('1.png'),\n",
    "                           pygame.image.load('2.png'),\n",
    "                           pygame.image.load('ball2.png')]\n",
    "        self.status = 0\n",
    "        self.birdX = 120\n",
    "        self.birdY = 250\n",
    "        self.jump = False\n",
    "        self.jumpSpeed = 10\n",
    "        self.gravity = 5\n",
    "        self.dead = False\n",
    "    \n",
    "    def birdUpdate(self):\n",
    "        if self.jump:\n",
    "            self.jumpSpeed -= 1\n",
    "            self.birdY -= self.jumpSpeed\n",
    "        else:\n",
    "            self.gravity += 0.2\n",
    "            self.birdY += self.gravity\n",
    "        self.birdRect[1] = self.birdY\n",
    "        self.birdRect[2] = 50 + Pipeline.score/2000\n",
    "        self.birdRect[3] = 50 + Pipeline.score/2000\n",
    "class Pipeline(object):\n",
    "    def __init__(self):\n",
    "        self.wallx = 400\n",
    "        self.score = 0\n",
    "        self.x = 0\n",
    "        self.y = 0\n",
    "        self.z = 0\n",
    "        self.speed = 0\n",
    "        self.w = 0\n",
    "        self.h = 0\n",
    "        self.s = 0\n",
    "        self.pineUp = pygame.image.load('3.PNG')\n",
    "        self.pineDown = pygame.image.load('3.PNG')\n",
    "        self.award = pygame.image.load('2.PNG')\n",
    "    def updatePipeline(self):\n",
    "        self.speed = self.score/50\n",
    "        self.wallx -= 5 + self.speed\n",
    "        self.w = self.award.get_width()\n",
    "        self.h = self.award.get_height()        \n",
    "        awardRect = pygame.Rect(Pipeline.wallx+self.s,200+Pipeline.z,\n",
    "                         self.w ,\n",
    "                         self.h)\n",
    "\n",
    "        if awardRect.colliderect(Bird.birdRect) :\n",
    "\n",
    "            self.score +=10\n",
    "            self.s = -30\n",
    "            \n",
    "            if self.wallx < 50 or self.wallx > 170:\n",
    "                self.s = 0\n",
    "                   \n",
    "            \n",
    "        if self.wallx < -80:\n",
    "            self.score += 1\n",
    "            self.x = random.randint(1,50)\n",
    "            self.y = random.randint(1,50)\n",
    "            self.z = random.randint(-50,50)\n",
    "            self.wallx = 400\n",
    "    \n",
    "def createMap():\n",
    "    screen.fill((255,255,255))\n",
    "    screen.blit(background,(0,0))\n",
    "    \n",
    "    screen.blit(Pipeline.pineUp,(Pipeline.wallx, 0+Pipeline.x))\n",
    "    screen.blit(Pipeline.pineDown,(Pipeline.wallx, 400-Pipeline.y))\n",
    "    screen.blit(Pipeline.award,(Pipeline.wallx, 200+Pipeline.z))\n",
    "    Pipeline.updatePipeline()\n",
    "\n",
    "    \n",
    "    if Bird.dead:\n",
    "        Bird.status = 2\n",
    "    elif Bird.jump:\n",
    "        Bird.status = 1\n",
    "    screen.blit(Bird.birdStatus[Bird.status],\n",
    "                (Bird.birdX,Bird.birdY))\n",
    "    Bird.birdUpdate()\n",
    "    \n",
    "    screen.blit(font.render('Score:' + str(Pipeline.score), \n",
    "                            -1, \n",
    "                            (255,255,255)),(100,50))   \n",
    "    pygame.display.update()\n",
    "    \n",
    "def checkDead():\n",
    "    upRect = pygame.Rect(Pipeline.wallx,0+Pipeline.x,\n",
    "                         Pipeline.pineUp.get_width() - 10,\n",
    "                         Pipeline.pineUp.get_height())\n",
    "    downRect = pygame.Rect(Pipeline.wallx,400-Pipeline.y,\n",
    "                         Pipeline.pineDown.get_width() - 10,\n",
    "                         Pipeline.pineDown.get_height())\n",
    "    \n",
    "    if upRect.colliderect(Bird.birdRect) or downRect.colliderect(Bird.birdRect):\n",
    "        Bird.dead = True\n",
    "    if not 0 < Bird.birdRect[1] < height:\n",
    "        Bird.dead = True\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "def getResult():\n",
    "    final_text1 = 'Game Over'\n",
    "    final_text2 = 'Your final score is:' + str(Pipeline.score)\n",
    "    ft1_font = pygame.font.SysFont('Arial',50)\n",
    "    ft1_surf = font.render(final_text1,1,(242,2,36))\n",
    "    ft2_font = pygame.font.SysFont('Arial',50)\n",
    "    ft2_surf = font.render(final_text2,2,(253,177,6))\n",
    "    screen.blit(ft1_surf,[screen.get_width()/2 - ft1_surf.get_width()/2,100])\n",
    "    screen.blit(ft2_surf,[screen.get_width()/2 - ft1_surf.get_width()/2,100])    \n",
    "    pygame.display.flip()\n",
    "    \n",
    "if __name__ == '__main__':\n",
    "    pygame.init()\n",
    "    pygame.font.init()\n",
    "    font = pygame.font.SysFont('Arial',50)\n",
    "    size = width,height = 400,650\n",
    "    screen = pygame.display.set_mode(size)\n",
    "    clock = pygame.time.Clock()\n",
    "    time.sleep(3)\n",
    "    Pipeline = Pipeline()\n",
    "    \n",
    "    Bird = Bird()\n",
    "    \n",
    "    while True:\n",
    "        clock.tick(60)\n",
    "        for event in pygame.event.get():\n",
    "            if event.type == pygame.QUIT:\n",
    "                sys.exit()\n",
    "            if not (event.type == pygame.KEYDOWN) and not Bird.dead:\n",
    "                Bird.jump = True\n",
    "                Bird.gravity = 3\n",
    "                Bird.jumpSpeed = 10\n",
    "            background = pygame.image.load('tree.png')\n",
    "            if checkDead():\n",
    "                getResult()\n",
    "                time.sleep(3)\n",
    "                pygame.start()\n",
    "            \n",
    "        else:\n",
    "            createMap()\n",
    "        \n",
    "            \n",
    "    pygame.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
