def main():

    touchdowns = 85
    interceptions = "none"

    try:
        TIratio = touchdowns/interceptions
        print("The Touchdown/Interception Ratio is:",TIratio)
    except ZeroDivisionError:
        print("The QB has not thrown any interceptions")
        TIratio = "undetermined"
    except:
        print("Bad data")
        TIratio = "undetermined"
 
    if TIratio == "undetermined":
        print("The QB cannot be evaluated")
    elif TIratio > 5:
        print("The QB is awesome")
    elif TIratio > 2:
        print("The QB is acceptable")
    else:
        print("The QB is Brock Ostweiler")

main()
