# Questions Compiled

## 1. Explain the difference between descriptive and inferential statistics.

**Question Type:** Multiple choice

**Choices**

- A. Descriptive statistics draws conclusions about the sets of data based on sampling. Inferential statistics summarizes the information revealed in data sets.
- B. Descriptive statistics are measurements that are recorded on a naturally occurring numerical scale. Inferential statistics are measurements that cannot be measured on a natural number scale; they can only be classified into one of a group of categories.
- C. Descriptive statistics is a characteristic or property of an individual experimental unit. Inferential statistics is the process used to assign numbers to variables of individual population units.
- D. Descriptive statistics describes sets of data. Inferential statistics draws conclusions about the sets of data based on sampling.

**Correct Answer:** D

## 26. A lab orders a shipment of 100 frogs each week. Prices for the weekly shipments of frogs follow the distribution below:

- `$10.00` with probability `0.35`
- `$12.50` with probability `0.15`
- `$15.00` with probability `0.50`

How much should the lab budget for next year's frog orders assuming this distribution does not change? (Assume `52` weeks per year.)

**Question Type:** Expected value

**Expected Weekly Price**

- `E(X) = 10(0.35) + 12.5(0.15) + 15(0.50)`
- `E(X) = 3.5 + 1.875 + 7.5 = 12.875`

**Yearly Budget**

- `12.875 x 52 = 669.5`
- Rounded to the nearest dollar: `$670`

**Correct Answer:** A

## 27. A discrete random variable `x` can assume five possible values, `22`, `23`, `24`, `25`, and `26`. The histogram shows the likelihood of each value.

**Question Type:** Discrete probability from histogram

**Probabilities from the Histogram**

- `p(22) = 0.10`
- `p(23) = 0.15`
- `p(24) = 0.25`
- `p(25) = 0.25`
- `p(26) = 0.25`

**Part a:** What is `p(25)`?

**Correct Answer:** `0.25`

**Part b:** What is the probability that `x` equals `22` or `26`?

**Correct Answer:** `0.35`

**Explanation:** `P(22 or 26) = p(22) + p(26) = 0.10 + 0.25 = 0.35`.

**Part c:** What is `P(x ≤ 23)`?

**Correct Answer:** `0.25`

**Explanation:** `P(x ≤ 23) = p(22) + p(23) = 0.10 + 0.15 = 0.25`.

## 28. One airline averages about `2.3` fatalities per month. Assume that the probability distribution for `x`, the number of fatalities per month, can be approximated by a Poisson probability distribution. Complete parts (a) through (c).

**Question Type:** Poisson distribution

Let `lambda = 2.3`.

**Part a:** What is the probability that no fatalities will occur during any given month?

**Correct Answer:** `0.1003`

**Explanation:** `P(X = 0) = e^(-2.3) * 2.3^0 / 0! = e^(-2.3) ≈ 0.1002588`, which rounds to `0.1003`.

**Part b:** What is the probability that one fatality will occur during any given month?

**Correct Answer:** `0.2306`

**Explanation:** `P(X = 1) = e^(-2.3) * 2.3^1 / 1! ≈ 0.2305953`, which rounds to `0.2306`.

**Part c:** Find `E(x)` and the standard deviation of `x`.

**Correct Answers**

- `E(x) = 2.3`
- Standard deviation `= sqrt(2.3) ≈ 1.5166`

## 29. The university police department must write, on average, five tickets per day to keep department revenues at budgeted levels. Suppose the number of tickets written per day follows a Poisson distribution with a mean of `7.5`. Interpret the value of the mean.

**Question Type:** Interpretation of mean

**Choices**

- A. On half of the days less than 7.5 tickets are written and on half of the days more than 7.5 tickets are written.
- B. If we sampled all days, the arithmetic average number of tickets written would be 7.5 tickets per day.
- C. The number of tickets that is written most often is 7.5 tickets per day.
- D. The mean has no interpretation since 0.5 ticket can never be written.

**Correct Answer:** B

**Explanation:** The mean of `7.5` represents the long-run arithmetic average number of tickets written per day.

## 30. A journal published a study of the lifestyles of visually impaired students. Using diaries, the students kept track of several variables, including number of hours of sleep obtained in a typical day. These visually impaired students had a mean of `8.38` hours and a standard deviation of `2.05` hours. Assume that the distribution of the number of hours of sleep for this group of students is approximately normal. Complete parts a through c.

**Question Type:** Normal distribution

Let `X ~ N(8.38, 2.05)`.

**Part a:** Find `P(x > 12)`.

**Correct Answer:** `0.0387`

**Explanation:** Using `z = (12 - 8.38) / 2.05 ≈ 1.7659`,  
`P(X > 12) = P(Z > 1.7659) ≈ 0.0387`.

**Part b:** Find `P(8 < x < 10)`.

**Correct Answer:** `0.3588`

**Explanation:**  
`P(8 < X < 10) = P(X < 10) - P(X < 8) ≈ 0.3588`.

**Part c:** Find the value `a` for which `P(x < a) = 0.3`.

**Correct Answer:** `7.30`

**Explanation:** The 30th percentile of the standard normal is `z ≈ -0.5244`, so  
`a = 8.38 + (-0.5244)(2.05) ≈ 7.3050`, which rounds to `7.30`.

**Explanation:** Descriptive statistics is used to summarize and describe data, while inferential statistics uses sample data to make conclusions or predictions.

## 2. What is a representative sample? What is its value?

**Question Type:** Multiple choice

**Choices**

- A. A representative sample is a sample that exhibits characteristics typical of those possessed by the population of interest. It is valuable because these characteristics allow inferential statistics to be applied.
- B. A representative sample is a sample that is selected at random from the population of interest. It is valuable because its unbiased nature allows inferential statistics to be applied.
- C. A representative sample is a sample that exhibits characteristics typical of those possessed by the population of interest. It is valuable because these characteristics allow descriptive statistics to be applied.
- D. A representative sample is a sample that is selected at random from the population of interest. It is valuable because its unbiased nature allows descriptive statistics to be applied.

**Correct Answer:** A

**Explanation:** A representative sample reflects the important characteristics of the population, which makes it useful for drawing conclusions through inferential statistics.

## 3. Suppose you're given a data set that classifies each sample unit into one of four categories: A, B, C, or D. You plan to create a computer database consisting of these data, and you decide to code the data as A = 1, B = 2, C = 3, and D = 4. Are the data consisting of the classifications A, B, C, and D qualitative or quantitative? After the data are input as 1, 2, 3, or 4, are they qualitative or quantitative?

**Question Type:** Multiple choice

**Part 1:** Are the data consisting of the classifications A, B, C, and D qualitative or quantitative?

**Choices**

- A. Qualitative, because they are measured on a naturally occurring numerical scale.
- B. Qualitative, because they can only be classified into categories.
- C. Quantitative, because they are measured on a naturally occurring numerical scale.
- D. Quantitative, because they can only be classified into categories.

**Correct Answer:** B

**Explanation:** The values A, B, C, and D are category labels, so the data are qualitative.

**Part 2:** After the data are input as 1, 2, 3, or 4, are they qualitative or quantitative?

**Choices**

- A. Qualitative, because they are measured on a naturally occurring numerical scale.
- B. Quantitative, because they are measured on a naturally occurring numerical scale.
- C. Qualitative, because they cannot be meaningfully added, subtracted, multiplied, or divided.
- D. Quantitative, because they cannot be meaningfully added, subtracted, multiplied, or divided.

**Correct Answer:** C

**Explanation:** Even after being coded as numbers, the values still only represent categories, so they remain qualitative rather than quantitative.

## 4. Pollsters regularly conduct opinion polls to determine the popularity rating of the current president. Suppose a poll is to be conducted tomorrow in which 8,500 individuals will be asked whether the president is doing a good or bad job. The 8,500 individuals will be selected by random-digit telephone dialing and asked the question over the phone. Complete parts a through f.

**Question Type:** Multiple choice

**Part a:** What is the relevant population?

**Choices**

- A. All people who do not respond to the survey
- B. All people who respond that the president is doing a good job
- C. All people in the country
- D. The 8,500 individuals surveyed

**Correct Answer:** C

**Explanation:** The population is the entire group the pollster wants information about, which is all people in the country.

**Part b(1):** What is the variable of interest?

**Choices**

- A. The number of people in the country
- B. The number of people surveyed
- C. If the question was answered
- D. The president's job performance

**Correct Answer:** D

**Explanation:** The poll measures each person's opinion about whether the president is doing a good or bad job.

**Part b(2):** Is the variable quantitative or qualitative?

**Choices**

- A. The variable is a quantitative variable. Its values can be expressed on a naturally occurring numerical scale.
- B. The variable is a qualitative variable. Its values cannot be expressed on a naturally occurring numerical scale.
- C. The variable is a quantitative variable. Its values cannot be expressed on a naturally occurring numerical scale.
- D. The variable is a qualitative variable. Its values can be expressed on a naturally occurring numerical scale.

**Correct Answer:** B

**Explanation:** The responses are categories such as "good job" or "bad job," so the variable is qualitative.

**Part c:** What is the sample?

**Choices**

