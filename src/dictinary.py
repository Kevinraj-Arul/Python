#sample dictionary
dic={"name":"kevin","age":23,"place":"salem"}
print(dic)
#dictinary
trip={
    "trip_id": "Ub12345",
    "pickup": "chennai",
    "drop": "airport",
    "fare": 434,
    "status": "completed"
    }
print(trip.get("pickup"))
print(trip.keys())
print(trip.values())

#for iterating
trip={
    "trip_id": "Ub12345",
    "pickup": "chennai",
    "drop": "airport",
    "fare": 434,
    "status": "completed"
    }
for key,value in trip.items():
    print(key,":",value)
#update
trip={
    "trip_id": "Ub12345",
    "pickup": "chennai",
    "drop": "airport",
    "fare": 434,
    "status": "completed"
    }
trip.update({"fare":"450"})
print(trip)

#iterating loop
trip={
    "ub12345":{"trip_id": "Ub12345","pickup": "chennai","drop": "airport","fare": 434,"status": "completed"},
    "ub123456":{"trip_id": "Ub123456","pickup": "mumbai","drop": "airport","fare": 650,"status": "completed"}
}

for trips ,detail in trip.items():
    print(trips)
    print(detail["pickup"], "to ",detail["drop"])
