import pygame
import schedule

# Значения параметров
count, edifice1, edifice2, edifice3, \
 edifice4, edifice5, edifice6 = 0, 0, 0, 0, 0, 0, 0


# Алгоритмы работы объектов
def objects1():
    global count, edifice1
    count += 1 * edifice1


def objects2():
    global edifice2, count
    count += 2 * edifice2


def objects3():
    global edifice3, count
    count += 4 * edifice3


def objects4():
    global edifice4, count
    count += 8 * edifice4


def objects5():
    global edifice5, count
    count += 16 * edifice5


def objects6():
    global edifice6, count
    count += 32 * edifice6


# Главное меню
class MainMenu:
    def __init__(self, background_image_MM, background_pos):
        self.background_image_MM = background_image_MM
        self.background_pos = background_pos

    def start(self):
        global running, count, edifice1, edifice2, edifice3, \
            edifice4, edifice5, edifice6
        MM = True
        while MM:
            for event in pygame.event.get():
                # Выход
                if event.type == pygame.MOUSEBUTTONUP and \
                        (115 < pygame.mouse.get_pos()[0] < 630 and
                         736 < pygame.mouse.get_pos()[1] < 841):
                    MM = False
                    running = False
                # Новая игра
                if event.type == pygame.MOUSEBUTTONUP and \
                        (115 < pygame.mouse.get_pos()[0] < 630 and
                         300 < pygame.mouse.get_pos()[1] < 405):
                    slot = 1
                    running = True
                    MM = False
                # Продолжить игру
                if event.type == pygame.MOUSEBUTTONUP and \
                        (115 < pygame.mouse.get_pos()[0] < 630 and
                         440 < pygame.mouse.get_pos()[1] < 545):
                    f1 = open('Save/Slot.txt', mode='r')
                    line = (''.join((f1.read()).split('\n'))).split('/')
                    for i in range(0, len(line)):
                        line[i] = int(line[i])
                    count, edifice1, edifice2, edifice3, \
                        edifice4, edifice5, edifice6 = line
                    f1.close()
                    MM = False
                    running = True

            pygame.display.flip()
            screen.blit(self.background_image_MM, self.background_pos)


