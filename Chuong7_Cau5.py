#Câu 5: Xử lý JSON File, Chuyển đổi Python Object qua String Json 

import json
pythonObject = {
 "ten": "Trần Duy Thanh",
 "tuoi": 50,
 "ma": "nv1"
}
jsonString = json.dumps(pythonObject)

print(jsonString)
