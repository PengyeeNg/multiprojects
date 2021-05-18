class Deposit_Withdraw_Element:
    deposit_withdraw = "/html/body/div[1]/aside/section/ul/li[4]/a"  # by XPath
    filter_add_button = "btn-box-tool"  # by Class Name
    username_filter_field = "rechargesearch-username"  # by Id
    filter_search_button = "glyphicon-search"  # by Class Name
    no_results_found = "empty"  # by Class name
    select_column_button = "w2-cols"  # By Id
    select_columns = "kv-toggle-all"  # By Class Name
    export_button = "w4"  # Id
    html_button = "export-full-html"  # By Class Name
    export_confirmation_ok_button = "btn-warning"  # by Class Name
    all_button = "btn-default"  # by Class Name
    reset_search_button = "glyphicon-refresh"  # by Class Name

class Deposit_Element:
    deposit = "/html/body/div[1]/aside/section/ul/li[4]/ul/li[1]/a"  # by XPath
    topup_amount_header_sorting = "/html/body/div[1]/div/section[2]/div[2]/div/div/div[4]/table/thead/tr/th[3]/a"  # by XPath
    submit_period_header_sorting = "/html/body/div[1]/div/section[2]/div[2]/div/div/div[4]/table/thead/tr/th[7]/a"  # by XPath
    approval_time_header_sorting = "/html/body/div[1]/div/section[2]/div[2]/div/div/div[4]/table/thead/tr/th[8]/a"  # by XPath
    status_header_sorting = "/html/body/div[1]/div/section[2]/div[2]/div/div/div[4]/table/thead/tr/th[11]/a"  # by XPath
    lock_button = "fa-lock"  # by Class Name
    lock_confirmation_ok_button = "btn-warning"  # by Class Name
    deal_button = "check-btn"  # by Class Name
    deal_save_button = "bc"  # by Class Name
    all_button = "w2-togdata-page"  # by ID

class Deposit_History_Element:
    deposit_history = "/html/body/div[1]/aside/section/ul/li[4]/ul/li[2]/a"  # by XPath
    topup_amount_header_sorting = "/html/body/div[1]/div/section[2]/div[2]/div/div/div[4]/table/thead/tr/th[3]/a"  # by XPath
    submit_period_header_sorting = "/html/body/div[1]/div/section[2]/div[2]/div/div/div[4]/table/thead/tr/th[7]/a"  # by XPath
    approval_time_header_sorting = "/html/body/div[1]/div/section[2]/div[2]/div/div/div[4]/table/thead/tr/th[8]/a"  # by XPath
    status_header_sorting = "/html/body/div[1]/div/section[2]/div[2]/div/div/div[4]/table/thead/tr/th[11]/a"  # by XPath
    lock_button = "fa-lock"  # by Class Name
    lock_confirmation_ok_button = "btn-warning"  # by Class Name
    deal_button = "check-btn"  # by Class Name
    deal_save_button = "bc"  # by Class Name
    all_button = "w6-togdata-page"  # by Id

class Withdrawal_Element:
    withdrawal = "/html/body/div[1]/aside/section/ul/li[4]/ul/li[3]/a"  # by XPath
    username_filter_field = "withdrawsearch-username"  # by Id
    withdraw_type_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[2]/div/div[3]/table/thead/tr/th[3]/a"  # by XPath
    withdrawal_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[2]/div/div[3]/table/thead/tr/th[5]/a" # by XPath
    withdrawal_time_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[2]/div/div[3]/table/thead/tr/th[6]/a"  # by XPath
    status_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[2]/div/div[3]/table/thead/tr/th[7]/a"  # by XPath
    lock_withdrawal_button = "qxiao"  # by Class Name
    locked_withdrawal_button = "suoding"  # by Class Name
    deal_withdrawal_button = "fa-check"  # by Class Name
    deal_confirmation_submit_button = "submitwithdrawal"  # by Id
    all_button = "w2-togdata-page"  # by Id

