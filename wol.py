import socket
import struct

def wakeonlan(macaddr):
	# using 'XX:XX:XX:XX:XX:XX' format
	addr = macaddr.split(":")
	
	hwaddr = struct.pack("!BBBBBB", int(addr[0], 16),
									int(addr[1], 16),
									int(addr[2], 16),
									int(addr[3], 16), 
									int(addr[4], 16),
									int(addr[5], 16),
									)
	msg = b"\xff"*6 + hwaddr*16
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	s.sendto(msg, ("10.10.1.255",9))
	s.sendto(msg, ("10.10.1.255",7))
	
	s.close()
	
if __name__ == "__main__":
	wakeonlan("XX:XX:XX:XX:XX:XX")
