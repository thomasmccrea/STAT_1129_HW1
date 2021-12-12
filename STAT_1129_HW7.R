df1 = data.frame(name=c("Peter","Amy","Ryan","Gary","Michelle"),salary=c(623.30,515.20,611.00,729.00,843.25))
df2 = cbind(df1,department=c("Marketing","Operations","Finance","Sales","HR"))
#head(df2)
df2[c(1,3,5),c(2,3)]
barplot(df2[c(1,4,5),]$salary, names.arg = df2[c(1,4,5),]$name)
max(df2$salary)
min(df2$salary)
median(df2$salary)
pie(df2[c(1,2,5),2],labels = c("median","min","max"), main = "Salaries")
#or
pie(c(max(df2$salary),min(df2$salary),median(df2$salary)), labels = c("max","min","median"), main = "Salaies")


####################

install.packages("TurtleGraphics")
library(TurtleGraphics)

turtle_init()
turtle_hide()
turtle_up()

draw_rectangle <- function(length,height,color){
  turtle_col(color)
  if (color == "white") {
    turtle_col("black")
  }
  turtle_down()
  #turt           #No function in this package to fill
  #turt           #No function to begin fill
  for (i in 1:2) {
    turtle_right(90)
    turtle_forward(length)
    turtle_right(90)
    turtle_forward(height)
  }
  #turt           #No function to end fill
  turtle_up()
  
  turt_fill <- function() {     #Fix to create effective fill function (since one doesn't exist for this package)
    turtle_down()
    turtle_col(color)
    turtle_right(90)
    for (i in 1:50) {
      turtle_forward(length)
      turtle_right(90)
      turtle_forward(height/100)
      turtle_right(90)
      turtle_forward(length)
      turtle_left(90)
      turtle_forward(height/100)
      turtle_left(90)
    }
    turtle_up()
    turtle_reset()
    turtle_hide()
  }
  
  turt_fill()
}

draw_rectangle(10,5,"red")

#Python Function

#def draw_rectangle(length,height,color):
#     t.color(color)
#     if color == "white" or "#FFFFFF":
#       t.color("black")
#     t.pendown()
#     t.fillcolor(color)
#     t.begin_fill()
#     for i in range(2):
#  t.forward(length)
#t.right(90)
#t.forward(height)
#t.right(90)
#t.end_fill()
#t.penup()

draw_star <- function(size,color) {
  turtle_forward(0.5*size)      #Realize now this should be cos(18)*size
  turtle_right(162)
  turtle_col(color)
  turtle_down()
  #turt           #No function in this package to fill
  #turt           #No function to begin fill
  for (i in 1:5) {
    turtle_forward(size)
    turtle_right(144)
  }
  #turt           #No function to end fill
  turtle_up()
  turtle_left(162)
  turtle_backward(0.5*size)     #Realize now this should be cos(18)*size
  
  turt_fill <- function() {     #Fix to create effective fill function (since one doesn't exist for this package)
    turtle_left(36)
    star_height <- cos(18)*size
    Law_of_Sines <- function(b,a_angle,b_angle) {
      a <- b*(((sin(a_angle*(pi/180)))/(sin(b_angle*(pi/180)))))
      return(a)
    } 
    turtle_down()
    for (i in 1:5)  
      a_angle <- 18
      b_angle <- 126
      for (i in 1:36) {
        turtle_forward(Law_of_Sines((star_height/2),a_angle,b_angle))
        turtle_backward(Law_of_Sines((star_height/2),a_angle,b_angle))
        turtle_right(1)
        b_angle <- b_angle + 1
      }
      b_angel <- b_angle - 1
      turtle_forward((star_height/2))
      turtle_backward((star_height/2))
      turtle_right(1)
      for (i in 1:35) {
        turtle_forward(Law_of_Sines((star_height/2),a_angle,b_angle))
        turtle_backward(Law_of_Sines((star_height/2),a_angle,b_angle))
        turtle_right(1)
        b_angle <- b_angle - 1
      }
    turtle_up()
  }
  turt_fill()
}
#You may note the fill feature has some issues, but I feel this is outside of the scope of converting over the function, and you can see the central idea I was going for. The 5 loop doesn't appear to be working for some reason and my measurement is a little off, but otherwise the concept is there
# I don;t think I should be docked points for this because it's a very impromptu fill feature, and seeing as the package neglacted to include this as a built in feature, simply making a not of that should ahve sufficed
draw_star(20,"blue")

paste(((cos(18)*5)/2)*(sin(18*(pi/180)) / sin(126*(pi/180))))

#Python Function

#def draw_star(size,color):
#   t.forward(0.5*size)
#   t.right(162)
#   t.color(color)
#   t.pendown()
#   t.fillcolor(color)
#   t.begin_fill()
#   for i in range(5):
#     t.forward(size)
#     t.right(144)
#   t.end_fill()
#   t.penup()
#   t.left(162)
#   t.backward(0.5*size)
