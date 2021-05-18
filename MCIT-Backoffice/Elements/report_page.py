class Report_Element:
    report = "/html/body/div[1]/aside/section/ul/li[6]/a"  # by XPath
    member_name_filter_field = "memberreportsearch-username"  # by ID
    search_filter_button = "glyphicon-search"  # by Class Name
    no_results_found = "empty"  # by Class Name
    view_all_button = "w5-togdata-page"  # by ID
    select_columns_button = "w1-cols"  # by ID
    select_columns = "kv-toggle-all"  # by Class Name
    export_button = "w3"  # by ID
    export_to_html = "export-full-html"  # by Class Name
    export_confirmation_ok_button = "btn-warning"  # by Class Name
    reset_search_button = "glyphicon-refresh"  # by Class Name
    start_date_filter_field = "begin_time"  # by Class Name
    end_date_filter_field = "end_time"  # by Class Name
    range_today_button = "fui-date-btn" # by Class Name

class Overall_Element:
    overall = "/html/body/div[1]/aside/section/ul/li[6]/ul/li[1]/a"  # by XPath

class Affiliate_Element:
    affiliate = "/html/body/div[1]/aside/section/ul/li[6]/ul/li[2]/a"  # by XPath

class Cash_Flow_Element:
    cash_flow = "/html/body/div[1]/aside/section/ul/li[6]/ul/li[3]/a"  # by XPath
    username_header_sorting = "/html/body/div[1]/div[1]/section[2]/div[3]/div/div[3]/table/thead/tr/th[2]/a" # by XPath
    third_party_game_betting_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div[3]/div/div[3]/table/thead/tr/th[3]/a" # by XPath
    third_party_game_win_lose_header_sorting = "/html/body/div[1]/div[1]/section[2]/div[3]/div/div[3]/table/thead/tr/th[4]/a" # by XPath
    third_party_game_rebate_header_sorting = "/html/body/div[1]/div[1]/section[2]/div[3]/div/div[3]/table/thead/tr/th[5]/a" # by XPath
    manual_deposit_header_sorting = "/html/body/div[1]/div[1]/section[2]/div[3]/div/div[3]/table/thead/tr/th[6]/a" # by XPath
    manual_deduct_header_sorting = "/html/body/div[1]/div[1]/section[2]/div[3]/div/div[3]/table/thead/tr/th[7]/a" # by XPath
    manual_bonus_header_sorting = "/html/body/div[1]/div[1]/section[2]/div[3]/div/div[3]/table/thead/tr/th[8]/a" # by XPath
    manual_withdrawal_header_sorting = "/html/body/div[1]/div[1]/section[2]/div[3]/div/div[3]/table/thead/tr/th[9]/a" # by XPath
    overall_affiliate_withdrawal_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div[3]/div/div[3]/table/thead/tr/th[10]/a" # by XPath
    overall_online_topup_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div[3]/div/div[3]/table/thead/tr/th[11]/a" # by XPath
    overall_deposit_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div[3]/div/div[3]/table/thead/tr/th[12]/a" # by XPath
    overall_topup_bonus_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div[3]/div/div[3]/table/thead/tr/th[13]/a" # by XPath
    overall_registration_bonus_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div[3]/div/div[3]/table/thead/tr/th[14]/a" # by XPath
    overall_withdrawal_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div[3]/div/div[3]/table/thead/tr/th[15]/a" # by XPath
    slide_bar = "/html/body/div[1]/div[1]/section[2]/div[3]/div/div[3]/table/thead/tr/th[15]/a" # by Class Name

class Merchant_Win_Loss_Element:
    merchant_win_loss = "/html/body/div[1]/aside/section/ul/li[6]/ul/li[4]/a"  # by XPath

class Merchant_Daily_Win_Loss_Element:
    merchant_daily_win_loss = "/html/body/div[1]/aside/section/ul/li[6]/ul/li[5]/a"  # by XPath

