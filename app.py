from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

st.set_page_config(
    page_title="Demo Phân Loại Hoa Iris Dataset",
    page_icon="🌸",
    layout="wide",
)


@st.cache_resource(show_spinner="Đang tải dữ liệu và huấn luyện Gaussian Naive Bayes...")
def load_model_bundle():
    """Đo accuracy holdout rồi huấn luyện mô hình cuối trên toàn bộ Iris."""
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data,
        iris.target,
        test_size=0.2,
        random_state=42,
        stratify=iris.target,
    )
    evaluation_model = GaussianNB()
    evaluation_model.fit(X_train, y_train)
    accuracy = accuracy_score(y_test, evaluation_model.predict(X_test))

    model = GaussianNB()
    model.fit(iris.data, iris.target)
    return iris, model, float(accuracy)


@st.cache_data
def load_iris_frame():
    iris = load_iris()
    frame = pd.DataFrame(iris.data, columns=iris.feature_names)
    frame["Loài hoa"] = [iris.target_names[target].capitalize() for target in iris.target]
    return frame


def predict_iris(model, values):
    input_data = np.asarray(values, dtype=float).reshape(1, -1)
    predicted_class = int(model.predict(input_data)[0])
    probabilities = model.predict_proba(input_data)[0]
    return predicted_class, probabilities


def show_probability_bars(target_names, probabilities):
    st.markdown("#### Xác suất từng loài")
    for index, probability in enumerate(probabilities):
        st.write(f"**{target_names[index].capitalize()}** — {probability:.2%}")
        st.progress(float(probability))


def show_petal_chart(frame, features, target_names):
    fig, ax = plt.subplots(figsize=(8, 5))
    palette = ["#2E7D32", "#1976D2", "#D84315"]
    for index, species in enumerate(target_names):
        subset = frame[frame["target"] == index]
        ax.scatter(
            subset["petal length (cm)"],
            subset["petal width (cm)"],
            label=species.capitalize(),
            color=palette[index],
            alpha=0.65,
            s=38,
        )
    ax.scatter(
        features[2],
        features[3],
        marker="*",
        s=280,
        color="#F9A825",
        edgecolors="#222222",
        linewidths=1,
        label="Điểm bạn vừa nhập",
        zorder=5,
    )
    ax.set_title("Phân bố kích thước cánh hoa")
    ax.set_xlabel("Chiều dài cánh hoa (Petal Length - cm)")
    ax.set_ylabel("Chiều rộng cánh hoa (Petal Width - cm)")
    ax.grid(alpha=0.2)
    ax.legend()
    fig.tight_layout()
    st.pyplot(fig, clear_figure=True)
    plt.close(fig)


iris, model, test_accuracy = load_model_bundle()
iris_frame = load_iris_frame()
plot_frame = iris_frame.copy()
plot_frame["target"] = iris.target

with st.sidebar:
    st.header("Thông tin mô hình")
    st.write("**Thuật toán:** Gaussian Naive Bayes")
    st.write("**Dữ liệu:** Iris, 150 mẫu, 4 đặc trưng")
    st.write("**Huấn luyện:** toàn bộ dữ liệu Iris")
    st.metric("Accuracy trên tập Test", f"{test_accuracy:.2%}")
    st.caption("Tập Test: 20%, random_state=42, stratify=y.")

st.title("Demo Phân Loại Hoa Iris Dataset")
st.subheader("Mô hình: Gaussian Naive Bayes")
st.write("Điều chỉnh bốn thông số hoa, sau đó chọn **Dự đoán ngay** để xem kết quả.")

demo_tab, data_tab = st.tabs(["Dự đoán", "Dữ liệu Iris"])

with demo_tab:
    input_column, result_column = st.columns(2, gap="large")
    with input_column:
        st.markdown("### Thông số đầu vào")
        with st.form("iris_prediction_form"):
            sepal_length = st.slider(
                "Chiều dài lá đài (Sepal Length - cm)",
                min_value=4.0, max_value=8.0, value=5.1, step=0.1,
            )
            sepal_width = st.slider(
                "Chiều rộng lá đài (Sepal Width - cm)",
                min_value=2.0, max_value=4.5, value=3.5, step=0.1,
            )
            petal_length = st.slider(
                "Chiều dài cánh hoa (Petal Length - cm)",
                min_value=1.0, max_value=7.0, value=1.4, step=0.1,
            )
            petal_width = st.slider(
                "Chiều rộng cánh hoa (Petal Width - cm)",
                min_value=0.1, max_value=2.5, value=0.2, step=0.1,
            )
            submitted = st.form_submit_button("Dự đoán ngay", width="stretch")

        if submitted:
            st.session_state["iris_last_input"] = [
                sepal_length, sepal_width, petal_length, petal_width,
            ]

    with result_column:
        st.markdown("### Kết quả")
        last_input = st.session_state.get("iris_last_input")
        if last_input is None:
            st.info("Kết quả sẽ hiển thị sau khi bạn bấm **Dự đoán ngay**.")
        else:
            predicted_class, probabilities = predict_iris(model, last_input)
            predicted_species = iris.target_names[predicted_class]
            st.success(f"Loài hoa được dự đoán: **{predicted_species.upper()}**")
            show_probability_bars(iris.target_names, probabilities)

            image_path = Path(__file__).resolve().parent / "assets" / f"{predicted_species}.jpg"
            if image_path.is_file():
                st.image(
                    str(image_path),
                    caption=f"Hoa Iris {predicted_species.capitalize()}",
                    width="stretch",
                )
            else:
                st.warning(f"Chưa có ảnh minh họa cho loài {predicted_species.capitalize()}.")

            with st.expander("Xem điểm dự đoán trên biểu đồ phân bố"):
                show_petal_chart(plot_frame, last_input, iris.target_names)

with data_tab:
    st.markdown("### Bảng dữ liệu Iris")
    st.caption("Dữ liệu gồm 150 mẫu, 4 đặc trưng đo kích thước và nhãn loài hoa.")
    st.dataframe(iris_frame, width="stretch", hide_index=True)
