import time

def format_time(secs):
    sec = secs%60
    minute = secs//60
    hour = minute//60

    mat = " " + str(minute) + ":" + str(sec)
    return mat  


def restart_vars(): 
    '''restart main loop vars on restart button ''' 
    run = True
    key=None
    strikes=0
    end=False
    start= time.time() #momentanium time
    return run,key, strikes,end,start


