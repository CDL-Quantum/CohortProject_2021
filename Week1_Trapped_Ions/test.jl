using PyPlot
p = plot()
for i in 0:10
    scatter(i,0,color="red",linewidth=40.0*0.1)
end
axis("off")


# display(gcf())
show()