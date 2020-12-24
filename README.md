# Shopee dataset

Gồm 3 bộ chính search, items và items_cmt với ý nghĩa lần lượt là sản phẩm được tìm kiếm bên trang search, thông tin chi tiết sản phẩm và bình luận đối với sản phẩm.

Hướng crawl là search -> items -> items_cmt

Có 2 bộ chính: bộ 100 dòng và 15k6 dòng sản phẩm. 

Bộ 100 dòng gồm các file: 
- search_100.csv cho dữ liệu search
- items_100_sorted_id.csv cho dữ liệu items
- items_cmt_100.csv cho dữ liệu items_cmt 

Bộ 15k6 dòng gồm:
- search_15k6.csv cho dữ liệu search
- items.csv cho dữ liệu items
- items_cmt_sorted_id.csv cho dữ liệu items_cmt 
- items_cmt_eachrate2cmt.csv cho dữ liệu items_cmt với điều kiện là items tương ứng có ít nhất 1 bình luận ở mỗi loại rate, và khi crawl sẽ lấy maximum 2 bình luận cho mỗi loại rate.

Notebook dùng để crawl gồm: 
- crawling_search.ipynb dành cho crawl dữ liệu search
- crawling_product.ipynb dành cho crawl bộ items
- crawling_product_api.ipynb dành cho crawl bộ items sử dụng query mà shopee dùng để parse data cho từng trang.
- crawling_product_cmt.ipynb dành cho crawl bộ items_cmt

Trong đó khi crawl sẽ import file cssselector.py, lưu những css selector đến vị trí cần lấy thông tin. 

