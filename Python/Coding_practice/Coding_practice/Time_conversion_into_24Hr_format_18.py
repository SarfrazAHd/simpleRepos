





def  Time_conevetimeion(s):
    len_s = len(s)

    if s[:2] =="12" and s[-2:]=="AM":

        return "00" + s[2:len_s-2]

    elif s[-2:] =="PM" and s[:2] !="12":
        return str(int(s[:2])+12) + s[2:len_s-2]

    elif s[-2:] =="PM" and s[:2] =="12":
        return s[:len_s-2]

    elif s[-2:] =="AM" and s[:2]!="12":
        return s[:len_s-2]

time = "12:40:22PM"

print(Time_conevetimeion(time))


