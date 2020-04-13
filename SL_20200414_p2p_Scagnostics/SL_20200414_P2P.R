#A real Scagnostics application
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
install.packages("factoextra")
install.packages("cluster")
install.packages("magrittr")


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
library(cluster)
library(factoextra)
library(magrittr)


# Data ------------------------------------------------------------------------------

#change the path to your own
df.input <- read.csv("C:/Users/User/Documents/UNI_Klagenfurt/MA_8Semester/Statistical Learning/SL_Klagenfurt_2020-master/SL_20200414_P2P/p2p.csv",sep=",",dec=".",header=TRUE,na.strings="")
df.input$X <- NULL
str(df.input)

df.data <- df.input[,c('ratio002', 'ratio003', 'ratio004', 'ratio005', 'ratio006', 'ratio011', 'ratio012', 'DPO', 'DSO', 'turnover', 'status', 'ratio037', 'ratio039', 'ratio040')]
df.data_heatmap2 <- df.input[,c('ratio002', 'ratio003', 'ratio004', 'ratio005', 'ratio006', 'turnover', 'status')]

df.cl <- df.input[,c('ratio011', 'ratio037','turnover', 'status')]


# Scatterplot ------------------------------------------------------------------------

df.data_scatter <- df.data[,c('ratio002', 'ratio003', 'ratio004', 'ratio005', 'ratio006', 'ratio011', 'ratio012', 'DPO', 'DSO', 'turnover')]

png(filename = 'Scatterplot_p2p.png', width = 3.25, height = 3.25, units = "in", res = 1200, pointsize = 4)
par(bg = NA, mar = c(5, 5, 2, 2), xaxs = "i", yaxs = "i", cex.axis = 2, cex.lab = 2 )
pairs(df.data_scatter, pch = ".", col = "dodgerblue", main = "P2P Scatterplot")
dev.off()


# Characteristic shape values --------------------------------------------------------

s <- scagnostics(df.data)
s1 <- scagnostics(df.data_heatmap2)
s.cl <- scagnostics(df.cl)

m.scl <- t(as.matrix(s.cl))
m.s <- t(as.matrix(s))
write.csv(m.s, file = paste0("20200414_Scagnostics_p2p.csv"))

m.s1 <- round(t(as.matrix(s1)),2)


# Plotting the SPLOM  ----------------------------------------------------------------

png("SPLOM_p2p.png", width = 3.25, height = 3.25, units = "in", res = 1200, pointsize = 4)
par(bg = NA, mar = c(5, 5, 2, 2), xaxs = "i", yaxs = "i", cex.axis = 2, cex.lab = 2)
pairs(m.s, col = "dodgerblue", main = "P2P SPLOM")
dev.off()


png('Heatmap_p2p.png', width=800, height=800, units = "px", bg = "transparent")
#par(bg = NA, mar = c(10, 10, 10, 10), xaxs = "i", yaxs = "i", cex.axis = 2, cex.lab = 2)
heatmap.2(s, scale="column", main="Heatmap of P2P", col = bluered(100), density="density", #dendrogram = "none",
          notecol="black", margins=c(20,5), cexRow=1, cexCol=1, trace = "none")
dev.off()

png('Heatmap_ratio011&037&turnover&status.png', width=800, height=800, units = "px", bg = "transparent")
#par(bg = NA, mar = c(10, 10, 10, 10), xaxs = "i", yaxs = "i", cex.axis = 2, cex.lab = 2)
heatmap.2(s.cl, scale="column", main="Heatmap of ratio011,ratio037,turnover,status", col = bluered(100), density="density", #dendrogram = "none",
          notecol="black", margins=c(20,5), cexRow=1, cexCol=1, trace = "none")
dev.off()


mypal = colorRampPalette(c("red", "white", "blue"))(n = 300)
png('Heatmap_2_p2p.png', width=800, height=800, units = "px", bg = "transparent")
heatmap.2(m.s1, col = mypal, cellnote = m.s1, scale = "column", density.inf = "none", dendrogram = "none", notecol = "black",
          cexRow = 1, cexCol = 1, margins=c(10,13), trace = "none", keysize = 0, main="Heatmap of P2P")
dev.off()


# plots of columns vs status --------------------------------------------------------------

