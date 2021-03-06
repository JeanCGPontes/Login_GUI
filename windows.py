import PySimpleGUI as sg


def login_window():
    sg.theme('Reddit')

    layout = [[sg.Text('Login', font='Arial 24 bold')],
              [sg.Text('Email:', font='Arial 12', justification='left', size=(100, 1))],
              [sg.Input(key='email', size=(30, 1), font='Arial 12')],
              [sg.Text('Senha:', font='Arial 12', justification='left', size=(100, 1))],
              [sg.Input(key='password', size=(30, 1), password_char='*', font='Arial 12')],
              [sg.Button('Logar', key='login_button', size=(10, 1), font='Arial 14', button_color=('#FFFFFF', '#44CA2F'), border_width=2)],
              [sg.Text('Ainda não tem conta? ', font='Arial 12'),
               sg.Button('Cadastre-se', key='register_button', font='Arial 12 bold', button_color=('black', 'white'), border_width=0)]]

    window = sg.Window('Login', layout, size=(300, 250), element_justification='center', finalize=True)

    return window


def register_window():
    sg.theme('Reddit')

    layout = [[sg.Text('Cadastro', font='Arial 24 bold')],
              [sg.Text('Nome Completo:', font='Arial 12', justification='left', size=(100, 1))],
              [sg.Input(key='full_name', size=(30, 1), font='Arial 12')],
              [sg.Text('Email:', font='Arial 12', justification='left', size=(100, 1))],
              [sg.Input(key='email', size=(30, 1), font='Arial 12')],
              [sg.Text('Senha:', font='Arial 12', justification='left', size=(100, 1))],
              [sg.Input(key='password', size=(30, 1), password_char='*', font='Arial 12')],
              [sg.Button('Criar conta', key='register_button', size=(10, 1), font='Arial 14', button_color=('#FFFFFF', '#44CA2F'), border_width=2)],
              [sg.Text('Já possui uma conta? ', font='Arial 12'),
               sg.Button('Entre', key='login_button', font='Arial 12 bold', button_color=('black', 'white'), border_width=0)]]

    window = sg.Window('Cadastro', layout, size=(300, 300), element_justification='center', finalize=True)

    return window


def popup_success_registered():
    layout = [[sg.Text('Cadastro realizado! \nBem vindo!', font='Arial 12 bold', justification='center')],
              [sg.Button('Fazer login', font='Arial 12', key='login_buttton', button_color=('#FFFFFF', '#44CA2F'), border_width=2, size=(14, 1))]]

    window = sg.Window('', layout, disable_close=True, element_justification='center').read(close=True)

    return window


def popup_incomplete_registration():
    layout = [[sg.Text('Faltam dados a serem inseridos!', font='Arial 12 bold', justification='center')],
              [sg.Button('OK', font='Arial 12', key='ok', button_color=('#FFFFFF', '#EF0F0F'), border_width=2, size=(14, 1))]]

    window = sg.Window('', layout, disable_close=True, element_justification='center').read(close=True)

    return window


def popup_no_input_data():
    layout = [[sg.Text('Nenhum dado inserido!', font='Arial 12 bold', justification='center')],
              [sg.Button('OK', font='Arial 12', key='ok', button_color=('#FFFFFF', '#EF0F0F'), border_width=2, size=(14, 1))]]

    window = sg.Window('', layout, disable_close=True, element_justification='center').read(close=True)

    return window


def popup_login_successfully(name):
    layout = [[sg.Text(f'Login efetuado com sucesso \nBem vindo {name}!', font='Arial 12 bold', justification='center')],
              [sg.Button('OK', font='Arial 12', key='ok', button_color=('#FFFFFF', '#44CA2F'), border_width=2, size=(14, 1))]]

    window = sg.Window('', layout, disable_close=True, element_justification='center').read(close=True)

    return window


def popup_unregistered_user():
    layout = [[sg.Text(f'Usuário ainda não cadastrado!', font='Arial 12 bold', justification='center')],
              [sg.Button('OK', font='Arial 12', key='ok', button_color=('#FFFFFF', '#EF0F0F'), border_width=2, size=(14, 1))]]

    window = sg.Window('', layout, disable_close=True, element_justification='center').read(close=True)

    return window


def popup_email_already_registered():
    layout = [[sg.Text(f'Este email já está sendo usado!', font='Arial 12 bold', justification='center')],
              [sg.Button('OK', font='Arial 12', key='ok', button_color=('#FFFFFF', '#EF0F0F'), border_width=2, size=(14, 1))]]

    window = sg.Window('', layout, disable_close=True, element_justification='center').read(close=True)

    return window
