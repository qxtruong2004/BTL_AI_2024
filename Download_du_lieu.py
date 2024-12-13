
import requests
import pandas as pd
from io import StringIO

# Đặt link download
url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/retrievebulkdataset?&key=L3XJYA63XYHB4THR9RNT28RMZ&taskId=7311e213131297811b296fec28cf47c2&zip=false"

# Gửi yêu cầu tải dữ liệu
response = requests.get(url)

# Kiểm tra nếu dữ liệu được tải thành công
if response.status_code == 200:
    # Nếu dữ liệu là CSV, chúng ta có thể trực tiếp đọc nó vào pandas
    csv_data = StringIO(response.text)
    df = pd.read_csv(csv_data)

    # Lưu dữ liệu vào file CSV
    df.to_csv('DuLieuThoiTiet2324.csv', index=False)
    print("Dữ liệu đã được lưu thành công dưới dạng file CSV.")
else:
    print("Tải dữ liệu thất bại, mã lỗi:", response.status_code)
