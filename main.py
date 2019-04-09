import smtplib
import pandas
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

###############################################################################################

from_address = "me17b168@smail.iitm.ac.in"
pass_word = ""
csv_path = "big.csv"
workshop_name = "Artificial Intelligence and Reinforcement Learning"


###############################################################################################

server.login(from_address, pass_word) #username and password
csv = pandas.read_csv(csv_path) #name of csv file


print("Logged in")


num_rows = csv.shape[0]
print("Number of participants:\t %d" %num_rows)

for i in range(10,num_rows):


    row = csv.iloc[i,:]
    mail = row[1]
    if mail == " ":
        continue


    print(mail)

    message  = """
    Hii
    """
    msg = MIMEMultipart()
    msg['From']=from_address
    msg['To']= mail
    msg['Subject']="Artificial Intelligence and Reinforcement Learning | Shaastra Workshops 2019"
    
    msg.attach(MIMEText(message, 'plain'))
    server.send_message(msg)

    print("%d of %d" %(i,num_rows))
    del msg



