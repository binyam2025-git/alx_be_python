def get_weather_recommendation():
    weather = input("what's the weather like today? (sunny/rainy/cold): ").lower()
    
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")

#Call the function to run the program
if  __name__ == "__main__":
     get_weather_recommendation()

