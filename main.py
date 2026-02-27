import turtle

drawing_board=turtle.Screen()
drawing_board=turtle.bgcolor("green")
drawing_board=turtle.title("Python turtle")

# #Kare Çizmek
# turtle_instance=turtle.Turtle()
# for i in range (4):
#     turtle_instance.forward(100)
#     turtle_instance.left(90)

# #Yıldız
# turtle_instance2=turtle.Turtle()
# for i in range(5):
#     turtle_instance.right(144)
#     turtle_instance.forward(100)
    
# #Belli bir kenarda dörtgen çizmek

turtle_i=turtle.Turtle()
kenar=6
aci=360.0/kenar
gidis=100

for i in range(kenar):
    turtle_i.right(aci)
    turtle_i.forward(gidis)
turtle.done()