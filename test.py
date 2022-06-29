import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import os

driver = webdriver.Firefox(executable_path="geckodriver.exe")
url = "https://www.ktemo.org/e_EMO"

list_of_CE = [file for file in os.listdir("CE")]
path_to_CE = [os.path.abspath("CE") + "\\" + file + " " for file in list_of_CE]
combine = "\n".join(path_to_CE)

driver.get(url)
login = driver.find_element_by_css_selector("td a")
login.click()

time.sleep(3)
driver.find_element_by_id("ctl00_cp_file_file_002_imgPopupRhea").click()
time.sleep(3)
iframe_certificates = driver.find_element_by_xpath('//*[@id="modal-body-iframe-0"]')
driver.switch_to.frame(iframe_certificates)
upload_certificate_button = driver.find_element_by_class_name("ruFileInput")
upload_certificate_button.send_keys(combine)
time.sleep(3)
unordered_list = driver.find_element(By.ID, "ctl00_cp_pnlBar1_i0_radFileUploadListContainer")
list_of_li = unordered_list.find_elements(By.TAG_NAME, "li")
last_il = list_of_li[-1]
wait = WebDriverWait(driver, 600)
wait.until(lambda d: "ruFileLI ruUploading" != last_il.get_attribute('class'))
driver.find_element_by_id("ctl00_cp_pnlBar1_i0_btnSelect_Upload").click()
driver.switch_to.default_content()




#
# emo_company_auto_fill = {
#     "ctl00_cp_cmb_cmb_ithalatci_ad_liste_combo_Input": "blue",
#     "ctl00_cp_txt_txt_vergi_no_text": "178001560",
#     "ctl00_cp_msktxt_msktxt_firma_tel_text": "0(542) 874 74 86",
#     "ctl00_cp_txt_txt_firma_e_posta_text": "mahmut",
#     "ctl00_cp_txt_txt_ihracatci_ad_text": "test",
#     #You should inspect elements after you click them because the thing you are looking for might not be visible!
#     "ctl00_cp_cmb_cmb_gonderilen_adres_combo_Input": "BAE (Birleşik Arap Emirlikleri)",
#     "ctl00_cp_txt_txt_p_f_no_text": "test",
#     "ctl00_cp_txt_txt_fatura_tarihi_text": "todays_date",
#     "ctl00_cp_cmb_cmb_para_birimi_combo_Input": "USD"
#
# }
# emo_products_auto_fill = {
#     "ctl00_cp_cmbCol_grd_000_cmb_malzeme_tipi_combo_Input": "2",
#     "ctl00_cp_txtCol_grd_malzeme_listesi_txtCol_urun_aciklamasi_text": "Bir beyaz eşya",
#     "ctl00_cp_txtCol_grd_malzeme_listesi_txtCol_marka_text": "Bir beyaz eşya markası",
#     "ctl00_cp_txtCol_grd_malzeme_listesi_txtCol_Miktar_text": "100",
#     "ctl00_cp_cmbCol_grd_malzeme_listesi_cmbCol_birim_combo_Input": "Adet",
#     "ctl00_cp_txtCol_grd_malzeme_listesi_txtCol_Birim_Fiyat_text": ""
# }
#
# wb = openpyxl.load_workbook("emo otomat listesi testing.xlsx")
# ws = wb.active
# max_row = ws.max_row
#
# EXPORTER_NAME = ws["B3"].value
# emo_company_auto_fill["ctl00_cp_txt_txt_ihracatci_ad_text"] = EXPORTER_NAME
# EXPORT_ADDRESS = ws["C3"].value
# emo_company_auto_fill["ctl00_cp_cmb_cmb_gonderilen_adres_combo_Input"] = EXPORT_ADDRESS
# INVOICE_NUMBER = ws["D3"].value
# emo_company_auto_fill["ctl00_cp_txt_txt_p_f_no_text"] = INVOICE_NUMBER
# CURRENCY_TYPE = ws["E3"].value
# emo_company_auto_fill["ctl00_cp_cmb_cmb_para_birimi_combo_Input"] = CURRENCY_TYPE
# pprint(emo_company_auto_fill)
#
# # print(EXPORTER_NAME, EXPORT_ADDRESS, INVOICE_NUMBER, CURRENCY_TYPE)
# for row in ws.iter_rows(min_col=2, max_col=5, min_row=6, values_only=True):
#     if None in row:
#         pass
#     else:
#         PRODUCT_NAME = row[0]
#         emo_products_auto_fill["ctl00_cp_txtCol_grd_malzeme_listesi_txtCol_urun_aciklamasi_text"] = PRODUCT_NAME
#         PRODUCT_BRAND = row[1]
#         emo_products_auto_fill["ctl00_cp_txtCol_grd_malzeme_listesi_txtCol_marka_text"] = PRODUCT_BRAND
#         PRODUCT_AMOUNT = row[2]
#         emo_products_auto_fill["ctl00_cp_txtCol_grd_malzeme_listesi_txtCol_Miktar_text"] = PRODUCT_AMOUNT
#         PRODUCT_PRICE = row[3]
#         emo_products_auto_fill["ctl00_cp_txtCol_grd_malzeme_listesi_txtCol_Birim_Fiyat_text"] = PRODUCT_PRICE
#         print(PRODUCT_PRICE, type(PRODUCT_PRICE))
# pprint(emo_products_auto_fill)
#         print(PRODUCT_NAME, PRODUCT_BRAND, PRODUCT_AMOUNT, PRODUCT_PRICE)