- A. All people in the country
- B. The 8,500 individuals surveyed
- C. All people who do not respond to the survey
- D. All people who respond that the president is doing a good job

**Correct Answer:** B

**Explanation:** The sample is the group from which the data are actually collected.

**Part d:** What is the inference of interest to the pollster?

**Choices**

- A. Estimate the proportion of all citizens who believe the president is doing a good job
- B. Estimate the number of people who will respond to the survey
- C. Estimate the number of people in the country
- D. Estimate the number of people surveyed

**Correct Answer:** A

**Explanation:** The goal is to use the sample results to estimate public opinion in the full population.

**Part e:** What method of data collection is employed?

**Choices**

- A. A stratified random sample
- B. A random number generator
- C. A survey
- D. A cluster sample

**Correct Answer:** C

**Explanation:** The poll collects responses by asking people a question, so the method is a survey.

**Part f:** How likely is the sample to be representative?

**Choices**

- A. Very likely, because the sample is a simple random sample and the sample size is large.
- B. Not very likely, because only people with telephones that are willing to answer a survey will be counted in the results.
- C. Not very likely, because the sample is a simple random sample and the sample size is large.
- D. Very likely, because the sample contains people who have telephones and the sample size is large.

**Correct Answer:** B

**Explanation:** Telephone polling can miss people without phone access or those who refuse to answer, so the sample may not fully represent the population.

## 5. One aspect of a study involved describing the type of tenant typically found at a shopping mall. Data were collected for 127 shopping malls, which housed 1,922 stores. Tenants were categorized based on amount of floor space: anchor tenants (more than 30,000 square feet, denoted by A), major space users (between 10,000 and 30,000 sq ft, denoted by MS), large standard tenants (between 4,000 and 10,000 sq ft, denoted by LS), small standard tenants (between 1,500 and 4,000 sq ft, denoted by SS), and small tenants (less than 1,500 sq ft, denoted by S). The number of stores in each tenant category was reported as 750, 72, 244, 827, and 29, respectively. Use this information to construct a Pareto diagram for the distribution of tenant groups at shopping malls. Interpret the graph.

**Question Type:** Multiple choice

**Data**

- A: 750
- MS: 72
- LS: 244
- SS: 827
- S: 29

**Part 1:** Construct a Pareto diagram for the data.

**Correct Answer:** D

**Explanation:** A Pareto diagram orders categories from greatest frequency to least frequency. The correct order is `SS (827)`, `A (750)`, `LS (244)`, `MS (72)`, `S (29)`, which matches option D.

**Part 2:** Interpret the Pareto diagram.

**Choices**

- A. Few stores in shopping malls are large standard tenants or small standard tenants.
- B. Most stores in shopping malls are small standard tenants or small tenants.
- C. Few stores in shopping malls are anchor tenants or major space users.
- D. Most stores in shopping malls are small standard tenants or anchor tenants.

**Correct Answer:** D

**Explanation:** The two largest categories are small standard tenants and anchor tenants, and together they account for most of the stores.

## 6. Consider the stem-and-leaf display to the right.

**Question Type:** Mixed response / multiple choice

**Stem-and-Leaf Display**

- 3 | 788
- 2 | 4888
- 1 | 0448
- 0 | 056

**Part a:** How many observations were in the original data set?

**Correct Answer:** 14

**Explanation:** The number of observations equals the total number of leaves: `3 + 4 + 4 + 3 = 14`.

**Part b:** In the bottom row of the stem-and-leaf display, identify the stem, the leaves, and the numbers in the original data set represented by this stem and its leaves.

**Choices**

- A. The stem is 0 and the leaves are 0, 5, 6. The numbers in the original data set are 10, 15, 16.
- B. The stem is 056 and the leaf is 0. The number in the original data set is 10.
- C. The stem is 0 and the leaves are 0, 5, 6. The numbers in the original data set are 0, 5, 6.
- D. The stem is 056 and the leaf is 0. The number in the original data set is 0.

**Correct Answer:** C

**Explanation:** In a stem-and-leaf plot, the stem is the leading digit and the leaves are the trailing digits. So `0 | 056` represents `0`, `5`, and `6`.

**Part c:** Re-create all the numbers in the data set and construct a dot plot.

**Re-created Data Set**

- 0, 5, 6, 10, 14, 14, 18, 24, 28, 28, 28, 37, 38, 38

**Correct Answer:** B

**Explanation:** The correct dot plot must show one dot at `0`, one at `5`, one at `6`, one at `10`, two at `14`, one at `18`, one at `24`, three at `28`, one at `37`, and two at `38`, which matches option B.

## 7. Researchers developed a method for ranking the total driving performance of golfers. The method requires knowing a golfer's average driving distance (yards) and driving accuracy (percent of drives that land in the fairway). The values of these two variables are used to compute a driving performance index. Twenty driving performance index observations are listed in the table below. Use this information to complete parts a through c.

**Question Type:** Mixed response / multiple choice

**Data**

- 1.23, 2.86, 1.66, 1.99, 1.31, 1.41, 1.77, 2.91, 2.56, 1.41
- 3.43, 2.34, 3.29, 1.41, 2.01, 1.23, 2.47, 2.14, 2.18, 1.39

**Part a:** Find the mean, median, and mode for the 20 driving performance index values.

**Correct Answers**

- Mean: `2.050`
- Median: `2.000`
- Mode: `1.41`

**Explanation:** The mean is the average of all 20 values, the median is the average of the 10th and 11th ordered values (`1.99` and `2.01`), and the mode is `1.41` because it appears three times.

**Part b(1):** Interpret the mean.

**Choices**

- A. The mean is the average driving performance index value.
- B. The mean is the driving performance index value that occurs most often in the data set.
- C. The mean is the driving performance index value such that half of the values in the data set are higher than it.

**Correct Answer:** A

**Part b(2):** Interpret the median.

**Choices**

- A. The median is the average driving performance index value.
- B. The median is the driving performance index value that occurs most often in the data set.
- C. The median is the driving performance index value such that half of the values in the data set are higher than it.

**Correct Answer:** C

**Part b(3):** Interpret the mode.

**Choices**

- A. The mode is the average driving performance index value.
- B. The mode is the driving performance index value that occurs most often in the data set.
- C. The mode is the driving performance index value such that half of the values in the data set are higher than it.

**Correct Answer:** B

**Part c:** Use the results from part a to make a statement about the type of skewness in the distribution of driving performance indexes. Support your statement with a graph. The class interval size is 0.4.

**Correct Answer:** A

**Explanation:** Since the mean (`2.050`) is slightly greater than the median (`2.000`), and both are greater than the mode (`1.41`), the distribution is skewed to the right. This matches histogram A.

## 8. A study examined the decay properties of sandstone when exposed to the weather. In the study, slices of sandstone blocks were tested for permeability under three conditions: no exposure to any type of weathering (A), repeatedly sprayed with 10% salt solution (B), and soaked in a 10% salt solution and dried (C). Measures of variation for the permeability measurements (mV) of each sandstone group are displayed in the accompanying technology printout. Complete parts a through c.

**Question Type:** Mixed response

**Technology Output**

- PermA: `N = 100`, `StDev = 14.87`, `Variance = 221.19`, `Minimum = 54.40`, `Maximum = 120.70`, `Range = 66.30`
- PermB: `N = 100`, `StDev = 22.22`, `Variance = 493.56`, `Minimum = 50.80`, `Maximum = 150.40`, `Range = 99.60`
- PermC: `N = 100`, `StDev = 20.49`, `Variance = 419.74`, `Minimum = 53.20`, `Maximum = 129.40`, `Range = 76.20`

**Part a:** Find the range of the permeability measurements for Group A sandstone slices. Verify its value using the minimum and maximum values shown on the printout.

**Correct Answers**

- Range from technology output: `66.30`
- Minimum: `54.40`
- Maximum: `120.70`
- Formula check: `120.70 - 54.40 = 66.30`

**Conclusion:** The range given in the technology output agrees with the result found with the range formula.

**Part b:** Find the standard deviation of the permeability measurements for Group A sandstone slices. Verify its value using the variance shown on the printout.

**Correct Answers**

- Standard deviation from technology output: `14.87`
- Variance: `221.19`
- Formula check: `Standard deviation = sqrt(221.19) = 14.872457765951127`, which rounds to `14.87`

**Conclusion:** The standard deviation given in the technology output agrees with the result found using the variance formula.

**Part c:** Which condition (A, B, or C) has the more variable permeability data?

**Correct Answer:** Condition `B`

**Explanation:** Condition B has the most variable permeability data because it has the largest values of the standard deviation, variance, and range.

## 9. Scores on a mathematics assessment test for eighth-graders have a mean of 276, a 10th percentile of 230, a 25th percentile of 250, a 75th percentile of 310, and a 90th percentile of 322. Interpret each of these numerical descriptive measures.

**Question Type:** Mixed response / multiple choice

**Part 1:** Interpret the mean value of 276.

**Choices**

