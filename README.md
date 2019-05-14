
### <a name="1"><a/>1. Đôi lời chia sẻ.
    
  ####  - Khái niệm domain controller có sẽ đã quá quen thuộc với các bạn, nên mình cũng không cần giới thiệu thêm.
  
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
 
  
  
  Domain trên winserver thì không có gì mà phải chia sẻ cả, vì việc cấu hình nó quá đơn giải với việc thao tác trên giao diện đồ họa. Bài viết này của mình sẽ hướng dẫn mọi người cấu hình domain controller trên linux(centos7), hay có khái niệm khác là **domain samba comtroller**.
  Việc tìm hiểu cài đặt và cấu hình nó chẳng hề đơn giản với những bạn mới bắt đầu tìm hiểu.
  
  

#### Script được mình viết bằng python3

#### Để thực hiện việc cài đặt này yêu cầu 2 host làm domain controller phải được cài đặt python3.0 trở lên.

#### Trước khi bắt đầu các bạn cần đảm bảo 2 host phải được kết nối ra internet.

Việc đầu tiên các bạn cần làm đó là cài đặt git

        yum -y install git
        
   Việc cài đặt **git** này phải được cài trên cả 2 server.
   
   Sau khi cài git xong các bạn thực hiện pull repo về
   
           git clone https://github.com/letran3691/domain.git
        
        
sau khi clone về các bạn sẽ có 1 thư mục có tên **domain**   
     
Trong thử mục **domain** các bạn quan tâm cho mình 3 file **PDC.py, BDC.py**, và **installpython3.6.sh**

   File **installpython3.6.sh**: Dùng để cài đặt python3.6

   File **PDC.py**:Dùng để cài đặt và cấu hình trên Primary domain controller.
     
   File **BDC.py**: Dùng để cài đăt và cầu hình domain backup(second domain controller) 
   
   
-  Việc đầu tiên là phải phân quyền cho file  **installpython3.6.sh** 
        
            chmod +x domain/installpython3.6.sh
         
 -  sau khi phân quyên xong các bạn thực hiện chạy file installpython3.6.sh này bằng lệnh:
 
            ./domain/installpython3.6.sh
        
        
   ![image](https://user-images.githubusercontent.com/19284401/57705211-a0b20b80-768d-11e9-92ea-b5d20b9606b0.png)

   - Quá trình cài đặt python3.6 bắt đầu (trong quá trình cài đặt, thực hiện đến bước nào thì sẽ có thông báo ở màn hình cho các bạn nắm được).
   
   - Sau khi cài đặt xong python bạn sẽ nhân được yêu cầu đặt hostname (đây sẽ là tên của primary domain controller).
         ![image](https://user-images.githubusercontent.com/19284401/57705620-69902a00-768e-11e9-9cb1-8705bb192b77.png)
         
        - Sau khi nhập **hostname** xong các bạn nhân **enter** host sẽ tự động reboot
        
   - Các bạn lại lập lại các bước vừa làm trên backup domain controller.
        ![image](https://user-images.githubusercontent.com/19284401/57706303-ae689080-768f-11e9-85ff-fe5e2f3cda58.png)
        
        
   - **Chú ý:** Các bạn tránh nhầm lẫn việc đặt hostname cho PDC vs BDC nhé, đây là 2 hostname cho 2 host các nhau không được đặt trùng.

    
   
           

         
 # Đang update.....           

        
   
   
   
   
   
   