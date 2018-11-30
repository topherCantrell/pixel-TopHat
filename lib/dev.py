import serial
import time
import make_sds

_ser = serial.Serial('COM9',115200)

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
    
def set_colors(colors):
    col_buffer = [0]*1024    
    pos = 0
    for col in colors:
        col_buffer[pos+0] = col & 0xFF
        col_buffer[pos+1] = (col>>8) & 0xFF
        col_buffer[pos+2] = (col>>16) & 0xFF
        col_buffer[pos+3] = (col>>24) & 0xFF        
        pos+=4
    _ser.write(b'A')
    _send_buffer(col_buffer)
    _ser.write(b'B')
    _send_buffer(col_buffer)
    
def play_movie(filename,start_frame=0,end_frame=None):
    movie = make_sds.readMovie(filename)
    set_colors(movie['colors'])
    mfrs = movie['frames'][start_frame:end_frame]
    for mfr in mfrs:
        show_frame(mfr)
        time.sleep(.5)

if __name__ == '__main__':    
    # play_movie('color_test.txt')
    play_movie('../FLL2018/lego.txt')
    