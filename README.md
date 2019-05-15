## Mục lục

---------------------------------------------

#### [1 Đôi lời chia sẻ](#1)
#### [2. Cài đặt](#2)
- [2.1 Cài đặt](#2.1)
- [2.2 Cài đặt](#2.2)
- [2.3 Cài đặt](#2.3)
- [2.4 Cài đặt](#2.4)
#### [3 Liên hệ](#3)
- [3.1 Tham khảo](#3.1)


---------------------------------------------
### <a name="1"><a/>1. Đôi lời chia sẻ.
    
 - Khái niệm domain controller có sẽ đã quá quen thuộc với các bạn, nên mình cũng không cần giới thiệu thêm.
  
  - Cũng đã khá lâu rồi mình không còn tiếp xúc với winserver đặc biệt là domain controller trên winserver. Tuy nhiên mình vẫn làm việc với domain controller nhưng ở trên nền linux(centos7). Hệ thống của mình không lớn (gần 100 user), nên mình cũng ảo hóa nó luôn. Không có bài viết nào đánh giá về
  khả năng chịu tải của **domain samba** được khoảng bao nhiêu user cả. Một hệ thống tầm 500-1k user thì mình không biết thế nào, nhưng theo đánh khá khách quan của mình thì tầm 100-200 user cho hoàn toàn tải ngon. Ở Việt Nam thì mình chưa thấy có doanh nghiệp nào chạy domain trên linux cả, có lẽ là
  do nó khó cấu hình, cũng như khó vẫn hành và quản lý.
  
  - Với các cty, tập đoàn có user tầm >500 thì việc đầu tư cho 2,3 cái bản quyền winserver nó dễ như trở bàn tay. Nhưng với những không tin vừa và nhỏ, thì việc đầu tư vào bản quyền winserver lại cần phải có sự tính toán.
  
  - Ở Viêt Nam hiện nay thì >70% (theo đánh giá của các nhân mình) các cty đều dùng đồ không có bản quyền, hay nói thẳng ra là crack, nhưng thời gian gần đây, các bạn cũng đã thấy Microsoft đang làm khá mạnh tay về vẫn đề bản quyền ở Viêt Nam.
  Vậy chẳng có lý do gì mà các cty vừa và nhỏ không muốn đầu từ vào winserver bản quyền, mà vẫn muốn qlý user trong domain lại không tìm đến linux cả. Những gì mà winserver làm được, thì server linux hoàn toàn đáp ứng được.
  
  - Và tất nhiên dùng đồ quản quyền nó vẫn hay hơn, đặc biết là khi gặp vấn đề thì sẽ có sự support từ chính nhà cung cấp điều này còn gì tuyệt vời hơn. Nhưng thực tế hiện này các bạn cũng đã thấy, khi gặp lỗi gần như chúng ta không liên hệ với Microsoft mà đi hỏi luôn ông google.
  - Nói ở trên là cái hay của bản quyền là như vậy, nhưng không phải **domain samba** không được support. Các bạn thử seach từ khóa **setup samba domain controller**, sẽ có khoảng > 700k kết quả trả về. Điều này cho thấy công đồng dùng domain trên linux không hề nhỏ chút nào.
  - Dĩ nhiên khi sử dụng domain trên linux các bạn sẽ không có support nào từ bất cứ hãng nào cả, mà là sự support từ công đồng. Các bạn đừng thấy mình nói vậy mà nản vì sao, đơn giản như mình đã nói ở trên khi các bạn dùng winserver gặp vấn đề có khi nào các bạn liên hệ với Microsoft không, Không không và không.
  Việc đầu tiên các bạn làm đó là đi nhờ sự trợ giúp từ công đồng (google). Các lỗi mà các bạn gặp phải trong khi xây dựng và qlý domain trên linux, thì các chắc đã có người gặp rồi, vì các bạn không phải là người đầu tiên sử dụng nó. Cho nên gặp lỗi thì đã có công đồng support.
  
   
### <a name='2'><a/>2. Cài đặt.

#### <a name='2.1'><a/>2.1 Cài đặt.

- Để thực hiện việc cài đặt này yêu cầu 2 host làm domain controller phải được cài đặt python3.0 trở lên.

- Trước khi bắt đầu các bạn cần đảm bảo 2 host phải được kết nối ra internet.

    - Việc đầu tiên các bạn cần làm đó là cài đặt git

             yum -y install git
        
    - Việc cài đặt **git** này phải được cài trên cả 2 server.
   
    - Sau khi cài git xong các bạn thực hiện pull repo về
    
           git clone https://github.com/letran3691/domain.git
          
    - Sau khi clone về các bạn sẽ có 1 thư mục có tên **domain**   
        
    - Trong thử mục **domain** các bạn quan tâm cho mình 3 file **PDC.py, BDC.py**, và **installpython3.6.sh**

        - File **installpython3.6.sh**: Dùng để cài đặt python3.6

        - File **PDC.py**:Dùng để cài đặt và cấu hình trên Primary domain controller.
     
        - File **BDC.py**: Dùng để cài đăt và cầu hình domain backup(second domain controller) 
   
    -  Việc đầu tiên là phải phân quyền cho file  **installpython3.6.sh** 
        
            chmod +x domain/installpython3.6.sh
         
    -  Sau khi phân quyên xong các bạn thực hiện chạy file installpython3.6.sh này bằng lệnh:

                    ./domain/installpython3.6.sh
                    
         ![image](https://user-images.githubusercontent.com/19284401/57705211-a0b20b80-768d-11e9-92ea-b5d20b9606b0.png)

   - Quá trình cài đặt python3.6 bắt đầu (trong quá trình cài đặt, thực hiện đến bước nào thì sẽ có thông báo ở màn hình cho các bạn nắm được).
   
   - Sau khi cài đặt xong python bạn sẽ nhân được yêu cầu đặt hostname (đây sẽ là tên của primary domain controller).
   
        ![image](https://user-images.githubusercontent.com/19284401/57705620-69902a00-768e-11e9-9cb1-8705bb192b77.png)
         
        - Sau khi nhập **hostname** xong các bạn nhân **enter** host sẽ tự động reboot
        
   - Các bạn lại lập lại các bước vừa làm trên backup domain controller.
        ![image](https://user-images.githubusercontent.com/19284401/57706303-ae689080-768f-11e9-85ff-fe5e2f3cda58.png)
         
        - **Chú ý:** Các bạn tránh nhầm lẫn việc đặt hostname cho PDC vs BDC nhé, đây là 2 hostname cho 2 host các nhau không được đặt trùng.
   
   
#### <a name=2.2><a/>2.2 Cài đặt-cấu hình domain 



-  **Primary domain controller**
   
      - Sau khi cài đặt xong python3.6 giờ, giờ các bạn chạy file **PDC.py** để cấu hình primary domain controller
   
                 python3.6 domain/PDC.py
                 
      - Việc đầu tiên các bạn được hỏi là nhập IP, subnetmask cho Primary DC, và nhập tên domain
            ![image](https://user-images.githubusercontent.com/19284401/57743834-e48a2c80-76f0-11e9-90bf-e96b1566bf3a.png)

        - Ở đây mình làm LAB nên mình lấy luôn IP từ DHCP cấp, trong thực tế các bạn nên đặt IP sao cho dễ quản lý.
   
        - Nhập subnetmask chính xác với hệ thống mạng của các bạn 
   
        - domain name: Là tên dommain sẽ được dựng trong hệ thống này.
   
      - Sau khi nhập xong các thông tin trên script sẽ tự động cấu hình và restart lại network (các bạn chú ý giúp mình là file cấu hình card mạng cứ để mặc định khi mới cài đặt os nhé, tránh thay đổi dẫn đến việc file script cấu hình sai thông tin).

      - Quá trình cài đặt packet và compile bắt đầu(việc này diễn ra nhanh hay chậm tùy thuộc vào cấu hình phần cứng của host).

      - Mẹo nhỏ giúp các bạn ko phải trờ đợi quá lâu khi PDC compile và install thì các bạn hãy qua BDC thực hiện chạy file cài đặt.

        **- Chú ý**: Dể để PDC thực hiên compile xong khoảng hơn 2k/4k thì hay thực hiên các bước dưới đây, để đảm bảo quá trình cài đặt và cấu hình diễn ra đúng thứ tự.
            ![image](https://user-images.githubusercontent.com/19284401/57747163-819f9200-76fe-11e9-8380-bb034469b843.png)

- **Backup domain controller**

                    python3.6 domain/BDC.py

     - Khi chạy file này các bạn cũng sẽ được yêu cầu nhập các thông tin cần thiết cho qua trình cấu hình.
      
          ![image](https://user-images.githubusercontent.com/19284401/57744478-94f93000-76f3-11e9-8d05-fda9231d7131.png)

     - BDC sẽ copy file hosts sang PDC

        ![image](https://user-images.githubusercontent.com/19284401/57744450-78f58e80-76f3-11e9-85db-d3b8c943061b.png)
 
     - Các bạn bạn nhập yes rồi nhập password của root bên PDC.
    
     - Sau khi copy file hosts xong, quá trình dowload và cài đặt samba bắt đầu. thực hiên đến bước nào sẽ được in ra màn hình để các bạn nắm được.

     -  **Chuyển sang PDC**

     - Quá trình cài đặt samba hoàn tất các bạn sẽ có lời nhắc như trong hình
        ![image](https://user-images.githubusercontent.com/19284401/57746185-4a2ee680-76fa-11e9-8424-f26be70272f2.png)
        
        - Realm: Các bạn để mặc định và nhấn Enter
        - Domain: Để mặc định và Enter
        - Server Role: Để mặc đinh và Enter
        - DNS backend: Để mặc đinh và Enter
        - DNS forward: Nếu các bạn có DNS server riêng thì nhập IP của DNS server đó, còn không thì các bạn nhập IP của router có khả năng phần giải DNS public. Đơn giản hơn các bạn nhập 8.8.8.8
        
     - Cấu hình xem các bạn sẽ nhận được thông báo sau.
     
        ![image](https://user-images.githubusercontent.com/19284401/57746221-777b9480-76fa-11e9-96a5-a08d2ef27561.png)
        
    - **Chuyển qua BDC.**
    
     - Sau khi cài đặt samba xong thì nó sẽ hỏi yêu cầu bạn nhập password của Administrator domain mà bạn vừa nhập bên PDC.
     
       ![image](https://user-images.githubusercontent.com/19284401/57746247-9712bd00-76fa-11e9-8fbb-dd7678853b0c.png)

     - Nhập password xong nhấn Enter các bạn sẽ có 1 thông báo về thời gian hết hạn password của Administrator như trong hình và yêu cầu bạn nhập lại password admin lần nữa.
     
       ![image](https://user-images.githubusercontent.com/19284401/57746330-ec4ece80-76fa-11e9-8af7-e2c0b6614af8.png)
    
     - Sau khi nhấp pasword lần 2 thì BDC sẽ thực hiện cấu hình và join vào domain vừa tạo từ PDC. Đồng thời sẽ có lời nhắc bạn sang PDC nhấn Enter.
       ![image](https://user-images.githubusercontent.com/19284401/57746453-77c85f80-76fb-11e9-99ee-174f674bb4d7.png)
        
    - **Sang PDC**

     - sau khi nhấn Enter các bạn sẽ được yêu cầu nhập hostname của BDC.
     
         ![image](https://user-images.githubusercontent.com/19284401/57747693-de9c4780-7700-11e9-8edb-956db4adb085.png)
        _- Chú ý: các bạn đừng để màn hình chờ nhập password quá lâu sẽ dễ đến mất kết nối và gây ra lỗi._
   
         - các bạn nhập hostname -> yes > nhâp password root của BDC rồi Enter.
         
         - Thông báo chuyển qua BDC để Enter
   
    - **Sang BDC**
 
      ![image](https://user-images.githubusercontent.com/19284401/57747767-291dc400-7701-11e9-80c4-05156c705299.png)
    
        - _Chú ý: Hãy đợi xuất hiện thông báo **Enter to continue** thì hãy Enter._
     
        - Sau khi Enter sẽ có yêu cầu bạn nhập password root PDC để copy file và thông báo chuyển qua PDC để Enter.
    
      ![image](https://user-images.githubusercontent.com/19284401/57747887-a0535800-7701-11e9-975b-52f227a7b6b2.png)

    - **Sang PDC**

        - Sau khi Enter các bạn sẽ được yêu cầu nhập password admin domain và chuyển qua BDC để enter.
    
         ![image](https://user-images.githubusercontent.com/19284401/57747968-0213c200-7702-11e9-88ed-663bfaa21353.png)

    - **Sang BDC**

        - Nhấn Enter các bạn sẽ thấy 1 bảng thông báo về việc đồng bộ dữ liệu giữa 2 DC và yêu cầu chuyển sang PDC để Enter.
     
        ![image](https://user-images.githubusercontent.com/19284401/57748059-7f3f3700-7702-11e9-8611-6dc010891a7b.png)
        ![image](https://user-images.githubusercontent.com/19284401/57748102-b1509900-7702-11e9-8e79-5c021dfdffd9.png)

    - **Sang PDC**

        - Tương tự như ở BDC sẽ có 1 bảng thông báo về việc đông bộ giữa 2 DC và thông báo chuyển qua BDC để enter. Đồng thời host sẽ tự động reboot.
    
        ![image](https://user-images.githubusercontent.com/19284401/57748334-b82bdb80-7703-11e9-9943-f93e84db6eb0.png)
        ![image](https://user-images.githubusercontent.com/19284401/57748306-903c7800-7703-11e9-8094-0d95a3dad9c7.png)
    - Chú ý: Các bạn cần kiểm tra  phần  **0 consecutive failure(s)** để xem có xảy ra lỗi gì ko

    -  **Sang BDC**

        - Enter host sẽ tự động reboot.
        
        ![image](https://user-images.githubusercontent.com/19284401/57748368-e27d9900-7703-11e9-9110-93a42ce3d89c.png)

    - Quá trình cài đặt và cấu hình domain đã xong

#### <a name=2.3><a/>2.3 Test đồng bộ

   - Hiển thị các user đang có trong domain.
            
                 samba-tool user list
                    
        ![image](https://user-images.githubusercontent.com/19284401/57748820-ac411900-7705-11e9-9d83-0f00e4cc4dab.png)
    
    
   - Tạo user

                 samba-tool user create test
                    
     ![image](https://user-images.githubusercontent.com/19284401/57748845-d4c91300-7705-11e9-9220-4e7ddb8fac7a.png)
    
   Chú ý: phần nhập password mặc định vẫn là >7 ký tự và yêu cầu độ phực tạp nhé (123456a@)
   
  - Hiển thị các user đang có trong domain trên cả 2 DC.
            
                samba-tool user list
            
       ![image](https://user-images.githubusercontent.com/19284401/57748943-41dca880-7706-11e9-8373-30af85935666.png)
      
      
  -  Đứng trên BDC để xóa user "test"   
        
              samba-tool user delete test
        
      ![image](https://user-images.githubusercontent.com/19284401/57748989-72bcdd80-7706-11e9-80c9-c0e386193ac9.png)

  - Kiểm tra lại đồng bộ giữa 2 DC

               samba-tool user list

    ![image](https://user-images.githubusercontent.com/19284401/57749029-9b44d780-7706-11e9-9d95-b4b98ddabc2b.png)
 
    - Ok như vậy là việc đồng bộ dữ liệu giữa 2 DC không có vấn đề gì. Giờ ta đi đến cấu hình DNS.
 
#### <a name=2.4><a/>2.4 Cấu hình DNS

   - Kiếm 1 con máy win clien nào đó join vào domain thôi.

      ![image](https://user-images.githubusercontent.com/19284401/57749236-6e44f480-7707-11e9-9a55-2f5afec96ac9.png)

   - Việc join clien vào domain thì mình ko cẩn phải nó thêm nữa 
      ![image](https://user-images.githubusercontent.com/19284401/57749307-ba903480-7707-11e9-9a3c-c9d38999a6fd.png)
      ![image](https://user-images.githubusercontent.com/19284401/57749685-48205400-7709-11e9-956e-8926ccb1d31a.png)

   - Sau khi jon domain xong các bạn dowload RSAT về và cài đặt trên máy vừa join domain.

        https://www.microsoft.com/en-us/download/details.aspx?id=7887 (đây là cho win 7)

   - Sau khi cài đặt xong các bạn vào **Turn Windows Features** để bật nó lên
     ![image](https://user-images.githubusercontent.com/19284401/57749898-30959b00-770a-11e9-8773-5e2f8e1e77b6.png)
    
   - Sau đó vào
 
            Control Panel\System and Security\Administrative Tools
            
   - Mở DNS lên.

        ![image](https://user-images.githubusercontent.com/19284401/57750018-adc11000-770a-11e9-86a2-10660e19a6ef.png)

   - Hãy nhập domain vào sau đó nhấn ok 
   
   - Cách quản lý domain bgio thì không khác gì các bạn quản lý trên winserver cả.
   
   OK bài viết đến đây là hết rồi, chúc các bạn thành công.
   
--------------------------------------------------------------------------------------   
                
       

#### <a name=3><a/>3 Tham khảo
    
   1. https://www.howtoforge.com/tutorial/samba-4-with-active-directory-on-centos-7-rpm-based-installation-with-share-support/

   2. https://www.howtoforge.com/tutorial/samba-4-additional-domain-controller-for-failover-replication-on-centos-7/
   
   3. https://www.golinuxhub.com/2014/02/how-to-configure-samba-4-secondary.html

   4. https://www.tecmint.com/manage-samba4-dns-group-policy-from-windows/

#### <a name=3.1><a/>3.1 Liên hệ

<a href="https://www.facebook.com/trunglv.91" rel="nofollow">Facebook<a>
     
    
    
    


 
 

            
            
    
            









   
   
    
   
   



        


    
 
            
        


    
    
    
        

      
   
   

   
    
  
        
   
   
   
   
   
   