https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask

Python version
Rpi4 contains python --version 2.7.16


sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 2
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1

update-alternatives --list python
update-alternatives --config python
Ref:https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux


sudo pip install megapi
sudo pip install flask

http://127.0.0.1:5000/

v1/devices
v1/device/m01
argument speed
Example v1/device/m01?speed=100


Jake Wright
https://www.youtube.com/watch?v=4T5Gnrmzjak
