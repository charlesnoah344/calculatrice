import pygame
import pygame_gui
from pygame_gui.elements import UIButton, UITextEntryLine, UILabel
import sys
import re

def afficher(text,position,taille,police,couleur):
    """cette fonction affiche à l'ecran un texte. 
     exemple d'utilisation:
     self.menu_label=afficher('Bienvenue\nby Lesno',(550,100),60)
     self.screen.blit(self.menu_label[0], self.menu_label[1])# Un autre appel dans le run avant le flip
       """
    pygame.init()
    font=pygame.font.SysFont(police, taille, bold=True)
    text_surface=font.render(text,True,couleur) #couleur blanche
    text_rect=text_surface.get_rect(center=position)#position en x et y
    clock = pygame.time.Clock()
    return (text_surface, text_rect)


class App:
  def __init__(self):
    pygame.init()
    self.size = (780, 460)
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
      manager=self.manager,
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
    self.open_parenthesis_button=UIButton(
       relative_rect=pygame.Rect(625, 115+170, 150, 50),
       text='(',
       manager=self.manager
    )
    self.close_parenthesis_button=UIButton(
       relative_rect=pygame.Rect(625, 170+170, 150, 50),
       text=')',
       manager=self.manager
    )

    self.cos_button=UIButton(
       relative_rect=pygame.Rect(5, 170+225, 150, 50),
       text='cos',
       manager=self.manager
    )

    self.pattern=r'\d+\.?\d*|[+\-*/]'


    self.number=''
    self.display_position=(400,120)
    self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))#couleur blanche
    self.screen.blit(self.display_label[0], self.display_label[1])

    self.welcome_label=afficher('Lesno calculator',(400,50),40,'comic sans ms',(255,0,0))#couleur rouge
    self.screen.blit(self.welcome_label[0], self.welcome_label[1])

    
  def calcul(self):
    """Cette fonction effectue les opérations."""
    try:
      return str(eval(self.number))
    except SyntaxError:
       return 'SYNTAX ERROR'
    except ZeroDivisionError:
       return "MATH ERROR"

  def process_events(self, event: pygame.event.Event):
    '''cette fonction gère les différents évènements'''
    p=re.compile(self.pattern)#regex

    if event.type == pygame_gui.UI_BUTTON_PRESSED:
        if event.ui_element is self.one_button:
            if p.match(self.number) is not None: #si il s'agit d'une séquence d'operation
              name = self.one_button.text
              self.number+=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])
            else:#sinon on supprime tout
              name = self.one_button.text
              self.number=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])

        if event.ui_element is self.two_button:
            if p.match(self.number) is not None: #si il s'agit d'une séquence d'operation
              name = self.two_button.text
              self.number+=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])
            else:#sinon on supprime tout
              name = self.two_button.text
              self.number=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])


        if event.ui_element is self.three_button:
            if p.match(self.number) is not None: #si il s'agit d'une séquence d'operation
              name = self.three_button.text
              self.number+=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])
            else:#sinon on supprime tout
              name = self.three_button.text
              self.number=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])


        if event.ui_element is self.four_button:
            if p.match(self.number) is not None: #si il s'agit d'une séquence d'operation
              name = self.four_button.text
              self.number+=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])
            else:#sinon on supprime tout
              name = self.four_button.text
              self.number=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])

        if event.ui_element is self.five_button:
            if p.match(self.number) is not None: #si il s'agit d'une séquence d'operation
              name = self.five_button.text
              self.number+=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])
            else:#sinon on supprime tout
              name = self.five_button.text
              self.number=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])

        if event.ui_element is self.six_button:
            if p.match(self.number) is not None: #si il s'agit d'une séquence d'operation
              name = self.six_button.text
              self.number+=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])
            else:#sinon on supprime tout
              name = self.six_button.text
              self.number=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])

        if event.ui_element is self.seven_button:
            if p.match(self.number) is not None: #si il s'agit d'une séquence d'operation
              name = self.seven_button.text
              self.number+=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])
            else:#sinon on supprime tout
              name = self.seven_button.text
              self.number=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])

        if event.ui_element is self.eight_button:
            if p.match(self.number) is not None: #si il s'agit d'une séquence d'operation
              name = self.eight_button.text
              self.number+=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])
            else:#sinon on supprime tout
              name = self.eight_button.text
              self.number=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])

        if event.ui_element is self.nine_button:
            if p.match(self.number) is not None: #si il s'agit d'une séquence d'operation
              name = self.nine_button.text
              self.number+=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])
            else:#sinon on supprime tout
              name = self.nine_button.text
              self.number=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])

        if event.ui_element is self.zero_button:
            if p.match(self.number) is not None: #si il s'agit d'une séquence d'operation
              name = self.zero_button.text
              self.number+=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])
            else:#sinon on supprime tout
              name = self.zero_button.text
              self.number=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])

        if event.ui_element is self.point_button:
            if p.match(self.number) is not None: #si il s'agit d'une séquence d'operation
              if '.' in self.number:
                for k in range(len(self.number)):
                    if self.number[k]=='.':
                      if self.number[k+1]=='.':
                          pass
                      else:
                          name = self.point_button.text
                          self.number+=name
                          self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
                          self.screen.blit(self.display_label[0], self.display_label[1])   

              else:
                name = self.point_button.text
                self.number+=name
                self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
                self.screen.blit(self.display_label[0], self.display_label[1])
            else:#sinon on supprime tout
              name = self.point_button.text
              self.number=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])
               

        if event.ui_element is self.erase_button:
           if p.match(self.number) is not None: #si il s'agit d'une séquence d'operation
              self.number=self.number[:-1]#on retire le dernier caractère
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])
           else: #sinon on supprime tout
              self.number=''
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])
          
        if event.ui_element is self.erase_all_button:
           self.number=''
           self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
           self.screen.blit(self.display_label[0], self.display_label[1])
        
           
        if event.ui_element is self.plus_button:
            if p.match(self.number) is not None: #si il s'agit d'une séquence d'operation
              name = self.plus_button.text
              self.number+=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])
            else:#sinon on supprime tout
              name = self.plus_button.text
              self.number=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])

        if event.ui_element is self.minus_button:
            if p.match(self.number) is not None: #si il s'agit d'une séquence d'operation
              name = self.minus_button.text
              self.number+=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])
            else:#sinon on supprime tout
              name = self.minus_button.text
              self.number=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])


        if event.ui_element is self.multi_button:
            if p.match(self.number) is not None: #si il s'agit d'une séquence d'operation
              name = self.multi_button.text
              self.number+=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])
            else:#sinon on supprime tout
              name = self.multi_button.text
              self.number=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])


        if event.ui_element is self.divide_button:
            if p.match(self.number) is not None: #si il s'agit d'une séquence d'operation
              name = self.divide_button.text
              self.number+=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])
            else:#sinon on supprime tout
              name = self.divide_button.text
              self.number=name
              self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
              self.screen.blit(self.display_label[0], self.display_label[1])

        if event.ui_element is self.egal_button:
            
            self.number=self.calcul()
            self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
            self.screen.blit(self.display_label[0], self.display_label[1])#affichage
        
        if event.ui_element is self.open_parenthesis_button:
            name = self.open_parenthesis_button.text
            self.number+=name
            self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
            self.screen.blit(self.display_label[0], self.display_label[1])

        if event.ui_element is self.close_parenthesis_button:
            name = self.close_parenthesis_button.text
            self.number+=name
            self.display_label=afficher(f'{self.number}',self.display_position,40,'arial',(255,255,255))
            self.screen.blit(self.display_label[0], self.display_label[1])
                                    

  def run(self):

    'cette fonction fait fonctionner le tout'

    clock = pygame.time.Clock()
    while True:
      time_delta = clock.tick(60)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        if not self.manager.process_events(event):
          self.process_events(event)

      
      self.manager.update(time_delta/1000)

      pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, 780, 460))
     
      self.manager.draw_ui(self.screen)

      self.screen.blit(self.display_label[0], self.display_label[1])

      self.screen.blit(self.welcome_label[0], self.welcome_label[1])

      pygame.display.flip()


App().run()