class Announcement_Element:
    announcement = "/html/body/div[1]/aside/section/ul/li[8]/a"  # by XPath
    all_button = "grid-togdata-page"  # by ID

class Member_Message_Element:
    member_message = "/html/body/div[1]/aside/section/ul/li[8]/ul/li/a"  # by XPath
    announcement_checkbox = "/html/body/div[1]/div[1]/section[2]/div/div/div/div/div[3]/table/tbody/tr[1]/td[1]/input"  # by XPath
    batch_deletion_button = "delete "  # by Class Name
    batch_delete_confirmation_ok_button = "btn-warning"  # by Class name
    site_notification_button = "create"  # by Class Name
    send_site_notification_save_button = "submitBtn"  # by ID
    delete_button = "glyphicon-trash"  # by Class Name
    delete_confirmation_ok_button = "btn-warning"  # by Class Name
    edit_button = "glyphicon-pencil"  # by Class Name
    recipient_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div/div[3]/table/thead/tr/th[2]/a"  # by XPath
    title_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div/div[3]/table/thead/tr/th[3]/a"  # by XPath
    time_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div/div[3]/table/thead/tr/th[4]/a"  # by XPath
    status_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div/div[3]/table/thead/tr/th[5]/a"  # by XPath
