def main():
    extent = input('File name: ').strip().lower()
    
    if ".gif" in extent:
        print('image/gif', end="")

    elif ".jpg" in extent:
        print('image/jpeg', end="")

    elif ".jpeg" in extent:
        print('image/jpeg', end="")

    elif ".png" in extent:
        print('image/png', end="")

    elif ".pdf" in extent:
        print('application/pdf', end="")

    elif ".txt" in extent:
        print('text/plain', end="")

    elif ".zip" in extent:
        print('application/zip', end="")

    else:
        print('application/octet-stream', end="")
    

main()