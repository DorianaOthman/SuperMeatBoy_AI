import pygame
# Control
lvl = 3
train = True
DW = True
get_nn_inputs = True
max_alive_time = 3.27
load_weights = False
render_blocks = True
save_img = True

# Levels
lvls = []

lvl1 = ['                                                                      ', 
        '                                                                      ', 
        'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 
        'X                                                                    X', 
        'X                                                                    X', 
        'X                                                                    X', 
        'X                                                                   XX', 
        'X                                                                  XX ', 
        'XX                                                                XX  ', 
        ' XX                                                               X   ', 
        '  XX                                                              X   ', 
        '   X                                                              X   ', 
        '   X                                                              X   ', 
        '   X                                                              X   ', 
        '   X                                                              X   ', 
        '   X                                                              X   ', 
        '   X                                                              X   ', 
        '   X                                                              X   ', 
        '   X                                                              X   ', 
        '   X                                                              X   ', 
        '   X                                                              X   ', 
        '   X                                                              X   ', 
        '   X                                                              X   ',
        '   X                             T                                X   ', 
        '   X                                                              X   ', 
        '   X                      XXXXXXXXXXXXXXXX                        X   ', 
        '   X                      X              X                        X   ', 
        '   X                      XX            XX                        X   ', 
        '   X                       XXXXXXXXXXXXXX                         X   ', 
        '   X                                                              X   ', 
        '   X                                                              X   ', 
        '   X                                                  XXXXXXXXXXXXX   ', 
        '   X                                                  X               ', 
        '   X                                                  X               ', 
        '   X                                                  X               ', 
        '   X                                                  X               ', 
        '   X                                                  X               ', 
        '   X   P            XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX               ', 
        '   X               XX                                                 ', 
        '   XXXXXXXXXXXXXXXXX                                                  ', 
        '                                                                      ', 
        '                                                                      ', 
        '                                                                      ', 
        '                                                                      ', 
        '                                                                      ', 
        '                                                                      ']


dw_lvl1 = ['                                                                      ', 
        '                                                                      ',
        '                                                                      ',
        'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 
        'X                                                                    X', 
        'X                                                                    X', 
        'X                                                                    X', 
        'X                                                                    X', 
        'X                                                                    X', 
        'X                                                                    X', 
        'X                                                                    X', 
        'X                                                                XXXXX', 
        'X                                                               X     ', 
        'XXXXXX                          DDDD                           X      ', 
        '      X                        D    D                          X      ', 
        '       X                      D      D                         X      ', 
        '       X                     D        D                        X      ', 
        '       X                     D        D                        X      ', 
        '       X                     D        D                        X      ', 
        '       X                     D       D                         X      ', 
        '       X                      D     D                          X      ', 
        '       X                       D   D                           X      ', 
        '       X                        DDD                            X      ',
        '       X                                                       X      ', 
        '       X                                                       X      ', 
        '       X                         T                             X      ', 
        '       X                 DD             DD                     X      ', 
        '       X                D  XXXXXXXXXXXXX  D                    X      ', 
        '       X                D                 D                    X      ', 
        '       X                D                 D                    X      ', 
        '       X                 DDXXXXXXXXXXXXXDD                     X      ', 
        '       X                                                       X      ', 
        '       X                                            XXXXXXXXXXXX      ', 
        '       X                                            X                 ', 
        '       X                                            X                 ', 
        '       X                                            X                 ', 
        '       X                                            X                 ', 
        '       X                                            X                 ', 
        '       X             XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                  ', 
        '       X      P     X                                                 ', 
        '       XXXXXXXXXXXXXX                                                 ', 
        '                                                                      ', 
        '                                                                      ', 
        '                                                                      ',
        '                                                                      ',  
        '                                                                      ']


