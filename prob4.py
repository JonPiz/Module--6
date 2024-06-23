from prob3 import correctTime

def PrintTimeAndMeasurements(timeDelta, feet, inches):
    print(f"The TimeDelta: {timeDelta} type: {type(correctTime)}")
    print(f"The feet: {feet} type: {type(feet)}")
    print(f"The inches: {inches} type: {type(feet)}")

PrintTimeAndMeasurements(correctTime, 5, 7)