class Withdraw_History_Element:
    withdraw_history = "/html/body/div[1]/aside/section/ul/li[4]/ul/li[4]/a"  # by XPath
    username_filter_field = "withdrawsearch-username"  # by Id
    all_button = "w6-togdata-page"  # by ID
    withdraw_type_header_sorting =  "/html/body/div[1]/div[1]/section[2]/div/div[3]/div/div[2]/div/div[3]/table/thead/tr/th[3]/a"  # by XPath
    withdrawal_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[3]/div/div[2]/div/div[3]/table/thead/tr/th[5]/a"  # by XPath
    withdrawal_time_header_sorting =  "/html/body/div[1]/div[1]/section[2]/div/div[3]/div/div[2]/div/div[3]/table/thead/tr/th[6]/a"  # by XPath
    approval_time_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[3]/div/div[2]/div/div[3]/table/thead/tr/th[7]/a" # by XPath
    status_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[3]/div/div[2]/div/div[3]/table/thead/tr/th[8]/a" # by XPath
    reason_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[3]/div/div[2]/div/div[3]/table/thead/tr/th[9]/a" # by XPath

class Adjust_Balance_Element:
    adjust_balance= "/html/body/div[1]/aside/section/ul/li[4]/ul/li[5]/a"  # by XPath
    deposite_yes_button = "btn-success"  # by Class Name
    deposite_confirmation_ok_button = "btn-warning"  # by Class Name
    member_list_navigation_link = "/html/body/div[1]/div[1]/section[1]/ul/li[2]/a"  # by XPath


class Account_Transaction_Record_Element:
    account_transaction = "/html/body/div[1]/aside/section/ul/li[4]/ul/li[6]/a"  # by XPath
    export_blue_button = "glyphicon-export"  # by Class Name
    export_blue_confirmation_ok_button = "btn-warning"  # by Class Name
    member_name_filter_field = "zhanghujilusearch-xing_ming"  # by ID
    select_column_button = "w1-cols"  # By Id
    export_button = "w3"  # Id
    username_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[3]/div/div[3]/table/thead/tr/th[2]/a"  # XPath
    name_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[3]/div/div[3]/table/thead/tr/th[3]/a"  # by XPath
    deposit_account_type_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[3]/div/div[3]/table/thead/tr/th[4]/a"  # by XPath
    type_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[3]/div/div[3]/table/thead/tr/th[5]/a"  # by XPath
    related_username_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[3]/div/div[3]/table/thead/tr/th[6]/a"  # by XPath
    original_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[3]/div/div[3]/table/thead/tr/th[7]/a"  # by XPath
    changes_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[3]/div/div[3]/table/thead/tr/th[8]/a"  # by XPath
    new_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[3]/div/div[3]/table/thead/tr/th[9]/a"  # by XPath
    operation_period_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[3]/div/div[3]/table/thead/tr/th[10]/a"  # by XPath
    remark_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[3]/div/div[3]/table/thead/tr/th[11]/a"  # by XPath
    administrator_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[3]/div/div[3]/table/thead/tr/th[12]/a"  # Path
    all_button = "w5-togdata-page"  # by Id

class Bonus_Element:
    bonus = "/html/body/div[1]/aside/section/ul/li[4]/ul/li[7]/a"  # by XPath
    username_filter_field = "reggivesearch-username"  # by ID
    all_button = "w1-togdata-page"  # by ID
    username_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[3]/table/thead/tr/th[2]/a" # by XPath
    credit_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[3]/table/thead/tr/th[3]/a" # by XPath
    bonus_type_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[3]/table/thead/tr/th[4]/a"  # by XPath
    status_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[3]/table/thead/tr/th[5]/a"  # by XPath
    bonus_period_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[3]/table/thead/tr/th[6]/a"  # by XPath
    verified_status_button = "btn-success"  # by Class Name

class Commission_Record_Element:
    commission_record = "/html/body/div[1]/aside/section/ul/li[4]/ul/li[8]/a"  # by XPath
    member_name_filter_field = "cashback-username"  # by ID
    all_button = "w1-togdata-page"  # by ID
    nickname_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div[3]/table/thead/tr/th[2]/a" # by XPath
    betting_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div[3]/table/thead/tr/th[4]/a"   # by XPath
    rebate_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div[3]/table/thead/tr/th[5]/a" # by XPath
    time_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div[3]/table/thead/tr/th[6]/a"  # by XPath

