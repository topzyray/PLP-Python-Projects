def main():
    # Accepting file name from user
    source_file = input("Source filename: ") + ".txt"
    destination_file = input("Destination filename: ") + ".txt"

    data = ""

    # Reading data from file
    try:
        # Opening file and closing automatically using the with keyword
        with open(source_file) as file:     
            result = file.read() # Read the content of the file
            data = result # Writing the content to a new file
    except FileNotFoundError:
        print(f"File not found.") # This code runs if no file with the specified name is found
    except:
        print("Something went wrong.") # This prints if any other error occur apart from FileNotFoundError

    # Writing data to file
    try:
        # Opening file and closing automatically using the with keyword
        with open(destination_file, 'a') as file:     
            result = file.write(data) # Writing to a file
            print("File written succesfully")
    except FileNotFoundError:
        print(f"File not found.") # This code runs if no file with the specified name is found
    except:
        print("Something went wrong.") # This prints if any other error occur apart from FileNotFoundError


if __name__ == "__main__":
    main()