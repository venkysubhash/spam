# # import pygame

# pygame.init()
# width, height = 400, 400
# screen = pygame.display.set_mode((width, height))
# running = True

# img = pygame.image.load("123.png")  # Load the image
# img = pygame.transform.scale(img, (200, 200))  # Resize the image to fit

# x = 250
# y = 100
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill((255, 255, 255)) 
#     screen.blit(img,(x,y)) # Fill the screen with white
#     pygame.display.update()
#     pygame.quit()