import itertools
import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def calculate_any_combinations_adc(button_resistors, R_pullup, adc_max=4095, min_keys=1, max_keys=None):
    """
    计算任意按键组合（单/双/.../n按键）同时按下时的ADC采集值

    参数:
    button_resistors (list): 单个按键对应的电阻值列表（单位：Ω）
    R_pullup (float): 上拉电阻值（单位：Ω）
    adc_max (int): ADC最大采集值（默认4095，对应12位ADC）
    min_keys (int): 最小同时按下按键数（默认1，即包含单按键）
    max_keys (int): 最大同时按下按键数（默认None，即等于按键总数n）

    返回:
    list: 包含所有组合的元组列表，格式为：
          (按键组合, 并联电阻(kΩ), ADC值)
          其中按键组合为按键编号元组（编号从1开始）
    """
    n = len(button_resistors)
    max_keys = n if max_keys is None else max_keys  # 默认为n按键组合
    results = []

    # 生成所有按键数量从min_keys到max_keys的组合
    for k in range(min_keys, max_keys + 1):
        for keys in itertools.combinations(range(n), k):
            # 提取组合中的电阻值
            resistors = [button_resistors[i] for i in keys]
            # 计算并联电阻（处理k=1的情况：单个电阻，非并联）
            if k == 1:
                R_total = resistors[0]
            else:
                # 多个电阻并联公式：1/R_total = 1/R1 + 1/R2 + ... + 1/Rk
                R_total = 1.0 / sum(1.0 / R for R in resistors)
            # 计算ADC值（保留整数）
            adc_value = int((R_total / (R_total + R_pullup)) * adc_max)
            # 转换按键编号为1开始，并排序（避免(2,1)和(1,2)视为不同组合）
            sorted_keys = tuple(sorted(i + 1 for i in keys))  # 按键编号从1开始，排序后存储
            results.append((sorted_keys, round(R_total / 1e3, 2), adc_value))

    return results


import matplotlib.pyplot as plt

def plot_combination_results(results):
    """
    按主按键分组绘制ADC值分布，单按键为点，组合按键为线
    """
    # 按主按键分组（单按键以自身为组，组合按键以第一个按键为组）
    main_key_groups = {}
    for combo in results:
        keys = combo[0]
        main_key = keys[0]  # 单按键或组合按键的第一个按键作为主按键
        resistance = combo[1]
        adc = combo[2]
        if main_key not in main_key_groups:
            main_key_groups[main_key] = []
        main_key_groups[main_key].append((resistance, adc))

    plt.figure(figsize=(12, 8))  # 创建画布

    for main_key, data in main_key_groups.items():
        resistances = [r for r, adc in data]
        adc_values = [adc for r, adc in data]
        label = f'按键 {main_key}'
        if len(data) == 1:
            # 单按键：绘制散点
            plt.scatter(resistances, adc_values, marker='o', label=label, s=80, edgecolors='black')
        else:
            # 组合按键：绘制曲线+散点
            plt.plot(resistances, adc_values, marker='o', label=label, linewidth=1, markersize=6,
                     linestyle='-', markerfacecolor='none')

    plt.xlabel('并联电阻 (kΩ)')
    plt.ylabel('ADC值 (0-4095)')
    plt.title('所有按键组合的ADC值分布（按主按键分组）')
    plt.legend(title='主按键', bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()


def plot_adjacent_diffs(results):
    """
    按组合类型（单按键、双按键等）计算相邻ADC值差值并绘制柱状图

    参数:
    results (list): 包含按键组合、电阻、ADC值的结果列表
    """
    # 按组合长度分组
    groups = {}
    for combo in results:
        k = len(combo[0])
        if k not in groups:
            groups[k] = []
        groups[k].append(combo)

    for k, group in groups.items():
        # 按ADC值排序
        sorted_group = sorted(group, key=lambda x: x[2])
        adc_values = [x[2] for x in sorted_group]

        if len(adc_values) < 2:
            continue  # 不足2个值无法计算差值，跳过

        # 计算相邻差值
        diffs = [adc_values[i + 1] - adc_values[i] for i in range(len(adc_values) - 1)]

        # 绘制柱状图
        plt.figure(figsize=(10, 6))
        plt.bar(
            range(len(diffs)),
            diffs,
            width=0.6,
            color='skyblue',
            edgecolor='black'
        )
        plt.title(f"{k}按键组合相邻ADC差值分布")
        plt.xlabel("相邻组合索引（按ADC值升序）")
        plt.ylabel("ADC差值（后一值 - 前一值）")
        plt.xticks(
            range(len(diffs)),
            [f"{i + 1}→{i + 2}" for i in range(len(diffs))],
            rotation=45,
            ha='right'
        )
        plt.grid(axis='y', linestyle='--', alpha=0.7)  # 仅显示Y轴网格
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    '''
    E 是: E48
    公比: 0.75
    最佳上拉电阻 (kΩ): 162.0
    第一个电阻 (kΩ): 511.0
    电阻值 (kΩ): [511.0, 383.0, 287.0, 215.0, 162.0, 121.0, 90.9, 68.1, 51.1]
    ADC 采集值 (0 - 4095): [3109, 2877, 2617, 2335, 2047, 1750, 1471, 1211, 981]
    相邻 ADC 采集值差值: [232, 260, 282, 288, 297, 279, 260, 230]
    '''

    # 您提供的9个按键电阻值（单位：kΩ）
    button_resistors_kΩ = [511.0, 383.0, 287.0, 215.0, 162.0, 121.0, 90.9, 68.1, 51.1]
    button_resistors = [r * 1e3 for r in button_resistors_kΩ]
    R_pullup = 162.0 * 1e3
    adc_max = 4095

    # 计算所有1~2按键组合（避免过多组合，可改为max_keys=9查看全部）
    all_combinations = calculate_any_combinations_adc(
        button_resistors, R_pullup, adc_max, min_keys=1, max_keys=4
    )
    # 打印结果（按组合长度排序）
    print(f"总组合数: {len(all_combinations)}")
    print("结果格式: (按键组合), 并联电阻(kΩ), ADC值")
    for combo in sorted(all_combinations, key=lambda x: len(x[0])):
        print(f"按键 {combo[0]}: 电阻 {combo[1]:.2f} kΩ, ADC值 {combo[2]}")

    # 打印并绘图
    plot_combination_results(all_combinations)
    plot_adjacent_diffs(all_combinations)