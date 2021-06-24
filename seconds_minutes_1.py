duration = 7265
if duration < 60:
    print(duration, "секунд")
elif duration < 3600:
    print(int(duration / 60), "мин.", duration % 60, "сек.")
elif duration == 3600 or duration > 3600:
    print(int(duration / 3600), "ч.", int(duration % 3600 / 60), "мин.", duration % 3600 % 60, "сек.")






