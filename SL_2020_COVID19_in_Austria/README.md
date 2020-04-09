[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SL_2020_COVID19_in_Austria** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: SL_2020_COVID19_in_Austria

Published in: SL_Klagenfurt_2020

Description: "Plots of COVID19 data in Austria in the time interval 27.02. - 02.04. in R. Additionaly a wordcloud - code from Python. Corona.txt is needed to create the wordcloud."

Keywords: 'corona, COVID-19, R-plots, wordcloud, ATX, oil-price'

Author: Chiara Wang and Julia Guggenberger

Submitted:  Thu, April 9 2020 by Chiara Wang 

Datafile: Corona.txt, .csv tables for R-plots

```

### R Code
```r

#######   data infections    ######################################################################################

inf<-read.csv("C:/Users/julia/Desktop/Uni/Master/Statistical Learning/infectionsAUT.csv", header=TRUE, sep=".", dec=",")
infections<-as.matrix(inf)

infB<-read.csv("C:/Users/julia/Desktop/Uni/Master/Statistical Learning/infectionsB.csv", header=TRUE, sep=".", dec=",")
infectionsB<-as.matrix(infB)

infK<-read.csv("C:/Users/julia/Desktop/Uni/Master/Statistical Learning/infectionsK.csv", header=TRUE, sep=".", dec=",")
infectionsK<-as.matrix(infK)

infV<-read.csv("C:/Users/julia/Desktop/Uni/Master/Statistical Learning/infectionsV.csv", header=TRUE, sep=".", dec=",")
infectionsV<-as.matrix(infV)

infS<-read.csv("C:/Users/julia/Desktop/Uni/Master/Statistical Learning/infectionsS.csv", header=TRUE, sep=".", dec=",")
infectionsS<-as.matrix(infS)

infSt<-read.csv("C:/Users/julia/Desktop/Uni/Master/Statistical Learning/infectionsSt.csv", header=TRUE, sep=".", dec=",")
infectionsSt<-as.matrix(infSt)

infN<-read.csv("C:/Users/julia/Desktop/Uni/Master/Statistical Learning/infectionsN.csv", header=TRUE, sep=".", dec=",")
infectionsN<-as.matrix(infN)

infO<-read.csv("C:/Users/julia/Desktop/Uni/Master/Statistical Learning/infectionsO.csv", header=TRUE, sep=".", dec=",")
infectionsO<-as.matrix(infO)

infT<-read.csv("C:/Users/julia/Desktop/Uni/Master/Statistical Learning/infectionsT.csv", header=TRUE, sep=".", dec=",")
infectionsT<-as.matrix(infT)

infW<-read.csv("C:/Users/julia/Desktop/Uni/Master/Statistical Learning/infectionsW.csv", header=TRUE, sep=".", dec=",")
infectionsW<-as.matrix(infW)


#########   data deaths    #########################################################################################################

deaths<-read.csv("C:/Users/julia/Desktop/Uni/Master/Statistical Learning/deaths.csv", header=TRUE, sep=".", dec=",")
deaths<-as.matrix(deaths)

deathsB<-read.csv("C:/Users/julia/Desktop/Uni/Master/Statistical Learning/deathsB.csv", header=TRUE, sep=".", dec=",")
deathsB<-as.matrix(deathsB)

deathsK<-read.csv("C:/Users/julia/Desktop/Uni/Master/Statistical Learning/deathsK.csv", header=TRUE, sep=".", dec=",")
deathsK<-as.matrix(deathsK)

deathsN<-read.csv("C:/Users/julia/Desktop/Uni/Master/Statistical Learning/deathsN.csv", header=TRUE, sep=".", dec=",")
deathsN<-as.matrix(deathsN)

deathsO<-read.csv("C:/Users/julia/Desktop/Uni/Master/Statistical Learning/deathsO.csv", header=TRUE, sep=".", dec=",")
deathsO<-as.matrix(deathsO)

deathsV<-read.csv("C:/Users/julia/Desktop/Uni/Master/Statistical Learning/deathsV.csv", header=TRUE, sep=".", dec=",")
deathsV<-as.matrix(deathsV)

deathsS<-read.csv("C:/Users/julia/Desktop/Uni/Master/Statistical Learning/deathsS.csv", header=TRUE, sep=".", dec=",")
deathsS<-as.matrix(deathsS)

deathsSt<-read.csv("C:/Users/julia/Desktop/Uni/Master/Statistical Learning/deathsSt.csv", header=TRUE, sep=".", dec=",")
deathsSt<-as.matrix(deathsSt)

deathsT<-read.csv("C:/Users/julia/Desktop/Uni/Master/Statistical Learning/deathsT.csv", header=TRUE, sep=".", dec=",")
deathsT<-as.matrix(deathsT)

deathsW<-read.csv("C:/Users/julia/Desktop/Uni/Master/Statistical Learning/deathsW.csv", header=TRUE, sep=".", dec=",")
deathsW<-as.matrix(deathsW)



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


####### plot infections Budeslaender #####################################

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

doubling<-read.csv("C:/Users/julia/Desktop/Uni/Master/Statistical Learning/doubling.csv", header=TRUE, sep=".", dec=",")
doublingtime<-as.matrix(doubling)
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

atx<-read.csv("C:/Users/julia/Desktop/Uni/Master/Statistical Learning/atx.csv", header=TRUE, sep=".", dec=",")
atx<-as.matrix(atx)


start <- as.POSIXct('2019-04-09 0:00:00')
end <- as.POSIXct('2020-04-09 0:00:00')
x <- seq(start, end, length.out = 35)
y <- atx
y
df <- data.frame(x, y)
#plot(y ~ x, data = df) #:(

png("atx.png")
par(bg=NA)
plot(y ~ x, data = df, xaxt = 'n', type="l", main="ATX from 9.4.2019 to 9.4.2020", xlab="1 year in steps of 10 days", ylab="Share Price")
axis.POSIXct(1, at = seq(start, end, by = '10 days')) #:)
dev.off()


##########    oil     ################################################

oil<-read.csv("C:/Users/julia/Desktop/Uni/Master/Statistical Learning/oil.csv", header=TRUE, sep=".", dec=",")
oil<-as.matrix(oil)

start <- as.POSIXct('2019-04-09 0:00:00')
end <- as.POSIXct('2020-04-09 0:00:00')
x <- seq(start, end, length.out = 35)
y <- oil
df <- data.frame(x, y)

png("oil.png")
par(bg=NA)
plot(y ~ x, data = df, xaxt = 'n', type="l",main="Development from the Oil-Price from 9.4.2019 to 9.4.2020 in Austria", xlab="1 year in steps of 10 days", ylab="Oil Price in ?")
axis.POSIXct(1, at = seq(start, end, by = '10 days'))
dev.off()


```

automatically created on 2020-04-09