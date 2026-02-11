#imports for generation and use of randomization
import pandas as pd
import random
from faker import Faker
fake = Faker()

#generation of random people and their pronouns
pronoun_preferences = [
    "she/her",
    "he/him",
    "they/them",
    "xe/xer"
]

number_of_people = 100

people = pd.DataFrame({
    "ID":range(1, number_of_people + 1),
    "Name": [fake.name() for _ in range(number_of_people)],
    "Pronouns": [random.choice(pronoun_preferences) for _ in range(number_of_people)]
})
people.head()


#generations of connections with at least 1-3 people
connective_lst = []
for person_id in people["ID"]:
    number_of_connections = random.randint(1,3)
    potential_connection = [pid for pid in people["ID"] if pid != person_id]
    connect_ids = random.sample(potential_connection, number_of_connections)
    for conid in connect_ids:
        connective_lst.append({
            "FromID": person_id,
            "ToID": conid
        })
connections = pd.DataFrame(connective_lst)
connections.head()


#merging both people and pronouns into a singular excel sheet
merging = connections.merge(
    people, left_on="FromID", right_on="ID"
).merge(
    people, left_on="ToID", right_on="ID", suffixes=("_From", "_To")
)

final = merging[[
    "Name_From", "Pronouns_From",
    "Name_To", "Pronouns_To"
]]

final.head()


#excel export
final.to_excel("people_connections_from_pronouns_100.xlsx", index=False)


        