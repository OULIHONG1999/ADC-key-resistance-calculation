import numpy as np
import matplotlib.pyplot as plt
# 设置字体为 SimHei（黑体）
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# E6 系列（公差 ±20%）
E6 = [1.0, 1.5, 2.2, 3.3, 4.7, 6.8]

# E12 系列（公差 ±10%）
E12 = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]

# E24 系列（公差 ±5%）
E24 = [1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1]

# E48 系列（公差 ±2%）
E48 = [1.00, 1.05, 1.10, 1.15, 1.21, 1.27, 1.33, 1.40, 1.47, 1.54, 1.62, 1.69, 1.78, 1.87, 1.96, 2.05, 2.15, 2.26, 2.37, 2.49, 2.61, 2.74, 2.87, 3.01, 3.16, 3.32, 3.48, 3.65, 3.83, 4.02, 4.22, 4.42, 4.64, 4.87, 5.11, 5.36, 5.62, 5.90, 6.19, 6.49, 6.81, 7.15, 7.50, 7.87, 8.25, 8.66, 9.09, 9.53]

# E96 系列（公差 ±1%）
E96 = [1.00, 1.02, 1.05, 1.07, 1.10, 1.13, 1.15, 1.18, 1.21, 1.24, 1.27, 1.30, 1.33, 1.37, 1.40, 1.43, 1.47, 1.50, 1.54, 1.58, 1.62, 1.65, 1.69, 1.74, 1.78, 1.82, 1.87, 1.91, 1.96, 2.00, 2.05, 2.10, 2.15, 2.21, 2.26, 2.32, 2.37, 2.43, 2.49, 2.55, 2.61, 2.67, 2.74, 2.80, 2.87, 2.94, 3.01, 3.09, 3.16, 3.24, 3.32, 3.40, 3.48, 3.57, 3.65, 3.74, 3.83, 3.92, 4.02, 4.12, 4.22, 4.32, 4.42, 4.53, 4.64, 4.75, 4.87, 4.99, 5.11, 5.23, 5.36, 5.49, 5.62, 5.76, 5.90, 6.04, 6.19, 6.34, 6.49, 6.65, 6.81, 6.98, 7.15, 7.32, 7.50, 7.68, 7.87, 8.06, 8.25, 8.45, 8.66, 8.87, 9.09, 9.31, 9.53, 9.76]

# E192 系列（公差 ±0.5%、±0.25%、±0.1%）
E192 = [1.00, 1.01, 1.02, 1.04, 1.05, 1.06, 1.07, 1.09, 1.10, 1.11, 1.13, 1.14, 1.15, 1.17, 1.18, 1.20, 1.21, 1.23, 1.24, 1.26, 1.27, 1.29, 1.30, 1.32, 1.33, 1.35, 1.37, 1.38, 1.40, 1.42, 1.43, 1.45, 1.47, 1.49, 1.50, 1.52, 1.54, 1.56, 1.58, 1.60, 1.62, 1.64, 1.65, 1.67, 1.69, 1.72, 1.74, 1.76, 1.78, 1.80, 1.82, 1.84, 1.87, 1.89, 1.91, 1.93, 1.96, 1.98, 2.00, 2.03, 2.05, 2.08, 2.10, 2.13, 2.15, 2.18, 2.21, 2.23, 2.26, 2.29, 2.32, 2.34, 2.37, 2.40, 2.43, 2.46, 2.49, 2.52, 2.55, 2.58, 2.61, 2.64, 2.67, 2.71, 2.74, 2.77, 2.80, 2.84, 2.87, 2.91, 2.94, 2.98, 3.01, 3.05, 3.09, 3.12, 3.16, 3.20, 3.24, 3.28, 3.32, 3.36, 3.40, 3.44, 3.48, 3.52, 3.57, 3.61, 3.65, 3.70, 3.74, 3.79, 3.83, 3.88, 3.92, 3.97, 4.02, 4.07, 4.12, 4.17, 4.22, 4.27, 4.32, 4.37, 4.42, 4.48, 4.53, 4.59, 4.64, 4.70, 4.75, 4.81, 4.87, 4.93, 4.99, 5.05, 5.11, 5.17, 5.23, 5.30, 5.36, 5.42, 5.49, 5.56, 5.62, 5.69, 5.76, 5.83, 5.90, 5.97, 6.04, 6.12, 6.19, 6.26, 6.34, 6.42, 6.49, 6.57, 6.65, 6.73, 6.81, 6.90, 6.98, 7.06, 7.15, 7.23, 7.32, 7.41, 7.50, 7.59, 7.68, 7.77, 7.87, 7.96, 8.06, 8.16, 8.25, 8.35, 8.45, 8.56, 8.66, 8.76, 8.87, 8.98, 9.09, 9.20, 9.31, 9.42, 9.53, 9.65, 9.76, 9.88]

E = E192

