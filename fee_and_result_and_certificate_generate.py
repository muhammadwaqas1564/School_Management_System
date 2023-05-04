from reportlab.lib.pagesizes import landscape, letter
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileMerger
import datetime
from time import strftime
import io
import os

#--------- link with database
import pymysql
conn = pymysql.connect(host="localhost",
                                user="root",
                                password="",
                                database="CMS"
)
courser =conn.cursor()





pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))


# =====================================================================
# ============================================  generate fee slip
def generatre_feeslip(data):
    # -----------------------------  claculate Due Date
    d,m,y = data[0][0].split("/")
    # print(d,m,y)
    d = int(d)+7
    # print(d)
    if d>30:
        d = d%30
        m = int(m)+1
    if int(m)>12:
        m = int(m)%12
        y = int(y)+1
    Due_Date = str(d)+"/"+str(m)+"/"+str(y)
    # print(Due_Date)
    # --------------------------------------------------
    pdf_files = []
    for i in data:
        pic_path = f"picture//{i[2]}_{i[3]}_{i[1]}.jpg"

        packet = io.BytesIO()       
        can = canvas.Canvas(packet, pagesize=(landscape(letter)))

        if os.path.exists(pic_path):
           can.drawImage(pic_path, 471, 348,68,70)
        else:
            can.drawString(495, 390,"No")
            can.drawString(485, 375,"Picture")
        can.setFont("VeraIt",11)
        can.drawString(190, 346,str(i[0]))
        can.drawString(365, 346,str(Due_Date))
        can.drawString(275, 298,str(i[1]))
        can.drawString(78, 320,str(i[2]+" "+i[3]))
        can.drawString(295, 320,str(i[4]))
        can.drawString(485, 320,str(i[5]))
        can.drawString(95, 298,str(i[6]))
        
        can.setFont("Vera",11)
        can.drawString(475, 253,str(i[7]))
        can.drawString(475, 236,str(i[8]))
        can.drawString(475, 219,str(i[9]))
        can.drawString(475, 202,str(i[10]))
        can.drawString(475, 185,str(i[11]))
        can.drawString(475, 168,str(i[12]))
        can.drawString(475, 151,str(i[13]))
        can.drawString(475, 136,str(i[14]))
        can.drawString(475, 117,str(i[15]))

        if os.path.exists(pic_path):
            can.drawImage(pic_path, 744, 282,69,71)
        else:
            can.drawString(765, 340,"No")
            can.drawString(755, 326,"Picture")

        can.setFont("VeraIt",9)        
        can.drawString(580, 350,str(i[2]+" "+i[3]))
        can.drawString(580, 333,str(i[4]))
        can.drawString(620, 314,str(i[5]))
        can.drawString(630, 296,str(i[6]))
        can.drawString(626, 278,str(i[1]))

        can.drawString(720, 243,str(i[0]))
        can.drawString(720, 226,str(Due_Date))

        can.drawString(725, 167,str(i[7]))
        current_fee = int(i[15])- int(i[7])
        can.drawString(725, 150,str(current_fee))
        can.drawString(725, 133,str(i[15]))
       
        can.showPage()
        can.save()

        #------------------------- move to the beginning of the StringIO buffer
        packet.seek(0)
        
        #------------------------- create a new PDF with Reportlab
        new_pdf = PdfFileReader(packet)
        
        #------------------------- read your existing PDF
        existing_pdf = PdfFileReader(open("Fee Slip.pdf", "rb"))
        output = PdfFileWriter()
        
        #------------------------- add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

        #-------------------------- finally, write "output" to a real file    
        outputStream = open(f"{i[2]}_{i[3]}_{i[1]}.pdf", "wb")
        pdf_files.append(f"{i[2]}_{i[3]}_{i[1]}.pdf")
        output.write(outputStream)
        outputStream.close()

    # ----------------------------------   merge th all pdf file to convert one file
    merger = PdfFileMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    
    Today_date = datetime.date.today()
    merger.write(f"Fee_{Today_date}_{data[0][5]}.pdf")
    merger.close()

    #----------------------------------- remove the the pdf files
    for i in pdf_files:
        os.system(f"rm -rf {i}")

    return f"Fee_{Today_date}_{data[0][5]}.pdf"



# =====================================================================
# ============================================  generate cresult

