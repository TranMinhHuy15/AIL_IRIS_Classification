# Demo Phân Loại Hoa Iris Dataset

Ứng dụng Streamlit phân loại hoa Iris bằng Gaussian Naive Bayes. Dự án gồm mã nguồn, hướng dẫn chạy và ảnh minh họa cần thiết.

## Mở ứng dụng trực tuyến

Giảng viên có thể mở và chạy ứng dụng trực tiếp tại: **https://se203499-iris-classification.streamlit.app/**.

Không cần tải ZIP hay cài Python để xem demo. Nếu app ngủ do không có lượt truy cập, mở link và chờ Streamlit khởi động lại.

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

## Kiểm thử

Các đầu vào mẫu, kết quả, xác suất và nhận xét ca ranh giới được ghi trong [`bao_cao_kiem_thu.md`](bao_cao_kiem_thu.md). Notebook [`iris_streamlit_demo.ipynb`](iris_streamlit_demo.ipynb) có các bước nạp dữ liệu, đánh giá, huấn luyện toàn bộ dữ liệu và kiểm tra bốn trường hợp theo đề.

Để chụp ảnh giao diện đính kèm báo cáo, mở link ứng dụng ở trên, chọn bộ giá trị trong bảng của báo cáo, bấm **Dự đoán ngay** rồi chụp màn hình vùng gồm thông số và kết quả.

## Cấu trúc

- `app.py`: ứng dụng Streamlit, đánh giá và huấn luyện mô hình.
- `iris_streamlit_demo.ipynb`: notebook code tiếng Việt để chạy trên Colab/Jupyter.
- `bao_cao_kiem_thu.md`: kết quả kiểm thử và nhận xét.
- `requirements.txt`: thư viện cần cài.
- `assets/`: ảnh minh họa Setosa, Versicolor và Virginica.
- `screenshots/`: ảnh chụp giao diện kiểm thử để đính kèm báo cáo.

## Triển khai lên Streamlit Community Cloud

1. Đăng nhập tại [share.streamlit.io](https://share.streamlit.io) bằng GitHub.
2. Chọn repository `TranMinhHuy15/AIL_IRIS_Classification`, branch `main`, file `app.py`.
3. Chọn **Deploy**. Ứng dụng hiện đã được triển khai tại https://se203499-iris-classification.streamlit.app/.

## Nguồn

- GitHub repository: https://github.com/TranMinhHuy15/AIL_IRIS_Classification
- Notebook cuối đã chạy trên Colab: https://colab.research.google.com/drive/1N_qrNQGuYEB7zwF57t6yY4Xd_aKAZG_w
- Mở notebook công khai từ GitHub bằng Colab: https://colab.research.google.com/github/TranMinhHuy15/AIL_IRIS_Classification/blob/main/iris_streamlit_demo.ipynb
- Ứng dụng Streamlit: https://se203499-iris-classification.streamlit.app/
