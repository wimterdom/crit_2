# Cryptography Engineering Crit. 2 Online Voting System Implement

- 系所：資訊科學工程研究所(博)
- student id : 412551016,412551010, 411551012
- Name : 張翔瑋, 林峻賢, 林哲偉

## 01-Requirement
- OS
    - Linux系列作業系統
        - Linux
        - Ubuntu 22.04
        - Kail
        - etc
- python
    - pandas
    - tkinter
    - subprocess
    - socket

- you can install the python library by typing the command below
    - Navigate to Project folder
    - `sudo ./requirement.sh`

## 02-How to Run
### server side
1. Open terminal/command prompt on your PC.
2. Navigate to `server` folder
3. Run command : `python3 Server.py`

### client side
1. Open terminal/command prompt on your PC
2. Navigate to `client` folder
3. Run command : `python3 homepage.py`

## 03-How to Login
### server side
- Admin Login :
    - Admin ID : `Admin`
    - Password : `admin`
### client side
- Client Login:
    - Voter Login:
        - Server should be running for voters to be able to login.
        - Already registered voter IDs : 10001 ~
        - Password (for already registered voters) : abcd

## 04-Workflow Description
- Inorder Description to run & test this project :
    - Server
        1. Open terminal & run `python3 homePage.py` to open Home Page Window.
        2. Log into Admin
        3. Press `Register Voter` and enter details to register a new voter. Remember or note down the `Voter ID` that you will receive on successful registration.
        5. Press `Home` to return to the Home.
        6. Open terminal & run `python3 Server.py` to start server. At the same time, the server will generate a private key and a public key, and listen on the port to wait for a connection.
    - Client
        1. Open terminal & run `python3 homePage.py` to open Home Page Window. When the client connects to server, the server will transfer the public key to client.
        2. Now, press `Voter Login` to open the voter login page.
        3. Enter the login details and you are redirected to the Voting Page. You will receive an error message if the Voter is invalid or has already cast a vote.
        4. Cast a Vote. Client will encrypt the vote result by public key and transfer the result to server. Now on receiving a success message, press home to return to home.
        5. Login voter again to see the votes results.

## 05-功能說明
1. Project區分server及client兩個部分
2. Server端有以下功能
    - 管理員功能
    - 註冊投票者  
        資料儲存在/server/database/voterList.csv
    - 檢視及更新投票數據  
        資料儲存在/server/database/cand_list.csv
    - 生成private key 及public key
3. Client端有以下功能
    - 投票者登入
    - 投票
    - 檢視投票數據  
        同步server端cand_list.csv，並顯示投票數據
4. 線上投票必須保證兩件事
    - 身分驗證  
    投票者一律由server端註冊，server再將登入帳密以電子郵件或其他方式告知投票者。
    ![身分驗證](./doc_fig/id_login.png)

    - 投票保密  
    我們必須保證投票者投完票後，其結果在傳輸過程中必須經過加密保護其投票內容不外流及修改，確保其完整性(Integrity)及機密性 (Confidentiality)。因此，我們透過RSA加密方式，投票者在登入系統後會從Server端接受public key。投票者在完成投票後使用public key進行加密，server收到後使用private key解密，並將結果更新到統計數據。
        - 選票未加密
    ![選票未加密](./doc_fig/non-encrypt_vote.png)
        - 選票已加密
        ![選票已加密](./doc_fig/encrypt_vote.png)

## 06- Stepwise Output / Test Cases
- Homepage
    - server
    ![image](./doc_fig/home_server.png)
    - client
    ![image](./doc_fig/client_home.png)

- Admin
    - Login
         ![image](./doc_fig/admin_login.png)
    - Home
        ![image](./doc_fig/admin_home.png)
    - Register Voter
        ![image](./doc_fig/reg_voter.png)
    - Register success
        ![image](./doc_fig/reg_success.png)

- Client
    - Voter Login
        ![image](./doc_fig/voter_login.png)
    - Vote
        ![image](./doc_fig/voter_vote.png)
    - Vote Success
        ![image](./doc_fig/vote_success.png)
    - Login again to see Results
        ![image](./doc_fig/voter_login.png)
        ![image](./doc_fig/voter_show.png)   