# Основная игра
class Game:
    def __init__(self, background_image_G, background_pos):
        self.background_image_G = background_image_G
        self.background_pos = background_pos

    def start(self):
        global count, edifice1, edifice2, edifice3, \
            edifice4, edifice5, edifice6
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                # Апгрейд первого объекта
                if event.type == pygame.MOUSEBUTTONUP and\
                        100 < pygame.mouse.get_pos()[0] < 280 and \
                        200 < pygame.mouse.get_pos()[1] < 380 and \
                        count > (edifice1 + 1) * 100:
                    edifice1 += 1
                    count -= (edifice1 + 1) * 100
                    pygame.draw.rect(screen, (255, 255, 255),
                                     [100, 200, 180, 180])
                # Апгрейд второго объекта
                if event.type == pygame.MOUSEBUTTONUP and\
                        200 < pygame.mouse.get_pos()[0] < 380 and \
                        450 < pygame.mouse.get_pos()[1] < 630 and \
                        count > (edifice2 + 1) * 100:
                    edifice2 += 1
                    count -= (edifice1 + 2) * 100
                    print(edifice2)
                # Апгрейд третьего объекта
                if event.type == pygame.MOUSEBUTTONUP and\
                        300 < pygame.mouse.get_pos()[0] < 380 and \
                        700 < pygame.mouse.get_pos()[1] < 880 and\
                        count > (edifice3 + 1) * 100:
                    edifice3 += 1
                    count -= (edifice3 + 1) * 100
                # Апгрейд четвертого объекта
                if event.type == pygame.MOUSEBUTTONUP and\
                        1200 < pygame.mouse.get_pos()[0] < 1380 and \
                        200 < pygame.mouse.get_pos()[1] < 380 and\
                        count > (edifice4 + 1) * 100:
                    edifice4 += 1
                    count -= (edifice4 + 1) * 100
                if event.type == pygame.MOUSEBUTTONUP and\
                        1100 < pygame.mouse.get_pos()[0] < 1280 and \
                        450 < pygame.mouse.get_pos()[1] < 630 and\
                        count > (edifice5 + 1) * 100:
                    edifice5 += 1
                    count -= (edifice5 + 1) * 100
                if event.type == pygame.MOUSEBUTTONUP and\
                        200 < pygame.mouse.get_pos()[0] < 1180 and \
                        700 < pygame.mouse.get_pos()[1] < 880 and\
                        count > (edifice6 + 1) * 100:
                    edifice6 += 1
                    count -= (edifice6 + 1) * 100
                if event.type == pygame.MOUSEBUTTONUP and\
                        pygame.mouse.get_pos()[0] < 35 and \
                    pygame.mouse.get_pos()[0] < 30:
                    self.running = False
                    f1 = open('Save/Slot.txt', mode='w')
                    f1.write('{}/{}/{}/{}/{}/{}/{}'.format(count, edifice1, edifice2,
                                                           edifice3, edifice4, edifice5, edifice6))
                else:
                    if event.type == pygame.MOUSEBUTTONUP:
                        count += 1

            screen.blit(self.background_image_G, self.background_pos)
            # Спрайт первого объекта в зависимости от уровня
            if edifice1 == 0:
                object1 = pygame.image.load("Sprite/Objects1_1.png").convert()
            if 0 < edifice1 < 10:
                object1 = pygame.image.load("Sprite/Objects1_2.png").convert()
            if 10 < edifice1 < 30:
                object1 = pygame.image.load("Sprite/Objects1_3.png").convert()
            if 30 < edifice1 < 60:
                object1 = pygame.image.load("Sprite/Objects1_4.png").convert()
            if 60 < edifice1 < 100:
                object1 = pygame.image.load("Sprite/Objects1_5.png").convert()
            if 100 < edifice1 < 150:
                object1 = pygame.image.load("Sprite/Objects1_6.png").convert()
            if 150 < edifice1:
                object1 = pygame.image.load("Sprite/Objects1_7.png").convert()
            screen.blit(object1, [100, 200])
            pygame.draw.rect(screen, (0, 0, 0), [300, 240, 200, 50])
            f1 = pygame.font.Font(None, 36)
            text1 = f1.render('Lv. {}'.format(edifice1), False, (255, 255, 255))
            screen.blit(text1, (300, 255))

            if edifice2 == 0:
                object2 = pygame.image.load("Sprite/Objects2_1.png").convert()
            if 0 < edifice2 < 10:
                object2 = pygame.image.load("Sprite/Objects2_2.png").convert()
            if 10 < edifice2 < 30:
                object2 = pygame.image.load("Sprite/Objects2_3.png").convert()
            if 30 < edifice2 < 60:
                object2 = pygame.image.load("Sprite/Objects2_4.png").convert()
            if 60 < edifice2 < 100:
                object2 = pygame.image.load("Sprite/Objects2_5.png").convert()
            if 100 < edifice2 < 150:
                object2 = pygame.image.load("Sprite/Objects2_6.png").convert()
            if 150 < edifice2 < 210:
                object2 = pygame.image.load("Sprite/Objects2_7.png").convert()
            screen.blit(object2, [200, 450])
            pygame.draw.rect(screen, (0, 0, 0), [400, 525, 200, 50])
            text2 = f1.render('Lv. {}'.format(edifice2), False, (255, 255, 255))
            screen.blit(text2, (400, 535))

            object3 = pygame.image.load("Sprite/Objects3_1.png").convert()
            screen.blit(object3, [300, 700])

            object4 = pygame.image.load("Sprite/Objects4_1.png").convert()
            screen.blit(object4, [1200, 200])

            object5 = pygame.image.load("Sprite/Objects5_1.png").convert()
            screen.blit(object5, [1100, 450])

            object6 = pygame.image.load("Sprite/Objects6_1.png").convert()
            screen.blit(object6, [1000, 700])
            pygame.draw.rect(screen, (0, 0, 0), [630, 100, 200, 50])
            money = str(count)
            letter = 0
            while len(money) > 3:
                money = money[:-3]
                letter += 1
            convert = {
                0: 'a',
                1: 'b',
                2: 'c',
                3: 'd',
                4: 'e',
                5: 'f',
                6: 'g'
            }
            schedule.every(1).seconds.do(objects1)
            schedule.every(2).seconds.do(objects2)
            schedule.every(4).seconds.do(objects3)
            schedule.every(8).seconds.do(objects4)
            schedule.every(16).seconds.do(objects5)
            schedule.every(32).seconds.do(objects6)
            schedule.run_pending()
            text_m = f1.render('{} {}'.format(money, convert[letter]), False, (255, 255, 255))
            screen.blit(text_m, (630, 110))
            clock.tick(fps)
            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    fps = 10
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    #
    background_image_G = pygame.image.load("Sprite/GBackground.png").convert()
    background_image_MM = pygame.image.load("Sprite/MMBackground.png").convert()
    background_pos = [0, 0]
    clock = pygame.time.Clock()
    running = 0
    MM = MainMenu(background_image_MM, background_pos)
    MM.start()
    G = Game(background_image_G, background_pos)
    if running:
        G.start()
    pygame.quit()
