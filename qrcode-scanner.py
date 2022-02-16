# Instruction: 
# (1) Reads the qrcode of the client.
# (2) Prints the information about the client.
# (3) Saves information through pdf.

from fpdf import FPDF
import time
import cv2
# from pyzbar.pyzbar import decode

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
    pdf.cell(12, 1, 'CONTACT TRACING SHEET', ln=1, border=1)
    
    # Set user data.
    pdf.set_font('times', '', 12)
    for u_data in data:
        pdf.cell(0, 1, u_data, ln=1)
    name = upper(name) + ".pdf"
    pdf.output(name)
# End of func.
    
# Captures the qrcode and saves data to pdf.    
# def scan_qrcode()
# End of func.    
 
# scan_qrcode()