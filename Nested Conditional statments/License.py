Age = 40
license = True
license_date = "valid"
if Age>=18:
    print("you are eligible to take license")
    if license == True:
        print("you have license")
        if license_date == "valid":
            print("you are free to go")
        else:
            print("pls renew the license")
    else:
        print("pls apply for the license")
        
else:
    print("you are not eligible to take license ")
    