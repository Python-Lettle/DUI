# -*- coding:utf-8 -*-

#DUI基础功能函数
__author__='Lettle'


#Main functions
def slen(value):
    length =len(value)
    utf8_length =len(value.encode('utf-8'))
    length =(utf8_length -length)/2+length
    return int(length)

def Getch():
    def _GetchUnix():
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def _GetchWindows():
        import msvcrt
        return msvcrt.getch()

    try:
        impl = _GetchWindows()
    except ImportError:
        impl = _GetchUnix()
    return impl

