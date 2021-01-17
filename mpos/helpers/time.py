from mpos.helpers.logger import log

def seconds_to_clock(seconds):

    hours = seconds // 3600
    minutes = (seconds - (hours * 3600)) // 60
    seconds = seconds - (seconds - (hours * 3600)) - (seconds - (minutes * 60))
    
    if hours < 0:
        hours = hours * (-1)
    if minutes < 0:
        minutes = minutes * (-1)
    if seconds < 0:
        seconds = seconds * (-1)
        
    if hours < 10:
        hours = "0" + str(hours)
    else:
        hours = str(hours)
    if minutes < 10:
        minutes = "0" + str(minutes)
    else:
        minutes = str(minutes)
    if seconds < 10:
        seconds = "0" + str(seconds)
    else:
        seconds = str(seconds)
    
    timestring = str(hours) + ":" + str(minutes) + ":" + str(seconds)
    return timestring