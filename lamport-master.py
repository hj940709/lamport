#-*- coding: UTF-8 -*-
import sys,linecache,socket,_thread,time




def beat(port):
	s = socket.socket()
	if s.connect_ex((socket.gethostname(),port)) == 0:
		s.send(bytes('start','UTF-8'))
	s.close()

i = 0
configs = linecache.getlines(sys.argv[1])
while i < len(configs):
	para = int(configs[i].split(' ')[1].strip())
	_thread.start_new_thread(beat,(para,))
	i += 1
	
time.sleep(int(len(configs)*0.7))
