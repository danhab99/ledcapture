install:
	pip3 install -r requirements.txt
	cp ledcapture.py /usr/bin/ledcapture
	chmod +x /usr/bin/ledcapture

	cp ledcap.service /etc/systemd/system
	systemctl daemon-reload
	systemctl start ledcap.service
	systemctl enable ledcap.service

uninstall:
	systemctl stop ledcap.service
	systemctl disable ledcap.service
	rm /etc/systemd/system/ledcap.service
	rm /usr/bin/ledcapture