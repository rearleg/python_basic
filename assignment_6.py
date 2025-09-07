# BLUEPRINT | DONT EDIT

import requests

movie_ids = [238, 680, 550, 185, 641, 515042, 152532, 120467, 872585, 906126, 840430]

# /BLUEPRINT

# 👇🏻 YOUR CODE 👇🏻:
results = []
for i in movie_ids:
    response = requests.get(f"https://nomad-movies.nomadcoders.workers.dev/movies/{i}")
    data = response.json()
    results.append(
        {
            "id": i,
            "title": data["title"],
            "overview": data["overview"],
            "vote_average": data["vote_average"],
        }
    )
print(results)
# /YOUR CODE
