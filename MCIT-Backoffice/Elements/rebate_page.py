class Rebate_Element:
    rebate = "/html/body/div[1]/aside/section/ul/li[5]/a"  # by XPath
    no_results_found = "empty"  #  by Class Name
    all_button = "w1-togdata-page"  # by ID
    search_filter_button = "glyphicon-search"  # by Class Name

class Rebate_Setting_Element:
    rebate_setting = "/html/body/div[1]/aside/section/ul/li[5]/ul/li[1]/a"  # by XPath
    add_rebate_button = "glyphicon-plus"  # by Class Name
    create_rebate_submit_button = "btn-primary"  # by Class Name
    edit_rebate_button = "glyphicon-pencil"  # by Class Name
    update_rebate_submit_button = "btn-primary"  # by Class Name
    start_date_filter_field = "begin_time"  # by ID
    close_date_filter_field = "end_time"  # by ID
    code_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[3]/table/thead/tr/th[1]/a"  # by XPath
    provider_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[3]/table/thead/tr/th[2]/a"  # by XPath
    percentage_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[3]/table/thead/tr/th[3]/a"  # by XPath
    created_time_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[3]/table/thead/tr/th[4]/a"  # by XPath
    category_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[3]/table/thead/tr/th[5]/a"  # by XPath
    status_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[3]/table/thead/tr/th[6]/a"  # by XPath

class Rebate_Record_Element:
    rebate_record = "/html/body/div[1]/aside/section/ul/li[5]/ul/li[2]/a"  # by XPath
    member_id_filter_field = "rebateamount-bian_hao"  # by ID
    bet_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div[2]/div/div[3]/table/thead/tr/th[2]/a"  # by XPath
    provider_header_sorting = "/html/body/div[1]/div[1]/section[2]/div[2]/div/div[3]/table/thead/tr/th[3]/a"  # by XPath
    rebate_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div[2]/div/div[3]/table/thead/tr/th[4]/a"  # by XPath
    rebate_date_header_sorting = "/html/body/div[1]/div[1]/section[2]/div[2]/div/div[3]/table/thead/tr/th[5]/a"  # by XPath
    created_date_header_sorting = "/html/body/div[1]/div[1]/section[2]/div[2]/div/div[3]/table/thead/tr/th[6]/a"  # by XPath

class Provider_Report_Element:
    provider_report = "/html/body/div[1]/aside/section/ul/li[5]/ul/li[3]/a"  # by XPath
    start_date_filter_field = "begin_time"  # by ID
    close_date_filter_field = "end_time"  # by ID
    provider_header_sorting = "/html/body/div[1]/div[1]/section[2]/div[2]/div/div[3]/table/thead/tr/th[1]/a"  # by XPath
    bet_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div[2]/div/div[3]/table/thead/tr/th[2]/a"  # by XPath
    rebate_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div[2]/div/div[3]/table/thead/tr/th[3]/a"  # by XPath

class Member_Report_Element:
    member_report = "/html/body/div[1]/aside/section/ul/li[5]/ul/li[4]/a"  # by XPath
    member_id_filter_field = "rebateamount-bian_hao"  # by ID
    bet_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div[2]/div/div[3]/table/thead/tr/th[2]/a" # by XPath
    rebate_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div[2]/div/div[3]/table/thead/tr/th[3]/a" # by XPath

