import PySimpleGUI as sg


def login_window():
    sg.theme('Reddit')

    layout = [[sg.Text('Login', font='Arial 24 bold')],
              [sg.Text('Seu Email ou Telefone:', font='Arial 12', justification='left', size=(100, 1))],
              [sg.Input(key='email_or_phone', size=(30, 1), font='Arial 12')],
              [sg.Text('Sua Senha:', font='Arial 12', justification='left', size=(100, 1))],
              [sg.Input(key='password', size=(30, 1), password_char='*', font='Arial 12')],
              [sg.Button('Logar', key='button_logar', size=(10, 1), font='Arial 14', button_color=('#FFFFFF', '#44CA2F'), border_width=2)],
              [sg.Text('Ainda não tem conta? ', font='Arial 12'),
               sg.Button('Cadastre-se', key='register_button', font='Arial 12 bold', button_color=('black', 'white'), border_width=0)]]

    window = sg.Window('Login', layout, size=(300, 250), element_justification='center', finalize=True)

    return window


def register_window():
    pass