- A. For this problem, the mean value of 276 represents the variation in the test scores on a mathematics assessment test for eighth-graders.
- B. For this problem, the mean value of 276 represents the average test score on a mathematics assessment test for eighth-graders.
- C. For this problem, the mean value of 276 represents the middle test score when the scores are arranged in ascending (or descending) order.
- D. For this problem, the mean value of 276 represents the range of test scores on a mathematics assessment test for eighth-graders.

**Correct Answer:** B

**Part 2:** Interpret the percentiles.

**Correct Answers**

- 10th percentile of `230`: `10%` of the scores fall below `230` and `90%` of the scores fall above `230`.
- 25th percentile of `250`: `25%` of the scores fall below `250` and `75%` of the scores fall above `250`.
- 75th percentile of `310`: `75%` of the scores fall below `310` and `25%` of the scores fall above `310`.
- 90th percentile of `322`: `90%` of the scores fall below `322` and `10%` of the scores fall above `322`.

**Explanation:** The mean is the average score, and the `p`th percentile indicates that about `p%` of observations are below that value and about `(100 - p)%` are above it.

## 10. For a sample of 114 transformers built for heavy industry, the mean and standard deviation of the number of sags per week were 323 and 38, respectively; also, the mean and standard deviation of the number of swells per week were 146 and 30, respectively. Consider a transformer that has 197 sags and 195 swells in a week. Complete parts a and b below.

**Question Type:** Multiple choice

**Part a:** Would you consider 197 sags per week unusual, statistically? Explain.

**Calculation**

- `z = (197 - 323) / 38 = -3.3157894736842106`
- Rounded to two decimals: `-3.32`

**Correct Answer:** C

**Explanation:** Because the z-score is less than `-2`, the value is unusual. It is far below the mean, so almost every other transformer has more sags.

**Part b:** Would you consider 195 swells per week unusual, statistically? Explain.

**Calculation**

- `z = (195 - 146) / 30 = 1.6333333333333333`
- Rounded to two decimals: `1.63`

**Correct Answer:** D

**Explanation:** Because the z-score is between `-2` and `2`, the value is not considered unusual and is not an outlier.

## 11. Consider the 2 x 3 (i.e., r = 2 and c = 3) contingency table shown to the right. Complete the below questions.

**Question Type:** Computation

**Observed Table**

- Row 1: `8, 32, 55`
- Row 2: `19, 26, 25`

**Totals**

- Row totals: `95`, `70`
- Column totals: `27`, `58`, `80`
- Grand total: `165`

**Expected Cell Counts**  
Using `E_ij = (row total x column total) / grand total`

- `E11 = (95 x 27) / 165 = 15.545`
- `E12 = (95 x 58) / 165 = 33.394`
- `E13 = (95 x 80) / 165 = 46.061`
- `E21 = (70 x 27) / 165 = 11.455`
- `E22 = (70 x 58) / 165 = 24.606`
- `E23 = (70 x 80) / 165 = 33.939`

**Chi-Squared Indicator**

- `chi^2 = 12.860`

**Cramer's V Coefficient**

- `V = 0.279`

## 12. A news magazine reported the results of its annual travel professionals survey. A total of 284 travel professionals, 96 males and 188 females, participated in the 2005 survey. One question asked for the travel professional's opinion on the fairness of his/her salary. Responses were classified as "salary too low," "equitable/fair," or "paid well." The table gives a breakdown of the responses in each category by gender. Complete parts a through d.

**Question Type:** Mixed response / multiple choice

**Data**

- Salary too low: Males `30`, Females `99`
- Equitable/fair: Males `56`, Females `66`
- Paid well: Males `10`, Females `23`
- Totals: Males `96`, Females `188`

**Part a:** Compare the proportions who believe their salary is too low.

**Correct Answers**

- Male proportion: `30 / 96 = 0.313`
- Female proportion: `99 / 188 = 0.527`

**Conclusion:** The proportions are different.

**Part b:** Compare the proportions who believe their salary is equitable/fair.

**Correct Answers**

- Male proportion: `56 / 96 = 0.583`
- Female proportion: `66 / 188 = 0.351`

**Conclusion:** The proportions are different.

**Part c:** Compare the proportions who believe they are paid well.

**Correct Answers**

- Male proportion: `10 / 96 = 0.104`
- Female proportion: `23 / 188 = 0.122`

**Conclusion:** The proportions are approximately the same.

**Part d:** Based on the comparisons in parts a-c, do you think opinion on the fairness of a travel professional's salary differs for males and females?

**Correct Answer:** D

**Explanation:** There appear to be differences between males and females on 2 of the 3 response levels.

## 13. Plot the following lines.

- a. `y = 6 + x`
- b. `y = 6 - 3x`
- c. `y = -5x`

**Question Type:** Multiple choice

**Part a:** Choose the correct graph.

**Correct Answer:** A

**Explanation:** `y = x + 6` has slope `+1` and y-intercept `6`, so the line rises left to right and crosses the y-axis above the origin.

**Part b:** Choose the correct graph.

**Correct Answer:** B

**Explanation:** `y = 6 - 3x` has slope `-3` and y-intercept `6`, so the line falls steeply from left to right and crosses the y-axis at `6`.

**Part c:** Choose the correct graph.

**Correct Answer:** B

**Explanation:** `y = -5x` has a steep negative slope and passes through the origin.

## 14. An economic research firm ranked the 40 best-paid CEOs. The data were collected on a CEO's age and ratio of salary to a typical worker's pay at the firm. One objective is to predict the ratio of salary to worker pay based on the CEO's age. In this study, identify the explanatory (predictor) and response (predicted) variables.

**Question Type:** Multiple choice

**Choices**

- A. The predictor variable is the CEO's age and the predicted variable is the CEO's salary.
- B. The predictor variable is the ratio of CEO salary to worker pay and the predicted variable is the CEO's age.
- C. The predictor variable is the CEO's age and the predicted variable is the ratio of CEO salary to worker pay.
- D. The predictor variable is the CEO's salary and the predicted variable is the CEO's age.

**Correct Answer:** C

**Explanation:** The problem says the ratio of salary to worker pay is being predicted based on the CEO's age, so age is the predictor and the ratio is the response.

## 15. Consider the following pairs of measurements.

**Question Type:** Multiple choice

**Data Pairs**

- `(5, 3)`
- `(4, 5)`
- `(-2, 0)`
- `(2, 1)`
- `(8, 9)`
- `(5, 4)`
- `(4, 3)`

**Part a:** Construct a scatterplot of these data.

**Correct Answer:** D

**Explanation:** The correct scatterplot must include the point `(-2, 0)`, the point `(2, 1)`, two points with `x = 4`, two points with `x = 5`, and the high point `(8, 9)`. This matches option D.

**Part b:** What does the scatterplot suggest about the relationship between x and y?

**Correct Answer:** A

**Explanation:** As `x` increases, `y` tends to increase, so the scatterplot suggests a positive linear relationship.

**Part c:** Plot the least squares line on your scatterplot. Does the line appear to fit the data well? Explain.

**Least Squares Line**

- Slope: approximately `0.838`
- Intercept: approximately `0.458`
- Regression line: `y = 0.458 + 0.838x`

**Correct Graph:** D

**Fit Interpretation:** C

**Explanation:** The line has a positive slope and fits the pattern reasonably well because the data points do not vary very far from the line.

## 16. An association was formed by students to protest labor exploitation in the apparel industry. There were 18 student "sit-ins" for a "sweat-free campus" organized at several universities. Data were collected for the duration (in days) of each sit-in, as well as the number of student arrests. The data for 5 sit-ins in which there was at least one arrest and the results of a simple linear regression are found below. Let `y` be the number of arrests and `x` be the duration. Complete the parts shown.

**Question Type:** Mixed response / multiple choice

**Data**

- `(duration, arrests) = (4, 50)`
- `(duration, arrests) = (1, 11)`
- `(duration, arrests) = (2, 14)`
- `(duration, arrests) = (4, 16)`
- `(duration, arrests) = (1, 12)`

**Regression Results**

- Intercept (`Constant`) = `2.913`
- Slope (`DURATION`) = `7.370`

**Part a:** Write the equation of a straight-line model relating `y` to `x`.

**Correct Answer:** A

**Model Form:** `y = beta_0 + beta_1 x`

**Part b:** Use the results of the linear regression to find the least squares prediction equation.

**Correct Answer:** `y_hat = 2.913 + 7.370x`

**Part c(1):** Give a practical interpretation of the y-intercept of the least squares line.

**Correct Answer:** B

**Explanation:** A sit-in with duration `0` days is outside the range of the sample data, so the y-intercept has no practical interpretation here.

**Part c(2):** Give a practical interpretation of the slope of the least squares line.

**Correct Answer:** C

**Explanation:** For each additional one day of duration, the predicted number of arrests is estimated to increase by `7.370`.

**Part c(3):** Over what range is the interpretation meaningful?

**Correct Answer:** B

**Explanation:** The interpretation is valid only for sit-ins with durations within the range of the sample data, which is from `1` to `4` days.

## 17. A researcher notes that, in a certain country, a disproportionate number of software millionaires were born around the year 1955. The researcher investigated this question by analyzing the data shown in the accompanying table.

**Question Type:** Mixed response / multiple choice

**Data**

