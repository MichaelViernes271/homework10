# PROGRAM: COVID TRACKING APPLICATION
# Instruction: 
# (1) Reads the qrcode of the client.
# (2) Prints the information about the client.
# (3) Saves information through pdf.

from fpdf import FPDF
import time
import cv2
from pyzbar.pyzbar import decode

# Saves data to pdf.
# Parameters:
    # name - naming the pdf file
    # data - the scanned qrcode
def save_pdf(name, data):
    
    pdf = FPDF('p', 'cm', 'A4')
    pdf.add_page()
    pdf.set_margin(2)
    
    # Set title.
    pdf.set_font('times', 'B', 16)
    pdf.set_text_color(100,100,255)
    pdf.cell(20, 1, 'CONTACT TRACING SHEET', ln=1, border=1)
    
    # Set user data.
    pdf.set_font('times', '', 12)
    pdf.set_text_color(0,0,0)
    for u_data in data:
        pdf.cell(0, 1, u_data, ln=1)
    name = name.upper() + ".pdf"
    pdf.output(name)
    
    print('PDF SAVED!')
# End of func.
    
# Captures the qrcode and saves data to pdf.    
def scan_qrcode():
    qrcode = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    qrcode.set(3, 640)
    qrcode.set(4, 480)

    cam = True
    while cam == True:
        success, frame = qrcode.read() # not needed success variable 
        
        for user_data in decode(frame):
            print("""
            =====================
            SCANNED SUCCESSFULLY!
            =====================
            
            """)
            userinfo = user_data.data.decode('utf-8')
            print('Type of Code: ', user_data.type,'\n')    
            print(userinfo)
            userinfo = userinfo.split('\n')
            print('\n\n')
            pdf = input('Name saved data: ')
            save_pdf(str(pdf), userinfo)
            time.sleep(3)
            cam = False
            
        cv2.imshow("QRCODE SCANNER", frame)    
        cv2.waitKey(1)
# End of func.    
 
def main():
    scan_qrcode()
# End of function.

while True: # My template for usual main().
    main()
    quit = input("Quit (y/n): ")
    if quit is type(str):
        quit = quit.lower()
        print(quit)
    if (quit == 'y' or quit == 0):
        print("Closing...\n")    
        break
# End of Func.

exit() # Exits program.