promotion_student_data = []
def generatre_result(data):
    pdf_files = []
    term = data[0][0][6]
    total_marks = 0
    obtain_marks = 0
    status = []
    for i in data:
        packet = io.BytesIO()       
        can = canvas.Canvas(packet, pagesize=(landscape(letter)))
        count=0
        space=310
        for j in i:
            if count==0:
                pic_path = f"picture//{j[1]}_{j[2]}_{j[0]}.jpg"
                if os.path.exists(pic_path):
                    can.drawImage(pic_path, 730, 482,75,76)
                Today_date = datetime.date.today()
                can.setFont("Vera",12)
                can.drawString(80, 448,"KASS/-2529")
                can.drawString(315, 448,str(j[6]+" "+"Term"))
                can.drawString(570, 448,str(Today_date))

                can.drawString(90, 405,str(j[0]))
                can.drawString(80, 427,str(j[1]+" "+j[2]))
                can.drawString(295, 427,str(j[3]))
                can.drawString(480, 427,str(j[4]))
                can.drawString(590, 427,str(j[5]))    

                can.drawString(170, 340,str(j[7]))
                can.drawString(410, 340,str(j[8]))
                can.drawString(560, 340,str(j[9]))
                can.drawString(710, 340,str(j[10]))
                count = count+1
                total_marks = total_marks+ int(j[8])
                obtain_marks = obtain_marks+int(j[9])
                status.append(j[10])
            else:
                can.drawString(170, space,str(j[7]))
                can.drawString(410, space,str(j[8]))
                can.drawString(560, space,str(j[9]))
                can.drawString(710, space,str(j[10]))
                total_marks = total_marks+int(j[8])
                obtain_marks = obtain_marks+int(j[9])
                status.append(j[10])
                space=space-30
        can.drawString(410,128 ,str(total_marks))
        can.drawString(560,128 ,str(obtain_marks))

        if "Fail" in status:
            can.drawString(710,128 ,"Fail")
            promotion_student_data.append([j[0],"Fail"])
        else:
            can.drawString(710,128 ,"Pass")
            promotion_student_data.append([j[0],"Pass"])
        
        per = (obtain_marks/total_marks)*100
        
        can.drawString(685,78,str(per.__round__(2))+" %")
        can.showPage()
        can.save()
        # ------------------  to clear the status of the first student for the next student
        status.clear()
        #------------------------- move to the beginning of the StringIO buffer
        packet.seek(0)
        #------------------------- create a new PDF with Reportlab
        new_pdf = PdfFileReader(packet)
        #------------------------- read your existing PDF
        existing_pdf = PdfFileReader(open("Result.pdf", "rb"))
        output = PdfFileWriter()
        #------------------------- add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))

        output.addPage(page)
        #-------------------------- finally, write "output" to a real file
        
        outputStream = open(f"{i[0][1]}_{i[0][2]}_{i[0][0]}.pdf", "wb")
        pdf_files.append(f"{i[0][1]}_{i[0][2]}_{i[0][0]}.pdf")
        output.write(outputStream)
        outputStream.close()

    # ----------------------------------   merge th all pdf file to convert one file
    merger = PdfFileMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    
   
  
    merger.write(f"Result_{Today_date}_{term}_term.pdf")
    merger.close()

    # ----------------------------------  print the status and registeration no of student
    # print(promotion_student_data)
    #----------------------------------- remove the the pdf files
    for i in pdf_files:
        os.system(f"rm -rf {i}")
    
    return f"Result_{Today_date}_{term}_term.pdf",promotion_student_data


# =====================================================================
# ===================================  generate result of one student
def generatre_result_one(data):
    pdf_files = []
    total_marks = 0
    obtain_marks = 0
    status = []
    count=0
    space=310
    packet = io.BytesIO()       
    can = canvas.Canvas(packet, pagesize=(landscape(letter)))
    for i in data:
        if count==0:
            pic_path = f"picture//{i[1]}_{i[2]}_{i[0]}.jpg"
            if os.path.exists(pic_path):
                can.drawImage(pic_path, 730, 482,75,76)
            Today_date = datetime.date.today()
            can.setFont("Vera",12)
            can.drawString(80, 448,"KASS/-2529")
            can.drawString(315, 448,str(i[6]+" "+"Term"))
            can.drawString(570, 448,str(Today_date))

            can.drawString(90, 405,str(i[0]))
            can.drawString(80, 427,str(i[1]+" "+i[2]))
            can.drawString(295, 427,str(i[3]))
            can.drawString(480, 427,str(i[4]))
            can.drawString(590, 427,str(i[5]))    

            can.drawString(170, 340,str(i[7]))
            can.drawString(410, 340,str(i[8]))
            can.drawString(560, 340,str(i[9]))
            can.drawString(710, 340,str(i[10]))
            count = count+1
            total_marks = total_marks+ int(i[8])
            obtain_marks = obtain_marks+int(i[9])
            status.append(i[10])
        else:
            can.drawString(170, space,str(i[7]))
            can.drawString(410, space,str(i[8]))
            can.drawString(560, space,str(i[9]))
            can.drawString(710, space,str(i[10]))
            total_marks = total_marks+int(i[8])
            obtain_marks = obtain_marks+int(i[9])
            status.append(i[10])
            space=space-30
        
    can.drawString(410,128 ,str(total_marks))
    can.drawString(560,128 ,str(obtain_marks))

    if "Fail" in status:
        can.drawString(710,128 ,"Fail")
    else:
        can.drawString(710,128 ,"Pass")
    per = (obtain_marks/total_marks)*100
        
    can.drawString(685,78,str(per.__round__(2))+" %")
    can.showPage()
    can.save()

    #------------------------- move to the beginning of the StringIO buffer
    packet.seek(0)
    
    #------------------------- create a new PDF with Reportlab
    new_pdf = PdfFileReader(packet)
    
    #------------------------- read your existing PDF
    existing_pdf = PdfFileReader(open("Result.pdf", "rb"))
    output = PdfFileWriter()
    
    #------------------------- add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)

    #-------------------------- finally, write "output" to a real file
    outputStream = open(f"Result_{i[1]}_{i[2]}_{i[0]}.pdf", "wb")
    pdf_files.append(f"Result_{i[1]}_{i[2]}_{i[0]}.pdf")
    output.write(outputStream)
    outputStream.close()

    return pdf_files



