import os, signal, serial
print("Make sure sensors deployed!")
print("Search PID of process using task manager (ctrl+shift+escape)")
pid=int(input("Enter PID of the parent process:"))

baud=9600

com_address=input("Enter name of port ex COM5,/dev/ttyAMC0, etc:")


com=serial.Serial(com_address,baud,timeout=None)

temp="abc"
print("running...");
while True:
	temp=com.readline().decode().strip()
	if temp=="killbill":
		os.kill(pid,signal.SIGKILL)
		break
	else:
		continue

print("PID "+str(pid)+" killed successfully by call "+temp)
input("Press Enter key to quit this program and you may start again...")