class Outstanding_Element:
    outstanding = "/html/body/div[1]/aside/section/ul/li[6]/ul/li[6]/a"  # by XPath
    id_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[1]/a"  # by XPath
    source_name_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[2]/a"  # by XPath
    reference_no_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[4]/a"  # by XPath
    soc_trans_id_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[5]/a"  # by XPath
    is_first_half_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[6]/a"  # by XPath
    trans_date_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[7]/a"  # by Xpath
    is_home_give_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[8]/a"  # by XPath
    is_bet_home_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[9]/a"  # by XPath
    bet_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[10]/a"  # by XPath
    outstanding_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[11]/a"  # by XPath
    hdp_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[12]/a"  # by XPath
    odds_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[13]/a"  # by XPath
    currency_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[14]/a"  # by XPath
    win_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[15]/a"  # by XPath
    exchange_rate_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[16]/a"  # by XPath
    win_lose_status_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[17]/a"  # by XPath
    trans_type_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[18]/a"  # by XPath
    danger_status_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[19]/a"  # by XPath
    mem_commission_set_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[20]/a"  # by XPath
    mem_commission_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[21]/a"  # by XPath
    bet_ip_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[22]/a"  # by XPath
    home_score_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[23]/a"  # by XPath
    away_score_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[24]/a"  # by XPath
    run_home_score_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[25]/a"  # by XPath
    run_away_score_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[26]/a"  # by XPath
    is_running_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[27]/a"  # by XPath
    reject_reason_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[28]/a"  # by XPath
    sort_type_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[29]/a"  # by XPath
    choice_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[30]/a"  # by XPath
    working_date_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[31]/a"  # by XPath
    odds_type_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[32]/a"  # by XPath
    match_date_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[33]/a"  # by XPath
    home_team_id_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[34]/a"  # by XPath
    away_team_id_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[35]/a"  # by XPath
    special_id_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[37]/a"  # by XPath
    is_cash_out_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[38]/a"  # by XPath
    cash_out_total_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[39]/a"  # by XPath
    cash_out_take_back_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[40]/a"  # by XPath
    cash_out_win_lose_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[41]/a"  # by XPath
    bet_source_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[42]/a"  # by XPath
    status_change_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[43]/a"  # by XPath
    state_update_ts_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[44]/a"  # by XPath
    aos_excluding_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[45]/a"  # by XPath
    mmr_percent_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[46]/a"  # by XPath
    bet_remarks_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[47]/a"  # by XPath
    is_special_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[48]/a"  # by XPath
    created_time_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[49]/a"  # by XPath
    username_filter_field = "cmdbetrecord-username"  # by ID
    view_all_button = "w0-togdata-page"  # by ID
    slide_bar_01 = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[22]/a" # by XPath
    slide_bar_02 = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[33]/a" # by XPath
    slide_bar_03 = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[44]/a"  # by XPath
    slide_bar_04 = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[49]/a"  # by XPath
    slide_bar_05 = "/html/body/div[1]/div[1]/section[2]/div/div/div/div[3]/table/thead/tr/th[39]/a"  # by XPath

class Betting_Record_Element:
    betting_record = "/html/body/div[1]/aside/section/ul/li[6]/ul/li[7]/a"  # by XPath
    all_button = "w1-togdata-page"  # by ID
    search_filter_button = "glyphicon-search"  # by Class Name
    no_results_found = "empty"  # by Class Name


class Betting_Record_Evo_Betting_Record_Element:
    evo = "/html/body/div[1]/aside/section/ul/li[6]/ul/li[7]/ul/li[1]/a"  # by XPath
    member_name_filter_field = "evobetdetail-username"  # by ID
    transaction_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[2]/a"  # by XPath
    username_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[3]/a"  # by XPath
    wager_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[4]/a"  # by XPath
    game_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[5]/a"  # by XPath
    bet_time_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[6]/a"  # by XPath
    payout_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[7]/a"  # by XPath
    win_lose_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[8]/a"  # by XPath

class Betting_Record_SPA_Betting_Record_Element:
    SPA = "/html/body/div[1]/aside/section/ul/li[6]/ul/li[7]/ul/li[2]/a"  # by XPath
    member_name_filter_field = "spabetdetail-username"  # by ID
    user_id_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[3]/a"  # by XPath
    jackpot_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[4]/a"  # by XPath
    bet_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[5]/a"  # by XPath
    win_lose_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[6]/a"  # by XPath
    betting_period_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[7]/a"  # by XPath

class Betting_Record_Mega_Betting_Record_Element:
    mega = "html/body/div[1]/aside/section/ul/li[6]/ul/li[7]/ul/li[3]/a"  # by XPath
    member_name_filter_field = "megabetdetail-username"  # by ID
    idx_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[2]/a"  # by XPath
    user_id_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[3]/a"  # by XPath
    bet_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[4]/a"  # by XPath
    win_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[5]/a"  # by XPath
    win_lose_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[6]/a"  # by XPath
    betting_period_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[7]/a"  # by XPath

