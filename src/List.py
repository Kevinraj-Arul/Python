playlist=["shape of you","Naa Ready","Believer","Hukum"]
favorite_foods=["Pizza","Burger","Dosa","Biriyani"]
recent_Location=["Home","Airport","Work","Mail"]

#print("Spotify Playlist",playlist)
print("Zomato Foods",favorite_foods)
#print("uber location",recent_Location)

#list methods

playlist.append("Badas")
print("after added",playlist)

playlist.insert(1,"powerhouse")
print("after insert",playlist) 

playlist.remove("Badas")
print("after remove",playlist)


playlist.pop()
print("after pop",playlist)

print("count",playlist.count("Naa Ready"))

playlist.reverse()
print("after reverse",playlist)


#list slicing'
print("top 2 songs",playlist[0:2])

print("last 2 location",recent_Location[-2:])

#list iteration

for i in favorite_foods:
    print("My favorite",i)


