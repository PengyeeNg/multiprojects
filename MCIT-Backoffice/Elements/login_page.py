class Login_Element:
    page_logo = "/html/body/div[1]/div[1]/a"  # by Full Xpath
    username = "loginform-username"  # by Id
    password = "loginform-password"  # Id
    log_in_button = "login-button"  # by Name
    incorrect_password_prompt = "#login-form > div.form-group.has-feedback.field-loginform-password.required.has-error > p"  # by CSS
    blank_password_prompt = "#login-form > div.form-group.has-feedback.field-loginform-password.required.has-error > p"  # by CSS
    blank_username_prompt = "#login-form > div.form-group.has-feedback.field-loginform-username.required.has-error > p"  # by CSS
    remember_me_checkbox = "loginform-rememberme"  # By CSS