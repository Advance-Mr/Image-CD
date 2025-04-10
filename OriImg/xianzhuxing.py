import cv2
import os

# 输入图片路径
input_image_path = "D:\Image-Encryption-Decryption-main\OriImg\HorizonZero.png"

# 读取图片
image = cv2.imread(input_image_path)

# 创建显著性检测对象
saliency = cv2.saliency.StaticSaliencyFineGrained_create()

# 计算显著性图
(success, saliency_map) = saliency.computeSaliency(image)
# 将显著性图转换为8位无符号整数（用于可视化）
saliency_map = cv2.convertScaleAbs(saliency_map * 255)

# 生成新的图片路径
output_dir = "D:\Image-Encryption-Decryption-main\OriImg\HorizonZero1.png"
os.makedirs(output_dir, exist_ok=True)
filename = os.path.basename(input_image_path)
output_image_path = os.path.join(output_dir, f"saliency_{filename}")

# 保存显著性图
cv2.imwrite(output_image_path, saliency_map)

print(f"显著性图已保存至: {output_image_path}")