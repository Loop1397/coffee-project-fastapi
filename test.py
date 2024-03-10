data = [[{"id":1, "hello":2}, {"id":3, "hello":4}], [{"id":5, "hello":6}, {"id":7, "hello":8}]]

# 이중 리스트 컴프리헨션을 사용하여 중첩된 리스트를 하나의 리스트로 펼칩니다.
flattened_data = [item for sublist in data for item in sublist]

print(flattened_data)