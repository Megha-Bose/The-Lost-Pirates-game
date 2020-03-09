import random
import os.path
import math

import pygame
from pygame.locals import *

import config
from config import *


def main():
    # initialiation
    pygame.init()

    screen = pygame.display.set_mode((1400, 950))
    all = pygame.sprite.RenderUpdates()
    Explosion.containers = all

    # declaring a bool variable to continue running
    running = True
    # initialising number of rounds and scores
    rounds = 3
    score1 = 0
    score2 = 0

    # to keep check on who wins a round and
    # increase the speed of obstacles accordingly
    win1 = 0
    win2 = 0
    while running:
        # adding background music
        if pygame.mixer:
            pygame.mixer.music.load('./data/background.mp3')
            pygame.mixer.music.play(-1)

        while rounds > 0:
            # declaring objects of classes
            player1 = Player1([690, 920])
            player1.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
            player1.vx = 5
            player1.vy = 5

            player2 = Player2([690, 30])
            player2.move = [pygame.K_KP4, pygame.K_KP6, pygame.K_KP8, pygame.K_KP2]
            player2.vx = 5
            player2.vy = 5

            player_group = pygame.sprite.Group()
            player_group.add(player1)
            player_group.add(player2)

            mov0 = Movingobs([-200, 105], 0)
            mov1 = Movingobs([-100, 255], 1)
            mov2 = Movingobs([-100, 400], 2)
            mov3 = Movingobs([-100, 555], 3)
            mov4 = Movingobs([-150, 705], 4)
            mov5 = Movingobs([-40, 855], 5)
                
            movobs_group = pygame.sprite.Group()
            movobs_group.add(mov0, mov1, mov2, mov3, mov4, mov5)

            f0 = Fixedobs([300, 170], 0)
            f1 = Fixedobs([900, 170], 2)
            f2 = Fixedobs([700, 320], 1)
            f3 = Fixedobs([1200, 320], 0)
            f4 = Fixedobs([200, 475], 1)
            f5 = Fixedobs([500, 475], 2)
            f6 = Fixedobs([800, 620], 0)
            f7 = Fixedobs([1300, 620], 1)
            f8 = Fixedobs([400, 770], 2)
            f9 = Fixedobs([690, 770], 1)
            
            fobs_group = pygame.sprite.Group()
            fobs_group.add(f0, f1, f2, f3, f4, f5, f6, f7, f8, f9)
            flag0 = flag1 = flag2 = flag3 = flag4 = flag5 = 0
            flag6 = flag7 = flag8 = flag9 = flag10 = 0

            # keeping start time
            st = pygame.time.get_ticks()/1000

            # when player 1 plays in a round
            while player1.alive():

                screen = pygame.display.set_mode((1400,950))
                setscreen()
                curr = pygame.time.get_ticks()/1000
                score1 = score1 - (curr - st) / 1000 # decreasing score as time passes

                # increasing speed of obstacles on winning
                mov0.vx = 3 + (win1 * 1)
                mov1.vx = 5 + (win1 * 1)
                mov2.vx = 4 + (win1 * 1)
                mov3.vx = 4 + (win1 * 1)
                mov4.vx = 2 + (win1 * 1)
                mov5.vx = 3 + (win1 * 1)

                # showing scores

                text1 = largeFont.render('Score 1: ' + str(round(score1)), 1, (0, 0, 0))
                screen.blit(text1, (40, 10))
                text2 = largeFont.render('Score 2: ' + str(round(score2)), 1, (0, 0, 0))
                screen.blit(text2, (40, 30))
                start = largeFont.render('END', 1, (0, 0, 0))
                screen.blit(start, (1300, 20))
                end = largeFont.render('START', 1, (0, 0, 0))
                screen.blit(end, (1290, 910))
                status = largeFont.render("PLAYER 1'S TURN | ROUND:" + str(4-rounds), 1, (0, 0, 0))
                screen.blit(status, (50, 910))
                
                # keeping obstacles moving 
                mov0.rect.x += mov0.vx
                if mov0.rect.x >= 1400:
                    mov0.rect.x = -200
                mov1.rect.x += mov1.vx
                if mov1.rect.x >= 1400:
                    mov1.rect.x = -100
                mov2.rect.x += mov2.vx
                if mov2.rect.x >= 1400:
                    mov2.rect.x = -100
                mov3.rect.x += mov3.vx
                if mov3.rect.x >= 1400:
                    mov3.rect.x = -100
                mov4.rect.x += mov4.vx
                if mov4.rect.x >= 1400:
                    mov4.rect.x = -150
                mov5.rect.x += mov5.vx
                if mov5.rect.x >= 1400:
                    mov5.rect.x = -40

                # movement controls
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False
                key = pygame.key.get_pressed()

                for i in range(2):
                    if key[player1.move[i]]:
                        player1.rect.x += player1.vx * [-1, 1][i]
                        if player1.rect.x <= 0:
                            player1.rect.x = 0
                        elif player1.rect.x >= 1368:
                            player1.rect.x = 1368
                for i in range(2):
                    if key[player1.move[2:4][i]]:
                        player1.rect.y += player1.vy * [-1, 1][i]
                        if player1.rect.y <= 0:
                            player1.rect.y = 0
                        elif player1.rect.y >= 900:
                            player1.rect.y = 900

                # score updatation
                if player1.rect.y < 855 and flag0 == 0:
                    score1 += 10
                    flag0 = 1
                if player1.rect.y < 770 and flag1 == 0:
                    score1 += 10
                    flag1 = 1
                if player1.rect.y < 705 and flag2 == 0:
                    score1 += 10
                    flag2 = 1
                if player1.rect.y < 620 and flag3 == 0:
                    score1 += 10
                    flag3 = 1
                if player1.rect.y < 555 and flag4 == 0:
                    score1 += 10
                    flag4 = 1
                if player1.rect.y < 475 and flag5 == 0:
                    score1 += 10
                    flag5 = 1
                if player1.rect.y < 400 and flag6 == 0:
                    score1 += 10
                    flag6 = 1
                if player1.rect.y < 320 and flag7 == 0:
                    score1 += 10
                    flag7 = 1
                if player1.rect.y < 255 and flag8 == 0:
                    score1 += 10
                    flag8 = 1
                if player1.rect.y < 170 and flag9 == 0:
                    score1 += 10
                    flag9 = 1
                if player1.rect.y < 105 and flag10 == 0:
                    score1 += 10
                    flag10 = 1
                if player1.rect.y < 60:
                    player1.kill()
                    
                # checking collisions and giving penalty
                for player in pygame.sprite.groupcollide(fobs_group, player_group, True, True):
                    exp = Explosion(player)
                    exp_group = pygame.sprite.Group()
                    exp_group.add(exp)
                    exp_group.draw(screen)
                    score1-=50
                    player.kill()
                for player in pygame.sprite.groupcollide(movobs_group, player_group, True, True):
                    exp = Explosion(player)
                    exp_group = pygame.sprite.Group()
                    exp_group.add(exp)
                    exp_group.draw(screen)
                    score1-=50
                    player.kill()
                player_group.draw(screen)
                movobs_group.draw(screen)
                fobs_group.draw(screen)
                pygame.display.update()

            # reinitialisation for player 2

            player1 = Player1([690, 920])
            player1.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
            player1.vx = 5
            player1.vy = 5

            player2 = Player2([690, 30])
            player2.move = [pygame.K_KP4, pygame.K_KP6, pygame.K_KP8, pygame.K_KP2]
            player2.vx = 5
            player2.vy = 5

            player_group = pygame.sprite.Group()
            player_group.add(player1)
            player_group.add(player2)

            mov0 = Movingobs([-200, 105], 0)
            mov1 = Movingobs([-100, 255], 1)
            mov2 = Movingobs([-100, 400], 2)
            mov3 = Movingobs([-100, 555], 3)
            mov4 = Movingobs([-150, 705], 4)
            mov5 = Movingobs([-40, 855], 5)

            movobs_group = pygame.sprite.Group()
            movobs_group.add(mov0, mov1, mov2, mov3, mov4, mov5)

            f0 = Fixedobs([300, 170], 0)
            f1 = Fixedobs([900, 170], 2)
            f2 = Fixedobs([700, 320], 1)
            f3 = Fixedobs([1200, 320], 0)
            f4 = Fixedobs([200, 475], 1)
            f5 = Fixedobs([500, 475], 2)
            f6 = Fixedobs([800, 620], 0)
            f7 = Fixedobs([1300, 620], 1)
            f8 = Fixedobs([400, 770], 2)
            f9 = Fixedobs([690, 770], 1)

            fobs_group = pygame.sprite.Group()
            fobs_group.add(f0, f1, f2, f3, f4, f5, f6, f7, f8, f9)
            flag0 = flag1 = flag2 = flag3 = flag4 = flag5 = 0
            flag6 = flag7 = flag8 = flag9 = flag10 = 0

            st = pygame.time.get_ticks()/1000
            # when player 2 plays in a round
            while player2.alive():

                screen = pygame.display.set_mode((1400, 950))
                setscreen()

                curr = pygame.time.get_ticks()/1000
                score2 = score2 - (curr - st)/1000 # decresing score as time passes 

                # increasing speed if player 2 wins a round
                mov0.vx = 3 + (win2 * 1)
                mov1.vx = 5 + (win2 * 1)
                mov2.vx = 4 + (win2 * 1)
                mov3.vx = 4 + (win2 * 1)
                mov4.vx = 2 + (win2 * 1)
                mov5.vx = 3 + (win2 * 1)

                # showing score
                text1 = largeFont.render('Score 1: ' + str(round(score1)), 1, (0, 0, 0))
                screen.blit(text1, (40, 10))
                text2 = largeFont.render('Score 2: ' + str(round(score2)), 1, (0, 0, 0))
                screen.blit(text2, (40, 30))
                start = largeFont.render('END', 1, (0, 0, 0))
                screen.blit(start, (1290, 910))
                end = largeFont.render('START', 1, (0, 0, 0))
                screen.blit(end, (1300, 20))
                status = largeFont.render("PLAYER 2'S TURN | ROUND:" + str(4-rounds), 1, (0, 0, 0))
                screen.blit(status, (50, 910))
                mov0.rect.x += mov0.vx
                if mov0.rect.x >= 1400:
                    mov0.rect.x = -200
                mov1.rect.x += mov1.vx
                if mov1.rect.x >= 1400:
                    mov1.rect.x = -100
                mov2.rect.x += mov2.vx
                if mov2.rect.x >= 1400:
                    mov2.rect.x = -100
                mov3.rect.x += mov3.vx
                if mov3.rect.x >= 1400:
                    mov3.rect.x = -100
                mov4.rect.x += mov4.vx
                if mov4.rect.x >= 1400:
                    mov4.rect.x = -150
                mov5.rect.x += mov5.vx
                if mov5.rect.x >= 1400:
                    mov5.rect.x = -40
                
                # player 2 movement controls
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False
                key = pygame.key.get_pressed()

                for i in range(2):
                    if key[player2.move[i]]:
                        player2.rect.x += player2.vx * [-1, 1][i]
                        if player2.rect.x <= 0:
                            player2.rect.x = 0
                        elif player2.rect.x >= 1368:
                            player2.rect.x = 1368
                for i in range(2):
                    if key[player2.move[2:4][i]]:
                        player2.rect.y += player2.vy * [-1, 1][i]
                        if player2.rect.y <= 0:
                            player2.rect.y = 0
                        elif player2.rect.y >= 900:
                            player2.rect.y = 900

                # checking collisions
                if player2.rect.y > 105 and flag0 == 0:
                    score2 += 10
                    flag0 = 1
                if player2.rect.y > 170 and flag1 == 0:
                    score2 += 10
                    flag1 = 1
                if player2.rect.y > 255 and flag2 == 0:
                    score2 += 10
                    flag2 = 1
                if player2.rect.y > 320 and flag3 == 0:
                    score1 += 10
                    flag3 = 1
                if player2.rect.y > 400 and flag4 == 0:
                    score2 += 10
                    flag4 = 1
                if player2.rect.y > 475 and flag5 == 0:
                    score2 += 10
                    flag5 = 1
                if player2.rect.y > 555 and flag6 == 0:
                    score2 += 10
                    flag6 = 1
                if player2.rect.y > 620 and flag7 == 0:
                    score2 += 10
                    flag7 = 1
                if player2.rect.y > 705 and flag8 == 0:
                    score1 += 10
                    flag8 = 1
                if player2.rect.y > 770 and flag9 == 0:
                    score2 += 10
                    flag9 = 1
                if player2.rect.y > 855 and flag10 == 0:
                    score2 += 10
                    flag10 = 1
                if player2.rect.y > 890:
                    player2.kill()

                for player in pygame.sprite.groupcollide(fobs_group, player_group, True, True):
                    exp = Explosion(player)
                    exp_group = pygame.sprite.Group()
                    exp_group.add(exp)
                    exp_group.draw(screen)
                    player.kill()
                    score2 -= 50
                for player in pygame.sprite.groupcollide(movobs_group, player_group, True, True):
                    exp = Explosion(player)
                    exp_group = pygame.sprite.Group()
                    exp_group.add(exp)
                    exp_group.draw(screen)
                    score2 -= 50
                    player.kill()
                player_group.draw(screen)
                movobs_group.draw(screen)
                fobs_group.draw(screen)
                pygame.display.update()
            if score1 > score2:
                win1 = win1 + 1
            else:
                win2 = win2 + 1
            rounds = rounds - 1
        if rounds == 0:
            endscreen(llFont, lFont, score1, score2) # show game over message and winner after 3 rounds
            running = False

if __name__ == '__main__':
   main()