def add(a,b):
  return a + b

user_dictionary = {
  "company": "Casper",
  "location": {"town": "Middlesbrough", "phone": "01642243662" }
}

places = [
    {
        "company": "The Jet d'Eau",
        "location": {"town": "Geneva", "phone": ""}
    },
    {
        "company": "CERN",
        "location": {"town": "Meyrin", "phone": "+41227671111"}
    },
    {
        "company": "Lake Geneva",
        "location": {"town": "Geneva", "phone": ""}
    },
    {
        "company": "Geneva Old Town",
        "location": {"town": "Geneva", "phone": ""}
    },
    {
        "location": {"town": "Dublin", "phone": "+35318141111"}
    },
]


print(add(1,2))

# lambda -> throw away function, does one thing, it's defined as you use it
# anonymous function

def get_town(dictionary):
  return dictionary.get("location", {}).get("town", "Unknown")



places.sort(key=lambda d: d.get("company", "AAAA"))

print(places)

def add(a,b):
  return a + b

add = lambda a,b: a + b
print(add(1,2))