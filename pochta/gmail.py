import smtplib
import shutil
from time import strftime
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
from config import pochta, EMAIL_FROM,  EMAIL_TO, YANDEX_PASSWORD
import pochta.gmail_app as gm_app

month, month_1 = strftime('%y'), str(int(strftime('%y')) - 1)


def gmail_bimgor():
    if gm_app.order_number():
        for zakaz in gm_app.order_number():
            gm_app.change_namber_gmail(zakaz)
            gm_app.zamena_gmail(1, zakaz)
            shutil.copyfile(f'DATA\gmail.txt', f'.\pochta\Заказы{month}.RSB')
    else:
        shutil.copyfile(f'{pochta}\Заказы{month}.RSB', f'.\pochta\Заказы{month}.RSB')

    shutil.copyfile(f'{pochta}\Заказы{month_1}.RSB', f'.\pochta\Заказы{month_1}.RSB')
    shutil.copyfile(f'{pochta}\расходы.RSB', '.\pochta\расходы.RSB')
    shutil.copyfile(f'{pochta}\dati\DAT.DB', '.\pochta\DAT.DB')
    shutil.copyfile(f'{pochta}\dati\Fasad.DB', '.\pochta\Fasad.DB')

    msg = MIMEMultipart()
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = f'Отчет за {strftime("%d.%m.%Y")}'
    msg.attach(MIMEText(f'Отчет за {strftime("%d.%m.%Y")}'))

    part1 = MIMEBase('application', "octet-stream")
    part1.set_payload(open(f".\pochta\Заказы{month}.RSB", "rb").read())
    encoders.encode_base64(part1)
    part1.add_header('Content-Disposition', 'attachment', filename=f"Заказы{month}.RSB")
    msg.attach(part1)

    part5 = MIMEBase('application', "octet-stream")
    part5.set_payload(open(f".\pochta\Заказы{month_1}.RSB", "rb").read())
    encoders.encode_base64(part5)
    part5.add_header('Content-Disposition', 'attachment', filename=f"Заказы{month_1}.RSB")
    msg.attach(part5)

    part2 = MIMEBase('application', "octet-stream")
    part2.set_payload(open(".\pochta\расходы.RSB", "rb").read())
    encoders.encode_base64(part2)
    part2.add_header('Content-Disposition', 'attachment', filename="расходы.RSB")
    msg.attach(part2)

    part3 = MIMEBase('application', "octet-stream")
    part3.set_payload(open(".\pochta\DAT.DB", "rb").read())
    encoders.encode_base64(part3)
    part3.add_header('Content-Disposition', 'attachment', filename="DAT.DB")
    msg.attach(part3)

    part4 = MIMEBase('application', "octet-stream")
    part4.set_payload(open(".\pochta\Fasad.DB", "rb").read())
    encoders.encode_base64(part4)
    part4.add_header('Content-Disposition', 'attachment', filename="Fasad.DB")
    msg.attach(part4)

    smtp = smtplib.SMTP('smtp.yandex.ru', 587)
    smtp.starttls()

    smtp.login(msg['From'], YANDEX_PASSWORD)

    smtp.sendmail(msg['From'], msg['To'], msg.as_string())
    smtp.quit()


if __name__ == '__main__':
    gmail_bimgor()
