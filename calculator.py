import pygame
import pygame_gui
from pygame_gui.elements import UIButton, UITextEntryLine, UILabel
import sys

def afficher(text,position,taille):
    """cette fonction affiche à l'ecran un texte. 
     exemple d'utilisation:
     self.menu_label=afficher('Bienvenue\nby Lesno',(550,100),60)
     self.screen.blit(self.menu_label[0], self.menu_label[1])# Un autre appel dans le run avant le flip
       """
    pygame.init()
    font=pygame.font.SysFont('arial', taille, bold=True)
    text_surface=font.render(text,True,(255, 255, 255))#couleur blanche
    text_rect=text_surface.get_rect(center=position)#position en x et y
    clock = pygame.time.Clock()
    return (text_surface, text_rect)


class App:
  def __init__(self):
    pygame.init()
    self.size = (800, 400)
    self.screen = pygame.display.set_mode(self.size)
    self.manager = pygame_gui.UIManager(self.size)
  
    #déclaration de mes boutons
    self.one_button = UIButton(
      relative_rect=pygame.Rect(5, 5+170, 150, 50),
      text='1',
      manager=self.manager
    )
    self.two_button = UIButton(
      relative_rect=pygame.Rect(160, 5+170, 150, 50),
      text='2',
      manager=self.manager
    )
    self.three_button = UIButton(
      relative_rect=pygame.Rect(315, 5+170, 150, 50),
      text='3',
      manager=self.manager
    )
    self.four_button = UIButton(
      relative_rect=pygame.Rect(5, 60+170, 150, 50),
      text='4',
      manager=self.manager
    )
    self.five_button = UIButton(
      relative_rect=pygame.Rect(160, 60+170, 150, 50),
      text='5',
      manager=self.manager
    )
    self.six_button = UIButton(
      relative_rect=pygame.Rect(315, 60+170, 150, 50),
      text='6',
      manager=self.manager
    )
    self.seven_button = UIButton(
      relative_rect=pygame.Rect(5, 115+170, 150, 50),
      text='7',
      manager=self.manager
    )
    self.eight_button = UIButton(
      relative_rect=pygame.Rect(160, 115+170, 150, 50),
      text='8',
      manager=self.manager
    )
    self.nine_button = UIButton(
      relative_rect=pygame.Rect(315, 115+170, 150, 50),
      text='9',
      manager=self.manager
    )
    self.point_button = UIButton(
      relative_rect=pygame.Rect(5, 170+170, 150, 50),
      text='.',
      manager=self.manager
    )
    self.zero_button = UIButton(
      relative_rect=pygame.Rect(160, 170+170, 150, 50),
      text='0',
      manager=self.manager
    )
    self.erase_button = UIButton(
      relative_rect=pygame.Rect(315, 170+170, 150, 50),
      text='<<',
      manager=self.manager
    )
    self.plus_button = UIButton(
      relative_rect=pygame.Rect(470, 5+170, 150, 50),
      text='+',
      manager=self.manager
    )
    self.minus_button = UIButton(
      relative_rect=pygame.Rect(470, 60+170, 150, 50),
      text='-',
      manager=self.manager
    )
    self.multi_button = UIButton(
      relative_rect=pygame.Rect(470, 115+170, 150, 50),
      text='*',
      manager=self.manager
    )
    self.divide_button = UIButton(
      relative_rect=pygame.Rect(470, 170+170, 150, 50),
      text='/',
      manager=self.manager
    )
    self.egal_button = UIButton(
      relative_rect=pygame.Rect(625, 5+170, 150, 50),
      text='=',
      manager=self.manager
    )
    self.erase_all_button= UIButton(
       relative_rect=pygame.Rect(625, 60+170, 150, 50),
       text='erase all',
       manager=self.manager
    )

    self.number=''
    self.display_label=afficher(f'{self.number}',(350, 50),40)#c'est ce que j'affiche
    self.screen.blit(self.display_label[0], self.display_label[1])

  def calcul(self):
            '''Cette fonction effectue des calculs simple en fonction de l'opérateur '''
            L=['+','-','*','/' ]
            for i in range(4):
               if L[i] in self.number:#si l'opération à faire est dans est dans notre chaine de caractère
                  
                  if i==0:#addition
                    for j in range(len(self.number)):
                        if L[i]==self.number[j]:
                           m1=float(self.number[:j])+float(self.number[j+1:len(self.number)])
                    self.number=str(m1)
                    
                  if i==1:#soustraction
                     for j in range(len(self.number)):
                        if L[i]==self.number[j]:
                           m1=float(self.number[:j])-float(self.number[j+1:len(self.number)])
                     self.number=str(m1)

                  if i==2:#multiplication
                     for j in range(len(self.number)):
                        if L[i]==self.number[j]:
                           m1=float(self.number[:j])*float(self.number[j+1:len(self.number)])
                     self.number=str(m1)

                  if i==3:#division
                     for j in range(len(self.number)):
                        if L[i]==self.number[j]:
                           if self.number[j+1:len(self.number)]=='0':#si le terme du dénominateur est nulle
                              self.number='impossible'
                            
                           else:            
                            m1=float(self.number[:j])/float(self.number[j+1:len(self.number)])
                            self.number=str(m1)

            return self.number    


  def process_events(self, event: pygame.event.Event):
    
    if event.type == pygame_gui.UI_BUTTON_PRESSED:
        if event.ui_element is self.one_button:
            name = self.one_button.text
            self.number+=name
            self.display_label=afficher(f'{self.number}',(350, 50),40)
            self.screen.blit(self.display_label[0], self.display_label[1])

        if event.ui_element is self.two_button:
            name = self.two_button.text
            self.number+=name
            self.display_label=afficher(f'{self.number}',(350, 50),40)
            self.screen.blit(self.display_label[0], self.display_label[1])

        if event.ui_element is self.three_button:
            name = self.three_button.text
            self.number+=name
            self.display_label=afficher(f'{self.number}',(350, 50),40)
            self.screen.blit(self.display_label[0], self.display_label[1])

        if event.ui_element is self.four_button:
            name = self.four_button.text
            self.number+=name
            self.display_label=afficher(f'{self.number}',(350, 50),40)
            self.screen.blit(self.display_label[0], self.display_label[1])

        if event.ui_element is self.five_button:
            name = self.five_button.text
            self.number+=name
            self.display_label=afficher(f'{self.number}',(350, 50),40)
            self.screen.blit(self.display_label[0], self.display_label[1])

        if event.ui_element is self.six_button:
            name = self.six_button.text
            self.number+=name
            self.display_label=afficher(f'{self.number}',(350, 50),40)
            self.screen.blit(self.display_label[0], self.display_label[1])

        if event.ui_element is self.seven_button:
            name = self.seven_button.text
            self.number+=name
            self.display_label=afficher(f'{self.number}',(350, 50),40)
            self.screen.blit(self.display_label[0], self.display_label[1])

        if event.ui_element is self.eight_button:
            name = self.eight_button.text
            self.number+=name
            self.display_label=afficher(f'{self.number}',(350, 50),40)
            self.screen.blit(self.display_label[0], self.display_label[1])

        if event.ui_element is self.nine_button:
            name = self.nine_button.text
            self.number+=name
            self.display_label=afficher(f'{self.number}',(350, 50),40)
            self.screen.blit(self.display_label[0], self.display_label[1])

        if event.ui_element is self.zero_button:
            name = self.zero_button.text
            self.number+=name
            self.display_label=afficher(f'{self.number}',(350, 50),40)
            self.screen.blit(self.display_label[0], self.display_label[1])

        if event.ui_element is self.point_button:
            if '.' in self.number:
               for k in range(len(self.number)):
                  if self.number[k]=='.':
                     if self.number[k+1]=='.':
                        pass
                     else:
                        name = self.point_button.text
                        self.number+=name
                        self.display_label=afficher(f'{self.number}',(350, 50),40)
                        self.screen.blit(self.display_label[0], self.display_label[1])   

            else:
               name = self.point_button.text
               self.number+=name
               self.display_label=afficher(f'{self.number}',(350, 50),40)
               self.screen.blit(self.display_label[0], self.display_label[1])
        if event.ui_element is self.erase_button:
           self.number=self.number[:-1]#on retire le dernier caractère
           self.display_label=afficher(f'{self.number}',(350, 50),40)
           self.screen.blit(self.display_label[0], self.display_label[1])
          
        if event.ui_element is self.erase_all_button:
           self.number=''
           self.display_label=afficher(f'{self.number}',(350, 50),40)
           self.screen.blit(self.display_label[0], self.display_label[1])


        if event.ui_element is self.plus_button:
            name = self.plus_button.text
            self.number+=name
            self.display_label=afficher(f'{self.number}',(350, 50),40)
            self.screen.blit(self.display_label[0], self.display_label[1])

        if event.ui_element is self.minus_button:
            name = self.minus_button.text
            self.number+=name
            self.display_label=afficher(f'{self.number}',(350, 50),40)
            self.screen.blit(self.display_label[0], self.display_label[1])


        if event.ui_element is self.multi_button:
            name = self.multi_button.text
            self.number+=name
            self.display_label=afficher(f'{self.number}',(350, 50),40)
            self.screen.blit(self.display_label[0], self.display_label[1])

        if event.ui_element is self.divide_button:
            name = self.divide_button.text
            self.number+=name
            self.display_label=afficher(f'{self.number}',(350, 50),40)
            self.screen.blit(self.display_label[0], self.display_label[1])

        if event.ui_element is self.egal_button:
            
            self.number=self.calcul()
            self.display_label=afficher(f'{self.number}',(350, 50),40)
            self.screen.blit(self.display_label[0], self.display_label[1])#affichage
                                      

  def run(self):
    clock = pygame.time.Clock()
    while True:
      time_delta = clock.tick(60)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        if not self.manager.process_events(event):
          self.process_events(event)

      
      self.manager.update(time_delta/1000)

      pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, 800, 600))
     
      self.manager.draw_ui(self.screen)

      self.screen.blit(self.display_label[0], self.display_label[1])

      pygame.display.flip()


App().run()