# =====================================================================
# ==============================  generate certificate of one student
def generatre_certificate(data):
    for i in data:
        Today_date = datetime.date.today()
        packet = io.BytesIO()       
        can = canvas.Canvas(packet)
            
        can.setFont("VeraIt",18)
        can.drawString(240, 311,str(i[0]+" "+i[1]))
        can.drawString(520, 311,str(i[2]))
        can.drawString(670, 280,str(i[3]))
        can.drawString(300, 250,str(i[4]))
        can.drawString(50, 103,str(Today_date))

        pic_path = f"Images//signature.png"
        if os.path.exists(pic_path):
            can.drawImage(pic_path, 670, 105,75,76)
       
        can.showPage()
        can.save()

        #------------------------- move to the beginning of the StringIO buffer
        packet.seek(0)
        #------------------------- create a new PDF with Reportlab
        new_pdf = PdfFileReader(packet)
        #------------------------- read your existing PDF
        existing_pdf = PdfFileReader(open("Certificate.pdf", "rb"))
        output = PdfFileWriter()
        #------------------------- add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))

        output.addPage(page)
        #-------------------------- finally, write "output" to a real file
        path=[]
        outputStream = open(f"{i[0]}_{i[1]}_Certificate.pdf", "wb")
        path.append(f"{i[0]}_{i[1]}_Certificate.pdf")
        output.write(outputStream)
        outputStream.close()
    return path




# =====================================================================
# ===========================================  generate certificate
def generatre_certificate_of_class(data):
    pdf_files_cert = []
    for i in data:
        Today_date = datetime.date.today()
        packet = io.BytesIO()       
        can = canvas.Canvas(packet)
            
        can.setFont("VeraIt",18)
        can.drawString(240, 311,str(i[0]+" "+i[1]))
        can.drawString(520, 311,str(i[2]))
        can.drawString(670, 280,str(i[3]))
        can.drawString(300, 250,str(i[4]))
        can.drawString(50, 103,str(Today_date))

        pic_path = f"Images//signature.png"
        if os.path.exists(pic_path):
            can.drawImage(pic_path, 670, 105,75,76)
       
        can.showPage()
        can.save()

        #------------------------- move to the beginning of the StringIO buffer
        packet.seek(0)
        #------------------------- create a new PDF with Reportlab
        new_pdf = PdfFileReader(packet)
        #------------------------- read your existing PDF
        existing_pdf = PdfFileReader(open("Certificate.pdf", "rb"))
        output = PdfFileWriter()
        #------------------------- add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))

        output.addPage(page)
        #-------------------------- finally, write "output" to a real file
        outputStream = open(f"{i[0]}_{i[1]}_Certificate.pdf", "wb")
        pdf_files_cert.append(f"{i[0]}_{i[1]}_Certificate.pdf")
        output.write(outputStream)
        outputStream.close()



    # ----------------------------------   merge th all pdf file to convert one file
    merger = PdfFileMerger()
    for pdf in pdf_files_cert:
        merger.append(pdf)
    
    merger.write(f"Class_{i[4]}_Certificate.pdf")
    merger.close()
    
    path = f"Class_{i[4]}_Certificate.pdf"
    # ----------------------------------  print the status and registeration no of student
    # print(promotion_student_data)
    #----------------------------------- remove the the pdf files
    for i in pdf_files_cert:
        os.system(f"rm -rf {i}")
    
    return path



