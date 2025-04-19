def calc_days(days_later, day):
    day = day.capitalize()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    i = 0
    for i in range(len(days)):
        if day == days[i]:
            i = i
            break
    new_day = (i + days_later)%7
    return days[new_day]

def add_time(start, duration, day=None):
    # Séparer l'heure de départ
    start_time = start.split()
    clock = start_time[1]
    start_hours, start_minutes = map(int, start_time[0].split(':'))

    # Convertir en 24h
    if clock == 'PM' and start_hours != 12:
        start_hours += 12
    if clock == 'AM' and start_hours == 12:
        start_hours = 0

    # Durée
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # Minutes totales
    total_start_minutes = start_hours * 60 + start_minutes
    total_duration_minutes = duration_hours * 60 + duration_minutes
    total_final_minutes = total_start_minutes + total_duration_minutes

    # Calcul du nouveau temps
    final_hour_24 = (total_final_minutes // 60) % 24
    final_minutes = total_final_minutes % 60

    # Calcul du nombre de jours
    days_later = total_final_minutes // (24 * 60)

    # Repasser en format 12h
    if final_hour_24 == 0:
        final_hour = 12
        final_clock = "AM"
    elif final_hour_24 < 12:
        final_hour = final_hour_24
        final_clock = "AM"
    elif final_hour_24 == 12:
        final_hour = 12
        final_clock = "PM"
    else:
        final_hour = final_hour_24 - 12
        final_clock = "PM"

    # Construction du résultat
    new_time = f"{final_hour}:{str(final_minutes).zfill(2)} {final_clock}"

    if day:
        new_time += ', ' + calc_days(days_later, day)

    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time

print(add_time('3:30 PM', '2:12'))                  # 5:42 PM
print(add_time('11:55 AM', '3:12'))                 # 3:07 PM
print(add_time('2:59 AM', '24:00'))                 # 2:59 AM (next day)
print(add_time('11:59 PM', '24:05'))                # 12:04 AM (next day)
print(add_time('8:16 PM', '466:02'))                # 6:18 AM (20 days later)
print(add_time('3:30 PM', '2:12', 'Monday'))        # 5:42 PM, Monday
print(add_time('2:59 AM', '24:00', 'saturDay'))     # 2:59 AM, Sunday (next day)
print(add_time('11:59 PM', '24:05', 'Wednesday'))   # 12:04 AM, Friday (2 days later)
print(add_time('8:16 PM', '466:02', 'tuesday'))     # 6:18 AM, Monday (20 days later)