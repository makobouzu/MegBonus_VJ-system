import os
from PIL import Image, ImageEnhance

def apply_bw_and_contrast(image_path, output_path, contrast_factor=2.0):
    """
    画像を白黒（グレースケール）に変換し、コントラストを強調する関数
    """
    with Image.open(image_path) as img:
        # 1. 画像を白黒（グレースケール）に変換
        bw_img = img.convert('L')
        
        # 2. コントラストを調整する準備
        enhancer = ImageEnhance.Contrast(bw_img)
        
        # 3. コントラストを適用（1.0が元のまま、数値を上げるとより白黒がはっきりする）
        final_img = enhancer.enhance(contrast_factor)
        
        # 保存
        final_img.save(output_path, quality=95)

# --- 設定 ---
# 白黒・高コントラストにしたい「特定のフォルダ」のパスを指定
target_folder = "./img/geo"  

# 処理後の画像を保存するフォルダのパスを指定
output_folder = "./img/contrast"

# コントラストの強さ（1.0で変更なし。1.5〜3.0あたりで調整すると効果的です）
CONTRAST_STRENGTH = 2.0
# ------------

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')

print("白黒＆コントラスト強調の処理を開始します...")

for root, dirs, files in os.walk(target_folder):
    for file in files:
        if file.lower().endswith(valid_extensions):
            input_path = os.path.join(root, file)
            
            # 元のフォルダ構成を維持
            rel_path = os.path.relpath(input_path, target_folder)
            output_path = os.path.join(output_folder, rel_path)
            
            output_dir = os.path.dirname(output_path)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
                
            try:
                apply_bw_and_contrast(input_path, output_path, contrast_factor=CONTRAST_STRENGTH)
                print(f"処理成功: {rel_path}")
            except Exception as e:
                print(f"エラー発生 ({rel_path}): {e}")

print("すべての処理が完了しました！")