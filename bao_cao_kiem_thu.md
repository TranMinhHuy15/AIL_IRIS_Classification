# Báo cáo kiểm thử — Demo phân loại hoa Iris

**Sinh viên:** SE203499 — Trần Minh Huy  
**Ứng dụng:** https://se203499-iris-classification.streamlit.app/  
**Mô hình dự đoán:** Gaussian Naive Bayes, huấn luyện trên toàn bộ 150 mẫu Iris.

## Kết quả kiểm thử

Accuracy tham chiếu được đo bằng một mô hình riêng trên tập Test 20%, với `random_state=42` và `stratify=y`: **96.67%**. Mô hình dùng trong app sau đó được huấn luyện lại trên toàn bộ tập Iris.

| STT | Sepal Length | Sepal Width | Petal Length | Petal Width | Dự đoán | Setosa | Versicolor | Virginica |
|---:|---:|---:|---:|---:|---|---:|---:|---:|
| 1 | 5.1 | 3.5 | 1.4 | 0.2 | **Setosa** | 100.00% | 0.00% | 0.00% |
| 2 | 6.0 | 2.9 | 4.5 | 1.5 | **Versicolor** | 0.00% | 98.65% | 1.35% |
| 3 | 6.5 | 3.0 | 5.8 | 2.2 | **Virginica** | 0.00% | 0.00% | 100.00% |
| 4 | 6.0 | 2.7 | 5.0 | 1.7 | **Virginica** | 0.00% | 40.99% | 59.01% |

## Nhận xét trường hợp ranh giới

Ở trường hợp 4, mô hình chọn **Virginica** vì xác suất 59.01% cao hơn **Versicolor** 40.99%. Hai xác suất cách nhau 18.02 điểm phần trăm, cho thấy mẫu nằm gần ranh giới giữa hai loài nên mức độ chắc chắn thấp hơn các ví dụ điển hình. Setosa có xác suất 0.00%.

## Cách lưu ảnh chụp màn hình

Mở link ứng dụng, nhập lần lượt bốn hàng trong bảng, bấm **Dự đoán ngay** và chụp vùng giao diện có bốn thông số cùng tên loài/xác suất/ảnh. Lưu ảnh theo tên `case_1_setosa.jpg`, `case_2_versicolor.jpg`, `case_3_virginica.jpg`, `case_4_ambiguous.jpg` vào thư mục `screenshots/`, rồi đính kèm báo cáo khi nộp EDUNEXT.
