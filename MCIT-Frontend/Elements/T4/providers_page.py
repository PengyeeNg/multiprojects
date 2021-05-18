from Input_Data.T4.providers_page import SportData
from Input_Data.T4.providers_page import SlotData

class ProvidersElement:
    enter_the_game_button = "/html/body/div[2]/div[1]/div/div/footer/div/button"  # by XPath
    log_in_button = "my-1"  # by Class Name
    main_wallet_amount = "/html/body/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]"  # by XPath
    game_amount = "/html/body/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]"  # by XPath
    transfer_amount_field = "/html/body/div[2]/div[1]/div/div/div/div/div/div[3]/div[2]/input"  # by XPath
    quick_transfer_button = "mt-1"  # by Class Name


class CasinoElement:
    evo_gaming_button = "/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/ul/li[1]/a/img"
    big_gaming_button = "/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/ul/li[3]/a/img"
    sbo_button = "/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/ul/li[2]/a/img"
    wm_casino_button = "/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/ul/li[4]/a/img"
    single_game_button = "/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/ul/li/img"  # by XPath


class SlotElement:
    spade_gaming_button = "/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/ul/li[1]/a/img"
    sbo_gaming_button = "/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/ul/li[2]/a/img"
    big_gaming_button = "/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/ul/li[3]/a/img"
    igs_button = "/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/ul/li[4]/a/img"
    single_game = "/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/ul/li/img"  # by XPath
    sbo_game = "/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/ul/li[" + str(SlotData.loopran_sbo) + "]/img"  # by XPath
    big_game = "/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/ul/li[" + str(SlotData.loopran_big) + "]/img"  # by XPath
    igs_game = "/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/ul/li[" + str(SlotData.loopran_igs) + "]/img"  # by XPath


class SportElement:
    cmd_button = "/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/ul/li[1]/a/img"
    sbo_button = "/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/ul/li[2]/a/img"
    ibc_button = "/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/ul/li[3]/a/img"
    m8_sports_button = "/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/ul/li[4]/a/img"
    single_game = "/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/ul/li/img"  # by XPath
    sbo_game = "/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/ul/li[" + str(SportData.loopran_sbo) + "]/img"  # by XPath



