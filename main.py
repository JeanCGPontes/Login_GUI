import windows

import PySimpleGUI as sg


if __name__ == "__main__":
    login_window, register_window = windows.login_window(), None

    while True:
        window, event, values = sg.read_all_windows()

        if window == login_window and event == sg.WIN_CLOSED:
            break

        if window == login_window and event == 'button_logar':
            print(f"Bem vindo {values['email_or_phone']}!")