- 1920: total births `28.627`, software millionaire birthdays `2`
- 1930: total births `24.272`, software millionaire birthdays `1`
- 1940: total births `31.992`, software millionaire birthdays `10`
- 1950: total births `40.413`, software millionaire birthdays `16`
- 1960: total births `38.456`, software millionaire birthdays `9`
- 1970: total births `33.141`, software millionaire birthdays `6`

Let `x` = total births in the country (millions) and `y` = number of software millionaire birthdays.

**Part a:** Give the least squares prediction equation.

**Correct Answer:** `y_hat = -19.71 + 0.82x`

**Explanation:** Using the six data pairs, the least squares estimates are intercept `-19.7146` and slope `0.8242`, which round to two decimals.

**Part b(1):** Practically interpret the estimated y-intercept.

**Correct Answer:** C

**Explanation:** The y-intercept would correspond to a decade with `0` total births, which is outside the observed data range and has no practical interpretation.

**Part b(2):** Practically interpret the estimated slope.

**Correct Answer:** B

**Explanation:** For each additional increase of `1` million births in the country, the predicted number of software millionaire birthdays is estimated to increase by about `0.82`.

**Part c:** Predict the number of software millionaire birthdays that will occur in a decade where the total number of births in this country is 26 million.

**Correct Answer:** `1.71`

**Explanation:** Substituting `x = 26` into the least squares line gives `y_hat = -19.7146 + 0.8242(26) = 1.7148`, which rounds to `1.71`.

## 18. In a study, college students repeatedly played a version of the game "prisoner's dilemma," where competitors chose cooperation, defection, or costly punishment. At the conclusion of the games, the researchers recorded the average payoff and the number of times cooperation, defection, and punishment were used for each player. The accompanying scatterplots plot average payoff (`y`) against level of cooperation use, defection use, and punishment use, respectively.

**Question Type:** Scatterplot interpretation

**Part a:** Consider cooperation use (`x`) as a predictor of average payoff (`y`). Based on the scatterplot, is there evidence of a linear trend?

**Correct Answer:** There is **no clear evidence** of a linear trend, because as the value of the x-variable increases, the y-variable does not consistently increase or decrease.

**Part b:** Consider defection use (`x`) as a predictor of average payoff (`y`). Based on the scatterplot, is there evidence of a linear trend?

**Correct Answer:** There is **no clear evidence** of a linear trend, because as the value of the x-variable increases, the y-variable does not consistently increase or decrease.

**Part c:** Consider punishment use (`x`) as a predictor of average payoff (`y`). Based on the scatterplot, is there evidence of a linear trend?

**Correct Answer:** There **is evidence** of a linear trend, because as the value of the x-variable increases, the y-variable tends to decrease.

**Part d:** Refer to part c. Is the slope of the line relating punishment use (`x`) to average payoff (`y`) positive or negative?

**Correct Answer:** The slope is **negative**.

## 19. Suppose `P(B) = 0.5`, `P(D) = 0.4`, and `P(B ∩ D) = 0.3`. Find the probabilities below.

**Question Type:** Probability computation

**Part a:** `P(D^c)`

**Correct Answer:** `0.6`

**Explanation:** `P(D^c) = 1 - P(D) = 1 - 0.4 = 0.6`.

**Part b:** `P(B^c)`

**Correct Answer:** `0.5`

**Explanation:** `P(B^c) = 1 - P(B) = 1 - 0.5 = 0.5`.

**Part c:** `P(B ∪ D)`

**Correct Answer:** `0.6`

**Explanation:** `P(B ∪ D) = P(B) + P(D) - P(B ∩ D) = 0.5 + 0.4 - 0.3 = 0.6`.

## 20. A certain magazine published a study on how well firefighter gloves fit. In a group of 591 firefighters who reported their glove size, the researchers determined whether the gloves fit well or poorly, by gender. Consider the gender and glove fit status of a randomly selected firefighter. Complete parts a through f.

**Question Type:** Probability from contingency table

**Data Table**

- Males, glove fits well: `404`
- Males, glove fits poorly: `140`
- Females, glove fits well: `22`
- Females, glove fits poorly: `25`
- Total firefighters: `591`

**Part a:** Identify the sample points for this experiment.

**Correct Answer:** C

**Explanation:** The sample points are the four possible combined outcomes:
- male and glove fits well
- male and glove fits poorly
- female and glove fits well
- female and glove fits poorly

**Part b:** Assign reasonable probabilities to the sample points, in the same order as part a.

**Correct Answer:** D

**Probabilities**

- `P(male and well) = 404 / 591 = 0.684`
- `P(male and poorly) = 140 / 591 = 0.237`
- `P(female and well) = 22 / 591 = 0.037`
- `P(female and poorly) = 25 / 591 = 0.042`

**Part c:** Find the probability the firefighter is a female.

**Correct Answer:** `47 / 591 = 0.080`

**Part d:** Find the probability the glove fits well.

**Correct Answer:** `426 / 591 = 0.721`

**Part e:** Find the probability the firefighter is a male and has a poorly-fitting glove.

**Correct Answer:** `140 / 591 = 0.237`

**Part f:** Find the probability the firefighter is a male or has a poorly-fitting glove.

**Correct Answer:** `0.963`

**Explanation:** `P(male or poorly fitting) = P(male) + P(poorly fitting) - P(male and poorly fitting) = 544/591 + 165/591 - 140/591 = 569/591 = 0.963`.

## 21. In a certain region, the competition for social networking is between Network A and Network B. According to a survey, `13%` of the region's citizens visit Network A, `11%` visit Network B, and `2%` visit both Network A and Network B. Complete parts a through c.

**Question Type:** Probability / Venn diagram

**Part a:** Draw a Venn diagram to illustrate the results.

**Correct Answer:** C

**Explanation:** Since some citizens visit both networks, the circles for A and B must overlap.

**Part b:** Find the probability that a citizen from the region visits either Network A or Network B.

**Correct Answer:** `0.22`

**Explanation:** `P(A ∪ B) = P(A) + P(B) - P(A ∩ B) = 0.13 + 0.11 - 0.02 = 0.22`.

**Part c:** Use your answer to part b to find the probability that a citizen from the region does not visit either social networking site.

**Correct Answer:** `0.78`

**Explanation:** The complement of visiting either network is `1 - 0.22 = 0.78`.

## 22. For two events, `P(A) = 0.4`, `P(B) = 0.5`, and `P(A ∩ B) = 0.2`.

**Question Type:** Conditional probability / independence

**Part a:** Find `P(A|B)`.

**Correct Answer:** `0.4`

**Explanation:** `P(A|B) = P(A ∩ B) / P(B) = 0.2 / 0.5 = 0.4`.

**Part b:** Find `P(B|A)`.

**Correct Answer:** `0.5`

**Explanation:** `P(B|A) = P(A ∩ B) / P(A) = 0.2 / 0.4 = 0.5`.

**Part c:** Are A and B independent events?

**Correct Answer:** B

**Explanation:** The events are independent because `P(A|B) = 0.4 = P(A)`.

## 23. Some statisticians investigated the accuracy of using ultrasound to test for a genetic marker of a medical condition. Let `D` denote that the fetus has the genetic marker and `N` denote that the ultrasound test is normal. The statisticians desire the probability `P(D|N)`. Use Bayes's rule and represent the probabilities using a tree diagram to find the desired probability.

**Question Type:** Bayes's rule

**Given**

- `P(D) = 1/84`
- `P(D^c) = 83/84`
- `P(N|D) = 1/2`
- `P(N^c|D) = 1/2`
- `P(N|D^c) = 1`
- `P(N^c|D^c) = 0`

**Find:** `P(D|N)`

**Correct Answer:** `0.0060`

**Explanation:**  
`P(D and N) = P(D)P(N|D) = (1/84)(1/2) = 1/168`  
`P(N) = P(D)P(N|D) + P(D^c)P(N|D^c) = 1/168 + 83/84 = 167/168`  
So,
`P(D|N) = P(D and N) / P(N) = (1/168) / (167/168) = 1/167 ≈ 0.0060`.

## 24. A company published the results of a study that found that arrogant workers are more likely to have poor performance ratings. Suppose that `22%` of all full-time workers exhibit arrogant behaviors on the job and that `16%` of all full-time workers will receive a poor performance rating. Also, assume that `12%` of all full-time workers exhibit arrogant behaviors and receive a poor performance rating. Let `A` be the event that a full-time worker exhibits arrogant behavior on the job. Let `B` be the event that a full-time worker will receive a poor performance rating.

**Question Type:** Probability / conditional probability / independence

**Given**

- `P(A) = 0.22`
- `P(B) = 0.16`
- `P(A ∩ B) = 0.12`

**Part a:** Are the events A and B mutually exclusive?

**Correct Answer:** B

**Explanation:** The events are not mutually exclusive because `P(A ∩ B) = 0.12`, so some workers both exhibit arrogant behaviors and receive a poor performance rating.

**Part b:** Find `P(B|A)`.

**Correct Answer:** `0.545`

**Explanation:** `P(B|A) = P(A ∩ B) / P(A) = 0.12 / 0.22 = 0.54545...`, which rounds to `0.545`.

