# -*- coding:utf-8 -*-
"""cut corners script around email."""
# :copyright: (c) 2012 makoto tsuyuki.
# :license: BSD

import smtplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.Header import Header
from email.Utils import formatdate
from email import Encoders

def add_attachement(msg, attach, fname):
    file_part = MIMEBase('application', "octet-stream")
    file_part.set_payload( attachment.read() )
    Encoders.encode_base64(file_part)
    file_part.add_header('Content-Disposition', 'attachment; filename="%s"' % filename)
    body_part = MIMEText(body.encode(charset), 'plain', charset)
    msg.attach(file_part)
    msg.attach(body_part)

def send_mail(sender, sender_label, receivers, subject, body, charset,
        attachments=None, attachment=None, filename=None):
    SMTP_SERVER = ('127.0.0.1', 25)
    assert not (attachments and attachment), 'either attachements or attachement can be specified.'

    msg = None
    if attachments or attachment:
        msg = MIMEMultipart()
        if attachments:
            for attach, fname in attachments:
                add_attachement(msg, attach, fname)
        else:
            add_attachement(msg, attachment, filename)
    else:
        msg = MIMEText(body.encode(charset), 'plain', charset)
    if sender_label:
        msg['From'] = u"%s <%s>" % (str(Header(sender_name, charset)), sender)
    else:
        msg['Form'] = sender
    msg['Subject'] = Header(subject.encode(charset), charset)
    msg['To'] = ','.join(receivers)
    msg['Date'] = formatdate()
    s = smtplib.SMTP(*SMTP_SERVER)
    s.sendmail(sender, receivers, msg.as_string())
    s.close()

if __name__ == '__main__':
    from StringIO import StringIO
    csvfile1 = StringIO('''123,456\n789,101\n111,112''')
    csvfile2 = StringIO('''456,789\n101,111\n112,113''')
    receivers = ['mtsuyuki@gmail.com',]
    sender_name = u"露木 誠"
    subject = u"メール送信のテスト"
    body = u"""日本語の本文です。
    なんか書いたりする"""
    send_mail('tsuyuki@tsuyukimakoto.com', None, receivers, subject, body, 'ISO-2022-JP')#, csvfile, '20121024.csv')
    send_mail('tsuyuki@tsuyukimakoto.com', None, receivers, subject, body, 'ISO-2022-JP', csvfile1, '20121024.csv')
    send_mail('tsuyuki@tsuyukimakoto.com', None, receivers, subject, body, 'ISO-2022-JP', [(csvfile1, '20121024.csv'), (csvfile2, '20130904.csv')])
