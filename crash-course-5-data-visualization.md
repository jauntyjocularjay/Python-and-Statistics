# Data Visualization

## Quantitative Data

- has both order and consistent spacing
- ex perchases of olive oil by ounce

## Categorical Data

- does not have meaningful order or consisent spacing
- ex favorite pastas (macaroni, spaghetti, angel hair, rotini)

## Frequency table

Most common for categorical data

|pasta type|frequency|relative frequency|
|---|---|---|
|macaroni|10|20%|
|linguine|15|30%|
|rotini|20|40%|
|penne|5|10%|

## Binning

takes a quantitative variable and bins it into categories (real or made up)

## Bar charts

represents quantities as comparable bars

## Histogram

a bar chart smooshed together to show continuous data

library(dplyr)

cyl_mpg <- mtcars %>%
        group_by(cyl) %>%
        summarise(avg_mpg = mean(mpg, na.rm = TRUE))

ggplot(cyl_mpg, aes(x = factor(cyl), y = avg_mpg)) +
        geom_bar(stat = "identity")