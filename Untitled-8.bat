
 mkdir "$env:USERPROFILE\.node-gyp\20.19.5"
C:\Users\88692\.node-gyp\20.19.5\include\node\node.h

npm install node-addon-api --save-dev

勾選 Desktop development with C++

確認勾選：

MSVC v143 – VS 2022 C++ x64/x86 build tools

Windows 10 SDK

set npm_config_nodedir=C:\Users\88692\.node-gyp\20.19.5

npm run rebuild

npm pack

npm install sqlite3-5.1.7.tgz