class Betting_Record_XE88_Betting_Record_Element:
    XE88 = "html/body/div[1]/aside/section/ul/li[6]/ul/li[7]/ul/li[4]/a"  # by XPath
    member_name_filter_field = "xe88betdetail-username"  # by ID
    username_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[2]/a"  # by XPath
    username_01_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[3]/a"  # by XPath
    bet_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[4]/a"  # by XPath
    win_lose_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[5]/a"  # by XPath
    bet_time_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[6]/a"  # by XPath

class Betting_Record_Joker_Betting_Record_Element:
    joker = "html/body/div[1]/aside/section/ul/li[6]/ul/li[7]/ul/li[5]/a"  # by XPath
    member_name_filter_field = "jokerbetdetail-username"  # by ID
    username_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[3]/a"  # by XPath
    bet_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[4]/a"  # by XPath
    player_win_loss_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[5]/a"  # by XPath
    bet_time_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[6]/a"  # by XPath

class Betting_Record_Playtech_Betting_Record_Element:
    playtech = "html/body/div[1]/aside/section/ul/li[6]/ul/li[7]/ul/li[6]/a"  # by XPath
    member_name_filter_field = "playtechbetdetail-username"  # by ID
    username_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[3]/a"  # by XPath
    bet_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[4]/a"  # by XPath
    player_win_loss_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[5]/a"  # by XPath
    bet_time_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[6]/a"  # by XPath

class Betting_Record_CMD_Betting_Record_Element:
    CMD = "html/body/div[1]/aside/section/ul/li[6]/ul/li[7]/ul/li[7]/a"  # by XPath
    member_name_filter_field = "cmdbetdetail-username"  # by ID
    user_id_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[3]/a"  # by XPath
    valid_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[4]/a"  # by XPath
    win_loss_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[5]/a"  # by XPath
    bet_time_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[6]/a"  # by XPath

class Betting_Record_BG_Betting_Record_Element:
    BG = "html/body/div[1]/aside/section/ul/li[6]/ul/li[7]/ul/li[8]/a"  # by XPath
    member_name_filter_field = "bgbetdetail-username"  # by ID
    user_id_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[3]/a"  # by XPath
    valid_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[4]/a"  # by XPath
    win_loss_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[5]/a"  # by XPath
    bet_time_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[6]/a"  # by XPath

class Betting_Record_IBC_Betting_Record_Element:
    IBC = "html/body/div[1]/aside/section/ul/li[6]/ul/li[7]/ul/li[9]/a"  # by XPath
    member_name_filter_field = "ibcbetdetail-username"  # by ID
    user_id_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[3]/a"  # by XPath
    valid_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[4]/a"  # by XPath
    win_loss_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[5]/a"  # by XPath
    bet_time_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[6]/a"  # by XPath

class Betting_Record_IGS_Betting_Record_Element:
    IGS = "html/body/div[1]/aside/section/ul/li[6]/ul/li[7]/ul/li[10]/a"  # by XPath
    member_name_filter_field = "igsbetdetail-username"  # by ID
    user_id_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[3]/a"  # by XPath
    valid_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[4]/a"  # by XPath
    win_loss_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[5]/a"  # by XPath
    bet_time_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[6]/a"  # by XPath

class Betting_Record_M8_Betting_Record_Element:
    M8 = "html/body/div[1]/aside/section/ul/li[6]/ul/li[7]/ul/li[11]/a"  # by XPath
    member_name_filter_field = "m8betdetail-username"  # by ID
    user_id_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[3]/a"  # by XPath
    valid_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[4]/a"  # by XPath
    win_loss_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[5]/a"  # by XPath
    bet_time_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[6]/a"  # by XPath

class Betting_Record_Nextspin_Betting_Record_Element:
    nextspin = "/html/body/div[1]/aside/section/ul/li[6]/ul/li[7]/ul/li[12]/a"  # by XPath
    member_name_filter_field = "nextspinbetdetail-username"  # by ID
    user_id_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[3]/a"  # by XPath
    valid_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[4]/a"  # by XPath
    win_loss_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[5]/a"  # by XPath
    bet_time_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[6]/a"  # by XPath

class Betting_Record_WM_Betting_Record_Element:
    WM = "/html/body/div[1]/aside/section/ul/li[6]/ul/li[7]/ul/li[13]/a"  # by XPath
    member_name_filter_field = "wmbetdetail-username"  # by ID
    user_id_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[3]/a"  # by XPath
    valid_amount_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[4]/a"  # by XPath
    win_loss_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[5]/a"  # by XPath
    bet_time_header_sorting = "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div/div/div[3]/table/thead/tr/th[6]/a"  # by XPath