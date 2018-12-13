import smtplib
import pandas
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

###############################################################################################

from_address = "dopamine_workshop@shaastra.org"
pass_word = "isitencrypted"
csv_path = "Artificial"
workshop_name = "Artificial Intelligence and Reinforcement Learning"
link_address = "https://www.techgig.com/hackathon/iamai"

###############################################################################################

server.login(from_address, pass_word) #username and password
csv = pandas.read_csv(csv_path) #name of csv file


print("Logged in")


num_rows = csv.shape[0]
print("Number of participants:\t %d" %num_rows)
fp = open("cache.txt" , 'r')
txt = fp.read()
txt = int(txt)
print(txt)
fp.close()
fp = open("cache.txt" ,'w')
for i in range(txt,609):
    fp.seek(0,0)
    fp.write(str(i))
    fp.flush()
    row = csv.iloc[i,:]
    mail = row[3]
    name = row[1].lower()
    parts = name.split(" ")
    name = " "
    for part in parts:
        part = part.capitalize() + " "
        name = name + part
    message = "Hi" + name + """,
Greetings from Shaastra 2019.

You have successfully registered for """ + workshop_name + """ Workshop. To confirm your selection for the workshop, please take the screening test in the link provided below.

""" + link_address +

"""

Important Details about Registration:
1. The earlier you take the test and submit the answers, earlier you get the confirmation to attend the workshop if you are selected.
2. Make sure you enter your Shaastra ID correctly in the required field in the test link.
3. If the workshop mentions any fees in the Shaastra website, you will be provided with the payment link once you are selected for the workshop.

If you have any queries, please be free to contact us through dopamine_workshop@shaastra.org
Thanks and Regards,
Workshop Team,
Shaastra 2019 """
    msg = MIMEMultipart()
    # message = "Blah. This is send from a bot"
    msg['From']=from_address
    msg['To']= mail
    msg['Subject']="Artificial Intelligence and Reinforcement Learning | Shaastra Workshops 2019"
    
    msg.attach(MIMEText(message, 'plain'))
    server.send_message(msg)

    print("%d of %d" %(i,num_rows))
    del msg

    # print(message)

