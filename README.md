# privateRoom
Make your work private by building a system using arduino which instantly kills a program when someone enters your room/cabin


STEPS:

1. Upload "killbill/killbill.ino" to arduino board

2. Install pyserial, os, signal library in python using: "pip install pyserial" etc..

3. run start.py using "python3 start.py" or "python start.py"

4. type in PID of the process to be killed, PID can be looked up by task manager or just search the net how to find PID of a process

5. Type full name of port, ex - "COM5" or "/dev/ttyACM0" etc.

6. "Running..." means program is running now. Don't touch the command prompt and DO WHATEVER YOU WANT NOW

7. Now any signal to PIN A0 on arduino which is greater than 750 (analogRead) will kill the process.


NOTE: COnfigure your sensors or edit the arduino code, Remember that you need to send a "killbill" to serial from arduino i.e. Serial.println("killbill"); to kill the process. SO, configure accordingly. Use motion sensor or build a sensor using copuple of LDR, IR detectors and a light source or UV distance finder. Put sensors on door step

NOTE2: Linux users may need to "sudo chmod a+rw /dev/ttyACM0" in case of permission denied error
