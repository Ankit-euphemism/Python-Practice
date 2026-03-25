# care_products= {
#     "brand":"deramco",
#     "hair_care":"minoxidil",
# }
# print(care_products)
# print(type(care_products))
# print(care_products.keys())
# print(care_products.values())
# print(care_products["brand"])

# print(care_products)

# data= {"a":1,"a":2} # value changes
# print(data)

students=[
    {"name":"Amit","marks":80},
    {"name":"Ravi","marks":45},
    {"name":"Neha","marks":90},
]

for s in students:
    if s["marks"]>=60:
        print(s["name"])
    # print(s["name"],s["marks"])

