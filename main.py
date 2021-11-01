import windows

import PySimpleGUI as sg


if __name__ == "__main__":
    login_window, register_window = windows.login_window(), None

    while True:
        window, event, values = sg.read_all_windows()

        if window == login_window and event == sg.WIN_CLOSED:
            break

        if window == login_window and event == 'login_button':
            print('Button Login OK')

        if window == login_window and event == 'register_button':
            register_window = windows.register_window()
            login_window.hide()

        if window == register_window and event == sg.WIN_CLOSED:
            break

        if window == register_window and event == 'register_button':
            print('Button Register OK')

        if window == register_window and event == 'login_button':
            login_window.un_hide()
            register_window.hide()
