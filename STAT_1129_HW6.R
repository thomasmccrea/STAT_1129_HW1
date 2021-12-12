df.m1 = matrix(c(7,2,9,4,12,13),nrow=2,ncol=3)
df.m2 = matrix(c(1:3,7:9,12:14,19:21),nrow=3,ncol=4)
df.m1%*%df.m2

###################

library(readr)

df <- read_csv("C:/Users/tmccr/Desktop/GWU_Junior_Fall_2021/STAT_1129/midterm project/01-Jan-2020_to_01-Jan-2021.csv")
View(df)
df2 <- read_csv("C:/Users/tmccr/Desktop/GWU_Junior_Fall_2021/STAT_1129/midterm project/Items-01-Jan-2020_to_01-Jan-2021.csv")
View(df2)

df[is.na(df)] <- "0" 
df$'Total Charged'  <- sub('[[:punct:]]','',df$"Total Charged") # need function for str.replace('$','').astype(float)

#Number of items purchased
paste("Number of items purchased in 2020:",length(df$'Total Charged'))

#Calculating the Total Amount of Money Spent on Amazon
paste("Total amount of money spent on Amazon:",sum(as.numeric(df$'Total Charged')))

#Average Spent on Amazon
paste("Average spent per purchase:",mean(as.numeric(df$'Total Charged')))

#Median Purchase on Amazon
paste("Median Purchase:",median(as.numeric(df$'Total Charged')))

### All below was just copied over from Python ###

#Largest Order
paste("Largest Order:",max(as.numeric(df$'Total Charged')))
OrderID_largest_Series = df[as.numeric(df$`Total Charged`)==max(as.numeric(df$`Total Charged`)),]$"Order ID"
paste("Largest Order Item:",df2[df2$`Order ID`==OrderID_largest_Series,"Title"])

#Smallest Order
paste("Smallest Order:",min(as.numeric(df$'Total Charged')))
OrderID_smallest_Series = df[as.numeric(df$`Total Charged`)==min(as.numeric(df$`Total Charged`)),]$"Order ID"
paste("Smallest Order Item:",df2[df2$`Order ID`==OrderID_smallest_Series,"Title"])


df$"Tax Charged" <- sub('[[:punct:]]','',df$"Tax Charged")
View(df)

#Money paid in taxes
paste("Total money paid in taxes:",sum(as.numeric(df$"Tax Charged")))

#Overall tax rate
paste("Overall tax rate:",(sum(as.numeric(df$"Tax Charged")) / sum(as.numeric(df$"Total Charged")))*100,"%")



#df['Order Date'] = pd.to_datetime(df['Order Date'])

#df$`Order Date` = strptime(df$`Order Date`, format = "%m/%d/%Y")
#pd.set_option('display.max_columns', None)
#print(df.head())
#pd.reset_option('display.max_columns')

#Every order plotted chronoligically and measuring money spent
barplot(as.integer(df$`Total Charged`),names.arg = df$`Order Date`)

library(dplyr)
daily_orders = df %>% group_by(`Order Date`) %>% summarise(Freq = sum(as.numeric(`Total Charged`)))

#daily_orders = as.Date(df$`Order Date`)
#aggregate(list(df['Total Charged']),by=list(daily_orders['Order Date']), sum)

#Orders grouped nd plotted reflecting money spent on any given day 
barplot(daily_orders$Freq, xlab = 'Order Date', ylab = 'Total Charged', col = '#61D199')