png(filename = 'variables vs status.png', width = 8, height = 4, units = "in", res = 1200, pointsize = 8)
par(bg = NA, xaxs = "i", yaxs = "i", cex.axis = 2, cex.lab = 2)
par(mfrow = c(2,5))
plot(df.data$ratio002, df.data$status, pch = 1, main = "ratio002 vs status", col = "dodgerblue", xlab = " ", ylab = " ")
plot(df.data$ratio003, df.data$status, pch = 1, main = "ratio003 vs status", col = "dodgerblue", xlab = " ", ylab = " ")
plot(df.data$ratio004, df.data$status, pch = 1, main = "ratio004 vs status", col = "dodgerblue", xlab = " ", ylab = " ")
plot(df.data$ratio005, df.data$status, pch = 1, main = "ratio005 vs status", col = "dodgerblue", xlab = " ", ylab = " ")
plot(df.data$ratio006, df.data$status, pch = 1, main = "ratio006 vs status", col = "dodgerblue", xlab = " ", ylab = " ")
plot(df.data$ratio011, df.data$status, pch = 1, main = "ratio011 vs status", col = "dodgerblue", xlab = " ", ylab = " ")
plot(df.data$ratio012, df.data$status, pch = 1, main = "ratio012 vs status", col = "dodgerblue", xlab = " ", ylab = " ")
plot(df.data$DPO, df.data$status, pch = 1, main = "DPO vs status", col = "dodgerblue", xlab = " ", ylab = " ")
plot(df.data$DSO, df.data$status, pch = 1, main = "DSO vs status", col = "dodgerblue", xlab = " ", ylab = " ")
plot(df.data$turnover, df.data$status, pch = 1, main = "turnover vs status", col = "dodgerblue", xlab = " ", ylab = " ")
dev.off()


png(filename = 'ratio011&037_turnover&status.png', width = 8, height = 4, units = "in", res = 1200, pointsize = 8)
par(bg = NA, xaxs = "i", yaxs = "i", cex.axis = 2, cex.lab = 2)
par(mfrow = c(2,3))
plot(df.data$ratio011, df.data$ratio037, pch = 4, main = "ratio011 vs ratio037", col = "dodgerblue", xlab = " ", ylab = " ")
plot(df.data$ratio011, df.data$turnover, pch = 4, main = "ratio011 vs turnover", col = "dodgerblue", xlab = " ", ylab = " ")
plot(df.data$ratio011, df.data$status, pch = 4, main = "ratio011 vs status", col = "dodgerblue", xlab = " ", ylab = " ")
plot(df.data$ratio037, df.data$turnover, pch = 4, main = "ratio037 vs turnover", col = "dodgerblue", xlab = " ", ylab = " ")
plot(df.data$ratio037, df.data$status, pch = 4, main = "ratio037 vs status", col = "dodgerblue", xlab = " ", ylab = " ")
plot(df.data$status, df.data$turnover, pch = 4, main = "status vs turnover", col = "dodgerblue", xlab = " ", ylab = " ")
dev.off()


# Clustering -----------------------------------------------------------------------

res.dist <- get_dist(s, stand = TRUE, method = "pearson")
  #for computing a distance matrix between the rows of a data matrix. 
  #Compared to the standard dist() function, it supports correlation-based distance measures including "pearson", "kendall" and "spearman" methods.

png(filename = 'distancematrix.png', width=500, height=500, units = "px", bg = "transparent")
par(bg = "transparent", xaxs = "i", yaxs = "i", cex.axis = 2, cex.lab = 2)
fviz_dist(res.dist, gradient = list(low = "#00AFBB", mid = "white", high = "#FC4E07"))+ theme(
  panel.background = element_rect(fill = "transparent",colour = NA),
  panel.grid.minor = element_blank(), 
  panel.grid.major = element_blank(),
  plot.background = element_rect(fill = "transparent",colour = NA)
)#low = turquoise, high = orange
dev.off()


#hierarchical clustering
res.hc <- s %>%
          scale() %>%                    # Scale the data
          dist(method = "euclidean") %>% # Compute dissimilarity matrix
          hclust(method = "ward.D2")     # Compute hierachical clustering

png(filename = 'dendrogram.png', width=500, height=500, units = "px", bg = "transparent")
#par(bg = "transparent", xaxs = "i", yaxs = "i", cex.axis = 2, cex.lab = 2)
fviz_dend(res.hc, k = 4, # Cut in four groups
          cex = 0.5, # label size
          lwd = 1,
          k_colors = c("#2E9FDF", "#00AFBB", "#E7B800", "#FC4E07"),
          color_labels_by_k = TRUE, # color labels by groups
          rect = TRUE # Add rectangle around groups
)+ theme(text = element_text(size=20),
  panel.background = element_rect(fill = "transparent",colour = NA),
  panel.grid.minor = element_blank(), 
  panel.grid.major = element_blank(),
  plot.background = element_rect(fill = "transparent",colour = NA)
)
dev.off()

