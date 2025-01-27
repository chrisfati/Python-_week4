
def modify_file():
    try:
        # Prompt the user for the input file name
        input_file = input("Enter the name of the input file: ")

        # Attempt to open and read the input file
        with open(input_file, 'r') as file:
            content = file.read()

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Prompt the user for the output file name
        output_file = input("Enter the name of the output file: ")

        # Write the modified content to the output file
        with open(output_file, 'w') as file:
            file.write(modified_content)

        print(f"Modified content has been written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{input_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the program
modify_file()
