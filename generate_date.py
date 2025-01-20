import random
import datetime

# 生成随机数据的函数
def generate_random_data(num_records):
    data = []
    base_time = datetime.datetime.now()

    for i in range(num_records):
        timestamp = base_time - datetime.timedelta(minutes=i)
        temperature = round(random.uniform(-10, 35), 1)  # 温度范围 -10到35摄氏度
        humidity = round(random.uniform(10, 90), 1)  # 湿度范围 10%到90%
        pressure = round(random.uniform(950, 1050), 1)  # 气压范围 950到1050 hPa
        data.append({
            "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "temperature": temperature,
            "humidity": humidity,
            "pressure": pressure
        })
    return data

# 写入数据到文件
def write_data_to_file(data, file_path):
    with open(file_path, 'w') as file:
        file.write("Timestamp, Temperature(C), Humidity(%), Pressure(hPa)\n")
        for entry in data:
            file.write(f"{entry['timestamp']}, {entry['temperature']}, {entry['humidity']}, {entry['pressure']}\n")

# 生成并写入60条记录到data.txt文件
data = generate_random_data(20)
write_data_to_file(data, 'data.txt')

print(f"Generated {len(data)} records in data.txt")