lvl2 = ['                                                                      ',
        '                                                                      ',
        'DXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                  ',
        'D                                                  X                  ',
        'D                                                  XXXX               ',
        'D                                                  XXXXXXX            ',
        'D                                                        XX           ', 
        'D                                                         XX          ', 
        'D                                                          XX         ', 
        'D                                                           X         ', 
        'D                                                           X         ', 
        'D                                                           X         ', 
        'D                                                           X         ', 
        'D                               T                           X         ', 
        'D                                                           X         ', 
        'D                             XXXXXXXXXXXXXXXXXXX           X         ', 
        'D                             X                 XX          X         ', 
        'D                             X                  X          X         ', 
        'D                             X                  X          X         ', 
        'D                             XX                 X          X         ', 
        'D                              XX                X          X         ', 
        'D                               XX               X          X         ', 
        'D                                X               X          X         ',
        'D                                X               X          X         ', 
        'D                                X               X          X         ', 
        'D                                X               X          X         ', 
        'D                                X               X          X         ', 
        'D                                X               X          X         ', 
        'D                                XX              X          X         ', 
        'D                                X               X          X         ', 
        'D                                XX             XX          X         ', 
        'D                                 XXXXXXXXXXXXXXX           X         ', 
        'D                                                           X         ', 
        'D                                                           X         ', 
        'XXXX                                                        X         ', 
        '   XX                                                       X         ', 
        '    XXXXX                                                   X         ', 
        '       XX                                                   X         ', 
        '       XX   P                                              XX         ', 
        '       XX                                                 XX          ', 
        '       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX           ', 
        '                                                                      ', 
        '                                                                      ', 
        '                                                                      ', 
        '                                                                      ', 
        '                                                                      ']
dw_lvl2 = ['                                                                      ',
        '                                                                      ',
        'DXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                  ',
        'D                                                   X                 ',
        'D                                                    XX               ',
        'D                                                     XXXX            ',
        'D                                                        D            ', 
        'D                                                        D            ', 
        'D                                                         D           ', 
        'D                                                          DDX        ', 
        'D                                                             X       ', 
        'D                                                             X       ', 
        'D                                                             X       ', 
        'D                                  T             DDD          X       ', 
        'D                                               D   D         X       ', 
        'D                               XXXXXXXXXXXXXXXXX    D        X       ', 
        'D                               X                    D        X       ', 
        'D                               X                   D         X       ', 
        'D                               X                  D          X       ', 
        'D                               X                  X          X       ', 
        'D                               D                  X          X       ', 
        'D                               D                  X         D        ', 
        'D                               D                  X        DD        ',
        'D                                D                 X       DDD        ', 
        'D                                 D                X       DDD        ', 
        'D                                  X               X        DD        ', 
        'D                                  X               X         D        ', 
        'D                                  X               X          X       ', 
        'D                                  X                D         X       ', 
        'D                                  X                 D        X       ', 
        'D                                 X                  D        X       ', 
        'D                                  XXXXXXXXXXXXXD    D        X       ', 
        'D                                                DDDD         X       ', 
        'D                                                             X       ', 
        'XXXXX                                                         X       ', 
        '     X                                                        X       ', 
        '     XXXX                                                  DD X       ', 
        '         X                                                D           ', 
        '          X                               DD              D           ', 
        '          X    P                         DDDD             D           ', 
        '          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXXX            ', 
        '                                                                      ', 
        '                                                                      ', 
        '                                                                      ', 
        '                                                                      ', 
        '                                                                      ']

lvl3 = ['                                                                      ', 
        '                                                                      ', 
        'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 
        'X                                                                    X', 
        'X                                                                    X', 
        'X                                                                    X', 
        'X        XXXXXX                                        XXXX          X', 
        'X       XX   XXDDD                                     XXXXX         X', 
        'X      XX    X   DD                                 DDD  X XXXX      X', 
        'X      X    XX    DD                               DD    X    XX     X', 
        'X     XX    X      D                               D     X     X     X', 
        'X     X     X      D                               D     X     X     X', 
        'X    XX     X      D                               D     X     X     X', 
        'X    X      X      D                               D     X     X     X', 
        'X   XX      X     DD                               DD    X     X     X', 
        'X   X       X    DD                                 D    X     XXXXX X', 
        'X  XX       XX   D                                  D    X         XXX', 
        'X  X         XXXXX                                  XXXXXX          XX', 
        'X  X             X                                  X                 ', 
        'X XX             X                                  X                 ', 
        'XXX              X                                  X                 ', 
        '                 X                                  X                 ', 
        '                 X                                  X                 ',
        '                 X                                  X                 ', 
        '                XX                                  X                 ', 
        '                XX                                  XX                ', 
        '            XXXXX                                    XXXXX            ', 
        '          XX                                             XXX          ', 
        '          X                                                X          ', 
        '          X                                                X          ', 
        '          X                                                X          ', 
        '          X                                                X          ', 
        '          X                                                X          ', 
        '          X                                                X          ', 
        '          X                                                X          ', 
        '          X                                                X          ', 
        '          X    P                                       T   X          ', 
        '          X                                                X          ', 
        '          XXXXXXXXXXXX                          XXXXXXXXXXXX          ', 
        '                     X                          X                     ', 
        '                    XX                          XX                    ', 
        '                    X                            X                    ', 
        '                    X                            X                    ', 
        '                    X                            X                    ', 
        '                    X                            X                    ', 
        '                    XDDDDDDDDDDDDDDDDDDDDDDDDDDDDX                    ']

