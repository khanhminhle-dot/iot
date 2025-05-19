import pygame
from pygame.locals import *
import sys

# Khởi tạo pygame
pygame.init()
pygame.mixer.init()

# Tạo cửa sổ nhỏ để nhận sự kiện bàn phím
screen = pygame.display.set_mode((300, 100))
pygame.display.set_caption("Soundboard với bàn phím")

# Load file âm thanh (bạn đổi tên đường dẫn nếu cần)
soundA = pygame.mixer.Sound("music/A.mp3")
soundB = pygame.mixer.Sound("music/B.mp3")
soundC = pygame.mixer.Sound("music/C.mp3")

# Kênh riêng cho mỗi âm thanh
channelA = pygame.mixer.Channel(1)
channelB = pygame.mixer.Channel(2)
channelC = pygame.mixer.Channel(3)

print("Nhấn phím 1 / 2 / 3 để phát âm thanh. ESC để thoát.")

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_1:
                channelB.stop()
                channelC.stop()
                channelA.play(soundA)
            elif event.key == K_2:
                channelA.stop()
                channelC.stop()
                channelB.play(soundB)
            elif event.key == K_3:
                channelA.stop()
                channelB.stop()
                channelC.play(soundC)

pygame.quit()
sys.exit()
