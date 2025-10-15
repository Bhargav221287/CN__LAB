from ftplib import FTP

ftp_server = "ftp.dlptest.com"  
ftp_user = "dlpuser"
ftp_pass = "rNrKYTX9g7z3RgJRmxWuGHbeu"

ftp = FTP(ftp_server)
ftp.login(user=ftp_user, passwd=ftp_pass)

print("Connected to FTP server")

print("\nDirectory listing before upload:")
ftp.retrlines("LIST")

filename = "test_upload.txt"
with open(filename, "w") as f:
    f.write("Hello FTP, this is a test upload file.")

with open(filename, "rb") as f:
    ftp.storbinary(f"STOR {filename}", f)
print(f"\nUploaded {filename}")

print("\nDirectory listing after upload:")
ftp.retrlines("LIST")

downloaded_file = "downloaded_test.txt"
with open(downloaded_file, "wb") as f:
    ftp.retrbinary(f"RETR {filename}", f.write)
print(f"\nDownloaded file saved as {downloaded_file}")

with open(downloaded_file, "r") as f:
    print("\nDownloaded file content:")
    print(f.read())

ftp.quit()
