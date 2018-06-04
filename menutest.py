def avp(amount):
    vat = amount * 7/107
    price = amount - vat
    return price , vat
avp(107)
