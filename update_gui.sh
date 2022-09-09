
sudo python3 -m pyside6-uic kfq.ui -o ui_kfq.py
sudo python3 -m pyside6-uic output.ui -o ui_output.py

cd SupportLib
sudo python3 -m pyside6-uic download.ui -o ui_download.py
sudo python3 -m pyside6-uic frp.ui -o ui_frp.py
sudo python3 -m pyside6-uic help.ui -o ui_help.py
sudo python3 -m pyside6-uic setting.ui -o ui_setting.py
sudo python3 -m pyside6-uic license.ui -o ui_license.py
sudo python3 -m pyside6-uic start_options.ui -o ui_start_options.py