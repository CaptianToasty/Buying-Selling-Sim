import pygame, sys, random
from button import Button

class Game:
    def __init__(self):
        # Button Attributes
        self.buy_button = Button()
        self.sell_button = Button()
        self.sell_button.rect.y += 100
        self.next_day_button = Button()
        self.next_day_button.rect.y += 200
        self.button_list = [self.buy_button, self.sell_button, self.next_day_button]
        # Stat Attributes
        self.money = 50
        self.price = 20
        self.quanity_owned = 0
        self.day = 0
        # Text Setup
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.buy_text = "Buy"
        self.sell_text = "Sell"
        self.next_day_button_text = "Next Day"
        

        
        

    # Checking if mouse click is within button
    def check_collisions(self):
        mouse = pygame.mouse.get_pos()

        for butt in self.button_list:
            if butt.rect.collidepoint(mouse):
                butt.touching = True
                if mouse_click:
                    butt.pressed = True
                    self.transaction()
            else: butt.touching = False

    def transaction(self):
        if self.buy_button.pressed:
            if self.money >= self.price:
                self.money -= self.price
                self.quanity_owned += 1
            self.buy_button.pressed = False

        if self.sell_button.pressed:
            if self.quanity_owned > 0:
                self.money += self.price
                self.quanity_owned -= 1
            self.sell_button.pressed = False

        if self.next_day_button.pressed:
            self.day += 1
            self.price = random.randint(15,35)
            self.next_day_button.pressed = False

    # Drawing the buttons on screen
    def draw_buttons(self):
        for butt in self.button_list:
            if butt.touching == True:
                color = GREY
            else: color = WHITE
            pygame.draw.rect(screen, color, butt.rect)

    def render_text(self, text, pos, color):
        text_str = str(text)
        text_image = self.font.render(text_str, True, color)
        textRect = text_image.get_rect()
        textRect.center = pos
        screen.blit(text_image, (textRect))

    def draw_text(self):
        self.render_text(self.buy_text, (300,340), BLACK)
        self.render_text(self.sell_text, (300, 440), BLACK)
        self.render_text(self.next_day_button_text, (300,540), BLACK)
        self.render_text(money_text, (300, 125), GREEN)
        self.render_text(quanity_text, (300,175), GREEN)
        self.render_text(price_text, (300, 225), GREEN)
        self.render_text(day_text, (520, 40), GREEN)

    # Calling all the functions here
    def update(self):
        self.check_collisions()
        self.draw_buttons()
        self.draw_text()

if __name__ == "__main__":
    # Setting up the game
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    WHITE = (255,255,255)
    GREY = (200,200,200)
    BLACK = (0,0,0)
    GREEN = (0,255,0)
    clock = pygame.time.Clock()
    game = Game()
    mouse_click = False
    # Text Setup
    money_text = 0
    price_text = 0
    quanity_text = 0
    day_text = 0
    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_click = True
        # This all happens once per frame
        screen.fill((30,30,30))
        game.update()
        pygame.display.flip()
        clock.tick(60)
        mouse_click = False
        # Text Adjustments
        money_text = "Money: " + "$" + str(game.money)
        price_text = "Price: " + "$" + str(game.price)
        quanity_text = "Quanity Owned: " + str(game.quanity_owned)
        day_text = "Day: " + str(game.day)