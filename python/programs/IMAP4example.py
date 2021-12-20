import imaplib, email

M = imaplib.IMAP4_SSL('imap.naver.com')
M.login('andycho1120@naver.com','whdudxkr')
M.select()

def findEncodingInfo(txt):    
    info = email.header.decode_header(txt)
    s, encoding = info[0]
    return s, encoding

typ, data = M.search(None, '(FROM "sosul1120@naver.com")')
for num in data[0].split():
    typ, data = M.fetch(num,'(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email)
    print('FROM:', email_message['From'])
    print('SENDER:', email_message['Sender'])
    print('TO:', email_message['To'])
    print('DATE:', email_message['Date'])
    b, encode = findEncodingInfo(email_message['Subject'])
    print('SUBJECT:', str(b, encode))
 
    #이메일 본문 내용 확인
    print('[CONTENT]')
    print('='*80)
    if email_message.is_multipart():
        for part in email_message.get_payload():        
            bytes = part.get_payload(decode = True)    
            encode = part.get_content_charset()        
            print('1', str(bytes, encode))
    print('='*80)
M.close()
M.logout()