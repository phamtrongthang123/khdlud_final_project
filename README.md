# Khoa học dữ liệu và ứng dụng
- [Khoa học dữ liệu và ứng dụng](#khoa-h-c-d--li-u-v---ng-d-ng)
  * [Thành viên nhóm](#tha-nh-vi-n-nho-m)
  * [Phân công công việc](#ph-n-c-ng-c-ng-vi--c)
- [Đề tài](#---t-i)
- [Thu thập dữ liệu](#thu-th-p-d--li-u)
- [Shopee datasets](#shopee-datasets)
- [Khám phá dữ liệu](#kha-m-pha--d---li--u)
- [Mô hình hóa dữ liệu](#m--hi-nh-ho-a-d---li--u)
  * [Sold Capability Prediction](#sold-capability-prediction)
    + [Random Forest Regression](#random-forest-regression)
      - [Dự đoán sử dụng toàn bộ features (one hot + numeric) 82 chiều:](#d---o-n-s--d-ng-to-n-b--features--one-hot---numeric--82-chi-u-)
      - [Chỉ sử dụng các numerical features (10 chiều):](#ch--s--d-ng-c-c-numerical-features--10-chi-u--)
      - [Chỉ sử dụng các features liên quan đến shop và sản phẩm (loại bỏ các feature về rating, số lượt yêu thích,...):](#ch--s--d-ng-c-c-features-li-n-quan---n-shop-v--s-n-ph-m--lo-i-b--c-c-feature-v--rating--s--l--t-y-u-th-ch---)
    + [Linear Regression](#linear-regression)
      - [Linear Regression sử dụng toàn bộ features (one hot + numeric) 82 chiều:](#linear-regression-s--d-ng-to-n-b--features--one-hot---numeric--82-chi-u-)
      - [Linear Regression chỉ sử dụng các numerical features:](#linear-regression-ch--s--d-ng-c-c-numerical-features-)
      - [Linear Regression sử dụng Mean Encoding cho các categorical features (12 chiều):](#linear-regression-s--d-ng-mean-encoding-cho-c-c-categorical-features--12-chi--u--)
    + [Neural Network Regression](#neural-network-regression)
      - [Sử dụng toàn bộ features (Onehot Encoding + numeric) 82 chiều:](#s--d-ng-to-n-b--features--onehot-encoding---numeric--82-chi--u-)
      - [Chỉ sử dụng các numerical features:](#ch--s--d-ng-c-c-numerical-features-)
      - [Sử dụng Mean Encoding cho các categorical features (12 chiều):](#s--d-ng-mean-encoding-cho-c-c-categorical-features--12-chi--u--)
  * [Review Rating Prediction](#review-rating-prediction)
    + [Dự đoán sử dụng đặc trưng TF-IDF](#d----oa-n-s---du-ng----c-tr-ng-tf-idf)
    + [Dự đoán sử dụng đặc trưng trích xuất từ mô hình BERT](#d----oa-n-s---du-ng----c-tr-ng-tri-ch-xu--t-t---m--hi-nh-bert)
  * [Image Product Category Prediction](#image-product-category-prediction)
- [Hướng dẫn chạy chương trình](#h--ng-d-n-ch-y-ch--ng-tri-nh)
  * [Thu thập dữ liệu](#thu-th--p-d---li--u)
  * [Khám phá dữ liệu](#kha-m-pha--d---li--u-1)
  * [Mô hình hóa dữ liệu](#m--hi-nh-ho-a-d---li--u-1)
- [Demo](#demo)



## Thành viên nhóm

|Họ & tên|MSSV|
|-|-|
|Lê Minh Nhật| 1712114|
|Phạm Trọng Thắng| 1712760 |

## Phân công công việc

|Công việc|Thành Viên|Mức độ hoàn thành|
|---|---|---|
|Chuẩn bị mã nguồn thu thập dữ liệu|Thắng|100%|
|Thu thập dữ liệu|Nhật, Thắng|100%|
|Khám phá dữ liệu|Thắng|100%|
|Xử lý và mô hình hóa dữ liệu để giải quyết bài toán|Nhật|100%|
|Báo cáo kết quả|Thắng, Nhật|100%|

# Đề tài 

**Dự đoán khả năng bán của cửa hàng trên shopee. (Sold Capability Prediction)**

Nhóm nhận thấy khi cửa hàng khi đăng sản phẩm lên để bán online thì sẽ quan tâm nhiều vấn đề, trong đó cũng có mong muốn biết khả năng bán của sản phẩm. Dựa trên tâm lý này nên nhóm chọn shopee làm nguồn dữ liệu cho bài toán Dự đoán khả năng bán của cửa hàng trên shopee.

Mục đích của đề tài này là khám phá và phát triển một phương pháp có thể dựa vào những dữ liệu đã có để dự đoán sản phẩm mới mà shop tính đăng bán. 

Bên cạnh đề tài lớn, nhóm cũng tìm hiểu và phát triển 2 đề tài nhỏ dựa trên các dữ liệu thu thập được mà nhóm thấy chưa ứng dụng nhiều đó là **Image Product Category Prediction** và **Review Rating Prediction**. 

# Thu thập dữ liệu

Khi vào trang chủ shopee, nhóm chọn các danh mục rồi gọi query theo page để lấy dữ liệu cho tập search. Có tổng cộng 16 danh mục được chọn: `AUDIO, CAPSAC, CHUOTBANPHIM, DIENTHOAI, GAYCHUPHINH, LAPTOP, LINHKIENMAYTINH, MAYBAN, MAYTINHBANG, MIENGDAN, OCUNG, PHUKIEN, PINSAC, SIM, THIETBIMANG, VOBAOOPLUNG`. Mỗi danh mục được crawl tối đa 1000 sản phẩm. Tổng cộng nhóm crawl được 15648 sản phẩm. Tất cả đều được crawl bằng selenium (parse html), được crawl chứa càng nhiều thông tin có thể càng tốt, trong đó quan trọng nhất phải lưu được url dẫn tới trang chi tiết của sản phẩm. Các dữ liệu được lưu trong file `search_15k6.csv`

Với mỗi url trong dữ liệu search 15k6 trên, nhóm dùng selenium để tiếp tục parse html, tuy nhiên vì trở ngại thời gian, parse 100 url tốn khoảng 1 tiếng do trang web load nhiều thành phần bằng js (phải scroll tới đúng vị trí mới chịu load) nên nhóm đã đổi cách crawl, nhóm kiểm tra khi load web shopee sẽ gọi tới đâu để lấy thông tin parse thì phát hiện shopee có gửi query về server với cú pháp đủ đơn giản. Do đó nhóm sử dụng query này để kéo từng gói thông tin của từng url, một lần lấy sẽ phải gọi tới 3 query khác nhau, sau đó nhóm dùng nó làm dữ liệu cho phần thông tin chi tiết sản phẩm. Dữ liệu được lưu trong file items.csv, ngoài ra 100 link url đã parse bởi html cũng được lưu trong file `items_100_sorted_id.csv`

Bên cạnh thông tin chi tiết cho của từng url, nhóm cũng crawl thêm phần bình luận với mong muốn sử dụng các phương pháp xử lý ngôn ngữ tự nhiên để hỗ trợ giải quyết bài toán chính. Cách crawl và thời gian crawl cũng lâu tương tự như dữ liệu items.csv nên nhóm cũng sử dụng query để có thể tải đủ cho 15k6 dòng items. Dữ liệu được lưu trong file `items_cmt_sorted_id.csv`, ngoài ra 100 link url đã parse bởi html cũng được lưu trong file `items_cmt_100.csv`. 

Tuy nhiên sau khi kiểm tra thì thấy dữ liệu bình luận bị bias quá nhiều về đánh giá 5 sao, cho nên nhóm đã lọc ra các sản phẩm phải có ít nhất 1 bình luận ở mỗi loại sao đánh giá, sau đó crawl các url này, mỗi url sẽ lấy max là 2 bình luận mỗi loại để tránh bias lớn về phía 5 sao. Dữ liệu được lưu tại `items_cmt_eachrate2cmt.csv`


Hướng crawl là search -> items -> items_cmt

Notebook dùng để crawl gồm: 
- `crawling_search.ipynb` dành cho crawl dữ liệu search
- `crawling_product.ipynb` dành cho crawl bộ items
- `crawling_product_api.ipynb` dành cho crawl bộ items sử dụng query mà shopee dùng để parse data cho từng trang.
- `crawling_product_cmt.ipynb` dành cho crawl bộ items_cmt

Trong đó khi crawl sẽ import file `cssselector.py`, lưu những css selector đến vị trí cần lấy thông tin. 

# Shopee datasets

Gồm 3 bộ chính search, items và items_cmt với ý nghĩa lần lượt là sản phẩm được tìm kiếm bên trang search, thông tin chi tiết sản phẩm và bình luận đối với sản phẩm.

Có 2 bộ chính: bộ 100 dòng và 15k6 dòng sản phẩm. 

Bộ 100 dòng gồm các file: 
- `search_100.csv` cho dữ liệu search
- `items_100_sorted_id.csv` cho dữ liệu items
- `items_cmt_100.csv` cho dữ liệu items_cmt 

Bộ 15k6 dòng gồm:
- `search_15k6.csv` cho dữ liệu search
- `items.csv` cho dữ liệu items
- `items_cmt_sorted_id.csv` cho dữ liệu items_cmt 
- `items_cmt_eachrate2cmt.csv` cho dữ liệu items_cmt với điều kiện là items tương ứng có ít nhất 1 bình luận ở mỗi loại rate, và khi crawl sẽ lấy maximum 2 bình luận cho mỗi loại rate.

**Tổng quan và mô tả dữ liệu được sử dụng:**

- **search_15k6.csv:** 15648 dòng, 7 cột

|    | Column       | Dtype   | Description                                         |
|---:|:-------------|:--------|:----------------------------------------------------|
|  0 | name         | string  | Tên của sản phẩm                                    |
|  1 | category     | string  | Nhóm sản phẩm                                       |
|  2 | n_sold       | float64 | Số lượng sản phẩm đã bán                            |
|  3 | price        | float64 | Giá tiền của sản phẩm                               |
|  4 | shop_address | string  | Địa chỉ của shop                                    |
|  5 | image_url    | string  | Url của thumbnail sản phẩm                          |
|  6 | url          | string  | Url tới sản phẩm (phục vụ việc crawl dữ liệu items) |

**Ví dụ:** 

|    | name                                                             | category   |   n_sold |     price | shop_address    | image_url                                                     | url                                                                                                                                                |
|---:|:-----------------------------------------------------------------|:-----------|---------:|----------:|:----------------|:--------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | Điện thoại OPPO A37 Fullbox Mới - 2GB/16GB - Bảo hành 12 tháng - | DIENTHOAI  |     7800 | 1.299e+06 | TP. Hồ Chí Minh | https://cf.shopee.vn/file/654146756efe4b5fe7cf516a2221b153_tn | https://shopee.vn/%C4%90i%E1%BB%87n-tho%E1%BA%A1i-OPPO-A37-Fullbox-M%E1%BB%9Bi-2GB-16GB-B%E1%BA%A3o-h%C3%A0nh-12-th%C3%A1ng--i.48782032.6841251055 |
|  1 | điện thoại Samsung Galaxy S7 chính hãng / full chức năng         | DIENTHOAI  |     6600 | 1.899e+06 | TP. Hồ Chí Minh | https://cf.shopee.vn/file/622be579c39efa0ea92b8659aebfb90a_tn | https://shopee.vn/%C4%91i%E1%BB%87n-tho%E1%BA%A1i-Samsung-Galaxy-S7-ch%C3%ADnh-h%C3%A3ng-full-ch%E1%BB%A9c-n%C4%83ng-i.48782032.7241163781         |
---
- **items.csv:** 15638 dòng, 21 cột, cột cần được dự đoán là n_sold


|    | Column             | Dtype   | Value range   | Description                                                                                                            |
|---:|:-------------------|:--------|:--------------|:-----------------------------------------------------------------------------------------------------------------------|
|  0 | id                 | int64   | >= 0          | id của sản phẩm tại dòng tương ứng với index từ search_15k6, dùng để map sang bộ dữ liệu lưu bình luận                 |
|  1 | name               | string  | nan           | Tên của sản phẩm                                                                                                       |
|  2 | avg_rating         | float64 | 1 - 5         | Rating trung bình của sản phẩm                                                                                         |
|  3 | n_reviews          | int64   | >= 0          | Số lượng đánh giá cho sản phẩm                                                                                         |
|  4 | n_sold             | float64 | >= 0          | Số lượng sản phẩm đã bán                                                                                               |
|  5 | price              | float64 | > 0           | Giá tiền của sản phẩm                                                                                                  |
|  6 | n_loved            | int64   | >= 0          | Số lượt yêu thích cho sản phẩm                                                                                         |
|  7 | n_rate_5           | int64   | >= 0          | Số lượng người đánh giá với 5 sao                                                                                      |
|  8 | rate_4             | int64   | >= 0          | Số lượng người đánh giá với 4 sao                                                                                      |
|  9 | rate_3             | int64   | >= 0          | Số lượng người đánh giá với 3 sao                                                                                      |
| 10 | rate_2             | int64   | >= 0          | Số lượng người đánh giá với 2 sao                                                                                      |
| 11 | rate_1             | int64   | >= 1          | Số lượng người đánh giá với 1 sao                                                                                      |
| 12 | rate_with_cmt      | int64   | >= 2          | Số lượng người đánh giá có bình luận                                                                                   |
| 13 | rate_with_imgvid   | int64   | >= 3          | Số lượng người đánh giá có bình luận đính kèm hình ảnh / video                                                         |
| 14 | shop_name          | string  | nan           | Tên chủ shop bán                                                                                                       |
| 15 | shop_n_review      | int64   | >= 0          | Số lượng đánh giá cho shop bán                                                                                         |
| 16 | shop_n_product     | int64   | > 0           | Số lượng sản phẩm của shop                                                                                             |
| 17 | shop_rate_feedback | float64 | >=0           | Tỉ lệ phản hồi của shop                                                                                                |
| 18 | shop_time_feedback | float64 | > 0           | Thời gian phản hồi của shop (được tính bằng giây)                                                                      |
| 19 | shop_age           | float64 | > 0           | Thời gian shop tham gia (tuổi của shop từ ngày tạo trên hệ thống shopee, được tính bằng giây từ lúc thành lập tới nay) |
| 20 | shop_follower      | int64   | nan           | Số lượng người theo dõi shop                                                                                           |

**Ví dụ:** 

|    |   id | name                                                             |   avg_rating |   n_reviews |   n_sold |     price |   n_loved |   n_rate_5 |   rate_4 |   rate_3 |   rate_2 |   rate_1 |   rate_with_cmt |   rate_with_imgvid | shop_name        |   shop_n_review |   shop_n_product |   shop_rate_feedback |   shop_time_feedback |    shop_age |   shop_follower |
|---:|-----:|:-----------------------------------------------------------------|-------------:|------------:|---------:|----------:|----------:|-----------:|---------:|---------:|---------:|---------:|----------------:|-------------------:|:-----------------|----------------:|-----------------:|---------------------:|---------------------:|------------:|----------------:|
|  0 |    0 | Điện thoại OPPO A37 Fullbox Mới - 2GB/16GB - Bảo hành 12 tháng - |      4.95238 |          42 |     7800 | 1.299e+06 |      3733 |         40 |        2 |        0 |        0 |        0 |              39 |                 32 | thinhphat_mobile |            2331 |              259 |                   79 |                 6397 | 9.44918e+07 |           25619 |
|  1 |    1 | điện thoại Samsung Galaxy S7 chính hãng / full chức năng         |      4.90909 |          33 |     6600 | 1.899e+06 |      3063 |         32 |        0 |        0 |        1 |        0 |              31 |                 29 | thinhphat_mobile |            2331 |              259 |                   79 |                 6397 | 9.44918e+07 |           25620 |

---
- **items_cmt_eachrate2cmt.csv:** 23297 dòng, 3 cột

|    | Column   | Dtype   | Description                                                                                            |
|---:|:---------|:--------|:-------------------------------------------------------------------------------------------------------|
|  0 | id       | int64   | id của sản phẩm tại dòng tương ứng với index từ search_15k6, dùng để map sang bộ dữ liệu lưu bình luận |
|  1 | rating   | int64   | Rating mà người dùng quyết định                                                                        |
|  2 | content  | string  | Nội dung của bình luận của người dùng cho rating trên   

**Ví dụ:** 

|    |   id |   rating | content                                                                                             |
|---:|-----:|---------:|:----------------------------------------------------------------------------------------------------|
|  0 |    2 |        5 | Giao hàng hơi lâ. Chưa bóc gói hàng nên k biết hàng hoá ra sao nữa                                  |
|  1 |    2 |        5 | e đã nhận hàng nha shop . máy rất deph . máy bao gồm pin và sạc rất rẻ và máy xài rất ok ...... . . |
|  2 |    2 |        4 | Mới mua lần đầu. Cầm chắc tay. Chất lượng chưa kiểm chứng.                                          |

# Khám phá dữ liệu 

Phần này nhóm tập trung khám phá dữ liệu để phục vụ hỗ trợ cho phần mô hình hóa dữ liệu, do đó câu hỏi lớn sẽ là: **Những thuộc tính đã có sẽ ảnh hưởng thế nào đến việc dự đoán số lượng bán của một sản phẩm?**.

Dựa vào câu hỏi thì nhóm em chỉ tập trung EDA tập items.csv vì 2 bộ dữ liệu kia không phù hợp. Bên cạnh đó dựa vào bảng mô tả của items.csv, ban đầu nhóm nghĩ là tất cả các yếu tố có tính chất số học được crawl đều sẽ ảnh hưởng, đặc biệt là số yêu thích, số đánh giá và rating trung bình. 

Tuy nhiên sau khi tính toán correlation, dữ liệu cho thấy chỉ có số lượng đánh giá và các yếu tố tương tự là có mối tương quan đủ lớn (nhóm chọn threshold là 0.3, tham khảo trên mạng thì với giá trị corr x, |x| >= 0.3 tức là x đại diện cho độ tương quan vừa phải). Còn số yêu thích và rating trung bình đều không thỏa. Từ đây nhóm đặt ra câu hỏi: **Từ đâu mà 2 thuộc tính kia đều không thỏa yêu cầu corr mà nhóm đặt ra?**

Đối với câu hỏi trên, nhóm dựa trên quan sát lúc crawl dữ liệu là có những sản phẩm chỉ bán có 1, 2 sản phẩm nhưng đánh giá trung bình là 5 sao, đối với lượng yêu thích là vì có những sản phẩm người dùng chỉ quan tâm mua mà không đánh dấu yêu thích. Dựa vào quan sát này nhóm đã thử lấy top sản phẩm bán ít nhất, và thấy được là việc dựa vào đánh giá trung bình là không đánh tin cậy vì đúng là nhiều sản phẩm bán ít mà vẫn 5 sao. Tương tự, nhóm in ra các sản phẩm bán chạy nhất thì thấy thuộc tính yêu thích rất ngẫu nhiên nếu nhìn chung các sản phẩm, tức là bán nhiều nhưng yêu thích rất thấp, hoặc trung bình, hoặc cao. Tuy nhiên nếu lọc riêng ra lấy tên shop nào đó thì giá trị tương quan lại cao, do đó vẫn có thể dùng được số lượng yêu thích vào mô hình hóa dữ liệu. 

Bên cạnh các thuộc tính, nhóm cũng mong muốn có thể tìm một metric để phục vụ việc đánh giá mô hình dự đoán. Nhóm dự định sử dụng một metric sử dụng độ chênh lệch làm accuracy, gọi là ***Soft Interval Accuracy (SIA)***, tuy nhiên có 1 hyperparameter phải lựa chọn là epsilon (metric này có nghĩa là cho trước 1 giá trị epsilon, một dự đoán được xem là đúng (True) khi nó có giá trị nằm trong khoảng $(y - epsilon, y + epislon)$  hay $|y - \hat{y}| < eps$ với $y$ là groundtruth label và $\hat{y}$ là giá trị dự đoán). Từ dữ liệu nhóm vẽ ra distribution plot để xem thì phát hiện rất nhiều giá trị `n_sold` thấp hơn 1000, xem bảng mô tả của pandas thì thấy 75% sản phẩm đều có `n_sold` thấp như thế. Việc quan sát này đã giúp cho nhóm giới hạn lại epsilon cho phù hợp với đa số sản phẩm được thu thập.

Ở trên nhóm đã trình bày mô tả sơ lược kết quả và quá trình tìm hiểu. Chi tiết các lệnh gọi và kết quả đều nằm trong notebook `eda.ipynb`. 

# Mô hình hóa dữ liệu
## Sold Capability Prediction
Metrics đánh giá mà nhóm sử dụng: ***Mean Absolute Error (MAE)*** hoặc ***Soft Interval Accuracy (SIA)***
Các features sử dụng cho việc dự đoán: 

|Feature name | Type | 
|---|---|
|category |categorical|
|price|numerical|
|shop_address|categorical |
|avg_rating|numerical|
|n_reviews|numerical|
|n_loved|numerical|
|shop_n_review|numerical|
|shop_n_product|numerical|
|shop_rate_feedback|numerical|
|shop_time_feedback|numerical|
|shop_age|numerical|
|shop_age|numerical|

Ta sẽ phân chia dữ liệu thành các tập `train - validation - test` set theo tỉ lệ: `60% - 20% - 20%`
### Random Forest Regression
#### Dự đoán sử dụng toàn bộ features (one hot + numeric) 82 chiều:

Kết quả:

|Dataset|MAE|
|-|-|
|train| 159.64|
|val| 413.99|
|test| 472.69|

*Ghi chú*: do kết quả dự đoán có thể lên đến đơn vị nghìn (lượt bán), để dễ giải thích, ta sẽ sử dụng độ đo `MAE` (thay vì `MSE` như thông thường). Do đó ta có thể đánh giá `MAE` trên tập test ~473 có nghĩa là mô hình dự đoán trung bình sai số khoảng 473 cho một sản phẩm trong tập test.

Bây giờ ta sẽ xét `SIA` metric. 

- Với `epsilon = 1000` (cho phép sai số dự đoán lên đến 1k lượt bán):
    |Dataset | SIA-1000|
    |-|-|
    |train | 0.975|
    |val   | 0.919|
    |test  | 0.921|

- `epsilon = 500` (cho phép sai số dự đoán lên đến 500 lượt bán):
    |Dataset | SIA-500|
    |-|-|
    |train| 0.944|
    |val  | 0.843|
    |test | 0.835|


- `epsilon = 200` (cho phép sai số dự đoán lên đến 200 lượt bán):
    |Dataset | SIA-2000|
    |-|-|
    | train| 0.861|
    | val  | 0.67|
    | test | 0.67|
***Nhận xét***: ta thấy mô hình đạt được độ chính xác khá tốt. Hiệu năng trên tập `val` và `test` xấp xỉ nhau. Tuy nhiên khi xem xét `MAE` metric, kết quả trên tập `test` và `val` có một sự chênh lệch nhất định. Điều này có thể là do có một số sản phẩm (hoặc hệ số nào đó) làm lệch kết quả dự đoán.


---

#### Chỉ sử dụng các numerical features (10 chiều):
`price, avg_rating, n_reviews,n_loved, shop_n_review, shop_n_product, shop_rate_feedback, shop_time_feedback, shop_age, shop_follower`
(Bỏ đi `category` và `shop_address`)

Kết quả:

|Dataset|MAE|SIA-1000|SIA-500|SIA-200|
|---|---|---|---|---|
|train|169.52|0.975|0.942|0.853|
|val|433.01|0.916|0.835|0.641|
|test|491.87|0.909|0.825|0.655|


---

#### Chỉ sử dụng các features liên quan đến shop và sản phẩm (loại bỏ các feature về rating, số lượt yêu thích,...):
`category, price, shop_address, shop_n_review, shop_n_product, shop_rate_feedback, shop_time_feedback, shop_age, shop_follower`
(Bỏ đi `avg_rating, n_reviews, n_loved`)

Kết quả: 

|Dataset|MAE|SIA-1000|SIA-500|SIA-200|
|---|---|---|---|---|
|train|317.349|0.943|0.877|0.723|
|val|805.426|0.824|0.700|0.492|
|test|906.455|0.831|0.708|0.490|

***Nhận xét***: Ta thấy kết quả dự đoán có độ chính xác giảm mạnh so với 2 thử nghiệm trên (có sử dụng feature liên quan đến rating, yêu thích).Ta thấy mô hình xảy ra hiện tượng overfitting khá nặng (hiệu năng trên tập `val, test` thấp hơn nhiều so với `train`, giảm khả năng tổng quát hóa của mô hình trên dữ liệu không có trong huấn luyện. (lưu  là mô hình Decision Tree và Random Forest là các mô hình có variance cao, do đó ta cần thận trọng trong việc lựa chọn các đặc trưng) Do đó ta có thể kết luận các features này đóng vai trò rất quan trọng trong việc dự đoán chính xác khả năng bán của sản phẩm.


---

### Linear Regression
Ta sẽ tiến hành thực nghiệm trên một mô hình đơn giản hơn là Linear Regression.
Trước khi huấn luyện mô hình, ta sẽ chuẩn hóa các features theo phương pháp Z-score normalization:

\begin{equation}
    Z_i = \frac{X_i - \mu}{\sigma}
\end{equation}

#### Linear Regression sử dụng toàn bộ features (one hot + numeric) 82 chiều:

|Dataset|MAE|SIA-500|SIA-200|
|---|---|---|---|
|train|615.818|0.721|0.473|
|val|548840935861.995|0.702|0.451|
|test|433296680921.950|0.708|0.467|

***Nhận xét***: Ta thấy mô hình Linear Regression có `SIA` thấp hơn so với khi sử dụng Random Forest khá nhiều. Hơn nữa, ta thấy mô hình có `MAE` trên tập `val` và tập `test` cao bất thường. Sau khi tìm hiểu nguyên nhân thì ta nhận thấy có một vài hệ số (coefficient) của một số feature có giá trị rất cao (Ví dụ như `8.94728651e+14`). Hơn nữa, ta nhận thấy các hệ số này thuộc về feature `shop_address` (onehot). Nguyên nhân có thể là do việc tối ưu hàm mất mát (sử dụng phương pháp Ordinary Least Square để nghịch đảo một ma trận thưa (sparse matrix)). Để khắc phục, ta sẽ sử dụng `L2 Regularization` (Ridge) để giới hạn giá trị của các hệ số.

Kết quả khi sử dụng Ridge Regression (cùng với việc tinh chỉnh hyperparameter $\alpha$ tốt nhất sử dụng phương pháp GridSearch trên tập `val`), ta có kết quả như sau:

`Best cross-validation MAE: 582.711 
with alpha = 10.0`

|Dataset|MAE|SIA-500|SIA-200|
|---|---|---|---|
|train|609.247|0.721|0.473|
|val|582.710|0.704|0.453|
|test|615.954|0.707|0.467|

Ta thấy hiệu năng của mô hình thấp hơn phương pháp Random Forest khá nhiều (kể cả trên tập `train`). Điều này có thể là do mô hình vẫn chưa đủ phức tạp để nắm bắt được hết các thông tin từ input , đặc biệt là đối với các categorical feature chăng? (Ta sẽ kiểm chứng điều này trong phần Neural Network Regression - có thể coi như 1 phiên bản nâng cấp của Linear Regression :) )


---

#### Linear Regression chỉ sử dụng các numerical features:

Kết quả:

|Dataset|MAE|SIA-500|SIA-200|
|---|---|---|---|
|train|600.929|0.764|0.399|
|val|567.050|0.769|0.389|
|test|612.985|0.745|0.406|



***Nhận xét***: ta thấy kết quả `MAE` và `SIA-500` có phần cao hơn so với khi sử dụng các categorical features. Tuy nhiên `SIA-200` lại thấp hơn khá nhiều, do đó ta khó có thể đưa ra kết luận là việc sử dụng các features nào sẽ cho kết quả tốt hơn trong thực tế. Ta có thể dự đoán rằng việc `SIA-200` trong phần này thấp hơn khá nhiều so với việc sử dụng toàn bộ features là do thông tin của sản phẩm vẫn chưa đủ để mô hình có thể khớp được với dữ liệu đầu ra (hay nói cách khác là underfit), nhất là các mẫu dữ liệu có lượt bán thấp (<1000 chẳng hạn). Bằng chứng là `SIA-200` trên tập `train` khá thấp, trái ngược với mô hình phức tạp hơn là Random Forest (Linear Regression là mô hình thường có bias khá cao và variance thấp). Do vậy nhóm đưa ra đánh giá: các categorical features (`category` và `shop_address`) vẫn hữu ích trong việc dự đoán khả năng bán.
Tiếp theo ta sẽ thử sử dụng Mean Encoding thay thế cho One Hot Encoding (đối với categorical feature)


---

#### Linear Regression sử dụng Mean Encoding cho các categorical features (12 chiều):
Kết quả:

|Dataset|MAE|SIA-500|SIA-200|
|---|---|---|---|
|train|602.964|0.755|0.434|
|val|565.976|0.765|0.425|
|test|611.147|0.743|0.430|

Ta thấy kết quả có phần ổn định hơn so với 2 phần trên (xét toàn bộ metrics thì hiệu năng nằm ở khoảng giữa so với 2 mô hình ở trên). Lưu ý khi sử dụng Mean Encoding: đối với các giá trị categorical không xuất hiện trong tập `train`, ta sẽ mặc định gán cho nó giá trị `0` thay vì giá trị mean của các label. Ngoài ra, ta thấy kết quả trên tập train cũng xấp xỉ kết quả trên tập val và test (ngược lại với mô hình Random Forest có độ lỗi trên tập train thấp hơn rất nhiều so với val và test). Có thể là do mô hình Linear Regression chưa phải là phù hợp nhất với tập dữ liệu của ta (lưu ý là Linear Regression có thể đưa ra kết quả dự đoán mang giá trị âm)


---


### Neural Network Regression
Tương tự như Linear Regression , ta sẽ tiền xử lý input bằng việc chuẩn hóa các features theo phương pháp Z-score normalization.
Ta sẽ thực nghiệm với 1 mạng Neural Network nhỏ như sau:

```
Input Vector -> FC(32 units) + ReLU -> FC(64 units) + ReLU -> Output (1 unit) + ReLU
```
Nguyên nhân ta sử dụng hàm ReLU activation lên output (thay vì Linear) là do ta muốn các giá trị dự đoán đều không âm.
Với weights của mỗi layer, ta sẽ sử dụng `L2-Regularization` với $\alpha$ =0.1 để hạn chế việc overfitting.
Hàm mất mát ta sẽ sử dụng là hàm `MAE`:

\begin{equation}
    L(y, \hat{y}) = \frac{1}{N} \sum_{i=0}^{N}|y -     {\hat{y}}_i|
\end{equation}

#### Sử dụng toàn bộ features (Onehot Encoding + numeric) 82 chiều:

|Dataset|MAE|SIA-500|SIA-200|
|---|---|---|---|
|train|405.848|0.867|0.727|
|val|391.498|0.852|0.693|
|test|428.935|0.843|0.694|

---

#### Chỉ sử dụng các numerical features:

|Dataset|MAE|SIA-500|SIA-200|
|---|---|---|---|
|train|449.249|0.840|0.710|
|val|414.424|0.836|0.700|
|test|474.167|0.823|0.689|

---

#### Sử dụng Mean Encoding cho các categorical features (12 chiều):

|Dataset|MAE|SIA-500|SIA-200|
|---|---|---|---|
|train|433.238|0.851|0.723|
|val|401.349|0.848|0.714|
|test|457.555|0.836|0.707|

***Nhận xét***: Đối với mô hình Neural Network, Mean Encoding dường như phù hợp hơn so với khi sử dụng Onehot Encoding với khi ta cần quan tâm đến sai số dự đoán một cách chặt chẽ hơn (`SIA-200`). (còn với `MAE` và `SIA-500` thì Onehot lại tốt hơn).

**KẾT LUẬN**: thực nghiệm cho thấy 2 mô hình cho kết quả tốt nhất là Random Forest và Neural Network với việc sử dụng toàn bộ các features. Tuy nhiên mô hình Neural Network có thời gian huấn luyện khá lâu so với Random Forest. Hơn nữa, nhóm nhận thấy metric đánh giá `SIA-200` là phù hợp với tập dữ liệu này, nguyên nhân là vì trong phần **EDA**, ta thấy phần lớn các sản phẩm đều có số lượt bán thấp (75% dữ liệu có số lượt bán dưới 1000). Do đó mà việc giới hạn sai số dự đoán (epsilon) thấp sẽ cho ta đánh giá phù hợp với mong muốn hơn.

## Review Rating Prediction
Trong quá trình thu thập dữ liệu, nhóm nhận thấy có một số dữ liệu nhiễu làm ảnh hưởng đến rating của sản phẩm, ví dụ như review giả, comment spam, abc xyz các kiểu, review chê nhưng rating lại cao hay ngược lại,... Nên nhóm dự định sẽ áp dụng các kỹ thuật xử lý ngôn ngữ tự nhiên (NLP) và máy học với mong muốn điều chỉnh lại các rating cho sản phẩm, cụ thể là dự đoán Rating (số sao đánh giá mang giá trị rời rạc từ 1 đến 5) của sản phẩm dựa trên văn bản của một lượt review của khách hàng.

Metrics đánh giá mà nhóm sử dụng: ***Class Accuracy*** *(Acc.)*

Ta sẽ phân chia dữ liệu thành các tập `train - validation - test` set theo tỉ lệ: `60% - 20% - 20%`

Trong phần này, ta sẽ thực nghiệm với phương pháp trích xuất đặc trưng văn bản là **TF-IDF** và phương pháp sử dụng học sâu, cụ thể ở đây là mô hình **BERT** (Bidirectional Encoder Representations from Transformers).

Vì dữ liệu ở đây có dạng văn bản thô nên ta sẽ tóm tắt quá trình tiền xử lý dữ liệu như sau:

* Xóa các dấu câu (. , ! ? ..etc..) ở giữa và cuối mỗi câu đối với 1 review comment (optional)
* Phân đoạn các từ (word segmenting), các từ ghép có ý nghĩa sẽ được coi là một từ:
    vd: hàng hóa => hàng_hóa
	(Bước này rất quan trọng khi sử dụng mô hình     BERT)
* Lọc ra các từ có khả năng là spam (vd: từ có tần suất xuất hiện trong toàn bộ tập dữ liệu < ngưỡng nào đó). Sau đó ta sẽ lọc các review comment mà chỉ chứa những từ spam (optional)

### Dự đoán sử dụng đặc trưng TF-IDF
Ta sẽ sử dụng thư viện sklearn để trích xuất đặc trưng TF-IDF từ tập `train`
```
extractor = TfidfVectorizer(min_df=5, max_df=0.8, max_features=768)
extractor.fit(X_train)
```
Trong đó:
`min_df=5` có nghĩa là ta sẽ chỉ xét những từ nào xuất hiện lớn hơn 5 lần trong toàn bộ dữ liệu (thấp hơn có thể là từ spam)
`max_df=0.8` có nghĩa là sẽ chỉ xét những từ nào có tần suất xuất hiện dưới 80% trong toàn bộ dữ liệu (các từ xuất hiện có thể là các stop_word)

Sau khi trích xuất ra các features, tám tiến hành thực nghiệm việc huấn luyện một số mô hình phân lớp dựa trên các features này. Kết quả được cho trong bảng sau:

|Method|train acc.|val acc.|test acc.|
|-|-|-|-|
|Linear SVM|0.543| 0.485| 0.486|
|Softmax Regression|0.565|0.482|0.488|
|Random Forest|0.951|0.438|0.431|
|Neural Network|0.5424|0.4966|0.5021|

Trong đó mô hình Neural Network mà nhóm thực nghiệm có kiến trúc khá đơn giản như sau (ta sẽ 	huấn luyện và chọn bộ trọng số có accuracy tốt nhất trên tập `val` và tiến hành đánh giá):
```
Input Vector -> FC(256) + ReLU -> FC(256) + ReLU -> Dropout(p=0.5) -> Output(5) + Softmax
```
Ở đây ta sẽ sử dụng Dropout với xác suất `p=0.5` để hạn chế overfitting.


***Nhận xét***: ta thấy mô hình cho kết quả tốt nhất vẫn là Neural Network, mô hình Random Forest dường như bị vấn đề overfitting khá nặng. Lưu ý ở đây là nhóm đã thử số lượng features lớn hơn 768 nhưng kết quả cũng không có quá nhiều sự khác biệt, mà còn gia tăng độ phức tạp của mô hình.Ngoài ra trong quá trình huấn luyện các mô hình, nhóm đã tinh chỉnh các giá trị hyperparameter bằng tay (để tìm ra giá trị tối ưu) nên có thể các giá trị ở đây chỉ mang tính tham khảo



---


### Dự đoán sử dụng đặc trưng trích xuất từ mô hình BERT

Trong phần này ta sẽ sử dụng mô hình BERT đã được pretrained cho tiếng Việt (cụ thể là các văn bản tin tức và wiki), hay phoBERT
```
Dat Quoc Nguyen, & Anh Tuan Nguyen (2020). PhoBERT: Pre-trained language models for Vietnamese. In Findings of the Association for Computational Linguistics: EMNLP 2020 (pp. 1037–1042)
```

Một số lưu ý khi sử dụng phoBERT làm feature extractor:
- Độ dài một sequence tối đa khi đưa vào phobert là `256`, do đó ta sẽ tiến hành truncate các văn bản có độ dài vượt quá `max_sequence_length`, và padding các văn bản có độ dài ngắn hơn. 
- Output của mô hình BERT sẽ là 1 tensor có số chiều `(N, sequence_length, 768)`. 
- Ta sẽ sử dụng vector ứng với token đầu tiên (`<cls>` token), vector này là vector mã hóa đại diện cho toàn bộ văn bản (khi được train trên task Next Sentence Prediction). Ta sẽ lấy vector 768 chiều này làm vector đặc trưng và tiến hành huấn luyện một mô hình classifier dựa trên đó.

Do dữ liệu văn bản ở đây chưa đủ lớn nên ta sẽ fine-tune mô hình bằng việc đóng băng các trọng số của BERT, chỉ cần huấn luyện bộ classifier.

Kết quả thu được:
|Method|train acc.|val acc.|test acc.|
|---|---|---|---|
|Linear SVM|0.535|0.494|0.479|
|Softmax Regression|0.542|0.495|0.484
|Random Forest|0.983|0.349|0.354|
|Neural Network|0.584|0.490|0.489|

***Nhận xét***: ta thấy kết quả khi sử dụng đặc trưng từ phoBERT chưa thực sự tốt như mong đợi (trong lúc huấn luyện nhóm đã thử việc xóa các dấu câu và lọc ra các văn bản spam, tuy nhiên kết quả thu được lại không tốt bằng việc chỉ sử dụng word segmentation). Nguyên nhân BERT chưa được tốt có lẹ là do mô hình này được huấn luyện trên văn bản tin tức và wiki, còn dữ liệu của ta lại là các bình luận đời thường, do đó có phân phối rất khác so với dữ liệu được pretrained. Ngoài ra, ngữ vựng của cả 2 tập dữ liệu khá khác nhau (tập shopee reviews còn chứa khá nhiều từ bị lỗi chính tả, sai cú pháp,...) => Feature nhận được chưa thực sự tốt, dẫn đến việc mô hình phân lớp bị overfitting (Ở đây ta đã early-stopping khi huấn luyện để chọn mô hình có validation accuracy cao nhất)
Nhóm đề xuất nếu có thời gian finetune lại toàn bộ mô hình BERT và huấn luyện lại cả bộ tokenizer (vocabulary) thì kết quả có thể sẽ tốt hơn nhiều.


## Image Product Category Prediction

Khi shop đăng bán các sản phẩm, đôi khi có những mục không rõ ràng là vì sản phẩm không rõ ràng, hoặc sản phẩm thuộc nhiều danh mục, hoặc shop muốn tự động hóa quá trình chọn (vì shopee có quá nhiều danh mục để chọn) thì có thể shop mong muốn đưa sản phẩm của mình vào nơi phù hợp nhất mà tốn ít công sức tìm hiểu nhất. Dựa trên dữ liệu ảnh thu thập được, nhóm mong muốn áp dụng một mô hình phân loại sản phẩm dựa trên hình ảnh.

Về việc thu thập dữ liệu hình ảnh, ta sẽ dựa trên trường `image_url` trong file `search_15k6.csv` với nhãn tương ứng là `category` (Do điều kiện giới hạn nhóm chỉ thu thập 16 loại sản phẩm khác nhau).

Sau khi thu thập dữ liệu, nhóm sẽ tiến hành chia thành các tập `train` `val` và `test` theo tỉ lệ: 70% - 10% - 20% (Kèm theo xóa các file ảnh bị hư, lỗi).
Số lượng ảnh trong từng tập con:

|Dataset|No. of images|
|---|---|
|train|11261|
|val|1253|
|test|3131|
|Total|15645|

Dữ liệu ảnh thu thập được có trong các thư mục 
- `data/images` (chưa chia subset)
- `data/images_splitted` (đã chia train -val - test)

Nhóm sử dụng mô hình ResNet-50 được huấn luyện sẵn trên tập ImageNet để làm baseline model, sau đó tiến hành fine-tune trên dữ liệu thu thập được. Kết quả thu được trong bảng sau:

|Dataset|Accuracy|
|-|-|
|train|0.9853|
|val|0.7590|
|test|0.7614|

Có thể thấy mô hình có độ chính xác khá tốt.




# Hướng dẫn chạy chương trình

## Thu thập dữ liệu

Nhóm giả định người dùng notebook crawling sẽ dùng mạng trong điều kiện thông thường. Nếu khác đường truyền (yếu hơn) thì có thể dẫn đến việc treo máy vẫn không lấy đủ dữ liệu. 

Bên dưới là thứ tự crawl dữ liệu:

- `crawling_search.ipynb` chạy từ đầu tới cuối, phải treo máy vì sử dụng selenium.
- (Optional)`crawling_product.ipynb` chạy từ đầu đến cuối, có 2 cell có vẻ trùng nhau là vì có thể bị miss id nào đó (do đường truyền mạng) nên sẽ chạy lại với các id bị lỗi.
- `crawling_product_api.ipynb` tương tự cho notebook trên, chỉ khác là dùng query request lên nên sẽ nhanh hơn một chút.
- `crawling_product_cmt.ipynb` chạy từ đầu đến trước phần `using requests` nếu chỉ crawling html, nếu muốn dùng query thì sau khi import thư viện chỉ việc chạy các cell bên trong phần `using requests`

Trong phần crawl trên phải theo đúng thứ tự, vì dữ liệu `search.csv` sau khi crawl xong sẽ không có cột id. Do đó bên crawl product và cmt sẽ đọc và thêm id bên trong, save thành file mới là `search_withid.csv` có cột id. Nếu muốn dùng tiếp vào EDA thì bước đọc dữ liệu search sẽ đọc file này vì sẽ có bước join dựa trên id. 

Sau khi đã thu thập toàn bộ dữ liệu 
*Hoặc*
***Download toàn bộ dữ liệu mà nhóm đã chuẩn bị sẵn trên [Google Drive](https://)***
Ta sẽ giải nén dữ liệu vào thư mục `./data`
Ta sẽ thực hiện các bước tiếp theo đó là *Khám phá dữ liệu* và *Mô hình hóa dữ liệu* để giải quyết bài toán.


## Khám phá dữ liệu
Với notebook `eda.ipynb`, chạy từ đầu tới cuối là được. Lưu ý là ở đây, là nhóm giả sử ta đang lấy dữ liệu trong thư mục `./data`, nên nếu muốn dùng dữ liệu từ bước crawl thì phải di chuyển vào thư mục đó. Nếu dùng dữ liệu nhóm cung cấp thì không cần quan tâm điều này.

## Mô hình hóa dữ liệu
Nhóm đã thực hiện 3 bài toán ở trên một cách độc lập nhau trong các file:

- `[Modeling] Sold Prediction.ipynb`
- `[Modeling] Reviews Rating Prediction.ipynb`
- `[Modeling] Image Product Category Prediction.ipynb`

Lưu ý: Ở đây nhóm đã giả sử các thư viện cần thiết được cài đặt đầy đủ (ngoài các thư viên thông dụng thì các thư viện đặc biệt cài đặt có trong các file notebooks). Đặc biệt là thư viện `tensorflow>=2.0.0`


Do đó chỉ cần dữ liệu hợp lệ là có thể chạy riêng từng file từ trên xuống dưới.

Ngoài ra nhóm còn tổng hợp 3 Bài toán trên vào một file `Demo.ipynb` để thực hiện kiểm tra các mô hình dự đoán trong sản phẩm thực tế.
# Demo


![](https://i.imgur.com/eccH8Yg.png)


```
sas
```

