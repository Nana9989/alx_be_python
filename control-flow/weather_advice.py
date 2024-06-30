current_weather = (input("What's the weather like today? (sunny/rainy/cold):"))
if current_weather == "sunny":
    advice = "Wear a t-shirt and sunglasses."
elif current_weather == "rainy":
    advice = "Don't forget your umbrella and a raincoat."
elif current_weather == "cold":
    advice = "Make sure to wear a warm coat and a scarf."
else:
    advice = "Sorry, I don't have recommendations for this weather."

print(advice)
