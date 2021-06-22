duration = 121
if duration < 60:
    print(duration, "секунд")
elif duration < 3600:
    print(round(duration / 60), "минут" , duration % 60, "секунд")


