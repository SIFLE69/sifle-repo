# # #for i in range(5,0,-1):
# #  #   print("*"*i)







# # #for i in range(0,6):
# #    # print("*"*i)







# # # for i in range (1,6):
# # #     for j in range(1,6):
# # #         print(i*j)







# # n =  input("enter a no.")
# # s = len (n)
# # sum = 0

# # n = int(n)

# # while n>0:
# #    f =  n%10
# #    t = f**s
# #    sum+= t

# # if t == n:
# #    print(n,"is armstrong no.")

# # else:
# #    print("it is not a armstrong no")









# import pygame
# import sys

# # Initialize Pygame
# pygame.init()

# # Set up display
# width, height = 800, 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Dheeraj Animation")

# # Set up colors
# white = (255, 255, 255)
# black = (0, 0, 0)

# # Set up font
# font = pygame.font.Font(None, 36)
# text = font.render("Dheeraj", True, white)
# text_rect = text.get_rect()
# text_rect.center = (width // 2, height // 2)

# # Set up clock
# clock = pygame.time.Clock()

# # Set up initial position
# x, y = width // 2, height // 2

# # Set up speed
# speed = 5

# # Main game loop
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     # Update position
#     x += speed

#     # Wrap around when reaching the right edge
#     if x > width:
#         x = 0 - text_rect.width

#     # Clear the screen
#     screen.fill(black)

#     # Draw the text
#     screen.blit(text, (x, y))

#     # Update the display
#     pygame.display.flip()

#     # Cap the frame rate
#     clock.tick(30)












