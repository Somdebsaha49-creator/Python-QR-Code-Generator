import qrcode
print('')
print('Hello👋😄, Welcome to my qrcode creator code :)')
print('')
item=input('Enter anything like Plain Text, Numbers, URL (Website Link), Contact Information (vCard..please enter it in string format in one line), Wi-Fi Credentials, Payment Information (UPI/PayPal/etc.), Binary / Custom Encoded Data, etc., but in one line📌: ')
qrcode.make(item).save("qrcode.png")
print('')
print('😄 qrcode generated✅, please check :)')
print('')