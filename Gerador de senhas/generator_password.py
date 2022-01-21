import random
import PySimpleGUI as sg

class PassGen:
    def __init__(self):
        sg.theme('Python')
        layout = [ # Setting up the program layout
            [sg.Text('Quantidade de caracteres:', font='Arial 13 bold'),
             sg.Input(key='total_chars', size=(14, 1))],
            [sg.Checkbox(text='Caracteres especiais', key='chars_especiais', font='Arial 11', size=(15, 1)),
             sg.Checkbox(text='Números', key='chars_numeros', font='Arial 11', size=(10, 1))],
            [sg.Output(key='output', size=(44, 8), font='Arial 11', text_color='white')],
            [sg.Button('Limpar saída', size=(19, 2), font='Arial 11'), sg.Button('Gerar senha', size=(19, 2), font='Arial 11')]
        ]
        self.window = sg.Window('Gerador de senhas', layout) # Defining the name and layout

    def Iniciar(self): # Function to launch the window
        while True:
            event, value = self.window.read()
            if event == sg.WINDOW_CLOSED: 
                break
            if event == 'Limpar saída':
                self.clear()
            if event == 'Gerar senha':
                if value['chars_especiais'] and value['chars_numeros'] == True:
                    chars_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%¨&*'
                    nova_senha = self.generate_password(value, chars_list) # Calling the function to generate password
                    print(nova_senha)
                if value['chars_especiais'] == False and value['chars_numeros'] == False:
                    chars_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
                    nova_senha = self.generate_password(value, chars_list)
                    print(nova_senha)
                if value['chars_especiais'] == True and value['chars_numeros'] == False:
                    chars_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%¨&*'
                    nova_senha = self.generate_password(value, chars_list)
                    print(nova_senha)
                if value['chars_especiais'] == False and value['chars_numeros'] == True:
                    chars_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'  
                    nova_senha = self.generate_password(value, chars_list)
                    print(nova_senha)

    def clear(self): # Function to clear the output
        self.window.FindElement('output').Update('')

    def generate_password(self, value, chars_list): # Function to generate the password
        try:
            value_input = int(value['total_chars']) # Converting input value to an integer
            if value_input > 7 and value_input < 101: # Checking if the number entered is less than 8 or greater than 100
                chars = random.choices(chars_list, k=int(value['total_chars'])) # Generating a random password with the 'chars_list' parameter
                new_pass = ''.join(chars) # Creating the password and saving it in a variable
                return new_pass # Returning password
            else:
                return 'Por favor, gere uma senha entre 8 a 100 caracteres.'
        except:
            return 'Por favor digite um número válido.'

gen = PassGen() # Starting the class
gen.Iniciar() # Starting the program