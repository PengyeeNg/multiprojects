class MainPage_Element:
    main_page_title = "/html/body/div[1]/aside/section/ul/li[1]/a"  # by Xpath
    username_dropdown = "/html/body/div[1]/header/nav/div/ul/li[3]/a"  # by Xpath
    username_dropdown_menu = "/html/body/div[1]/header/nav/div/ul/li[3]/ul/li[1]"  # by Xpath
    log_out_button = "/html/body/div[1]/header/nav/div/ul/li[3]/ul/li[2]/div[2]/a"  # by Xpath
    change_password_button = "/html/body/div[1]/header/nav/div/ul/li[3]/ul/li[2]/div[1]/a"  # by Xpath
    change_button = "/html/body/div[1]/div[1]/section[2]/div/div/div/form/div[4]/button"  # by CSS
    old_password = "changepassword-oldpassword"  # by Id
    new_password = "changepassword-newpassword"  # by Id
    retype_password = "changepassword-retypepassword"  # by Id
    incorrect_old_password_prompt = "#form-change > div.form-group.field-changepassword-oldpassword.required.has-error > p"  # by CSS
    incorrect_retype_password_prompt = "#form-change > div.form-group.field-changepassword-retypepassword.required.has-error > p"  # by CSS
    blank_old_password_prompt = "#form-change > div.form-group.field-changepassword-oldpassword.required.has-error > p"  # by CSS
    blank_new_password_prompt = "#form-change > div.form-group.field-changepassword-newpassword.required.has-error > p"  # by CSS
    blank_retype_password_prompt = "#form-change > div.form-group.field-changepassword-retypepassword.required.has-error > p" # by CSS
    number_online_member = "body > div.wrapper > header > nav > div > ul > li:nth-child(1) > a > span"  # by CSS
    online_member_icon = "/html/body/div[1]/header/nav/div/ul/li[1]/a"  # by Xpath
    online_member_menu = "/html/body/div[1]/header/nav/div/ul/li[1]/ul/li/div/ul/li/a"  # by Xpath
    online_member_dropdown = "/html/body/div[1]/header/nav/div/ul/li[1]/ul/li/div/ul/li/a"  # by XPath
    member_list_page = "/html/body/div[1]/div[1]/section[1]/h1"  # by Xpath
    total_online_member = "#w2 > div > div.kv-panel-before > div:nth-child(2) > div > div > div > b:nth-child(2)"  # by CSS
    notification_icon = "/html/body/div[1]/header/nav/div/ul/li[2]/a"  # by XPath
    notification_menu = "/html/body/div[1]/header/nav/div/ul/li[2]/ul/li/div"  # by XPath
    chong_zhi_records = "/html/body/div[1]/header/nav/div/ul/li[2]/ul/li/div/ul/li[1]/a"  # by XPath
    withdrawal_records = "/html/body/div[1]/header/nav/div/ul/li[2]/ul/li/div/ul/li[2]/a"  # by XPath
    new_file_records = "/html/body/div[1]/header/nav/div/ul/li[2]/ul/li/div/ul/li[3]/a"  # by XPath
    bank_balance_records = "/html/body/div[1]/header/nav/div/ul/li[2]/ul/li/div/ul/li[4]/a"  # by XPath
    no_online_member = "#w2-container > table > tbody > tr > td > div"  # by CSS

class General_Element:
    all_button = "btn-default"  # by Class Name
    delete_confirmation_dialog_box = "bootstrap-dialog-title"  # by Class Name
    filter_search_button = "glyphicon-search"  # by Class Name
    scroll_to_bottom = "yii-debug-toolbar__bar" # by Class Name

