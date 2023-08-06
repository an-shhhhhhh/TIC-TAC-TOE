
name=input("enter your name")
age=input("age")
fav_movies=input("your favourite movies seperated by comma").split(",")
fav_songs=input("your favourite songs seperated by comma").split(",")
users={}
users["name"]=name
users["age"]=age
users["favourite_movies"]=fav_movies
users["favorite_songs"]=fav_songs
for key,value in users.items():
    print(f"{key} : {value}")

