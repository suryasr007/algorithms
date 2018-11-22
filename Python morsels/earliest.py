
def get_earliest(*dates):
    """Return earliest of given MM/DD/YYYY-formatted date strings."""
    def date_key(date):
        (m, d, y) = date.split('/')
        return (y, m, d)
    return min(dates, key=date_key)


val = get_earliest("01/24/2007", "01/21/2008", "02/29/2009", "02/30/2006", "02/28/2006", "02/29/2006")
print(val)