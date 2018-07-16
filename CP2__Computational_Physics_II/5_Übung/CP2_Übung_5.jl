using PyPlot

N = 16

spins = rand([-1,1],(N,N))
imshow(spins)

#xkcd()



#=
x, y = rand(1:N,(N^2//2).num), rand(1:N,(N^2//2).num)

for i = 1:(N^2//2).num
    spins[x[i],y[i]]= -1
end
liste = zero(N^2)
for x in 1:N
    for y in 1:N
        liste[x,y]=(x, y)
    end
end

x = sum(spins)
#x = 5 // 3
#x = (5//3).num
#println("Ende")
#print(x)
=#
