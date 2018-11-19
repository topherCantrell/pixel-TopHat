import serial
import time

_ser = serial.Serial('COM10',115200)

#_ser.write(b'sparkle\r')

_ser.write(b'?\r') # Put in dev mode
time.sleep(1)

def _send_buffer(buf):
    for g in buf:
        _ser.write([g])
        
def show_frame(frame):
    _ser.write(b'1')
    _send_buffer(frame.get_binary(True))
    time.sleep(.1)
    _ser.write(b'2')
    _send_buffer(frame.get_binary(False))
    time.sleep(.1)
