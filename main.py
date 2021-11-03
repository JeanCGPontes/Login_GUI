import functions
import windows

import PySimpleGUI as sg
import sqlite3

if __name__ == "__main__":
    login_window = windows.login_window()
    register_window = None

    while True:
        window, event, values = sg.read_all_windows()

        if window == login_window and event == sg.WIN_CLOSED:
            break

        if window == login_window and event == 'login_button':
            email, password = values['email'], values['password']

            if email == '':
                if password == '':
                    windows.popup_no_input_data()
                else:
                    windows.popup_incomplete_registration()

            else:
                try:
                    name, email, password = functions.check_user_exists(email, password)
                    windows.popup_login_successfully(name)

                except TypeError:
                    windows.popup_unregistered_user()

        if window == login_window and event == 'register_button':
            register_window = windows.register_window()
            login_window.hide()

        if window == register_window and event == sg.WIN_CLOSED:
            break

        if window == register_window and event == 'register_button':
            name, email, password = values['full_name'], values['email'], values['password']

            if name and email and password != '':
                return_check_email = functions.check_email(email)

                if return_check_email is not None:
                    print('Usuário já cadastrado com este email!')

                else:
                    database = sqlite3.connect('database_Login_GUI.db')
                    cursor = database.cursor()
                    cursor.execute("INSERT INTO user_data VALUES (?, ?, ?)", (name, email, password))
                    database.commit()
                    database.close()

                    windows.popup_success_registered()
                    register_window.hide()
                    login_window.un_hide()

            elif name == '':
                if email == '':
                    if password == '':
                        windows.popup_no_input_data()
                    else:
                        windows.popup_incomplete_registration()
                else:
                    windows.popup_incomplete_registration()
            else:
                windows.popup_incomplete_registration()

        if window == register_window and event == 'login_button':
            register_window.hide()
            login_window.un_hide()