def find_closest_resistor(target, series=E, multiplier_range=(1, 1000000)):
    """
    查找最接近目标阻值的标准电阻值。

    参数:
    target (float): 目标电阻值。
    series (list): 标准电阻值系列，默认为 E48 系列。
    multiplier_range (tuple): 乘数范围，用于扩展标准电阻值系列，默认为 (1, 1000000)。

    返回:
    float: 最接近目标阻值的标准电阻值。
    """
    all_resistors = []
    for multiplier in [10 ** i for i in range(len(str(int(min(multiplier_range)))), len(str(int(max(multiplier_range)))))]:
        all_resistors.extend([r * multiplier for r in series])
    return min(all_resistors, key=lambda x: abs(x - target))


def calculate_adc_values(n=9, adc_max=4095, R_pullup_range=np.linspace(50e3, 400e3, 100),
                         R1_range=np.linspace(500e3, 2000e3, 100), r=0.5):
    """
    计算不同公比下的 ADC 相关值。

    参数:
    n (int): 按键数量，默认为 9。
    adc_max (int): ADC 采集值的最大值，默认为 4095。
    R_pullup_range (numpy.ndarray): 上拉电阻的搜索范围，默认为 50kΩ 到 400kΩ 之间的 100 个均匀分布的值。
    R1_range (numpy.ndarray): 第一个电阻的搜索范围，默认为 500kΩ 到 2000kΩ 之间的 100 个均匀分布的值。
    r (float): 公比，默认为 0.5。

    返回:
    dict 或 None: 如果找到有效的最佳参数，返回包含计算结果的字典；否则返回 None。
    """
    max_total_diff = 0
    best_R_pullup = 0
    best_R1 = 0

    for R_pullup in R_pullup_range:
        for R1 in R1_range:
            resistances = [R1 * (r ** i) for i in range(n)]
            # 排除电阻值过小的情况
            if any(R < 1e3 for R in resistances):
                continue
            adc_values = [int((R / (R + R_pullup)) * adc_max) for R in resistances]
            adc_differences = [adc_values[i] - adc_values[i + 1] for i in range(n - 1)]
            total_diff = sum(adc_differences)
            if total_diff > max_total_diff:
                max_total_diff = total_diff
                best_R_pullup = R_pullup
                best_R1 = R1

    # 检查最佳参数是否有效
    if best_R_pullup == 0 or best_R1 == 0:
        print(f"公比 {r} 下未找到有效的最佳参数。")
        return None

    # 计算最终结果
    resistances = [best_R1 * (r ** i) for i in range(n)]
    # 查找最接近的标准电阻值
    real_resistances = [find_closest_resistor(R) for R in resistances]
    best_R_pullup = find_closest_resistor(best_R_pullup)
    adc_values = [int((R / (R + best_R_pullup)) * adc_max) for R in real_resistances]
    adc_differences = [adc_values[i] - adc_values[i + 1] for i in range(n - 1)]

    # 对输出结果保留两位小数
    result = {
        "公比": round(r, 2),
        "最佳上拉电阻 (kΩ)": round(best_R_pullup / 1e3, 2),
        "第一个电阻 (kΩ)": round(real_resistances[0] / 1e3, 2),
        "电阻值 (kΩ)": [round(R / 1e3, 2) for R in real_resistances],
        "ADC 采集值 (0 - 4095)": adc_values,
        "相邻 ADC 采集值差值": adc_differences
    }
    return result


def plot_adc_results(adc_results):
    """
    绘制不同公比下的 ADC 采集值和相邻 ADC 采集值差值的折线图。

    参数:
    adc_results (list): 包含不同公比下计算结果的列表。
    """
    # 绘制 ADC 采集值折线图
    plt.figure(figsize=(12, 6))
    for result in adc_results:
        r = result["公比"]
        adc_values = result["ADC 采集值 (0 - 4095)"]
        plt.plot(range(1, len(adc_values) + 1), adc_values, marker='o', label=f'公比: {r}')

    plt.title('不同公比下的 ADC 采集值')
    plt.xlabel('按键序号')
    plt.ylabel('ADC 采集值 (0 - 4095)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # 绘制相邻 ADC 采集值差值折线图
    plt.figure(figsize=(12, 6))
    for result in adc_results:
        r = result["公比"]
        adc_differences = result["相邻 ADC 采集值差值"]
        plt.plot(range(1, len(adc_differences) + 1), adc_differences, marker='o', label=f'公比: {r}')

    plt.title('不同公比下相邻 ADC 采集值差值')
    plt.xlabel('按键序号（相邻差值）')
    plt.ylabel('相邻 ADC 采集值差值')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # 不同公比列表，调整范围为 0~1
    r_values = np.linspace(0.75, 0.85, 5)
    print(r_values)
    adc_results = []

    for r in r_values:
    # for r in rv:
        result = calculate_adc_values(n=20,r=r)
        if result:
            adc_results.append(result)
            for key, value in result.items():
                print(f"{key}: {value}")
            print("-" * 80)

    # 绘制图像
    plot_adc_results(adc_results)