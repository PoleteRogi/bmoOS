import os

yn = input('Do you want to use the offline version? y/n: ')

if yn == 'n':
    try:
        os.system('py -m pip install pyqt5')
        os.system('py -m pip install PyQtWebEngine')

        print('\nLIBRARIES DOWNLOADED SUCCESSFULLY')
    except:
        print('Error trying to install dependencies from PyPi. Please try the offline version.')
elif yn == 'y':
    try:
        os.system('py -m pip install --no-index --find-link=/lib/ pyqt5')
        os.system('py -m pip install --no-index --find-link=/lib/ pyqtwebengine')

        print('\nLIBRARIES DOWNLOADED SUCCESSFULLY')
    except:
        print('Error trying to install dependencies offline. Please add an issue on the GitHub page: https://github.com/PoleteRogi/bmoOS/')
else:
    print('Please enter a valid response.')