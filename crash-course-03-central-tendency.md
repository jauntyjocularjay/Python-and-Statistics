# Basics

## the Mean

$$
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
$$

The mean (average) is good for measuring things with a normal distribution.

## normal

- A distribution of data that is symmetric around the mean and the most common values around the middle of the data.
- Think bell curve

## distribution

shows how often each value occurs in a data list

## outliers

unusually large and small values in a data list

## Median

For an ordered data set $x_1, x_2, \ldots, x_n$:

- the middle number if we line up data from smallest to largest
- ex. in [-5,1,1,1,2,2,3,3,3,7], the median is 2
- If $n$ is odd:
  $$
  \text{Median} = x_{\left(\frac{n+1}{2}\right)}
  $$
- If $n$ is even:
  $$
  \text{Median} = \frac{x_{\left(\frac{n}{2}\right)} + x_{\left(\frac{n}{2} + 1\right)}}{2}
  $$

## Mode

- from modus, meaning 'manner, fashion, or style' and gives us the French expression 'a la mode' meaning fashionable
- The most common repeating value in a list of data
- There may be more than one mode
- most useful when there is a large sample with a large number of popular values

## Bimodal

when two values are the most common

## Multimodal data

- when many datum values are similarly common. results from two or more underlying groups are measured together.
- A multimodal distribution can appear to be a single, unified population when two (or more) peaks are symmetrically positioned. In reality there will be two (or more) separate subgroups with their own mean and median.
- The single pooled mean or median will not represent any subgroup well.
- Visualizing data with a histogram or density plot is an important step to detect subgroup structure.

## skewed

when a sample list has unusually extreme values on one side of the distribution

1. the mode (most common value) will be pulled away from the outliers of the distribution
1. the median (middle value) remains in the middle
1. the mean (average) pulls toward the tail toward the outliers
1. Right-skew: mode < median < mean
1. Left-skew: mean < median < mode
1. Symmetric unimodal: mean ≈ median ≈ mode
