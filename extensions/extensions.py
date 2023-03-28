filename, dot, file_extension = input("Please give filename: ").lower().strip().rpartition(".")

#print(filename)
#print(dot)
#print(file_extension)

if file_extension == "gif":
    print("image/gif")
elif file_extension == "jpg":
    print("image/jpeg")
elif file_extension == "jpeg":
    print("image/jpeg")
elif file_extension == "png":
    print("image/png")
elif file_extension == "pdf":
    print("application/pdf")
elif file_extension == "txt":
    print("text/plain")
elif file_extension == "zip":
    print("application/zip")
else:
   print("application/octet-stream")