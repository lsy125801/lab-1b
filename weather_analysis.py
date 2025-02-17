fhandle = open("WeatherData.txt")
rainy_count = 0
for line in fhandle:
    line = line.strip()
    _, _, humidity, rainfall = [float(x) for x in line.split()]
    if rainfall > 2.5:
        rainy_count +=1
print("There are,", rainy_count, "rainy days in WeatherData.txt file")