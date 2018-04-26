def threshold(p):
    low = [x for x in p if x.islower()];
    up = [x for x in p if x.isupper()];
    num = [x for x in p if x.isdigit()];
    return len(low) >= 1 and len(up) >= 1 and len(num) >= 1;
threshold("asdhwfwq1234VDSDV#$%^&");
def strength(p):
    low = [x for x in p if x.islower()];
    up = [x for x in p if x.isupper()];
    num = [x for x in p if x.isdigit()];
    symbol = [x for x in p if not (x.islower() or x.isupper() or x.isdigit())];
    if(len(p) == 1):
        if(threshold(p)):
            if(len(p) > 6):
                return 2 + (len(p) - 6) / 2 + len(symbol)
                    
            else:
                return 2;
        else:
            return 1;
                
    else:
        return 0;
    
