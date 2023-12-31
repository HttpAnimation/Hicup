import os
import urllib.request

# Create directories
os.makedirs("Hicup/photos", exist_ok=True)
os.makedirs("Hicup/videos", exist_ok=True)
os.makedirs("Hicup/music", exist_os=True)
os.makedirs("Hicup/My-HTML", exist_ok=True)
os.chdir("Hicup")

# URLs to download
urls = [
 "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/000-default.conf",
 "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/Build.py",
 "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/Dockerfile",
 "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/Run.py",
 "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/apache2.conf",
 "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/hicup-css.css",
 "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/hicup-player.js",
 "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/index.html",
 "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/package-lock.json",
 "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/package.json",
 "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/server.js",
 "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/server.php",
 "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/styles.css"
]

# Download files
for url in urls:
    filename = os.path.basename(url)
    urllib.request.urlretrieve(url, filename)

# Change permissions for the Run.sh and Build.sh scripts
# Not needed
# os.chmod("Run.sh", 0o755)
# os.chmod("Build.sh", 0o755)

# Change back to the main directory
os.chdir("..")

# Create My-HTML directory and download files
os.makedirs("My-HTML", exist_ok=True)
os.chdir("My-HTML")

html_urls = [
    "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/My-HTML/index.html",
    "https://raw.githubusercontent.com/HttpAnimation/Hicup/main/My-HTML/styles.css"
]

for url in html_urls:
    filename = os.path.basename(url)
    urllib.request.urlretrieve(url, filename)

# Change back to the main directory
os.chdir("..")

# Install npm package
os.system("npm install express")
