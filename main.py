from email_sender import send_verification_code

user_email = input("Email manzilini kiriting: ")

sent_code = send_verification_code(user_email)

user_input = input("Emailga kelgan 6 xonali kodni kiriting: ")

if str(sent_code) == str(user_input):
    print("Tasdiqlandi")
else:
    print("Noto‘g‘ri kod")