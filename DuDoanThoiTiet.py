import csv
import numpy as np
import math
import pandas as pd

def loadData(path):
    with open(path, "r") as f:
        data = csv.reader(f)
        data = np.array(list(data))  # Chuyển thành mảng
        data = np.delete(data, 0, 0)  # Xóa header
        data = np.delete(data, 0, 1)  # Xóa index
        np.random.shuffle(data)  # Trộn dữ liệu

    trainSet = data[:503]  # Bộ train từ 1 -> 503
    testSet = data[503:]  # Bộ test là phần còn lại
    return trainSet, testSet

def calcDistancs(pointA, pointB, numOfFeature=5):  # Hàm tính khoảng cách
    tmp = 0
    for i in range(numOfFeature):
        tmp += math.pow(float(pointA[i]) - float(pointB[i]), 2)
    return math.sqrt(tmp)

def getValue(x):  # Hỗ trợ cho hàm sắp xếp
    return x["value"]

def kNearestNeighbor(trainSet, point, k):  # Tìm k hàng xóm gần nhất
    distances = []
    for item in trainSet:
        distances.append({
            "label": item[-1],  # Nhãn
            "value": calcDistancs(item, point)  # Khoảng cách 2 điểm
        })
    distances.sort(key=getValue)  # Sắp xếp dựa trên value
    labels = [item["label"] for item in distances]  # Lấy các nhãn
    return labels[:k]  # Lấy k nhãn gần nhất

def findMostOccur(arr):  # Tìm nhãn xuất hiện nhiều nhất
    labels = set(arr)
    ans = ""
    maxOccur = 0
    for label in labels:
        num = arr.count(label)
        if num > maxOccur:
            maxOccur = num
            ans = label
    return ans

# Đọc dữ liệu huấn luyện
trainSet, testSet = loadData("C:\\Users\\quach\\Downloads\\thoitietv2\\DuLieuThoiTiet2324.csv")

# Kiểm tra nếu testSet rỗng
if len(testSet) == 0:
    print("Lỗi: testSet rỗng. Kiểm tra lại dữ liệu đầu vào.")
else:
    numOfRightAnswer = 0
    # Ghi kết quả dự đoán vào file CSV
    with open("C:\\Users\\quach\\Downloads\\thoitietv2\\ThoiTiet_label_va_predicted.csv", "w", newline='') as f:
        writer = csv.writer(f)
        for item in testSet:
            knn = kNearestNeighbor(trainSet, item, 5)
            answer = findMostOccur(knn)
            numOfRightAnswer += int(item[-1] == answer)
            writer.writerow([item[-1], answer])

        print("Accuracy:", numOfRightAnswer / len(testSet))  # Tính độ chính xác

# Nhập dữ liệu từ người dùng
var_tempMax = input('Nhap vao nhiet do cao nhat: ')
var_tempMin = input('Nhap vao nhiet do thap nhat: ')
var_wind = input('Nhap vao toc do gio: ')
var_cloud = input('Nhap vao luong may: ')
var_rel = input("Nhap vao do am: ")

# Chuyển đổi dữ liệu đầu vào thành dạng phù hợp
try:
    var_tempMax = float(var_tempMax)
    var_tempMin = float(var_tempMin)
    var_wind = float(var_wind)
    var_cloud = float(var_cloud)
    var_rel = float(var_rel)
except ValueError:
    print("Dữ liệu nhập không hợp lệ. Vui lòng nhập lại các giá trị số.")
    exit()

# Tạo dữ liệu đầu vào dưới dạng DataFrame
data = {
    "Max Temperature": [var_tempMax],
    "Min Temperature": [var_tempMin],
    "Wind Speed": [var_wind],
    "Cloud Cover": [var_cloud],
    "Relative Humidity": [var_rel]
}

#lưu dữ liệu người dùng nhập
df = pd.DataFrame(data)
df.to_csv("C:\\Users\\quach\\Downloads\\thoitietv2\\ThoiTiet_input.csv", index=False)

# Hàm để xử lý dữ liệu đầu vào
def loadDataInput(path):
    with open(path, "r") as f:
        data = csv.reader(f)
        data = np.array(list(data))
        data = np.delete(data, 0, 0)  # Xóa header
    return data[:1]

item = loadDataInput("C:\\Users\\quach\\Downloads\\thoitietv2\\ThoiTiet_input.csv")  # Đọc dữ liệu đầu vào

# Xử lý dự đoán cho dữ liệu đầu vào
for i in item:
    knn = kNearestNeighbor(trainSet, i, 5)
    answer = findMostOccur(knn)
    print(f"Predicted: {answer}")  # In kết quả dự đoán
