# Demo Phân Loại Hoa Iris Dataset

Ứng dụng Streamlit phân loại hoa Iris bằng Gaussian Naive Bayes. Dự án gồm mã nguồn, hướng dẫn chạy và ảnh minh họa cần thiết.

## Mở ứng dụng trực tuyến

Sau khi triển khai trên Streamlit Community Cloud, đặt link ứng dụng tại đây để giảng viên mở trực tiếp.

## Chạy trên máy tính

Yêu cầu Python 3.10 trở lên. Giải nén thư mục, mở PowerShell tại thư mục dự án và chạy:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Streamlit sẽ hiện một địa chỉ cục bộ, thường là `http://localhost:8501`; mở địa chỉ đó trên trình duyệt.

## Chức năng

- Gaussian Naive Bayes được huấn luyện trên toàn bộ 150 mẫu Iris.
- Accuracy được đánh giá riêng trên tập test 20%, `random_state=42`, `stratify=y`.
- Bốn thanh trượt nhập đặc trưng; kết quả chỉ xuất hiện sau khi bấm **Dự đoán ngay**.
- Hiển thị loài được dự đoán, xác suất của ba loài và ảnh minh họa tương ứng.
- Có bảng dữ liệu Iris và biểu đồ vị trí điểm nhập mới trên phân bố cánh hoa.

## Cấu trúc

- `app.py`: ứng dụng Streamlit, đánh giá và huấn luyện mô hình.
- `requirements.txt`: thư viện cần cài.
- `assets/`: ảnh minh họa Setosa, Versicolor và Virginica.

## Triển khai lên Streamlit Community Cloud

1. Đăng nhập tại [share.streamlit.io](https://share.streamlit.io) bằng GitHub.
2. Chọn repository `TranMinhHuy15/AIL_IRIS_Classification`, branch `main`, file `app.py`.
3. Chọn **Deploy**. Sau khi build xong, chia sẻ URL kết thúc bằng `streamlit.app`.

## Nguồn

- GitHub repository: https://github.com/TranMinhHuy15/AIL_IRIS_Classification
- Notebook Colab: https://colab.research.google.com/drive/1fwpgCZQDlgDLHgQ3IHBJlW8tVYD3vzix
