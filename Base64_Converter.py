import base64

option = None

while option is not "3":
    print("\n============================="
          "\n1 - Encode text to Base64\n"
          "2 - Decode text from Base64\n"
          "3 - Exit.\n"
          "=============================\n")

    option = input("Escolha a opção: ")


    if option == "1":
        try:
            inpt = input("\nInsert data to be encoded: ")
            encodedBytes = base64.b64encode(inpt.encode("utf-8"))
            encodedStr = str(encodedBytes, "utf-8")

            print("\nConverted data: {}".format(encodedStr))
        except:
            print("\nHey, Something is wrong. Check the data.")

    elif option == "2":
        try:
            inpt = input("\nInsert data to be decoded: ")
            decodedBytes = base64.b64decode(inpt)
            decodedStr = str(decodedBytes, "utf-8")

            print("\nConverted data: {}".format(decodedStr))
        except:
            print("\nHey, something is wrong. Check the data.")
