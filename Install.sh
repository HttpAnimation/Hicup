mkdir Hicup
cd Hicup
mkdir photos
mkdir videos
mkdir My-HTML
wget https://github.com/HttpAnimation/Hicup/blob/main/styles.css
wget https://raw.githubusercontent.com/HttpAnimation/Hicup/main/server.php
wget https://raw.githubusercontent.com/HttpAnimation/Hicup/main/server.js
wget https://raw.githubusercontent.com/HttpAnimation/Hicup/main/package.json
wget https://raw.githubusercontent.com/HttpAnimation/Hicup/main/package-lock.json
wget https://raw.githubusercontent.com/HttpAnimation/Hicup/main/index.html
wget https://raw.githubusercontent.com/HttpAnimation/Hicup/main/apache2.conf
wget https://raw.githubusercontent.com/HttpAnimation/Hicup/main/Run.sh && chmod +x Run.sh
wget https://raw.githubusercontent.com/HttpAnimation/Hicup/main/README.md
wget https://raw.githubusercontent.com/HttpAnimation/Hicup/main/Dockerfile
wget https://raw.githubusercontent.com/HttpAnimation/Hicup/main/Build.sh && chmod +x Build.sh
wget https://raw.githubusercontent.com/HttpAnimation/Hicup/main/000-default.conf
cd My-HTML
wget https://raw.githubusercontent.com/HttpAnimation/Hicup/main/My-HTML/index.html
wget https://raw.githubusercontent.com/HttpAnimation/Hicup/main/My-HTML/styles.css
cd ../
npm install express