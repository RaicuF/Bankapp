# function auth
#
# from reportlab.pdfgen.canvas import Canvas
#
# canvas = Canvas("./Stament.pdf")
# canvas.setFont("Helvetica", 30)
# canvas.drawString(50, 800, "Bank Statement")
# canvas.setFont("Times-Bold", 12)
#
# informatii = ['Name - Florin Raicu', 'Adress - Two Mile Ash', 'Town - Milton Keynes', 'Postcode - MK88EU']
# x = 30
# y = 700
# canvas.setFont("Times-Italic", 12)
# for informatie  in informatii:
#     canvas.drawString(x, y, informatie)
#     y -= 15
#
# bank_info = ['Contact tel - 034887733', 'Text phone - 030043437', 'www.hbb.co.uk']
# x = 400
# y = 700
# canvas.setFont("Times-Italic",12)
# for bank in bank_info:
#     canvas.drawString(x,y, bank)
#     y -= 15
# account_option = ['Opening Balance - ', 'Paymennts In', 'Payments Out', 'Closing Balance']
# x = 400
# y = 630
# canvas.setFont("Times-Italic",12)
# for option in account_option:
#     canvas.drawString(x,y, option)
#     y -= 15
# date_option = ['19 March to 18 April 2021',
#
#                'Account Name - Florin Raicu']

# canvas.save()


dictionar_utilizatori = {}
file_auth = open('users.json', 'r')
file_auth.close()


def utilizatori(password):
    for user in dictionar_utilizatori.keys():
        if dictionar_utilizatori[user] == password:
            print('Login successful')
            return True
        else:
            return 'Wrong password'
    else:
        return 'Invalid password'


dictionar_utilizatori.keys()