dw_lvl3 = ['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 
        'X                                                                    X', 
        'X                                DDD                                 X', 
        'X        XXXXXX                 D   D                  XXXX          X', 
        'X        X    X                D     D                 X   X         X', 
        'X       X     DD               D     D               DD     X        X', 
        'X       X      DD              D     D              D        X       X', 
        'X      XX       D              D     D             D         X       X', 
        'X      XX        D             D     D             D          XX     X', 
        'X      X         D              D   D              D            X    X', 
        'X     XX         D               DDD               D            X    X', 
        'X     X          D                                 D             X   X', 
        'X    XX         D                                  D              X  X', 
        'X    X        DD                                    D              X X', 
        'X   XX       X                                      X              X X', 
        'X   X        XXXXX                                  X               XX', 
        'X  XX            X                                  X                 ', 
        'X  X             X                                  X                 ', 
        'X  X             X                                  X                 ', 
        'X XX             X               DDD                X                 ', 
        'XXX              X              D   D               X                 ', 
        '                 X             D     D              X                 ', 
        '                 X             D     D              X                 ',
        '                 X             D     D              X                 ', 
        '                XX              DDDDD               X                 ', 
        '                XX              X    X              X                 ', 
        '            XXXXX               X    X              X                 ', 
        '          XX                    X    X               XXXXX            ', 
        '          X                     X    X                   XX           ', 
        '          X                     X    X                    X           ', 
        '          X                     X    X                    X           ', 
        '          X                     X    X                    X           ', 
        '          X                     X    X                    X           ', 
        '          X                     X    X                    X           ', 
        '          X                     X    X                    X           ', 
        '          X                     X    X                    X           ', 
        '          X                      D  D                     X           ', 
        '          X                       DD                      X           ', 
        '          X                                           T   X           ', 
        '          X     P                                         X           ', 
        '          XXXXXXXXXXX                           XXXXXXXXXXX           ', 
        '                    X                           X                     ', 
        '                    X                           X                     ', 
        '                    X                           X                     ', 
        '                    X                           X                     ', 
        '                    XDDDDDDDDDDDDDDDDDDDDDDDDDDDX                     ']

lvl4 = ['                                                                      ',
        '                         XXXXXXXXXXXXXXXXXXX                          ',
        '                         X                 X                          ',
        '                         X                 X                          ',
        '                         X                 X                          ',
        '                         X         T       X                          ',
        '                         X     XXXXXXX     X                          ',
        '                         X     XXXXXXX     X                          ',
        '                         X                 X                          ',
        '                         X                 X                          ',
        '                         X                 X                          ',
        '                         X        XX  XX   X                          ',
        '                         X    XX  XX  XX   X                          ',
        '                         X    XX  XX  XX   X                          ',
        '                         X    XX  XX  XX   X                          ',
        '                         X    XX  XX  XX   X                          ',
        '                         X    XX  XX  XX   X                          ',
        '                         X    XX  XX  XX   X                          ',
        '                         X    XX  XX  XX   X                          ',
        '                         X    XX  XX  XX   X                          ',
        '                         X    XX  XX  XX   X                          ',
        '                         X    XX  XX  XX   X                          ',
        '                         X    XX  XX  XX   X                          ',
        '                         X    XX  XX  XX   X                          ',
        '                         X    XX  XX  XX   X                          ',
        '                         X    XX  XX  XXXXXX                          ',
        '                         X    XX  XX  XXXXXX                          ',
        '                         X                 X                          ',
        '                         X                 X                          ',
        '                         X   XXXXXXXXXXXXXXX                          ',
        '                         X   X                                        ',
        '                         X   X                                        ',
        '                         X   X XXXXXXXXXXXXXX                         ',
        '                         X   X X            X                         ',
        '                         X   X X            X                         ',
        '                         X   X X            X                         ',
        '                         X   XXX  XXXXXXX   X                         ',
        '                         X        X     X   X                         ',
        '                         X        X     X   X                         ',
        '                         X        X     X   X                         ',
        '                         XXXXXXXXXX     X   X                         ',
        '                           XXXXXXXXXXXXXX   X                         ',
        '                          XX                X                         ',
        '                          XX P              X                         ',
        '                          XX                X                         ',
        '                          XXXXXXXXXXXXXXXXXXX                         ']

