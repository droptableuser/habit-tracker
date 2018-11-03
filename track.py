import json
import datetime
data = ""

with open("datas.json","r") as f:
    data=json.loads(f.read())
    print(data)
    count=input('How many habits to track:')
    count=int(count)
    if count > 0:
        date = datetime.date.today().isoformat()
        values = data["data"]
        if values[-1]["date"] == date:
            values[-1]["count"]=count
        else:
            data["data"].append({"date":date, "count":count})

    print(data)

with open("datas.json","w") as output:
    output.write(json.dumps(data))
