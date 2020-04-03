[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SL_2020_Wetter_Scagnostics** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml


Name of Quantlet: SL_2020_Wetter_Scagnostics

Published in: SL_Klagenfurt_2020

Description: "Calculates the scagnostic measures for the dataset and plots the SPLOM, the scagnostics SPLOM and the heat-map of the scagnostic measures"

Keywords: 'scagnostics, scagnostic coefficients, SPLOM, heat-map, weather'

Author: Alina Kohlmayer and Michaela Kordasch

Submitted:  Fri, April 3 2020 by Alina Kohlmayer

Datafile: Wetter_Semlach_20200402.csv

```

### R Code
```r

#A real Scagnostics application on money
#Authors: Alina Kohlmayer & Michaela Kordasch

# Packages needed -----------------------------------------------------------

install.packages("rJava")
install.packages("lattice")
install.packages("alphahull")
install.packages("scagnostics")
install.packages("tripack")
install.packages("RTriangle")
install.packages("igraph")
install.packages("psych")
install.packages("gplots")
install.packages("RColorBrewer")


# Libraries -----------------------------------------------------------------

library(rJava)
library(lattice)
library(alphahull)
library(scagnostics)
library(tripack)
library(RTriangle)
library(igraph)
library(psych)
library(gplots)
library(RColorBrewer)


# Data ----------------------------------------------------------------------

df.data <- read.csv("C:/Users/User/Documents/UNI_Klagenfurt/MA_8Semester/Statistical Learning/Wetter-Scagnostics-master/Wetter_Semlach_20200402.csv",sep=",",dec=".",header=TRUE,na.strings="")
df.w <- df.data[,-1]
str(df.w)

df <- as.data.frame(cbind(df.w$temperature, df.w$windspeed))
colnames(df) <- c("temp", "windspeed")

png("temp_vs_windspeed.png")
plot(df, pch = 19, col = "dark red", xlab = "temp", ylab = "windspeed", main = "temperature vs. windspeed")
dev.off()

# Scatterplot ---------------------------------------------------------------

png("scatterplot.png")
plot(df.w)
dev.off()


# Alphashape ----------------------------------------------------------------

ashape.obj <- ashape(df.w, alpha = 0)
str(ashape.obj)


# DT & Minimum Spanning Tree -----------------------------------------------------

# DT
png("DT_MST.png")
par(mfrow = c(1, 2))
tdf <- tri.mesh(df[,1], df[,2], duplicate = "remove")
plot(tdf, xlab = "temperature", ylab = "windspeed", main = "Delaunay Triangulation")

# MST
distance <- dist(df)
G <- graph.adjacency(as.matrix(distance), weighted = TRUE)
mst <- minimum.spanning.tree(G)
edgelist <- matrix(data = as.integer(igraph::get.edgelist(mst)), ncol = 2, byrow = F)

plot(df, pch = 16, col = "dark red", main = "Minimum Spanning Tree") 
for (i in 1:dim(edgelist)[1]){
  from = edgelist[i, 1]
  to = edgelist[i, 2]
  lines(df[c(from, to), 'temp'], df[c(from, to), 'windspeed'])
}
dev.off()

png("Edgedistribution.png")
par(mfrow = c(1, 2))
hist(distance, main = "Edge length distribution of MST")
boxplot(distance)
dev.off()

# Characteristic c values --------------------------------------------------------

s <- scagnostics(df.w)
s
sw <- scagnostics(df)
sw

# Plotting the SPLOM  -----------------------------------------------------

m.s <- as.matrix(s)
m.s1 = as.matrix(t(m.s))

png("SPLOM.png")
pairs(m.s1, col = "dark red", main = "Scagnostics SPLOM")
dev.off()


png("Heatmap.png")
heatmap.2(s, scale="column",
          main="Heatmap of Scagnostics of the Weather",
          density="density",
          #dendrogram = "none",
          notecol="black",
          margins=c(10,5), cexRow=1, cexCol=1, trace = "none")
dev.off()



```

automatically created on 2020-04-03