**Part c:** Are the events A and B independent?

**Correct Answer:** D

**Explanation:** The events are not independent because `P(B|A) = 0.545` is not equal to `P(B) = 0.16`; workers who exhibit arrogant behaviors are more likely to receive a poor performance rating.

## 25. The Fresh Oven Bakery knows that the number of pies it can sell varies from day to day. The owner believes that on `50%` of the days she sells `100` pies. On another `25%` of the days she sells `150` pies, and she sells `200` pies on the remaining `25%` of the days. To make sure she has enough product, the owner bakes `200` pies each day at a cost of `$2.50` each. Assume any pies that go unsold are thrown out at the end of the day. If she sells the pies for `$5` each, find the probability distribution for her daily profit.

**Question Type:** Probability distribution / expected profit setup

**Cost**

- Daily production cost: `200 x $2.50 = $500`

**Profit Outcomes**

- If `100` pies are sold: revenue `100 x $5 = $500`, profit `$0`
- If `150` pies are sold: revenue `150 x $5 = $750`, profit `$250`
- If `200` pies are sold: revenue `200 x $5 = $1000`, profit `$500`

**Probability Distribution**

- `$0` with probability `0.50`
- `$250` with probability `0.25`
- `$500` with probability `0.25`

**Correct Answer:** D

## 26. A lab orders a shipment of 100 frogs each week. Prices for the weekly shipments of frogs follow the distribution below:

- `$10.00` with probability `0.35`
- `$12.50` with probability `0.15`
- `$15.00` with probability `0.50`

How much should the lab budget for next year's frog orders assuming this distribution does not change? (Assume `52` weeks per year.)

**Question Type:** Expected value

**Expected Weekly Price**

- `E(X) = 10(0.35) + 12.5(0.15) + 15(0.50)`
- `E(X) = 3.5 + 1.875 + 7.5 = 12.875`

**Yearly Budget**

- `12.875 x 52 = 669.5`
- Rounded to the nearest dollar: `$670`

**Correct Answer:** A

## 27. A discrete random variable `x` can assume five possible values, `22`, `23`, `24`, `25`, and `26`. The histogram shows the likelihood of each value.

**Question Type:** Discrete probability from histogram

**Probabilities from the Histogram**

- `p(22) = 0.10`
- `p(23) = 0.15`
- `p(24) = 0.25`
- `p(25) = 0.25`
- `p(26) = 0.25`

**Part a:** What is `p(25)`?

**Correct Answer:** `0.25`

**Part b:** What is the probability that `x` equals `22` or `26`?

**Correct Answer:** `0.35`

**Explanation:** `P(22 or 26) = p(22) + p(26) = 0.10 + 0.25 = 0.35`.

**Part c:** What is `P(x ≤ 23)`?

**Correct Answer:** `0.25`

**Explanation:** `P(x ≤ 23) = p(22) + p(23) = 0.10 + 0.15 = 0.25`.

## 28. One airline averages about `2.3` fatalities per month. Assume that the probability distribution for `x`, the number of fatalities per month, can be approximated by a Poisson probability distribution. Complete parts (a) through (c).

**Question Type:** Poisson distribution

Let `lambda = 2.3`.

**Part a:** What is the probability that no fatalities will occur during any given month?

**Correct Answer:** `0.1003`

**Explanation:** `P(X = 0) = e^(-2.3) * 2.3^0 / 0! = e^(-2.3) ≈ 0.1002588`, which rounds to `0.1003`.

**Part b:** What is the probability that one fatality will occur during any given month?

**Correct Answer:** `0.2306`

**Explanation:** `P(X = 1) = e^(-2.3) * 2.3^1 / 1! ≈ 0.2305953`, which rounds to `0.2306`.

**Part c:** Find `E(x)` and the standard deviation of `x`.

**Correct Answers**

- `E(x) = 2.3`
- Standard deviation `= sqrt(2.3) ≈ 1.5166`

## 29. The university police department must write, on average, five tickets per day to keep department revenues at budgeted levels. Suppose the number of tickets written per day follows a Poisson distribution with a mean of `7.5`. Interpret the value of the mean.

**Question Type:** Interpretation of mean

**Choices**

- A. On half of the days less than 7.5 tickets are written and on half of the days more than 7.5 tickets are written.
- B. If we sampled all days, the arithmetic average number of tickets written would be 7.5 tickets per day.
- C. The number of tickets that is written most often is 7.5 tickets per day.
- D. The mean has no interpretation since 0.5 ticket can never be written.

**Correct Answer:** B

**Explanation:** The mean of `7.5` represents the long-run arithmetic average number of tickets written per day.

## 30. A journal published a study of the lifestyles of visually impaired students. Using diaries, the students kept track of several variables, including number of hours of sleep obtained in a typical day. These visually impaired students had a mean of `8.38` hours and a standard deviation of `2.05` hours. Assume that the distribution of the number of hours of sleep for this group of students is approximately normal. Complete parts a through c.

**Question Type:** Normal distribution

Let `X ~ N(8.38, 2.05)`.

**Part a:** Find `P(x > 12)`.

**Correct Answer:** `0.0387`

**Explanation:** Using `z = (12 - 8.38) / 2.05 ≈ 1.7659`,  
`P(X > 12) = P(Z > 1.7659) ≈ 0.0387`.

**Part b:** Find `P(8 < x < 10)`.

**Correct Answer:** `0.3588`

**Explanation:**  
`P(8 < X < 10) = P(X < 10) - P(X < 8) ≈ 0.3588`.

**Part c:** Find the value `a` for which `P(x < a) = 0.3`.

**Correct Answer:** `7.30`

**Explanation:** The 30th percentile of the standard normal is `z ≈ -0.5244`, so  
`a = 8.38 + (-0.5244)(2.05) ≈ 7.3050`, which rounds to `7.30`.

## 31. Which one of the following suggests that the data set is not approximately normal?

**Question Type:** Normality assessment

**Choices**

- A. A data set with `IQR = 752` and `s = 574`.
- B. A data set with `68%` of the measurements within `x̄ ± 2s`.
- C. A stem-and-leaf display that is roughly symmetric and mound-shaped.
- D. A normal probability plot with points that are approximately linear.

**Correct Answer:** B

**Explanation:** For an approximately normal data set, about `68%` of observations should lie within `x̄ ± 1s`, while about `95%` should lie within `x̄ ± 2s`. So having only `68%` within `x̄ ± 2s` suggests the data are not approximately normal.

## 32. Consider a sample data set with the summary statistics `s = 192`, `Q_L = 77`, and `Q_U = 200`.

**Question Type:** Summary statistics / normality check

**Part a:** Calculate `IQR`.

**Correct Answer:** `123`

**Explanation:** `IQR = Q_U - Q_L = 200 - 77 = 123`.

**Part b:** Calculate `IQR/s`.

**Correct Answer:** `0.641`

**Explanation:** `IQR/s = 123 / 192 = 0.640625`, which rounds to `0.641`.

**Part c:** Is the value of `IQR/s` approximately equal to `1.3`? What does this imply?

**Correct Answers**

- Is it approximately `1.3`? `No`
- Best interpretation: `C`

**Explanation:** For data from an approximately normal distribution, `IQR/s` is often close to `1.3`. Since `0.641` is not close to `1.3`, this suggests the data may not be from an approximately normal distribution.

## 33. Understanding the characteristics of rock masses, especially the nature of the fractures, is essential when building dams and power plants. The shear strength of rock fractures was investigated in an engineering magazine. The Joint Roughness Coefficient (JRC) was used to measure shear strength. Civil engineers collected JRC data for over 700 rock fractures. The results are summarized in an SPSS histogram. Should the engineers use the normal probability distribution to model the behavior of shear strength for rock fractures? Explain.

**Question Type:** Histogram / normal distribution fit

**Correct Answer:** Yes

**Fill-in Conclusion:** It `is` appropriate to use a normal distribution because the histogram is `approximately bell-shaped` and generally `follows` the normal curve.

**Note:** This answer was inferred from a matching published solution to the same textbook problem, since the histogram itself was not expanded in the screenshot you provided.

## 34. Suppose `x` is a binomial random variable with `p = 0.4` and `n = 10`.

**Question Type:** Binomial / normal approximation

**Part a:** Would it be appropriate to approximate the probability distribution of `x` with a normal distribution?

**Correct Answer:** B

**Explanation:** For a binomial distribution, `mu = np = 4` and `sigma = sqrt(npq) = sqrt(2.4) ≈ 1.5492`. Then  
`mu ± 3sigma = 4 ± 3(1.5492) = 4 ± 4.6476`, which gives approximately `[-0.6476, 8.6476]`.  
Since this interval extends below `0`, `mu ± 3sigma` lies outside the boundaries of `0` and `10`.

**Part b:** Assuming that a normal distribution provides an adequate approximation to the distribution of `x`, what are the mean and variance of the approximating normal distribution?

**Correct Answers**

- Mean: `4`
- Variance: `2.4`

**Explanation:** For a binomial distribution, the approximating normal distribution uses  
`mu = np = 10(0.4) = 4` and `variance = npq = 10(0.4)(0.6) = 2.4`.

