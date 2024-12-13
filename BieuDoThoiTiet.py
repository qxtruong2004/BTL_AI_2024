import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Tải dữ liệu từ file CSV
data_path = "C:\\Users\\quach\\Downloads\\BTL_AI_DuDoanThoiTiet\\DuLieuThoiTiet2324.csv"
df = pd.read_csv(data_path)

# Đảm bảo cột 'datetime' có kiểu dữ liệu datetime
df['datetime'] = pd.to_datetime(df['datetime'], dayfirst=False, errors='coerce')


# Tạo cột 'Tháng-Năm' để nhóm theo tháng
df['Tháng-Năm'] = df['datetime'].dt.to_period('M')  # Lấy tháng và năm từ cột datetime

# Tính nhiệt độ cao nhất và thấp nhất trung bình cho mỗi tháng
monthly_avg = df.groupby('Tháng-Năm')[['tempmax', 'tempmin']].mean().reset_index()

# Vẽ biểu đồ
plt.figure(figsize=(12, 6))

# Vẽ nhiệt độ cao nhất
plt.plot(monthly_avg['Tháng-Năm'].astype(str), monthly_avg['tempmax'], label="Nhiệt độ cao nhất", marker="o", color="red")

# Vẽ nhiệt độ thấp nhất
plt.plot(monthly_avg['Tháng-Năm'].astype(str), monthly_avg['tempmin'], label="Nhiệt độ thấp nhất", marker="o", color="blue")

# Cấu hình biểu đồ
plt.title("Biểu đồ nhiệt độ trung bình theo từng tháng", fontsize=14)
plt.xlabel("Tháng-Năm", fontsize=12)
plt.ylabel("Nhiệt độ (°C)", fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Hiển thị biểu đồ
plt.tight_layout()
plt.show()
