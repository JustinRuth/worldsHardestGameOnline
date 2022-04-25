"""
pygame-menu
https://github.com/ppizarror/pygame-menu

EXAMPLE - MULTI-INPUT
Shows different inputs (widgets).
"""

__all__ = ['main']

import pygame
import pygame_menu
from pygame_menu.examples import create_example_window

from typing import Tuple, Optional

import client_single
import client_multi
# Constants and global variables
FPS = 60
WINDOW_SIZE = (1280, 720)

sound: Optional['pygame_menu.sound.Sound'] = None
surface: Optional['pygame.Surface'] = None
main_menu: Optional['pygame_menu.Menu'] = None

level = 1


def main_background() -> None:
    """
    Background color of the main menu, on this function user can plot
    images, play sounds, etc.
    """
    surface.fill((255, 0, 0))


def check_name_test(value: str) -> None:
    """
    This function tests the text input widget.

    :param value: The widget value
    """
    print(f'User name: {value}')


def main(test: bool = False) -> None:
    """
    Main program.

    :param test: Indicate function is being tested
    """

    # -------------------------------------------------------------------------
    # Globals
    # -------------------------------------------------------------------------
    global main_menu
    global sound
    global surface
    global level

    # -------------------------------------------------------------------------
    # Create window
    # -------------------------------------------------------------------------
    surface = create_example_window("The World's Hardest Game", WINDOW_SIZE)
    clock = pygame.time.Clock()

    # -------------------------------------------------------------------------
    # Set sounds
    # -------------------------------------------------------------------------
    sound = pygame_menu.sound.Sound()

    # Load example sounds
    sound.load_example_sounds()

    # Disable a sound
    sound.set_sound(pygame_menu.sound.SOUND_TYPE_ERROR, None)

    # -------------------------------------------------------------------------
    # Create menus: Settings
    # -------------------------------------------------------------------------
    settings_menu_theme = pygame_menu.themes.THEME_DARK.copy()
    settings_menu_theme.title_offset = (5, -2)
    settings_menu_theme.widget_alignment = pygame_menu.locals.ALIGN_LEFT
    settings_menu_theme.widget_font = pygame_menu.font.FONT_OPEN_SANS_LIGHT
    settings_menu_theme.widget_font_size = 50

    settings_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.85,
        theme=settings_menu_theme,
        title='Settings',
        width=WINDOW_SIZE[0] * 0.9
    )

    # Add text inputs with different configurations
    settings_menu.add.text_input(
        'First name: ',
        default='John',
        onreturn=check_name_test,
        textinput_id='first_name'
    )
    settings_menu.add.text_input(
        'Last name: ',
        default='Rambo',
        maxchar=10,
        textinput_id='last_name',
        input_underline='.'
    )
    settings_menu.add.text_input(
        'Your age: ',
        default=25,
        maxchar=3,
        maxwidth=3,
        textinput_id='age',
        input_type=pygame_menu.locals.INPUT_INT,
        cursor_selection_enable=False
    )
    settings_menu.add.text_input(
        'Some long text: ',
        maxwidth=19,
        textinput_id='long_text',
        input_underline='_'
    )
    settings_menu.add.text_input(
        'Password: ',
        maxchar=6,
        password=True,
        textinput_id='pass',
        input_underline='_'
    )

    # Selectable items
    items = [('Easy', 'EASY'),
             ('Medium', 'MEDIUM'),
             ('Hard', 'HARD')]

    # Create selector with 3 difficulty options
    settings_menu.add.selector(
        'Select difficulty:\t',
        items,
        selector_id='difficulty',
        default=1
    )
    settings_menu.add.selector(
        'Select difficulty fancy',
        items,
        selector_id='difficulty_fancy',
        default=1,
        style='fancy'
    )
    settings_menu.add.dropselect(
        'Select difficulty (drop)',
        items,
        default=1,
        dropselect_id='difficulty_drop'
    )
    settings_menu.add.dropselect_multiple(
        title='Pick 3 colors',
        items=[('Black', (0, 0, 0)),
               ('Blue', (0, 0, 255)),
               ('Cyan', (0, 255, 255)),
               ('Fuchsia', (255, 0, 255)),
               ('Green', (0, 255, 0)),
               ('Red', (255, 0, 0)),
               ('White', (255, 255, 255)),
               ('Yellow', (255, 255, 0))],
        dropselect_multiple_id='pickcolors',
        max_selected=3,
        open_middle=True,
        selection_box_height=6  # How many options show if opened
    )

    # Create switch
    settings_menu.add.toggle_switch('First Switch', False,
                                    toggleswitch_id='first_switch')
    settings_menu.add.toggle_switch('Other Switch', True,
                                    toggleswitch_id='second_switch',
                                    state_text=('Apagado', 'Encencido'))

    # Single value from range
    rslider = settings_menu.add.range_slider('Choose a number', 50, (0, 100), 1,
                                             rangeslider_id='range_slider',
                                             value_format=lambda x: str(int(x)))

    # Range
    settings_menu.add.range_slider('How do you rate pygame-menu?', (7, 10), (1, 10), 1,
                                   rangeslider_id='range_slider_double')

    # Create discrete range
    range_values_discrete = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
    settings_menu.add.range_slider('Pick a letter', 0, list(range_values_discrete.keys()),
                                   rangeslider_id='range_slider_discrete',
                                   slider_text_value_enabled=False,
                                   value_format=lambda x: range_values_discrete[x])

    # Add a progress bar
    progress = settings_menu.add.progress_bar('Progress', default=rslider.get_value(),
                                              progressbar_id='progress')

    def on_change_slider(val: int) -> None:
        """
        Updates the progress bar.

        :param val: Value of the progress from 0 to 100
        """
        progress.set_value(val)

    rslider.set_onchange(on_change_slider)

    # Add a block
    settings_menu.add.clock(clock_format='%Y/%m/%d %H:%M', title_format='Clock: {0}')

    def data_fun() -> None:
        """
        Print data of the menu.
        """
        print('Settings data:')
        data = settings_menu.get_input_data()
        for k in data.keys():
            print(f'\t{k}\t=>\t{data[k]}')

    # Add final buttons
    settings_menu.add.button('Store data', data_fun, button_id='store')  # Call function
    settings_menu.add.button('Restore original values', settings_menu.reset_value)
    settings_menu.add.button('Return to main menu', pygame_menu.events.BACK,
                             align=pygame_menu.locals.ALIGN_CENTER)

    # -------------------------------------------------------------------------
    # Create menus: Single Player
    # -------------------------------------------------------------------------
    single_player_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1],
        theme=settings_menu_theme,
        title='Single Player',
        width=WINDOW_SIZE[0]
    )

    def play_single() -> None:
        global level
        data = client_single.play_single(level)
        if data:
            pygame_menu.sp_finished_menu()

    single_player_menu.add.button(
        'Play',
        play_single,
        align=pygame_menu.locals.ALIGN_CENTER
    )

    levels = [('1', 1),
              ('2', 2),
              ('3', 3),
              ('4', 4),
              ('5', 5),
              ('6', 6),
              ('7', 7),
              ('8', 8),
              ('9', 9),
              ('10', 10)]

    def set_level(selected: Tuple, value: Optional) -> None:
        """
        Set the difficulty of the game.
        """
        global level
        level = value

    # Create selector with 3 difficulty options
    single_player_menu.add.vertical_margin(25)
    single_player_menu.add.selector(
        'Level Select:\t',
        levels,
        selector_id='Level',
        default=0,
        onchange=set_level,
        align=pygame_menu.locals.ALIGN_CENTER
    )

    single_player_menu.add.vertical_margin(50)
    single_player_menu.add.button(
        'Return to main menu',
        pygame_menu.events.BACK,
        align=pygame_menu.locals.ALIGN_CENTER
    )

    # -------------------------------------------------------------------------
    # Create menus: Single Player Finished
    # -------------------------------------------------------------------------
    sp_finished_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1],
        theme=settings_menu_theme,
        title='Multiplayer',
        width=WINDOW_SIZE[0]
    )

    sp_finished_menu.add.button(
        'Play Again',
        single_player_menu,
        align=pygame_menu.locals.ALIGN_CENTER
    )

    sp_finished_menu.add.vertical_margin(50)
    sp_finished_menu.add.button(
        'Return to main menu',
        pygame_menu.events.BACK,
        align=pygame_menu.locals.ALIGN_CENTER
    )

    # -------------------------------------------------------------------------
    # Create menus: Multiplayer
    # -------------------------------------------------------------------------
    multi_player_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1],
        theme=settings_menu_theme,
        title='Multiplayer',
        width=WINDOW_SIZE[0]
    )

    def join() -> None:
        global level
        data = multi_player_menu.get_input_data()
        code = data['code']
        if code:
            client_multi.set_network(['join', code])
            client_multi.play_multi()

    def host() -> None:
        global level
        client_multi.set_network('host')
        client_multi.play_multi()

    multi_player_menu.add.button(
        'Host',
        host,
        align=pygame_menu.locals.ALIGN_CENTER
    )
    multi_player_menu.add.vertical_margin(50)
    multi_player_menu.add.text_input(
        'Lobby Code: ',
        maxchar=6,
        maxwidth=6,
        textinput_id='code',
        input_type=pygame_menu.locals.INPUT_INT,
        cursor_selection_enable=False,
        align=pygame_menu.locals.ALIGN_CENTER
    )
    multi_player_menu.add.button(
        'Join',
        join,
        align=pygame_menu.locals.ALIGN_CENTER
    )

    multi_player_menu.add.vertical_margin(50)
    multi_player_menu.add.button(
        'Return to main menu',
        pygame_menu.events.BACK,
        align=pygame_menu.locals.ALIGN_CENTER
    )

    # -------------------------------------------------------------------------
    # Create menus: Main menu
    # -------------------------------------------------------------------------
    main_menu_theme = pygame_menu.themes.THEME_DARK.copy()
    main_menu_theme.title_font = pygame_menu.font.FONT_COMIC_NEUE
    main_menu_theme.widget_font = pygame_menu.font.FONT_COMIC_NEUE
    main_menu_theme.widget_font_size = 50

    main_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1],
        onclose=pygame_menu.events.EXIT,  # User press ESC button
        theme=main_menu_theme,
        title="The World's Hardest Game",
        width=WINDOW_SIZE[0]
    )

    main_menu.add.button('Single Player', single_player_menu)
    main_menu.add.vertical_margin(25)
    main_menu.add.button('Multiplayer', multi_player_menu)
    main_menu.add.vertical_margin(25)
    # main_menu.add.button('bruh', settings_menu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)

    # -------------------------------------------------------------------------
    # Main loop
    # -------------------------------------------------------------------------
    while True:
        # Tick
        clock.tick(FPS)

        # Paint background
        main_background()

        # Main menu
        main_menu.mainloop(surface, main_background, disable_loop=test, fps_limit=FPS)

        # Flip surface
        pygame.display.flip()

        # At first loop returns
        if test:
            break


if __name__ == '__main__':
    main()
