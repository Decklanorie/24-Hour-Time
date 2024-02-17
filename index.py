def convert_time(time12hr):
    time, period = re.split(r'([APMapm]{2})', time12hr)
    hours, minutes, seconds = map(int, time.split(':'))
    military_hours = hours + 12 if period.upper() == 'PM' and hours != 12 else (0 if period.upper() == 'AM' and hours == 12 else hours)

    military_time = ":".join([
        str(military_hours).zfill(2),
        str(minutes).zfill(2),
        str(seconds).zfill(2) if seconds else '00'
    ])

    return military_time

# Example usage:
time12hr = "03:45:30 PM"
print(convert_time(time12hr))  # Output: 15:45:30