lvl5 = ['                XXXXXXXXXXXXXXXXXXXXXXXXXXXXX                         ', '                X                           XX                        ', '                X                            X                        ', '                X                            X                        ', '                X                          T X                        ', '                X                            X                        ', '                X                         XXXX                        ', '                X                      XXXX                           ', '                X                     XX                              ', '                X                     X                               ', '                X           XXXX      X                               ', '                X           X         X                               ', '                X           X         X                               ', '                X           XXXX      X                               ', '                X           X  X      X                               ', '                X           XX X      X                               ', '                X            X X      X                               ', '                X            XXX      X                               ', '                X              X      X                               ', '                X                     X                               ', '                X                     X                               ', '                X                     X                               ', '                X                     X                               ',
        '                X                     XXXXXXXX                        ', '                X                            X                        ', '                X                            X                        ', '                X                            X                        ', '                X                  XXXXXXX   X                        ', '                X                     X  X   X                        ', '                X                     XX X   X                        ', '                X                      XXX   X                        ', '                X                            X                        ', '                X                            X                        ', '                X                            X                        ', '                X                            X                        ', '                X                            X                        ', '                X                            X                        ', '                XX                           X                        ', '                 XX                          X                        ', '                  X                          X                        ', '                  X                          X                        ', '                  XXXX                       X                        ', '                     XXXXXX                  X                        ', '                       X P                   X                        ', '                       X                     X                        ', '                       XXXXXXXXXXXXXXXXXXXXXXX                        ']

lvl6 = ['                                                                      ', '                                                                      ', '                                                                      ', '                       XXXXXXXXXXXXXXXXXXXXXXXXXX                     ', '                      XX                        X                     ', '                     XX                         X                     ', '                     X                          X                     ', '                     X                          X                     ', '                     X           DDDDD          X                     ', '                     X          DD   DD         X                     ', '                     X  T       D     D         X                     ', '                     XX         D     D         X                     ', '                      XXXXXXXXXXXXXXXXXXX       X                     ', '                                        X       X                     ', '                                       XX       X                     ', '                                      XX        X                     ', '                     XXXXXXXXXXXXXXXXXX         X                     ', '                     X                          X                     ', '                     X                          X                     ', '                     X                          X                     ', '                     X                          X                     ', '                     X                     DDD  X                     ', '                     X                     D D  X                     ',
        '                     X        XXXXXXXXXXXXXXXXXXX                     ', '                     X        XX                                      ', '                     X         XXXXXXXXXXXXXXXXXX                     ', '                     X                          X                     ', '                     X                          X                     ', '                     X                          X                     ', '                     X                          X                     ', '                     X                          X                     ', '                     X                          X                     ', '                     X              DDD         X                     ', '                     X             D  D         X                     ', '                     XXXXXXXXXXXXXXXXXXXX       X                     ', '                                       XX       X                     ', '                       XXXXXXXXXXXXXXXXX        X                     ', '                      XX                        X                     ', '                     XX                         X                     ', '                     X                          X                     ', '                     X                          X                     ', '                     X  P                       X                     ', '                     X                         XX                     ', '                     XXXXXXXXXXXXXXXXXXXXXXXXXXX                      ', '                                                                      ', '                                                                      ']

lvl7 = ['  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  ', '  X                                                                X  ', '  X                                                                X  ', '  X                                                                X  ', '  X                                                                X  ', '  X                                                                X  ', '  X                                                                X  ', '  X                                                                X  ', '  X                                                            T   X  ', '  X                                                                X  ', '  X                                        XXXXX             XXXXXXX  ', '  X                                       XX   X             X        ', '  X                                      XX    X             X        ', '  X                   DDXXXXXXXXXXXXXXXXXX     X             X        ', '  X                  D                         X             X        ', '  X                  D                         X             X        ', '  X                  D                         X             X        ', '  X                  X    XXXXXXXXXXXXXXXXX    X             X        ', '  X                  X   XX               XX  XX             X        ', '  X                  X   X                 X  X             XX        ', '  X                  X   X                 X  X          XXXX         ', '  X                  X   X                 X  X          X            ', '  X                  X   X                 X  X          X            ',
        '  X                  X   X                 X  X       DDDX            ', '  X                  X   X                 X  X      DD  X            ', '  X                  X   X       XXX       X  X      D   X            ', '  X                  X   X     DDX XX      X  X      D   X            ', '  X                  X   X    D  X  XX     X  X      D   X            ', '  X                  X   X    D  X   X     X  X      D   X            ', '  X                  X   X    D  X   X     X  X       XXXX            ', '  X                  X   X    D  X   X     X  X       X               ', '  X                  X   X    D  X   X     X  X       X               ', '  X                  X   X     DDX   X     X  X       X               ', '  X                  X   X       X   X     X XX       X               ', '  X                  X   X       X   X     XXX        X               ', '  X                  X   X       X   X     XX         X               ', '  X                  X   X       X   X                X               ', '  X                  X  XX       X   X                X               ', '  X                  XXXX        X   X                X               ', '  X                              X   X                X               ', '  X                              X   X                X               ', '   X                             X   X                X               ', '   XX                           XX   XX              XX               ', '    X     P                    X      XXXXXXXXXXXXXXXX                ', '    X                         XX                                      ', '    XXXXXXXXXXXXXXXXXXXXXXXXXXXX                                      ']

