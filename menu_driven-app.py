from main import buildResume
import os

def viewResume(filename):

    if os.path.exists(filename):
        print(f"\nOpening {filename}...")

        if os.name == "nt":      # Windows
            os.startfile(filename)
        else:
            print("Opening files automatically is only configured for Windows in this example.")

    else:
        print("File not found!")


def improveResume(filename):

    print(f"\nImproving Resume: {filename}")
    print("Feature Coming Soon...")


while True:

    print("\n==============================")
    print("     AI Resume Builder")
    print("==============================")
    print("1. Build Resume")
    print("2. View Resume")
    print("3. Improve Resume")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        buildResume()

    elif choice == '2':

        filename = input("Enter file name (Example: resume.pdf): ")
        viewResume(filename)

    elif choice == '3':

        filename = input("Enter file name: ")
        improveResume(filename)

    elif choice == '4':

        print("Thank you for using AI Resume Builder.")
        break

    else:

        print("Invalid Choice!")