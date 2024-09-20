import os

def search_files(directory, keywords):
    """
    指定されたディレクトリ内の.kifファイルから、複数のキーワードを含むファイルを検索します。

    Args:
        directory (str): 検索対象のディレクトリパス
        keywords (list): 検索するキーワードのリスト

    Returns:
        list: キーワードを含むファイルのパスリスト
    """

    result = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".kif"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding="shift-jis") as f:
                    text = f.read()
                    if all(keyword in text for keyword in keywords):
                        result.append(file_path)
    return result

# 検索対象のディレクトリを指定
directory = r"C:\Users\jpt\Desktop\shogi"

while True:
    keywords_str = input("検索するキーワードをカンマで区切って入力してください（終了する場合は'q'を入力）：")
    if keywords_str.lower() == 'q':
        break

    keywords = keywords_str.split(',')
    found_files = search_files(directory, keywords)
    if found_files:
        print("以下のファイルにキーワードが含まれています:")
        for file in found_files:
            print(file)
    else:
        print("キーワードが見つかりませんでした。")