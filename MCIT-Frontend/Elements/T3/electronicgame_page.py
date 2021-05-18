from Input_Data.T3.electronicgame_page import ElectronicGameData

class ElectronicGameElement:
    electronicgame_tab = "/html/body/div/div/div/div[1]/div[1]/nav/ul/li[3]/a"  # by XPath
    evo_gaming_button = "/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div[1]/ul/li[1]/a"  # by XPath
    spade_gaming_button = "/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div[1]/ul/li[2]/a"  # by XPath
    cmd_button = "/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div[1]/ul/li[3]/a"  # by XPath
    sbo_button = "/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div[1]/ul/li[4]/a"  # by Xpath
    big_gaming_button = "/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div[1]/ul/li[5]/a"  # by XPath
    ibc_button = "/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div[1]/ul/li[6]/a"  # by XPath
    m8sports_button = "/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div[1]/ul/li[7]/a"  # by XPath
    igs_button = "/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div[1]/ul/li[8]/a"  # by XPath
    wmcasino_button = "/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div[1]/ul/li[9]/a"  # by XPath
    nextspin_button = "/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div[1]/ul/li[10]/a"  # by XPath
    next_button = "/html/body/div/div/div/div[2]/div[2]/div/div/div[3]/button"  # by XPath
    evo_game = "/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[5]/div[1]/div/div["+ str(ElectronicGameData.loopranevo) +"]/div/button/div/p"  # by Xpath
    spa_game = "/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[2]/div["+ str(ElectronicGameData.loopranspa) +"]/div/div/div/button/div/p"  # by XPath
    cmd_game = "/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/div["+ str(ElectronicGameData.looprancmd) +"]/div/p"  # by XPath
    sbo_game = "/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[4]/div[1]/div/div["+ str(ElectronicGameData.loopransbo) +"]/div/button/div/p"  # by XPath
    big_game = "/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[5]/div[1]/div/div["+ str(ElectronicGameData.loopranbig) +"]/div/button/div/p"  # by XPath
    ibc_game = "/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[6]/div["+ str(ElectronicGameData.loopranibc) +"]/div/p"  # by XPath
    m8sports_game = "/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[7]/div["+ str(ElectronicGameData.loopranm8) +"]/div/p"
    igs_game = "/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[8]/div[1]/div/div["+ str(ElectronicGameData.loopranigs) +"]/div/button/div/p"  # by XPath
    wmcasino_game = "/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[9]/div["+ str(ElectronicGameData.loopranwm) +"]/div/p"  # by XPath
    nextspin_game = "/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[10]/div[1]/div/div["+ str(ElectronicGameData.looprannextspin) +"]/div/button/div/p"  # by XPath
    login_reminder_confirm_button = "btn-dark"  # by Class Name
    enter_the_game_button = "btn-block"  # by Class Name
    quick_transfer_amount_field = "nested-amount-input-1"  # by ID
    quick_transfer_button = "btn-outline-dark"  # by Class Name
    ini_exist_amount = "/html/body/div[2]/div[1]/div/div/div/div/div[1]/div[2]/b"  # by XPath
    ini_game_amount = "/html/body/div[2]/div[1]/div/div/div/div/div[2]/div[2]/b"  # by XPath
