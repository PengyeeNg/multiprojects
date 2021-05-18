class SignUppageElement:
    username_field = "/html/body/div[2]/div[1]/div/div/div/div/div/div[1]/span/form/span[1]/div/div/input"  # by XPath
    mobile_phone_field = "nested-hp-input-4"  # by ID
    email_field = "nested-hp-input-5"  # by ID
    password_field = "/html/body/div[2]/div[1]/div/div/div/div/div/div[1]/span/form/span[2]/div/div/input"  # by XPath
    confirm_password_field = "nested-pw-input-3"  # by ID
    invitation_code_field = "nested-invite-input-6"  # by ID
    sign_up = "#__layout > div > div.header-div > nav.navbar.navbar-light.navbar-expand > ul > li > form > span > button:nth-child(5)"  # by CSS
    sign_up_button = "/html/body/div[2]/div[1]/div/div/div/div/div/div[1]/span/form/button[1]"  # by XPath
