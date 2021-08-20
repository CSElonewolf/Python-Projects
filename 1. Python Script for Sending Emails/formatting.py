def format_msg(my_name="Justin", my_website="gmail",text_format='P'):
    if text_format == 'P':
        my_msg =f"""
            Hello {my_name},
            Thank you for joining {my_website}. We are very
            happy to have you with us.This is a mail sent suing a python script.
            """
    else:
        my_msg =f"""
            <h4>Hello {my_name},</h4>
            Thank you for joining <b>{my_website}</b>.
            <i>We are very happy to have you with us.</i>
            <h5>This is a mail sent using a python script.</h5>
            """

    return my_msg