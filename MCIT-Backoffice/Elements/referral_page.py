class Referral_Element:
    referral = "/html/body/div[1]/aside/section/ul/li[7]/a"  # by XPath
    search_filter_button = "glyphicon-search"  # by Class Name

class Member_Map_Element:
    member_map = "/html/body/div[1]/aside/section/ul/li[7]/ul/li/a"  # by XPath
    username_filter_field = "tuijianguanxitu-bian_hao"  # ID
    filter_no_result = "list-group"  # by Class Name
    transfer_username_filter_field = "xiugaituijianguanxi-yi_dong_hui_yuan"  # by ID
    transfer_membership_number_field = "xiugaituijianguanxi-xing_tui_jian_ren"  # by ID
    transfer_button = "glyphicon-transfer"  # Class Name
    transfer_failed_alert = "w2-error-0"  # by ID