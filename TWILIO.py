import random
from twilio.rest import Client

#configuration
password="secure123"
max_attempts=5

account_sid=""
auth_token=""
twilio_number="+"
user_phone_number="+"

user_input=""
attempts=0

while user_input!=password and attempts<max_attempts:
    try:
        user_input=input("enter the password: ")
        attempts+=1

        if user_input==password:
            print("generating OTP...")

            #generate 6-digit OTP
            otp=str(random.randint(100000,999999))

            try:
                #send otp using twilio
                client=Client(account_sid,auth_token)
                message=client.messages.create(
                    body=f"your otp is: {otp}",
                    from_=twilio_number,
                    to=user_phone_number

                )
                print("otp sent. Please check your phone.")
            except Exception as e:
                print(f"failed to send otp: {e}")
                break

            try:
                #prompt user to enter otp
                entered_otp=input("enter the otp:")
                if entered_otp==otp:
                    print("logged in")
                else:
                    print(f"incorrect otp. Access denied.")
                break
            except Exception as e:
                print(f"error while entering OTP: {e}")
                break
        elif attempts==max_attempts:
            print(f"too many failed attempts . You are locked out.")
            break
        else:
            print(f"incorrect password. You have {max_attempts-attempts}attempt(s) left")

    except Exception as e:
        print(f"an error occured: {e}")
        break
