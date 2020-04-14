getwd()
setwd("C:/Users/julia/Desktop/Uni/Master/Statistical Learning/")

#######   data infections    ######################################################################################

infections<-as.matrix(data(infectionsAUT.csv))
infectionsB<-as.matrix(data(infectionsB.csv))
infectionsK<-as.matrix(data(infectionsK.csv))
infectionsV<-as.matrix(data(infectionsV.csv))
infectionsS<-as.matrix(data(infectionsS.csv))
infectionsSt<-as.matrix(data(infectionsSt.csv))
infectionsN<-as.matrix(data(infectionsN.csv))
infectionsO<-as.matrix(data(infectionsO.csv))
infectionsT<-as.matrix(data(infectionsT.csv))
infectionsW<-as.matrix(data(infectionsW.csv))


#########   data deaths    #########################################################################################################

deaths<-as.matrix(data(deaths.csv))
deathsB<-as.matrix(data(deathsB.csv))
deathsK<-as.matrix(data(deathsK.csv))
deathsN<-as.matrix(data(deathsN.csv))
deathsO<-as.matrix(data(deathsO.csv))
deathsV<-as.matrix(data(deathsV.csv))
deathsS<-as.matrix(data(deathsS.csv))
deathsSt<-as.matrix(data(deathsSt.csv))
deathsT<-as.matrix(data(deathsT.csv))
deathsW<-as.matrix(data(deathsW.csv))



########   plots infections    ############################################################################################

InfectionsPerDay<-cbind(days, infections)
InfectionsPerDay

start <- as.POSIXct('2020-02-26 0:00:00')
end <- as.POSIXct('2020-04-01 0:00:00')
x <- seq(start, end, length.out = 36)
y <- infections
df <- data.frame(x, y)

png("infAT.png")
par(bg=NA)
plot(y ~ x, data = df, xaxt = 'n', type="l", main="Infections from 26.02 to 01.04 in Austria", xlab="", ylab=" total number of infections")
axis.POSIXct(1, at = seq(start, end, by = '1 days'))
dev.off()


####### plot inf Budesländer #####################################

start <- as.POSIXct('2020-02-26 0:00:00')
end <- as.POSIXct('2020-04-01 0:00:00')
x <- seq(start, end, length.out = 36)
y <- infectionsB
df <- data.frame(x, y)

png("infBund.png")
par(bg=NA)
plot(y ~ x, data = df, xaxt = 'n', col="blue", type="l", main="Infections from 26.02 to 01.04 in the 9 provinces of Austria", xlab="", ylab=" total number of infections", ylim=c(0,2500))
axis.POSIXct(1, at = seq(start, end, by = '1 days'))
#plot(days, infectionsB, col="blue", type="l", main="Infections from 26.02 to 01.04 in the 9 provinces of Austria", xlab="days", ylab=" total number of infections", ylim=c(0,2500), xaxt="n")
par(new=TRUE)
plot(days, infectionsK, col="green", type="l", xlab="", ylab="", yaxt="n", xaxt="n", ylim=c(0,2500))
par(new=TRUE)
plot(days, infectionsN, col="red", type="l", xlab="", ylab="", yaxt="n", xaxt="n", ylim=c(0,2500))
par(new=TRUE)
plot(days, infectionsO, col="purple", type="l", xlab="", ylab="", yaxt="n", xaxt="n", ylim=c(0,2500))
par(new=TRUE)
plot(days, infectionsS, col="cyan", type="l", xlab="", ylab="", yaxt="n", xaxt="n", ylim=c(0,2500))
par(new=TRUE)
plot(days, infectionsSt, col="magenta", type="l", xlab="", ylab="", yaxt="n", xaxt="n", ylim=c(0,2500))
par(new=TRUE)
plot(days, infectionsV, type="l", xlab="", ylab="", yaxt="n", xaxt="n", ylim=c(0,2500))
par(new=TRUE)
plot(days, infectionsT, col="gray", type="l", xlab="", ylab="", yaxt="n", xaxt="n", ylim=c(0,2500))
par(new=TRUE)
plot(days, infectionsW, col="orange", type="l", xlab="", ylab="", yaxt="n", xaxt="n", ylim=c(0,2500))
legend(x=5, y=2000, c("Burgenland", "Carinthia", "Lower Austria", "Upper Austria", "Salzburg", "Styria", "Vorarlberg", "Tyrol", "Vienna"), cex=.8, col=c("blue","green", "red", "purple", "cyan", "magenta", "black", "gray", "orange"), pch=c(1:9))
dev.off()


#########   plots deaths    ##########################################################################################

start <- as.POSIXct('2020-03-08 0:00:00')
end <- as.POSIXct('2020-04-01 0:00:00')
x <- seq(start, end, length.out = 36)
y <- deaths
df <- data.frame(x, y)

