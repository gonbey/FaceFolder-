import os
import shutil
import numpy as np
import cv2
from insightface.app import FaceAnalysis

# ハードコーディングされたフォルダパス
import_folder = "C:/Users/RyosukeSugisawa/Pictures/input"  # 実際のパスに置き換えてください
output_folder = "C:/Users/RyosukeSugisawa/Pictures/output"  # 実際のパスに置き換えてください

# 顔マップを初期化
face_map = {}

# 次の利用可能なIDを取得する関数
def get_next_id(face_map):
    if face_map:
        return max(face_map.keys()) + 1
    else:
        return 1

# InsightFaceの初期化
app = FaceAnalysis(providers=['CPUExecutionProvider'])
app.prepare(ctx_id=0)  # GPUを使用しない場合はctx_id=-1に設定

# インポートフォルダ内の画像ファイルを再帰的に探索
for root, dirs, files in os.walk(import_folder):
    for filename in files:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(root, filename)
            print(f"Processing image: {image_path}")

            # ファイルをバイナリモードで読み込み、cv2.imdecodeを使用
            with open(image_path, 'rb') as f:
                data = f.read()
                image_array = np.frombuffer(data, dtype=np.uint8)
                image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

            # 画像が読み込めなかった場合の処理
            if image is None:
                print(f"Failed to read image: {image_path}")
                continue

            faces = app.get(image)

            face_ids = []

            # 検出された各顔を処理
            for face in faces:
                face_embedding = face.normed_embedding

                # 既知の顔と比較
                known_encodings = list(face_map.values())
                ids = list(face_map.keys())

                if known_encodings:
                    # コサイン類似度で比較
                    similarities = np.dot(known_encodings, face_embedding)
                    max_similarity = np.max(similarities)
                    index = np.argmax(similarities)
                    if max_similarity > 0.5:  # 類似度の閾値を調整
                        matched_id = ids[index]
                    else:
                        # 一致しなかった場合、新しいIDを割り当て
                        matched_id = get_next_id(face_map)
                        face_map[matched_id] = face_embedding
                else:
                    # 顔マップが空の場合
                    matched_id = get_next_id(face_map)
                    face_map[matched_id] = face_embedding

                face_ids.append(matched_id)

                # 顔に枠を描画
                bbox = face.bbox.astype(int)
                cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)
                cv2.putText(image, f'ID: {matched_id}', (bbox[0], bbox[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # 各IDに対応するフォルダに画像をコピーし、サムネイルを保存
            for face_id in set(face_ids):  # 重複を避けるためにsetを使用
                relative_path = os.path.relpath(root, import_folder)
                dest_folder = os.path.join(output_folder, str(face_id))
                os.makedirs(dest_folder, exist_ok=True)
                dest_path = os.path.join(dest_folder, filename)
                shutil.copy(image_path, dest_path)

                # サムネイル画像を保存
                thumbnail_path = os.path.join(dest_folder, 'thumbnail.jpg')
                if not os.path.exists(thumbnail_path):
                    # 画像を縮小してサムネイルを作成
                    thumbnail = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
                    cv2.imwrite(thumbnail_path, thumbnail)

            # 処理後、元の画像を削除
            # os.remove(image_path)
