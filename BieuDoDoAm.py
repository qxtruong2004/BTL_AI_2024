import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ CSV
data_path = 'C:\\Users\\quach\\Downloads\\BTL_AI_DuDoanThoiTiet\\DuLieuThoiTiet2324.csv'
df = pd.read_csv(data_path)

# Kiểm tra dữ liệu đầu vào
print(df.head())

# Chuyển đổi cột datetime sang dạng datetime nếu chưa đúng
df['datetime'] = pd.to_datetime(df['datetime'], dayfirst=False, errors='coerce')

# Chuyển đổi các giá trị cloudcover và humidity thành số (float) nếu chưa phải số
df['cloudcover'] = pd.to_numeric(df['cloudcover'], errors='coerce')
df['humidity'] = pd.to_numeric(df['humidity'], errors='coerce')

# Vẽ biểu đồ cho 'cloudcover' và 'humidity'

# Tạo biểu đồ
plt.figure(figsize=(10, 6))

# Vẽ biểu đồ đường cho cloudcover
plt.subplot(2, 1, 1)  # 2 rows, 1 column, vị trí thứ nhất
plt.plot(df['datetime'], df['cloudcover'], label='Cloud Cover', color='blue')
plt.title('Cloud Cover Over Time')
plt.xlabel('Date')
plt.ylabel('Cloud Cover (%)')
plt.xticks(rotation=45)

# Vẽ biểu đồ đường cho humidity
plt.subplot(2, 1, 2)  # 2 rows, 1 column, vị trí thứ hai
plt.plot(df['datetime'], df['humidity'], label='Humidity', color='green')
plt.title('Humidity Over Time')
plt.xlabel('Date')
plt.ylabel('Humidity (%)')
plt.xticks(rotation=45)

plt.tight_layout()  # Để đảm bảo biểu đồ không bị chồng chéo
plt.show()
