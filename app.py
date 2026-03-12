from bakong_khqr import KHQR

khqr = KHQR()

qr_image = khqr.create_qr(
    bank_account= ("kimchou_kren@bkrt"),
    merchant_name=("kimchou"),
    merchant_city=("phnom penh"),
    amount=100.00,
    currency="KHR",
    store_label=("kimchou"),
    phone_number="085890059",
    bill_number="12343444tex",
    terminal_label=("webqr"),
    static=False,

)

print ("QR Image :", qr_image)