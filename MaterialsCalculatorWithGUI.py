# Author: Ryan Reyes, github.com/techproofreader
# Program Name: Materials Cost Calculator
# Version: 1.0

import PySimpleGUI as sg

menu_def = [['File', ['About']]
            ]
     
layout = [ [sg.Menu(menu_def, tearoff=False)],
           [sg.Txt('Enter your project\'s information to calculate total materials cost', font=("Zapfino", 15), text_color="darkBlue", background_color="beige")],      
           [sg.In(size=(20, 1), key='length', justification="center", font=("Zapfino", 10)), sg.T('Length', font="Zapfino", background_color="beige")],        
           [sg.In(size=(20, 1), key='width', justification="center", font=("Zapfino", 10)), sg.T('Width', font="Zapfino", background_color="beige")],
           [sg.In(size=(20, 1), key='unit cost', justification="center", font=("Zapfino", 10)), sg.T('Cost Per Unit (Ex: per sq-ft)', font="Zapfino", background_color="beige")],
           [sg.In(size=(20, 1), key='sales tax', justification="center", font=("Zapfino", 10)), sg.T('Sales Tax (% form)', font="Zapfino", background_color="beige")],      
           [sg.Txt('', size=(20, 1), key='output', font="Zapfino", background_color="beige") ],
           [sg.Button('Click For Total Cost', font="Zapfino", bind_return_key=True)]]      
     
window = sg.Window('Materials Cost Calculator', layout, background_color="beige")      
     
while True:
    event, values = window.Read()     

    if event == 'About':
        sg.Popup('Author: Ryan Reyes, https://github.com/TechProofreader',
                 'Program Name: Materials Cost Calculator',
                 'Version: 1.0',
                 'The GUI of this program was created with the PySimpleGUI Framework',
                 'PySimpleGUI is licensed under the GNU Lesser General Public License v3.0',
                 'The creator of PySimpleGUI is: https://github.com/MikeTheWatchGuy',
                 'This "Materials Cost Calculator" is licensed under the GNU Lesser General Public License v3.0', font="Herculanum", text_color="Purple", background_color="beige")
    
    elif event is not None:      
        try:

            salesTax = ((abs(float(values['sales tax']))/100)+1)
            area = abs((float(values['length'])*float(values['width'])))  
            totalCost = abs((float(values['unit cost'])*area))
            totalCostWithTax = abs(round(totalCost*salesTax, 2))
                
        except:

            totalCostWithTax = 'Numbers only, please :)'    
     
        window.Element('output').Update(totalCostWithTax)      
    else:
        break