lvl8 = ['                                                                      ', '                                                                      ', '                                                                      ', '           XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX           ', '           X                                              X           ', '            X                                            X            ', '             X                                           X            ', '             X                                           X            ', '             X                                           X            ', '          XXXX                                           XXX          ', '          X                                                X          ', '          X                                                X          ', '       XXXX                                                XXXXX      ', '      XX                                                       X      ', '   XXXX                                                        XXXXX  ', '  XX                                                               XX ', ' XX                            XXXXXXXXX                            X ', ' X                             X       X                            X ', ' X                             X       X                            X ', ' X                             X       X                            X ', ' X                             X       X                            X ', ' X                             X       X                            X ', ' X                             X       X                            X ',
        ' X                             X       X                            X ', ' X                             X       X                            X ', ' X                             X       X                            X ', ' X                             X       X                            X ', ' X                             X       X                            X ', ' X   P                         X       X                         T  X ', ' X                             X       X                            X ', ' XXXXXX                        X       X                        XXXXX ', '  XXXXX                        X       X                        XXXXX ', ' XX  DD                        XX     XX                      DDDD  X ', ' X  D  DD DDD  DDD DDD   DD  DD X     XDD  DDD      DDDD  DD  D   D X ', ' XXD     D   DD   D   DDD  DD DD         D D  DDDDDDD   DD  DD     XX ', '                                          D                           ', '                                                                      ', '                                                                      ', '                                                                      ', '                                                                      ', '                                                                      ', '                                                                      ', '                                                                      ', '                                                                      ', '                                                                      ', '                                                                      ']

#dw str variable used for file names
dw = ""
if not DW: 
        lvls.append(lvl1)  # Done
        lvls.append(lvl2)  # Done
        lvls.append(lvl3)  # Done
        lvls.append(lvl4)  # Done
        lvls.append(lvl5)  # Done
        lvls.append(lvl6)  # Done
        lvls.append(lvl7)  # Done
        lvls.append(lvl8)  # Done
else:
        dw = "dw_"
        lvls.append(dw_lvl1)
        lvls.append(dw_lvl2)
        lvls.append(dw_lvl3)

# Display
tile_size_x = 10
tile_size_y = 10
screen_width = 700
screen_height = 468


# Generates map based on desired level from settings at top of file
level_map = lvls[lvl-1]
output_format = "jpg"
level_bg = pygame.image.load(f"{dw}lvl{lvl}.{output_format}")
scale_factor = 0.35 if lvl in [1, 2, 3, 6, 7, 8] else 0.2
jump_speed = -9 if lvl in [5, 7] else -10

# Nnet Settings
GEN_SIZE = 100 #Number of meatboys in each generation
generation_size = GEN_SIZE if train else 1 #Sets generation size, but if not training will use one meatboy for testing
N_INPUT, N_HIDDEN, N_OUTPUT = 3, 10, 2 #values used for Nnet
MUTATION_WEIGHT_MODIFY_CHANCE = 0.1 #probability of mutation for each generation
MUTATION_ARRAY_MIX_PERC = 0.5 #Percentage of Meatboys you wanted mixed from both parents into new offspring
MUTATION_CUT_OFF = 0.5 #determines cut off between good and bad meatboys (Smaller the number, the stricter the algorithem considers a "good" meatboy)
MUTATION_BAD_TO_KEEP = 0.1 # Precentage of low fitness score meatboys to keep
MUTATION_MODIFY_CHANCE_LIMIT = 0.1 #Percentage chance to modify weights in newly created offspring

#Extra Info to Note (Training)
#-All Bad Meatboys kept in each new generation have their weights modified
#-Each new offspring of Meatboys is created randomly from 2 "good" Meatboys
#-Each new offspring of Meatboys have create new wights by getting a random mixture of weights from 2 "good" Meatboys
#-For each newly generated offspring, there is a chance the new weights can be modified