class Adjustment_Record_Element:
    adjustment_record = "/html/body/div[1]/aside/section/ul/li[4]/ul/li[9]/a"  # by XPath
    member_name_filter_field = "buckle-username"  # by ID
    all_button = "w1-togdata-page"  # by Id
    username_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div[2]/div/div[3]/table/thead/tr/th[2]/a"  # by XPath
    operation_type_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div[2]/div/div[3]/table/thead/tr/th[3]/a"  # by XPath
    operation_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div[2]/div/div[3]/table/thead/tr/th[4]/a"  # by XPath
    turn_over_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div[2]/div/div[3]/table/thead/tr/th[5]/a"  # by XPath
    turn_over_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div[2]/div/div[3]/table/thead/tr/th[6]/a"  # by XPath
    benefits_from_activity_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div[2]/div/div[3]/table/thead/tr/th[7]/a"  # by XPath
    credit_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div[2]/div/div[3]/table/thead/tr/th[8]/a"  # by XPath
    operation_period_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div[2]/div/div[3]/table/thead/tr/th[9]/a"  # by XPath
    remark_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div[2]/div/div[3]/table/thead/tr/th[10]/a"  # by XPath

class Turn_Over_Amount_Record_Element:
    turn_over_amount = "/html/body/div[1]/aside/section/ul/li[4]/ul/li[10]/a"  # by XPath
    member_name_filter_field = "betnumrddetailssearch-username"  # by ID
    all_button = "w1-togdata-page"  # by ID
    change_types_header_sorting= "/html/body/div[1]/div[1]/section[2]/div/div/div[2]/div/div[3]/table/thead/tr/th[3]/a"  # by XPath
    turn_over_amount_before_changes_header_sorting= "/html/body/div[1]/div[1]/section[2]/div/div/div[2]/div/div[3]/table/thead/tr/th[4]/a"  # by XPath
    turn_over_amount_changes_header_sorting= "/html/body/div[1]/div[1]/section[2]/div/div/div[2]/div/div[3]/table/thead/tr/th[5]/a"  # by XPath
    turn_over_amount_after_changes_header_sorting= "/html/body/div[1]/div[1]/section[2]/div/div/div[2]/div/div[3]/table/thead/tr/th[6]/a"  # by XPath
    changes_period_header_sorting= "/html/body/div[1]/div[1]/section[2]/div/div/div[2]/div/div[3]/table/thead/tr/th[7]/a"  # by XPath
    withdraw_amount_before_changes_header_sorting= "/html/body/div[1]/div[1]/section[2]/div/div/div[2]/div/div[3]/table/thead/tr/th[8]/a"  # by XPath
    withdraw_amount_changes_header_sorting= "/html/body/div[1]/div[1]/section[2]/div/div/div[2]/div/div[3]/table/thead/tr/th[9]/a"  # by XPath
    withdraw_amount_after_changes_header_sorting= "/html/body/div[1]/div[1]/section[2]/div/div/div[2]/div/div[3]/table/thead/tr/th[10]/a"  # by XPath
    remark_header_sorting="/html/body/div[1]/div[1]/section[2]/div/div/div[2]/div/div[3]/table/thead/tr/th[11]/a"  # by XPath

class Wallet_Transfer_Element:
    wallet_transfer = "/html/body/div[1]/aside/section/ul/li[4]/ul/li[11]/a"  # by XPath
    new_button = "btn-primary"  # by Class Name
    zhang_hu_page_element = "accounttransfer-amount"  # by ID
    user_id_filter_field = "wallettransfer-user_id" # by ID
    filter_search_button = "/html/body/div[1]/div[1]/section[2]/form/div/div[2]/button"  # by XPath
    user_id_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/table/thead/tr/th[1]/a"  # by XPath
    type_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/table/thead/tr/th[2]/a"  # by XPath
    provider_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/table/thead/tr/th[3]/a"  # by XPath
    amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/table/thead/tr/th[4]/a"  # by XPath
    status_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/table/thead/tr/th[5]/a"  # by XPath
    bonus_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/table/thead/tr/th[6]/a"  # by XPath
    related_activity_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/table/thead/tr/th[8]/a"  # by XPath
    created_time_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/table/thead/tr/th[9]/a"  # XPath
    error_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/table/thead/tr/th[10]/a"  # XPath
    result_message_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/table/thead/tr/th[11]/a"  # XPath
    remark_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/table/thead/tr/th[12]/a"  # XPath
    edited_time_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/table/thead/tr/th[13]/a"  # Xpath