import os
import requests

def download_file(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {url}")
    else:
        print(f"Failed to download: {url}")

def main():
    # Create the Hicup directory if it doesn't exist
    os.makedirs("Hicup", exist_ok=True)
    os.chdir("Hicup")

    # List of URLs to download
    urls = [
        "https://github.com/HttpAnimation/Hicup/blob/main/styles.css",
        "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/server.php",
        "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/server.js",
        "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/package.json",
        "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/package-lock.json",
        "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/index.html",
        "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/apache2.conf",
        "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/Run.py",
        "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/README.md",
        "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/Dockerfile",
        "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/Build.py",
        "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/000-default.conf"
    ]

    # Download files
    for url in urls:
        file_name = url.split("/")[-1]
        download_file(url, file_name)

    # Create photos and videos directories
    os.system("mkdir photos")
    os.system("mkdir videos")

    # Install Express using npm
    os.system("npm install express")

if __name__ == "__main__":
    main()
