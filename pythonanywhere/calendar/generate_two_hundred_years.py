import calendar
import locale
from pathlib import Path

CSS = """
.sun, .sat {
    color: red;
    text-align: center;
}

.mon, .tue, .wed, .thu, .fri {
    color: blue;
    text-align: center;
}

table, th, td {
    border: 5px solid white;
}

table {
    border-collapse: collapse;
}

th {
    height: 20px;
}

th, td {
  padding: 5px;
}
"""


class CustomHTMLCalendar(calendar.LocaleHTMLCalendar):
    cssclasses = [style + " text-nowrap" for style in
                  calendar.HTMLCalendar.cssclasses]
    cssclass_month_head = "text-center month-head"
    cssclass_month = "text-center month"
    cssclass_year = "text-italic lead"
    
    def __init__(self, locale):
        super().__init__(firstweekday=calendar.SUNDAY, locale=locale)

        
def generate_calendars(start, stop, c, target, stem):

    with open(Path(target, 'calendar.css'), 'w') as info:
        info.write(CSS)

    for year in range(start, stop):
        link = stem + f'calendar-{year:d}.html'
        with open(Path(target, f'calendar-{year:d}.html'), 'w') as info:
            info.write('<html>')
            info.write('<head>')
            info.write('<link rel="stylesheet" href="calendar.css">')
            info.write('</head>')
            info.write('<body>')
            info.write(c.formatyear(year))
            info.write('</body>')    
            info.write('</html>')
        yield link, year


def generate_calendars_loc(calendars, loc):
    stem = f'./{loc[0]:s}/'
    c = CustomHTMLCalendar(loc)
    
    calendars.write(f'<h2>{loc[0]:>5s}</h2>\n\n<div>\n')
    target_with_loc = Path('calendars', loc[0]).resolve()
    target_with_loc.mkdir(mode=0o700, parents=True, exist_ok=True)
    
    for link, year in generate_calendars(start, stop, c, target_with_loc, stem):
        calendars.write(f'<p><a href="{link:s}">{loc[0]:5s}/{year:>4d}</a></p>\n')
    calendars.write('</div>\n\n')


start = 1900
stop = 2100

original_loc = ('en_US', 'UTF-8') # locale.getlocale()
modified_loc = ('es_AR', 'UTF-8')

root = Path('calendars').resolve()
root.mkdir(mode=0o700, parents=True, exist_ok=True)

with open(Path(root, 'calendars.html'), 'w') as calendars:
    calendars.write('<html>\n')
    calendars.write('<head>\n<title>Calendars</title>\n</head>\n\n')
    calendars.write('<body>\n')
    calendars.write(f'<h1>Calendars from {start:>4d} to {stop-1:>4d}</h1>\n')
              
    # original_loc run
    generate_calendars_loc(calendars, original_loc)
    
    # modified_loc run
    generate_calendars_loc(calendars, modified_loc)
    
    calendars.write('</body>\n')
    
    calendars.write('<html>\n')
    
locale.setlocale(locale.LC_ALL, original_loc)
