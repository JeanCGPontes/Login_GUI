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
            print('Button Login OK')

        if window == login_window and event == 'register_button':
            register_window = windows.register_window()
            login_window.hide()

        if window == register_window and event == sg.WIN_CLOSED:
            break

        if window == register_window and event == 'register_button':
            name, email, password = values['full_name'], values['email'], values['password']

            if name and email and password != '':
                database = sqlite3.connect('database_Login_GUI.db')
                cursor = database.cursor()
                insert_values = f"""INSERT INTO user_data (name, email, password) VALUES ('{name}', '{email}', '{password}')"""
                cursor.execute(insert_values)
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
