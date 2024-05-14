import smtplib
#邮件需要专门的MINE格式
from email.mime.text import  MIMEText
#plain指普通文本格式邮件内容
msg = MIMEText('我喜欢你','plain',"utf-8")
#发件人
msg['From']='13462509350@163.com'
#收件人
msg['To']='13462509350@163.com'
#邮件的标题
msg['subject']='告白'

smtp=smtplib.SMTP_SSL('smtp.163.com')
smtp.login('13462509350@163.com','IPKXIGEGLJKJJCOO')
smtp.sendmail("13462509350@163.com","13462509350@163.com",msg.as_string())
smtp.quit()