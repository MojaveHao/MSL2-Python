pyside6-uic kfq.ui -o ui_kfq.py
pyside6-uic output.ui -o ui_output.py

cd SupportLib
pyside6-uic download.ui -o ui_download.py
pyside6-uic frp.ui -o ui_frp.py
pyside6-uic help.ui -o ui_help.py
pyside6-uic setting.ui -o ui_setting.py
pyside6-uic license.ui -o ui_license.py

echo GUI Update Success!
pause