**Part c:** Use the normal approximation to find `P(x ≥ 3)`.

**Correct Answer:** `0.8335`

**Explanation:** Using the continuity correction,  
`P(X ≥ 3) ≈ P(Y ≥ 2.5)` where `Y ~ N(4, 2.4)`.  
So,
`P(Y ≥ 2.5) ≈ 0.833539...`, which rounds to `0.8335`.

## 35. Will the sampling distribution of `x̄` always be approximately normally distributed? Explain.

**Question Type:** Central Limit Theorem

**Choices**

- A. No, because the Central Limit Theorem only states that the sampling distribution of `x̄` is approximately normally distributed if the sample size is large enough.
- B. Yes, because the Central Limit Theorem states that the sampling distribution of `x̄` is always approximately normally distributed.
- C. No, because the Central Limit Theorem only states that the sampling distribution of `x̄` is approximately normally distributed if the sample size is more than 5% of the population.
- D. No, because the Central Limit Theorem states that the sampling distribution of `x̄` is approximately normally distributed only if the population being sampled is normally distributed.

**Correct Answer:** A

**Explanation:** The sampling distribution of `x̄` is not always approximately normal; the Central Limit Theorem says it becomes approximately normal when the sample size is sufficiently large.

## 36. Consider a population that contains values of `x` equal to `0, 1, 2, ..., 97, 98, 99`. Assume that the values of `x` are equally likely. For the sample sizes `n = 2, n = 5, n = 10, n = 30, and n = 50`, a computer was used to generate `500` random samples and calculate `x̄` for each sample. Relative frequency histograms of the `500` values of `x̄` were constructed for each sample size. What changes occur in the histograms as the value of `n` increases? What similarities exist?

**Question Type:** Sampling distributions / Central Limit Theorem

**Part 1:** What changes occur in the histograms as the value of `n` increases?

**Correct Answer:** C

**Explanation:** As `n` increases, the sampling distribution of `x̄` has smaller variability, so the histograms become less spread out.

**Part 2:** What similarities exist?

**Correct Answer:** B

**Explanation:** All of the histograms are centered at about the same mean and have an approximately normal shape, with the normal shape becoming more pronounced as `n` increases.

## 38. The average salary for a certain profession is `$79,000`. Assume that the standard deviation of such salaries is `$29,500`. Consider a random sample of `80` people in this profession and let `x̄` represent the mean salary for the sample.

**Question Type:** Sampling distribution of the mean

**Part a:** What is `mu_x̄`?

**Correct Answer:** `79000`

**Explanation:** The mean of the sampling distribution of `x̄` equals the population mean.

**Part b:** What is `sigma_x̄`?

**Correct Answer:** `3298.20`

**Explanation:**  
`sigma_x̄ = sigma / sqrt(n) = 29500 / sqrt(80) ≈ 3298.2003`, which rounds to `3298.20`.

**Part c:** Describe the shape of the sampling distribution of `x̄`.

**Correct Answer:** C

**Explanation:** Because the sample size is large (`n = 80`), the sampling distribution of `x̄` is approximately normal by the Central Limit Theorem.

**Part d:** Find the z-score for the value `x̄ = 70,000`.

**Correct Answer:** `-2.73`

**Explanation:**  
`z = (70000 - 79000) / 3298.20 ≈ -2.7288`, which rounds to `-2.73`.

**Part e:** Find `P(x̄ > 70,000)`.

**Correct Answer:** `0.997`

**Explanation:** Since `z ≈ -2.73`,  
`P(x̄ > 70000) = P(Z > -2.73) ≈ 0.9968`, which rounds to `0.997`.

## 39. A random sample of `n = 87` measurements is drawn from a binomial population with probability of success `0.4`. Complete parts a through d below.

**Question Type:** Sampling distribution of the sample proportion

**Part a:** Give the mean and standard deviation of the sampling distribution of the sample proportion, `p̂`.

**Correct Answers**

- Mean: `0.4`
- Standard deviation: `0.0525`

**Explanation:**  
`mu_p̂ = p = 0.4`  
`sigma_p̂ = sqrt(p(1-p)/n) = sqrt(0.4(0.6)/87) ≈ 0.0525226`, which rounds to `0.0525`.

**Part b:** Describe the shape of the sampling distribution of `p̂`.

**Correct Answer:** C

**Explanation:** Since the sample size is large enough, the sampling distribution of `p̂` is approximately normal.

**Part c:** Calculate the standard normal z-score corresponding to a value of `p̂ = 0.41`.

**Correct Answer:** `0.19`

**Explanation:**  
`z = (0.41 - 0.4) / 0.0525 ≈ 0.1904`, which rounds to `0.19`.

**Part d:** Find `P(p̂ > 0.41)`.

**Correct Answer:** `0.4245`

**Explanation:**  
`P(p̂ > 0.41) = P(Z > 0.19) ≈ 0.4245`.

## 40. Explain the difference between an interval estimator and a point estimator for `mu`.

**Question Type:** Conceptual definition

**Choices**

- A. A single number calculated from the sample that estimates a target population parameter is called an interval estimator. A point estimator is a range of numbers that attempts to enclose the target parameter with a high degree of confidence.
- B. A single number calculated from the population that estimates a data value of the sample is called a point estimator. An interval estimator is a set of numbers estimating the range of a data set with a high degree of confidence.
- C. A single number calculated from a population that estimates a target sample statistic is called a point estimator. An interval estimator is a range of numbers that attempts to enclose the target statistic with a high degree of confidence.
- D. A single number calculated from the sample that estimates a target population parameter is called a point estimator. An interval estimator is a range of numbers that attempts to enclose the target parameter with a high degree of confidence.

**Correct Answer:** D

**Explanation:** A point estimator is a single sample-based value used to estimate a population parameter, while an interval estimator gives a range of likely values for that parameter with a specified confidence level.

## 41. Will a large-sample confidence interval be valid if the population from which the sample is taken is not normally distributed? Explain.

**Question Type:** Confidence intervals / Central Limit Theorem

**Choices**

- A. Yes. As long as a sample is sufficiently large that the Central Limit Theorem applies, the confidence interval will be valid regardless of the shape of the population distribution.
- B. No. A small-sample confidence interval is more likely to be valid, but as the sample size increases, the confidence interval will be affected more and more by the shape of the population distribution.
- C. Yes. Confidence intervals are always valid regardless of the shape of the population distribution.
- D. No. Confidence intervals require at least an approximately normal population distribution to be valid.

**Correct Answer:** A

**Explanation:** For large samples, the Central Limit Theorem implies that the sampling distribution of the estimator is approximately normal, so the large-sample confidence interval can still be valid even if the population itself is not normally distributed.

## 42. The heart rate variability (HRV) of police officers was the subject of research published in a biology journal. HRV is defined as the variation in the time intervals between heartbeats. For the 74 officers diagnosed with hypertension, a `90%` confidence interval for the mean HRV was `(9.2, 125.4)`. For the 307 officers that are not hypertensive, a `90%` confidence interval for the mean HRV was `(149.5, 198.8)`.

**Question Type:** Confidence intervals

**Part a:** What confidence coefficient was used to generate the confidence intervals?

**Correct Answer:** `0.90`

**Part b:** Give a practical interpretation of both 90% confidence intervals.

**Correct Fill-ins**

- `true`
- `city`
- `9.2`
- `125.4`

**Interpretation:** The researchers can be `90%` confident that the **true** mean HRV for all hypertensive police officers in the **city** is between `9.2` and `125.4`. A similar statement applies to the non-hypertensive officers, with interval `(149.5, 198.8)`.

**Part c:** When you say you are "90% confident," what do you mean?

**Correct Answer:** B

**Explanation:** About `90%` of confidence intervals constructed from similarly collected samples will contain the true population mean.

**Part d:** If you want to reduce the width of each confidence interval, should you use a smaller or larger confidence coefficient? Explain.

**Correct Fill-ins**

- `smaller`
- `smaller`
- `critical value`

**Explanation:** A smaller confidence coefficient gives a smaller critical value, which produces a narrower confidence interval.

## 43. A random sample of `100` observations from a normally distributed population possesses a mean equal to `75.3` and a standard deviation equal to `5.3`. Use this information to complete parts a through e below.

**Question Type:** Confidence intervals for `mu`

**Given**

- `x̄ = 75.3`
- `s = 5.3`
- `n = 100`
- `SE = s / sqrt(n) = 5.3 / 10 = 0.53`

**Part a:** Find a `95%` confidence interval for `mu`.

**Correct Answer:** `(74.26, 76.34)`

**Explanation:** Using `z = 1.96`,  
`75.3 ± 1.96(0.53) = 75.3 ± 1.0388`,  
so the interval is `(74.2612, 76.3388)`, which rounds to `(74.26, 76.34)`.

**Part b:** What do you mean when you say that a confidence coefficient is `0.95`?

**Correct Answer:** C

**Explanation:** A confidence coefficient of `0.95` means that the interval procedure captures the population parameter with probability `0.95` in repeated sampling.

**Part c:** Find a `99%` confidence interval for `mu`.

**Correct Answer:** `(73.93, 76.67)`

