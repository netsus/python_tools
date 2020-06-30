#!/home/cwjcsk/miniconda2/envs/py3/bin/python3.6
#-*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from os.path import basename
import warnings
warnings.filterwarnings("ignore")
import argparse

parser = argparse.ArgumentParser(description="Send E-amil")
parser.add_argument('-s','--subject',dest='subject', nargs='+', help='Mail Title.',required=True)
parser.add_argument('-c','--content',dest='content', nargs='+', help='Mail Contents.',required=True)
parser.add_argument('-i','--input_files',dest='files', nargs='+', help='input files to mail. if many files five space.',required=False)
args=parser.parse_args()

subject=args.subject
content=args.content
files=args.files

# 메세지 구성
msg = MIMEMultipart()
msg['Subject'] = (' ').join(subject)
msg['From'] = '[내 이메일 입력하는 곳]'
msg['To'] = '[받는 메일 입력하는 곳]'
# msg['Cc'] = 'hojaelee@naver.com'

# 파일 첨부
# files=['logo.jpg','sampleinfo.txt']
for f in files or []:
    with open(f, "rb") as fil:
        part = MIMEApplication(
            fil.read(),
            Name=basename(f)
        )
    # After the file is closed
    part['Content-Disposition'] = f'attachment; filename="{basename(f)}"'
    msg.attach(part)

# 메일 본문 첨부
msgText = MIMEText((' ').join(content), 'html') 
msg.attach(msgText)


#메일 발송
with smtplib.SMTP_SSL('smtp.naver.com') as smtp:
    smtp.login('[내 이메일 입력하는 곳]','[비밀번호 입력하는 곳]')