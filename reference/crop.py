import os
from PIL import Image

def crop_to_16_9(image_path, output_path):
    """
    画像を16:9のアスペクト比に合わせて中央でクロップする関数
    """
    with Image.open(image_path) as img:
        # 画像がRGBモードでない場合（PNGの透過など）はRGBに変換
        if img.mode not in ('RGB', 'RGBA'):
            img = img.convert('RGB')
            
        width, height = img.size
        
        target_ratio = 16 / 9
        current_ratio = width / height
        
        if current_ratio > target_ratio:
            # 画像が横に長すぎる場合（左右を削る）
            new_width = int(height * target_ratio)
            new_height = height
            left = (width - new_width) / 2
            top = 0
            right = left + new_width
            bottom = height
        else:
            # 画像が縦に長すぎる場合（上下を削る）
            new_width = width
            new_height = int(width / target_ratio)
            left = 0
            top = (height - new_height) / 2
            right = width
            bottom = top + new_height
            
        # 中央を基準にクロップ（切り取り）
        img_cropped = img.crop((left, top, right, bottom))
        
        # ※ もし「アスペクト比を合わせるだけでなく、実際のサイズも 1920x1080 に統一したい」場合は、
        # 以下の1行の先頭にある # を消して有効にしてください。
        # img_cropped = img_cropped.resize((1920, 1080), Image.Resampling.LANCZOS)
        
        # 保存
        img_cropped.save(output_path, quality=95)

# --- 設定 ---
# 3つのフォルダが入っている親フォルダのパスを指定してください
input_folder = "./260422"  

# 処理後の画像を保存するフォルダのパスを指定してください
output_folder = "./img"
# ------------

# 出力先フォルダが存在しない場合は作成
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 対応する画像ファイルの拡張子
valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')

print("画像処理を開始します...")

# フォルダ内を再帰的に検索して処理
for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.lower().endswith(valid_extensions):
            input_path = os.path.join(root, file)
            
            # 元のフォルダ構成（3つのサブフォルダなど）を維持して出力先パスを作成
            rel_path = os.path.relpath(input_path, input_folder)
            output_path = os.path.join(output_folder, rel_path)
            
            # 出力先のサブディレクトリが存在しない場合は作成
            output_dir = os.path.dirname(output_path)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
                
            try:
                crop_to_16_9(input_path, output_path)
                print(f"処理成功: {rel_path}")
            except Exception as e:
                print(f"エラー発生 ({rel_path}): {e}")

print("すべての画像の処理が完了しました！")