**Explanation:** Using `z = 2.5758`,  
`75.3 ± 2.5758(0.53) = 75.3 ± 1.365174`,  
so the interval is `(73.934826, 76.665174)`, which rounds to `(73.93, 76.67)`.

**Part d:** What happens to the width of a confidence interval as the value of the confidence coefficient is increased while the sample size is held fixed?

**Correct Fill-ins**

- `an increase`
- `critical value`
- `increase`

**Explanation:** Increasing the confidence coefficient increases the critical value, which increases the margin of error and therefore makes the interval wider.

**Part e:** Would your confidence intervals of parts a and c be valid if the distribution of the original population were not normal? Explain.

**Correct Answer:** D

**Explanation:** Because the sample size is large (`n = 100`) and the sample is randomly selected, the sampling distribution of `x̄` is approximately normal by the Central Limit Theorem.

## 44. The mean and standard deviation of a random sample of `n` measurements are equal to `33.5` and `3.1`, respectively. What is the effect on the width of a confidence interval of quadrupling the sample size while holding the confidence coefficient fixed?

**Question Type:** Confidence interval width

**Choices**

- A. Quadrupling the sample size while holding the confidence coefficient fixed decreases the width of the confidence interval by a factor of 4.
- B. Quadrupling the sample size while holding the confidence coefficient fixed increases the width of the confidence interval by a factor of 4.
- C. Quadrupling the sample size while holding the confidence coefficient fixed decreases the width of the confidence interval by a factor of 2.
- D. Quadrupling the sample size while holding the confidence coefficient fixed increases the width of the confidence interval by a factor of 2.
- E. Quadrupling the sample size while holding the confidence coefficient fixed does not affect the width of the confidence interval.

**Correct Answer:** C

**Explanation:** The width of a confidence interval is proportional to `1 / sqrt(n)`. If `n` is multiplied by `4`, the width is divided by `sqrt(4) = 2`.

## 45. Suppose data collected by observers at randomly selected intersections across the country revealed that in a sample of `40` drivers, `20` were using their cell phone.

**Question Type:** Confidence interval for a population proportion

**Part a:** Give a point estimate of `p`, the true driver cell phone use rate.

**Correct Answer:** `0.50`

**Explanation:** The point estimate is the sample proportion: `p̂ = 20 / 40 = 0.50`.

**Part b:** Compute a `95%` confidence interval for `p`.

**Correct Answer:** `(0.35, 0.65)`

**Explanation:**  
`p̂ = 0.50`  
`SE = sqrt(p̂(1-p̂)/n) = sqrt(0.5(0.5)/40) ≈ 0.0791`  
Margin of error `= 1.96(0.0791) ≈ 0.1550`  
So the interval is `0.50 ± 0.1550 = (0.3450, 0.6550)`, which rounds to `(0.35, 0.65)`.

**Part c:** Give a practical interpretation of the interval from part b.

**Correct Answer:** C

**Explanation:** We are `95%` confident that the true proportion of drivers using cell phones while driving lies within this interval.

## 46. A `90%` confidence interval for `p` is given as `(0.37, 0.63)`. How large was the sample used to construct this interval?

**Question Type:** Confidence interval for a proportion

**Correct Answer:** `41`

**Explanation:**  
The center of the interval is `p̂ = (0.37 + 0.63) / 2 = 0.50`.  
The margin of error is `E = (0.63 - 0.37) / 2 = 0.13`.  
For a `90%` confidence interval, `z = 1.645`.  
So,
`n = z^2 p̂(1-p̂) / E^2 = (1.645^2)(0.5)(0.5) / 0.13^2 ≈ 40.03`.  
Rounding **up** to the nearest observation gives `n = 41`.

## 47. In a test of the hypothesis `H0: mu = 10` versus `Ha: mu ≠ 10`, a sample of `n = 50` observations possessed mean `x̄ = 10.6` and standard deviation `s = 2.8`. Find and interpret the p-value for this test.

**Question Type:** Hypothesis test for a mean

**Test Statistic**

- `t = (10.6 - 10) / (2.8 / sqrt(50)) ≈ 1.5152`

**p-value**

- Two-tailed `p ≈ 0.1361`
- Rounded to three decimals: `0.136`

**Correct Interpretation:** D

**Explanation:** Since the p-value is about `0.136`, there is sufficient evidence to reject `H0` when `alpha > 0.136`. In particular, for `alpha = 0.15`, we would reject `H0`. This matches option `D` as stated in the choices.

## 50. A study was conducted to see if people who use the Internet have also paid to download music. In a representative sample of `658` adults who use the Internet, `433` admitted that they have paid to download music. Let `p` represent the true proportion of all Internet-using adults who have paid to download music. Complete parts a through g below.

**Question Type:** One-proportion z-test

**Part a:** Compute a point estimate of `p`.

**Correct Answer:** `0.66`

**Explanation:** `p̂ = 433 / 658 ≈ 0.6581`, which rounds to `0.66`.

**Part b:** Set up the null and alternative hypotheses for testing whether the true proportion exceeds `0.7`.

**Correct Answer:** F

**Hypotheses**

- `H0: p = 0.7`
- `Ha: p > 0.7`

**Part c:** Compute the test statistic for part b.

**Correct Answer:** `-2.35`

**Explanation:**  
`z = (p̂ - p0) / sqrt(p0(1-p0)/n)`  
`= (0.6581 - 0.7) / sqrt(0.7(0.3)/658) ≈ -2.3479`, which rounds to `-2.35`.

**Part d:** Find the rejection region for the test if `alpha = 0.01`.

**Correct Answer:** D

**Fill-in:** `z > 2.326`

**Part e:** Find the p-value for the test.

**Correct Answer:** `0.991`

**Explanation:** For an upper-tailed test with `z = -2.35`,  
`p-value = P(Z > -2.35) ≈ 0.9906`, which rounds to `0.991`.

**Part f:** Make the appropriate conclusion using the rejection region.

**Correct Fill-ins**

- `Do not reject`
- `is not`
- `insufficient`

**Conclusion:** Do not reject the null hypothesis because the test statistic is not in the rejection region. Therefore, there is insufficient evidence at the `0.01` level of significance to indicate that the true proportion exceeds `0.7`.

**Part g:** Make the appropriate conclusion using the p-value.

**Correct Fill-ins**

- `Do not reject`
- `greater than`
- `insufficient`

**Conclusion:** Do not reject the null hypothesis because the p-value is greater than `alpha = 0.01`. Therefore, there is insufficient evidence at the `0.01` level of significance to indicate that the true proportion exceeds `0.7`.

## 54. Researchers compared the redemption rates of m-coupons for products sold at a milkshake store and a donut store. In a sample of `2445` milkshake-store m-coupons, `81` were redeemed; in a sample of `6604` donut-store m-coupons, `71` were redeemed. Let `p1` be the redemption rate for milkshake-store coupons and `p2` the redemption rate for donut-store coupons.

**Question Type:** Inference for the difference of two proportions

**Part a:** Compute the redemption rate for the sample of milkshake m-coupons.

**Correct Answer:** `0.033`

**Explanation:** `p̂1 = 81 / 2445 ≈ 0.0331288`, which rounds to `0.033`.

**Part b:** Compute the redemption rate for the sample of donut m-coupons.

**Correct Answer:** `0.011`

**Explanation:** `p̂2 = 71 / 6604 ≈ 0.0107511`, which rounds to `0.011`.

**Part c:** Give a point estimate, `p̂1 - p̂2`, for the difference between the true redemption rates.

**Correct Answer:** `0.022`

**Explanation:** `p̂1 - p̂2 ≈ 0.0331288 - 0.0107511 = 0.0223778`, which rounds to `0.022`.

**Part d:** Form a `90%` confidence interval for the difference between the true redemption rates.

**Correct Answer:** `(0.016, 0.029)`

**Interpretation Choice:** C

**Explanation:** The `90%` confidence interval for `p1 - p2` is approximately `(0.0161, 0.0287)`, which rounds to `(0.016, 0.029)`. We are 90% confident this interval contains the true difference between the population redemption rates.

**Part e:** Explain the meaning of the phrase "90% confident."

**Correct Answer:** D

**Explanation:** The confidence level refers to the long-run success rate of the interval procedure in capturing the population parameter.

**Part f:** Based on the interval from part d, is there a statistically significant difference between the redemption rates?

**Correct Answer:** D

**Explanation:** Yes. Because the confidence interval does not contain `0`, there is evidence that the true difference in redemption rates is not `0`.

**Part g:** Assume the true difference between redemption rates must exceed `0.01` for the researchers to consider the difference to be practically significant. Based on the interval from part d, is there a practically significant difference?

**Correct Answer:** D

**Explanation:** Yes. Because the lower limit of the confidence interval is greater than `0.01`, the entire interval exceeds the threshold for practical significance.

## 55. Are MBA students from Group A more likely to begin their careers as entrepreneurs than MBA students from Group B? Of the `1312` students from Group A who responded to the survey, `210` reported their employment status after graduation as self-employed or a small business owner. Of the `7107` students from Group B who responded to the survey, `363` reported their employment status after graduation as self-employed or a small business owner. Use `alpha = 0.10`.