png("deaths.png")
par(bg=NA)
plot(y ~ x, data = df, xaxt = 'n', type="l",main="Deaths from 08.03 to 01.04 in Austria", xlab="", ylab=" total number of deaths")
axis.POSIXct(1, at = seq(start, end, by = '1 days'))
dev.off()

#plot(days, deaths, type="l", main="Deaths from 08.03 to 01.04 in Austria", xlab="days", ylab=" total number of deaths", xaxt="n")


start <- as.POSIXct('2020-03-08 0:00:00')
end <- as.POSIXct('2020-04-01 0:00:00')
x <- seq(start, end, length.out = 25)
y <- deathsB
df <- data.frame(x, y)

png("deathsBund.png")
par(bg=NA)
plot(y ~ x, data = df, xaxt = 'n', col="blue", type="l",main="Deaths from 08.03 to 01.04 in the 9 provinces of Austria", xlab="", ylab=" total number of deaths", ylim=c(0,35))
axis.POSIXct(1, at = seq(start, end, by = '1 days'))

#plot(day, deathsB, col="blue", type="l", main="Deaths from 08.03 to 01.04 in the 9 provinces of Austria", xlab="days", ylab=" total number of deaths", ylim=c(0,35), xaxt="n")
par(new=TRUE)
plot(day, deathsK, col="green", type="l", xlab="", ylab="", yaxt="n", xaxt="n", ylim=c(0,35))
par(new=TRUE)
plot(day, deathsN, col="red", type="l", xlab="", ylab="", yaxt="n", xaxt="n", ylim=c(0,35))
par(new=TRUE)
plot(day, deathsO, col="purple", type="l", xlab="", ylab="", yaxt="n", xaxt="n", ylim=c(0,35))
par(new=TRUE)
plot(day, deathsS, col="cyan", type="l", xlab="", ylab="", yaxt="n", xaxt="n", ylim=c(0,35))
par(new=TRUE)
plot(day, deathsSt, col="magenta", type="l", xlab="", ylab="", yaxt="n", xaxt="n", ylim=c(0,35))
par(new=TRUE)
plot(day, deathsV, type="l", xlab="", ylab="", yaxt="n", xaxt="n", ylim=c(0,35))
par(new=TRUE)
plot(day, deathsT, col="gray", type="l", xlab="", ylab="", yaxt="n", xaxt="n", ylim=c(0,35))
par(new=TRUE)
plot(day, deathsW, col="orange", type="l", xlab="", ylab="", yaxt="n", xaxt="n", ylim=c(0,35))
legend(x=5, y=30, c("Burgenland", "Carinthia", "Lower Austria", "Upper Austria", "Salzburg", "Styria", "Vorarlberg", "Tyrol", "Vienna"), cex=.8, col=c("blue","green", "red", "purple", "cyan", "magenta", "black", "gray", "orange"), pch=c(1:9))
dev.off()


############    doubling time    ##########################################################################################

doublingtime<-as.matrix(data(doubling.csv))
doublingtime

start <- as.POSIXct('2020-03-08 0:00:00')
end <- as.POSIXct('2020-04-01 0:00:00')
x <- seq(start, end, length.out = 35)
y <- doublingtime
df <- data.frame(x, y)

png("doublingtime.png")
par(bg=NA)
plot(y ~ x, data = df, xaxt = 'n', type="l",main="Development from the Doublingtime from 27.02 to 02.04 in Austria", xlab="", ylab="doublingtime in days")
axis.POSIXct(1, at = seq(start, end, by = '1 days'))
dev.off()

#plot(day, doublingtime, type="l", main="Development from the Doublingtime from 27.02 to 02.04 in Austria", xlab="days", ylab="doublingtime in days", xaxt="n")



################   ATX  ###########################################################

atx<-as.matrix(data(atx.csv))


start <- as.POSIXct('2019-04-09 0:00:00')
end <- as.POSIXct('2020-04-09 0:00:00')
x <- seq(start, end, length.out = 35)
y <- atx
y
df <- data.frame(x, y)

png("atx.png")
par(bg=NA)
plot(y ~ x, data = df, xaxt = 'n', type="l", main="ATX from 9.4.2019 to 9.4.2020", xlab="1 year in steps of 10 days", ylab="Share Price")
axis.POSIXct(1, at = seq(start, end, by = '10 days')) 
dev.off()


##########    oil     ################################################

oil<-as.matrix(data(oil.csv))

start <- as.POSIXct('2019-04-09 0:00:00')
end <- as.POSIXct('2020-04-09 0:00:00')
x <- seq(start, end, length.out = 35)
y <- oil
df <- data.frame(x, y)

png("oil.png")
par(bg=NA)
plot(y ~ x, data = df, xaxt = 'n', type="l",main="Development from the Oil-Price from 9.4.2019 to 9.4.2020 in Austria", xlab="1 year in steps of 10 days", ylab="Oil Price in €")
axis.POSIXct(1, at = seq(start, end, by = '10 days'))
dev.off()
