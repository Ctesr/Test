#!/bin/bash

# 获取当前目录
current_dir="$(pwd)"

# 定义输入和输出文件夹
input_folder="${current_dir}/input"
output_folder="${current_dir}/output"

# 确认输入和输出文件夹存在
if [ ! -d "$input_folder" ]; then
    echo "Input folder not found: $input_folder"
    read -p "Press any key to exit..."
    exit 1
fi

if [ ! -d "$output_folder" ]; then
    mkdir "$output_folder"
fi

# 定位到 PyInstaller 生成的可执行文件
app_path="${current_dir}/MyApp.app/Contents/MacOS/MyApp"

if [ -f "$app_path" ]; then
    # 赋予执行权限
    chmod +x "$app_path"
    # 传递输入和输出路径参数
    "$app_path" "$input_folder" "$output_folder"
else
    echo "App not found: $app_path"
    read -p "Press any key to exit..."
    exit 1
fi

echo "Processing complete!"
read -n 1