**Question Type:** Two-proportion z-test

Let `p1` be the proportion for Group A and `p2` the proportion for Group B.

**Part a:** Identify the null and alternative hypotheses.

**Correct Answer:** F

**Hypotheses**

- `H0: (p1 - p2) = 0`
- `Ha: (p1 - p2) > 0`

**Part b:** Find the test statistic.

**Correct Answer:** `14.40`

**Explanation:** Using the pooled-proportion z-test,
`p̂1 = 210/1312 ≈ 0.1601`, `p̂2 = 363/7107 ≈ 0.0511`, and the pooled estimate is  
`p̂ = (210 + 363)/(1312 + 7107) ≈ 0.0681`.  
This gives `z ≈ 14.4014`, which rounds to `14.40`.

**Part c:** Find the p-value.

**Correct Answer:** `0.000`

**Explanation:** For an upper-tailed test with `z = 14.40`, the p-value is essentially `0`.

**Part d:** State an appropriate conclusion.

**Correct Fill-ins**

- `Reject`
- `sufficient`
- `greater than`

**Conclusion:** Reject `H0`. There is sufficient evidence to conclude that the proportion of MBA students from Group A who reported being self-employed is greater than the proportion from Group B.

## 51. To use the small-sample t-statistic to test for a difference between the means of two populations (`sigma_1 = sigma_2`), what assumptions must be made about the two populations? About the two samples?

**Question Type:** Assumptions for a two-sample pooled t-test

**About the two populations:** Select all that apply.

**Correct Answers:** A, B

**Explanation:** For the pooled two-sample t-test with small samples, we assume the two populations are approximately normally distributed and have approximately equal variances.

**About the two samples:** Select all that apply.

**Correct Answer:** A

**Explanation:** The two samples must be independent of each other. There is no requirement here that each sample size exceed `30`, and normality is assumed for the populations rather than the samples themselves.

## 52. Independent random samples selected from two normal populations produced the sample means and standard deviations shown below.

**Data**

- Sample 1: `n1 = 18`, `x̄1 = 5.5`, `s1 = 3.6`
- Sample 2: `n2 = 12`, `x̄2 = 7.1`, `s2 = 4.6`

Assume equal variances.

**Question Type:** Two-sample pooled t-test and confidence interval

**Part a:** Conduct the test `H0: (mu1 - mu2) = 0` against `Ha: (mu1 - mu2) ≠ 0` using `alpha = 0.10`.

**Test Statistic**

- `t = -1.07`

**p-value**

- `0.295`

**Conclusion Choice:** A

**Explanation:** Since the p-value `0.295` is greater than `0.10`, we do not reject `H0`. There is insufficient evidence that the means differ.

**Part b:** Find and interpret the `90%` confidence interval for `(mu1 - mu2)`.

**Correct Answer:** `(-4.15, 0.95)`

**Interpretation Fill-ins**

- `within`
- `insufficient`
- `contains`

**Explanation:** With `90%` confidence, the true difference `(mu1 - mu2)` lies within `(-4.15, 0.95)`. Because this interval contains `0`, there is insufficient evidence to conclude that `(mu1 - mu2)` differs from `0`.

## 53. Independent random samples are selected from two populations and are used to test the hypothesis `H0: (mu1 - mu2) = 0` against the alternative `Ha: (mu1 - mu2) ≠ 0`. An analysis of `234` observations from population 1 and `313` from population 2 yielded a p-value of `0.116`. Complete parts a and b below.

**Question Type:** Hypothesis test interpretation

**Part a:** Interpret the results of the computer analysis. Use `alpha ≤ 0.10`.

**Correct Answer:** C

**Explanation:** Since the p-value `0.116` exceeds `alpha = 0.10`, we do not reject `H0`. There is insufficient evidence to indicate that the population means are different.

**Part b:** If the alternative hypothesis had been `Ha: (mu1 - mu2) < 0`, how would the p-value change? Interpret the p-value for this one-tailed test.

**Correct Answer:** A

**New p-value:** Cannot be determined from the information given alone.

**Explanation:** A two-tailed p-value of `0.116` implies a one-tailed tail area of `0.0580` only if the observed test statistic is in the direction of the alternative hypothesis. If the test statistic points in the opposite direction, the one-tailed p-value would instead be `0.9420`. Since the sign of the test statistic is not provided, there is not enough information to determine the new p-value or choose between the two directional conclusions.

## 37. A medical journal published the results of a study to compare the effectiveness of handwashing with soap and handrubbing with alcohol. Health care workers who used handrubbing had a mean bacterial count of `30` per hand with a standard deviation of `56`. Health care workers who used handwashing had a mean bacterial count of `61` per hand with a standard deviation of `105`. In a random sample of `50` health care workers, all using the same method of cleaning their hands, the mean bacterial count per hand, `x̄`, is greater than `64`. Give your opinion on whether this sample of workers used handrubbing with alcohol or handwashing with soap.

**Question Type:** Sampling distribution / normal approximation

**Alcohol Handrubbing**

- `mu_x̄ = 30`
- `sigma_x̄ = 56 / sqrt(50) ≈ 7.9196`
- `z = (64 - 30) / 7.9196 ≈ 4.2931`
- `P(x̄ > 64) ≈ 0.0000`  
  More precisely: `0.0000088`

**Soap Handwashing**

- `mu_x̄ = 61`
- `sigma_x̄ = 105 / sqrt(50) ≈ 14.8492`
- `z = (64 - 61) / 14.8492 ≈ 0.2020`
- `P(x̄ > 64) ≈ 0.4199`

**Conclusion**

Since the probability of `x̄` being greater than `64` is **very small** if the workers used handrubbing with alcohol, and **much larger** if they used handwashing with soap, it is more likely that this sample of workers used **handwashing with soap**.

## 48. A study analyzed the sustainability behaviors of CPA corporations. The level of support for corporate sustainability was obtained for each in a sample of `971` senior managers at CPA firms. The CEO of a CPA firm claims that the true mean level of support for sustainability is `74`. The provided printout reports a one-sample two-tailed z-test.

**Question Type:** Hypothesis test for a mean

**From the Printout**

- Hypothesized mean: `74`
- Sample size: `971`
- Sample mean: `67.834`
- Sample standard deviation: `26.752`
- Test statistic: `z = -7.1822`
- Two-tailed p-value: `0.0000`
- `alpha = 0.05`

**Part a:** Specify the null and alternative hypotheses for testing this claim.

**Correct Answer:** D

**Hypotheses**

- `H0: mu = 74`
- `Ha: mu ≠ 74`

**Part b(1):** What is a Type I error in this problem?

**Correct Answer:** B

**Explanation:** A Type I error is rejecting `H0` when it is actually true, so here it means concluding the true mean support level is not `74` when it really is `74`.

**Part b(2):** What is a Type II error in this problem?

**Correct Answer:** C

**Explanation:** A Type II error is failing to reject `H0` when it is false, so here it means concluding the true mean support level is `74` when it is actually not `74`.

**Part c:** Locate the test statistic and the p-value on the printout.

**Correct Answers**

- Test statistic: `-7.1822`
- p-value: `0.0000`

**Part d:** At `alpha = 0.05`, give the appropriate conclusion.

**Correct Answer:** C

**Explanation:** Since the p-value is essentially `0`, it is less than `0.05`, so we reject `H0` and conclude there is sufficient evidence that the true mean level of support for sustainability is not equal to `74`.

**Part e:** What assumptions, if any, about the distribution of support levels must hold true in order for the inference derived from the test to be valid? Select all that apply.

**Correct Answer:** D

**Explanation:** With a very large sample size (`n = 971`), the sampling distribution of the sample mean is approximately normal by the Central Limit Theorem, so no normality assumption about the original distribution is needed here.

## 49. Suppose you conduct a t-test for the null hypothesis `H0: mu = 2000` versus the alternative hypothesis `Ha: mu > 2000` based on a sample of `19` observations. The test results are `t = 1.91` and `p-value = 0.036`.

**Question Type:** One-sample t-test

**Part a:** What assumptions are necessary for the validity of this procedure? Select all that apply.

**Correct Answers:** A, B

**Explanation:** For a one-sample t-test with a small sample size, we assume the sample is random and the population distribution is approximately normal.

**Part b:** Interpret the results of the test using `alpha = 0.05`.

**Correct Fill-ins**

- `less than`
- `is`
- `sufficient`

**Interpretation:** Since the p-value is less than `alpha = 0.05`, the null hypothesis is rejected. There is sufficient evidence to support the alternative hypothesis that `mu > 2000`.

**Part c:** Suppose the alternative hypothesis had been the two-tailed `Ha: mu ≠ 2000`. If the t-statistic were unchanged, what would the p-value be for this test? Interpret the p-value for the two-tailed test.

**Correct Fill-ins**

- Two-tailed p-value: `0.072`
- `greater than`
- `is not`
- `insufficient`

**Explanation:** For the same test statistic, the two-tailed p-value is double the one-tailed p-value: `2(0.036) = 0.072`. Since `0.072 > 0.05`, the null hypothesis is not rejected, and there is insufficient evidence to support `Ha: mu ≠ 2000`.
