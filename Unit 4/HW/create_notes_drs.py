import os

def main():
    try:
        working_dir = os.path.join(os.getcwd(), "CyberSecurity-Notes")
        for x in range(1,25):

            folder_name ="week "+ str(x)
            for y in range(1,4):
                nested_folder = "day " + str(y)
                os.makedirs(os.path.join(os.path.join(working_dir, folder_name), nested_folder ))
    except OSError as error:
        print(str(error))

if __name__ == "__main__":        
    main()