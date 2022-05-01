
print("Welcome to the Activity Recommender!")
print("-" * 45)
temp_s = input("What is today's temperature (in F)? ")
temp = int(temp_s)

if temp > 100:
    print ("Too hot! Go see a movie.")
elif temp > 90:
    print ("It's a scorcher! Go swimming.")
elif temp > 70:
    print ("Nice day for a bike ride!")
elif temp > 50:
    print ("Great weather for a jog!")
elif temp > 30:
    print ("A bit brisk! Bundle up and go for a nice walk!")
elif temp > 20:
    print ("Great day for skiing! Hit the slopes!")
else:
    print ("Brrrr. I'd stay inside and warm up by the fire!")
