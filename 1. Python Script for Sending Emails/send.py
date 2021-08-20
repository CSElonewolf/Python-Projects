import sys
from formatting import format_msg
from send_email import send_email

# formats the given details and finally sends the mail
def send(name, website=None,sub=None, to_emails_list=None, verbose=False,text_format='P'):
    assert to_emails_list != None

    if website != None:
        formatted_msg = format_msg(my_name=name, my_website=website,text_format=text_format)
    else:
        formatted_msg = format_msg(my_name=name,text_format=text_format)

    if verbose:
        print(name, website, to_emails_list)

    # Passing on the formatted message with details 
    try:
        send_email(text_body=formatted_msg,subject=sub, to_emails=to_emails_list.split(','))
        sent = True
    except:
        sent = False
    return sent

if __name__ == "__main__":
    name = input("Enter Your Name: ")
    subject = input("Enter the subject: ")
    website = input("Would you like to add an website::")
    list_of_to_emails = input("Enter the emails separated by ',':")
    text_format = input("Press 'H' for html format or 'P' for plain text format: " )

# pass the detials for formatting
    response = send(name,sub= subject,website=website, to_emails_list=list_of_to_emails, verbose=True,text_format = text_format)

# final status of the mail 
    if response == True:
        print("Email sent!")
    else:
        print("Email not sent!!")