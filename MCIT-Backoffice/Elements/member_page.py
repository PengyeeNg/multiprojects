class Member_Element:
    member = "/html/body/div[1]/aside/section/ul/li[2]/a"  # by Xpath
    filter_add_icon = "/html/body/div[1]/div[1]/section[2]/div/form/div/div/div/div[1]/div/button"  # by Xpath
    member_name_field = "huiyuansearch-xing_ming"  # by Id
    filter_search_button = "/html/body/div[1]/div[1]/section[2]/div/form/div/div/div/div[2]/div/div[4]/div/button[1]"  # by Xpath
    filtered_results = "#w2-container > table > tbody > tr > td > div"  # by CSS

class Member_Edit_Element:
    member_edit = "/html/body/div[1]/aside/section/ul/li[2]/ul/li[1]/a"  # by Xpath
    activate_status_button = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/tbody/tr[1]/td[10]/a"  # by Xpath
    status_change_dialog_box = "huiyuan-feng_hao"  # by Id
    status_renew_button = "j-btn"  # by Id
    check_bank_button = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/tbody/tr[1]/td[11]/a"  # by Xpath
    add_bank_card_button = "/html/body/div[1]/div[1]/section[2]/div/p/a"  # by Xpath
    bank_username_field = "memberbank-bank_user_name"  # by Id
    bank_id_field = "memberbank-bank_id"  # by Id
    bank_account_field = "memberbank-bank_account"  # by Id
    bank_address_field = "memberbank-bank_address"  # by Id
    add_button = "/html/body/div[1]/div[1]/section[2]/div/div/form/div[5]/button"  # by Xpath
    last_row_bank_username = "/html/body/div[1]/div[1]/section[2]/div/div/div/div/div[3]/table/tbody/tr[last()]/td[3]"  # by Xpath
    last_row_branch_name = "/html/body/div[1]/div[1]/section[2]/div/div/div/div/div[3]/table/tbody/tr[last()]/td[4]"  # by Xpath
    last_row_bank_account = "/html/body/div[1]/div[1]/section[2]/div/div/div/div/div[3]/table/tbody/tr[last()]/td[5]"  # by Xpath
    last_row_bank_address = "/html/body/div[1]/div[1]/section[2]/div/div/div/div/div[3]/table/tbody/tr[last()]/td[6]"  # by Xpath
    edit_button = "/html/body/div[1]/div[1]/section[2]/div/div/div/div/div[3]/table/tbody/tr[last()]/td[7]/a[1]"  # by Xpath
    delete_button = "/html/body/div[1]/div[1]/section[2]/div/div/div/div/div[3]/table/tbody/tr[last()]/td[7]/a[2]"  # by Xpath
    delete_confirmation_dialog_box = "/html/body/div[5]/div/div/div[2]/div"  # by Xpath
    game_balance_button = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/tbody/tr[1]/td[12]/a"  # by Xpath
    game_balance_list = "/html/body/div[1]/div[2]/div/div/div[2]/div/div/table/thead/tr/th[1]"  # by Xpath
    game_balance_dialog_box = "/html/body/div[1]/div[2]/div/div"  #  by Xpath
    setting_button = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/tbody/tr[1]/td[13]/button"  # by Xpath
    setting_menu = "/html/body/div[6]/div[3]/a[1]"  # by Xpath
    member_information_edit_button = "/html/body/div[6]/div[3]/a[1]"  # by Xpath
    adjust_button = "/html/body/div[6]/div[3]/a[2]"  # by Xpath
    adjust_turn_over_amount_button = "/html/body/div[6]/div[3]/a[3]"  # by Xpath
    reset_password_button = "/html/body/div[6]/div[3]/a[4]"  # by XPath
    adjust_turn_over_amount_provider_button = "/html/body/div[6]/div[3]/a[5]"  # by Xpath
    inquire_button = "/html/body/form/div/div/div/div/button"  # by XPath
    member_finance_button = "/html/body/div[6]/div[3]/a[6]"  # by XPath
    member_finance_inquire_button = "w1"  # by Id
    game_history_tab = "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[1]/a"  # by XPath
    transfer_history_tab = "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[2]/a"  # by XPath
    bonus_history_tab = "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[3]/a"  # by XPath
    rebate_history_tab = "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[4]/a"  # by XPath
    deposit_history_tab = "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[5]/a"  # by XPath
    withdraw_history_tab = "/html/body/div[1]/div[2]/div/div/div[2]/div/ul/li[6]/a"  # by XPath
    export_button = "export"  # by Id
    username = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/tbody/tr[1]/td[2]"  # by XPath
    member_details = "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div[1]"  # by XPath
    username_filter = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[2]/a"  # by XPath
    affiliate_filter = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[3]/a"  # by XPath
    name_filter = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[4]/a"  # by XPath
    balance_filter = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[6]/a"  # by XPath
    member_level_id_filter = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[7]/a"  # by XPath
    # From Setting-Adjust
    member_list_navigation_link = "/html/body/div[1]/div[1]/section[1]/ul/li[2]/a"  # by Xpath

class Member_Levels_Element:
    member_levels = "/html/body/div[1]/aside/section/ul/li[2]/ul/li[2]/a"  # by Xpath
    add_member_level_button = "/html/body/div[1]/div[1]/section[2]/div/a"  # by XPath
    add_member_level_submit_button = "j-btn"  # by Id
    edit_member_level_edit_button = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/tbody/tr[1]/td[9]/a[1]"  # by XPath
    delete_member_level_button = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/tbody/tr[1]/td[9]/a[2]"  # by XPath
    setting_rebate_button = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/tbody/tr[1]/td[8]/a"  # by
    setting_rebate_submit_button = "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/form/div[2]/button"  # by XPath
    all_button_member_levels = "w0-togdata-page"  # by Id

class Member_Log_Element:
    member_log = "/html/body/div[1]/aside/section/ul/li[2]/ul/li[3]/a" # by Xpath
    member_name_filter_field = "loginlogsearch-bian_hao"  # by Id
    filter_search_button = "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/form/div[5]/button[1]"  # by XPath
    all_button = "w1-togdata-page"  # by Id
    reset_search_button = "/html/body/div[1]/div[1]/section[2]/div/div/div[1]/form/div[5]/button[2]"  # XPath
