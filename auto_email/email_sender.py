import smtplib
import os
from email.message import EmailMessage  # for setting the message variable easier
import imghdr

EMAIL_PASSWORD = os.environ.get('PY_EMAIL_PASS')
service_providers = {
    'gmail': "smtp.gmail.com",
    'hotmail': "smtp.live.com",
    'yahoo': "smtp.mail.yahoo.com"
}

my_email = 'vgsoftware.yahoo.com'
password = 'tvwhwjmaxsxxczut'  # 'vitismanXd2019'
address = 'victor@swappie.com'
mensaje = 'Hello\nThis is an atomated email test.'


def letter_handler(names_invited, name_of_document, common_text_letter):
    """args: names_invited must be a path to a txt of names in different lines,
            name_of_document is a raw string,
            common_text_letter is the path to a txt document.(document should place hold names as "[name]" )
    """
    with open(names_invited, 'r') as guess_list:
        for guess in guess_list.readlines():
            guess = guess.strip()
            file_name = f'./ReadyToSend_{name_of_document}/{name_of_document}{guess}.txt'
            with open(file_name, 'w') as letter:
                with open(common_text_letter, 'r') as text:
                    invitation = text.read()
                    final_invitation = invitation.replace('[name]', guess)

                letter.write(final_invitation)


def send_email(subject, from_address, to_address, content, sender_password, attachments=None):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address
    msg.set_content(content)

    # attaching a image
    if attachments:
        for attachment in attachments:
            with open(attachment, 'rb') as f:
                file_data = f.read()
                file_name = f.name
                if 'pdf' not in file_name:
                    file_type = imghdr.what(f.name)
                    main_type = 'image'
                else:
                    file_type = 'octet-stream'
                    main_type = 'application'

            msg.add_attachment(file_data, maintype=main_type, subtype=file_type, filename=file_name)

    # SSL connection more simple
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        # no need to identify to server
        smtp.login(from_address, sender_password)

        # change method
        smtp.send_message(msg)


def auto_email(from_email, to_email, text):
    for provider in service_providers:
        if provider in from_email:
            with smtplib.SMTP(service_providers[provider], 465) as connection:
                connection.starttls()
                connection.login(user=from_email, password=password)
                connection.sendmail(from_addr=from_email, to_addrs=to_email, msg=text)
        else:
            print('service provider not found')
