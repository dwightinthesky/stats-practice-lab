from __future__ import annotations


def choice(key: str, text: str) -> dict[str, str]:
    return {"key": key, "text": text}


PART_OVERRIDES: dict[int, dict[str, dict[str, object]]] = {
    5: {
        "Part 1": {
            "choices": [
                choice("A", "A Pareto diagram with categories ordered S, MS, LS, A, SS from left to right."),
                choice("B", "A Pareto diagram with categories ordered A, SS, S, MS, LS from left to right."),
                choice("C", "A Pareto diagram with categories ordered LS, S, MS, SS, A from left to right."),
                choice("D", "A Pareto diagram with categories ordered SS, A, LS, MS, S from left to right."),
            ]
        }
    },
    6: {
        "Part c": {
            "choices": [
                choice("A", "A dot plot with one dot at 0, 5, 6, 10, 14, 18, 24; two dots at 28 and 37; and three dots at 38."),
                choice("B", "A dot plot with one dot at 0, 5, 6, 10, 18, 24, 37; two dots at 14 and 38; and three dots at 28."),
                choice("C", "A dot plot with one dot at 0 and 5, two dots at 6 and 14, one dot at 18, two dots at 24, three dots at 28, and one dot at 37 and 38."),
                choice("D", "A symmetric dot plot centered near 20 with no repeated values."),
            ]
        }
    },
    7: {
        "Part c": {
            "choices": [
                choice("A", "The distribution is skewed to the right."),
                choice("B", "The distribution is skewed to the left."),
                choice("C", "The distribution is approximately symmetric."),
                choice("D", "The distribution is approximately uniform."),
            ]
        }
    },
    10: {
        "Part a": {
            "choices": [
                choice("A", "No. The z-score is -3.32, meaning that less than approximately 68% of transformers have a number of sags closer to the mean."),
                choice("B", "Yes. The z-score is -3.32, meaning that this is an outlier and almost every other transformer has fewer sags."),
                choice("C", "Yes. The z-score is -3.32, meaning that this is an outlier and almost every other transformer has more sags."),
                choice("D", "No. The z-score is -3.32, meaning that the number of sags is not unusual and is not an outlier."),
                choice("E", "This cannot be determined, since the IQR is not provided and cannot be found from the given information."),
            ]
        },
        "Part b": {
            "choices": [
                choice("A", "No. The z-score is 1.63, meaning that less than approximately 68% of transformers have a number of swells closer to the mean."),
                choice("B", "Yes. The z-score is 1.63, meaning that this is an outlier and almost every other transformer has fewer swells."),
                choice("C", "Yes. The z-score is 1.63, meaning that this is an outlier and almost every other transformer has more swells."),
                choice("D", "No. The z-score is 1.63, meaning that the number of swells is not unusual and is not an outlier."),
                choice("E", "This cannot be determined, since the IQR is not provided and cannot be found from the given information."),
            ]
        },
    },
    12: {
        "Part d": {
            "choices": [
                choice("A", "Yes, since there appeared to be differences between the proportions of males and females on all 3 levels."),
                choice("B", "No, since there appeared to be differences between the proportions of males and females on 2 of the 3 levels."),
                choice("C", "No, since there appeared to be no differences between the proportions of males and females on any of the levels."),
                choice("D", "Yes, since there appeared to be differences between the proportions of males and females on 2 of the 3 levels."),
            ]
        }
    },
    13: {
        "Part a": {
            "choices": [
                choice("A", "A line with slope +1 and y-intercept 6."),
                choice("B", "A line with slope +1 and y-intercept -6."),
                choice("C", "A line with slope -3 and y-intercept 6."),
                choice("D", "A line with slope +3 and y-intercept -6."),
            ]
        },
        "Part b": {
            "choices": [
                choice("A", "A line with positive slope passing through y = -6."),
                choice("B", "A line with slope -3 crossing the y-axis at 6."),
                choice("C", "A line with slope -1 passing through the origin."),
                choice("D", "A line with slope +3 crossing the y-axis at 6."),
            ]
        },
        "Part c": {
            "choices": [
                choice("A", "A line with positive slope and y-intercept -5."),
                choice("B", "A steep negative line passing through the origin."),
                choice("C", "A moderate negative line crossing the y-axis above the origin."),
                choice("D", "A steep positive line passing through the origin."),
            ]
        },
    },
    15: {
        "Part a": {
            "choices": [
                choice("A", "A scatterplot with only positive x-values and no high point near (8, 9)."),
                choice("B", "A scatterplot that places the only y = 0 point near x = 8."),
                choice("C", "A scatterplot with a negative trend and no repeated x-values."),
                choice("D", "A scatterplot that includes (-2, 0), (2, 1), two points at x = 4, two points at x = 5, and a high point at (8, 9)."),
            ]
        },
        "Part b": {
            "choices": [
                choice("A", "As x increases, y tends to increase. Thus, there appears to be a positive, linear relationship between x and y."),
                choice("B", "As x increases, y tends to increase. Thus, there appears to be a negative, linear relationship between x and y."),
                choice("C", "As x increases, y tends to decrease. Thus, there appears to be a negative, linear relationship between x and y."),
                choice("D", "As x increases, y tends to decrease. Thus, there appears to be a positive, linear relationship between x and y."),
            ]
        },
        "Part c": {
            "choices": [
                choice("A", "An upward-sloping least squares line, but the points vary widely around it, so the fit is poor."),
                choice("B", "A downward-sloping least squares line that fits the data quite well."),
                choice("C", "An upward-sloping least squares line, and the variation of the data points around the line is not very large."),
                choice("D", "A horizontal least squares line because the data show no linear pattern."),
            ],
            "answerDetails": ["Correct answer: C"],
        },
    },
    16: {
        "Part a": {
            "choices": [
                choice("A", "y = β0 + β1x"),
                choice("B", "y = β1x"),
                choice("C", "y = β1x^2 + β0"),
                choice("D", "y = β1 / x"),
            ]
        },
        "Part c(1)": {
            "choices": [
                choice("A", "For each additional one-day duration, the number of arrests is estimated to change by the value of the y-intercept."),
                choice("B", "Since a sit-in with duration 0 is outside the range of the sample data, the y-intercept has no practical interpretation."),
                choice("C", "Since a sit-in with 0 arrests is outside the range of the sample data, the y-intercept has no practical interpretation."),
                choice("D", "For each additional arrest, the duration is estimated to change by the value of the slope."),
            ]
        },
        "Part c(2)": {
            "choices": [
                choice("A", "For each additional arrest, the duration is estimated to change by the value of the slope."),
                choice("B", "Since a sit-in with duration 0 is outside the range of the sample data, the slope has no practical interpretation."),
                choice("C", "For each additional one day of duration, the number of arrests is estimated to increase by the value of the slope."),
                choice("D", "Since a sit-in with 0 arrests is outside the range of the sample data, the slope has no practical interpretation."),
            ]
        },
        "Part c(3)": {
            "choices": [
                choice("A", "The interpretation is valid for all sit-ins with the number of arrests greater than 0."),
                choice("B", "The interpretation is valid only for sit-ins with durations within the range of the sample data."),
                choice("C", "The interpretation is valid only for sit-ins with the number of arrests within the range of the sample data."),
                choice("D", "The interpretation is valid for all sit-ins with durations greater than 0."),
            ]
        },
    },
    17: {
        "Part b(1)": {
            "choices": [
                choice("A", "For a decade with 0 total births in this country, the predicted number of software millionaire birthdays is -19.71."),
                choice("B", "For a decade with 0 software millionaire birthdays, the total number of births is predicted to be 19.71 million."),
                choice("C", "The y-intercept does not have a practical interpretation."),
                choice("D", "The y-intercept means births and software-millionaire birthdays are unrelated."),
            ]
        },
        "Part b(2)": {
            "choices": [
                choice("A", "For each additional 1 million births in the country, the predicted number of software millionaire birthdays decreases by about 0.82."),
                choice("B", "For each additional 1 million births in the country, the predicted number of software millionaire birthdays increases by about 0.82."),
                choice("C", "The slope does not have a practical interpretation."),
                choice("D", "For each additional software-millionaire birthday, the number of births is predicted to increase by 0.82 million."),
            ]
        },
    },
    20: {
        "Part a": {
            "choices": [
                choice("A", "male and glove fits well, male and glove fits poorly, female and glove fits well, female and glove fits poorly, no response"),
                choice("B", "male and glove fits well, female and glove fits well"),
                choice("C", "male and glove fits well, male and glove fits poorly, female and glove fits well, female and glove fits poorly"),
                choice("D", "male, female, glove fits well, glove fits poorly"),
            ]
        },
        "Part b": {
            "choices": [
                choice("A", "0.684, 0.237"),
                choice("B", "0.920, 0.080, 0.721, 0.279"),
                choice("C", "0.316, 0.763, 0.963, 0.958"),
                choice("D", "0.684, 0.237, 0.037, 0.042"),
                choice("E", "0.25, 0.25, 0.25, 0.25"),
            ]
        },
    },
    21: {
        "Part a": {
            "choices": [
                choice("A", "A Venn diagram with two disjoint circles for A and B."),
                choice("B", "A Venn diagram with A completely inside B."),
                choice("C", "A Venn diagram with overlapping circles for A and B."),
                choice("D", "A Venn diagram with B completely inside A."),
            ]
        }
    },
    22: {
        "Part c": {
            "choices": [
                choice("A", "Yes, the events are independent because P(A|B) ≠ P(A)."),
                choice("B", "Yes, the events are independent because P(A|B) = P(A)."),
                choice("C", "No, the events are dependent because P(A|B) ≠ P(A)."),
                choice("D", "Yes, the events are independent because P(B|A) = P(A)."),
                choice("E", "No, the events are dependent because P(B|A) ≠ P(A)."),
                choice("F", "No, the events are dependent because P(A|B) = P(A)."),
            ]
        }
    },
    24: {
        "Part a": {
            "choices": [
                choice("A", "No, because some full-time workers exhibit arrogant behaviors but do not receive a poor performance rating."),
                choice("B", "No, because some full-time workers exhibit arrogant behaviors and receive a poor performance rating."),
                choice("C", "Yes, because some full-time workers exhibit arrogant behaviors and receive a poor performance rating."),
                choice("D", "Yes, because some full-time workers exhibit arrogant behaviors but do not receive a poor performance rating."),
            ]
        },
        "Part c": {
            "choices": [
                choice("A", "No, because if workers exhibit arrogant behaviors, they will receive a poor performance rating."),
                choice("B", "Yes, because if workers exhibit arrogant behaviors, they are more likely to receive a poor performance rating."),
                choice("C", "Yes, because if workers exhibit arrogant behaviors, they are neither more nor less likely to receive a poor performance rating."),
                choice("D", "No, because if workers exhibit arrogant behaviors, they are more likely to receive a poor performance rating."),
            ]
        },
    },
    25: {
        "Question": {
            "choices": [
                choice("A", "Profit distribution: $250 with probability 0.50, $375 with probability 0.25, and $500 with probability 0.25."),
                choice("B", "Profit distribution: $300 with probability 0.50, $550 with probability 0.25, and $800 with probability 0.25."),
                choice("C", "Profit distribution: $500 with probability 0.50, $750 with probability 0.25, and $1,000 with probability 0.25."),
                choice("D", "Profit distribution: $0 with probability 0.50, $250 with probability 0.25, and $500 with probability 0.25."),
            ]
        }
    },
    26: {
        "Question": {
            "choices": [
                choice("A", "$670"),
                choice("B", "$1,288"),
                choice("C", "$13"),
                choice("D", "$3,481,400"),
            ]
        }
    },
    34: {
        "Part a": {
            "choices": [
                choice("A", "No, because μ ± 3σ lies within the boundaries of 0 and 10."),
                choice("B", "No, because μ ± 3σ lies outside the boundaries of 0 and 10."),
                choice("C", "Yes, because μ ± 3σ lies outside the boundaries of 0 and 10."),
                choice("D", "Yes, because μ ± 3σ lies within the boundaries of 0 and 10."),
            ]
        }
    },
    36: {
        "Part 1": {
            "choices": [
                choice("A", "As the value of n increases, the x̄ value of the histograms' central tendencies decrease."),
                choice("B", "As the value of n increases, the histograms become more spread out."),
                choice("C", "As the value of n increases, the histograms become less spread out."),
                choice("D", "As the value of n increases, the x̄ value of the histograms' central tendencies increase."),
            ]
        },
        "Part 2": {
            "choices": [
                choice("A", "All of the histograms are about equally spread out."),
                choice("B", "All of the histograms have an approximately normal distribution shape and similar central tendencies."),
                choice("C", "All of the histograms have an approximately uniform distribution shape and similar central tendencies."),
                choice("D", "All of the histograms have an approximately uniform distribution shape."),
                choice("E", "All of the histograms have an approximately normal distribution shape."),
                choice("F", "There are no similarities between the different histograms."),
            ]
        },
    },
    38: {
        "Part c": {
            "choices": [
                choice("A", "The shape is that of a uniform distribution."),
                choice("B", "The shape is that of a Poisson distribution."),
                choice("C", "The shape is that of a normal distribution."),
                choice("D", "The shape is that of a binomial distribution."),
            ]
        }
    },
    39: {
        "Part b": {
            "choices": [
                choice("A", "The shape of the sampling distribution of p̂ is approximately uniform because the sample size is large."),
                choice("B", "The shape of the sampling distribution of p̂ is approximately uniform because the sample size is small."),
                choice("C", "The shape of the sampling distribution of p̂ is approximately normal because the sample size is large."),
                choice("D", "The shape of the sampling distribution of p̂ is approximately normal because the sample size is small."),
            ]
        }
    },
    42: {
        "Part c": {
            "choices": [
                choice("A", "The phrasing '90% confident' means that there is a 90% chance that the sample data were collected in such a way that the bounds of the confidence interval can be trusted."),
                choice("B", "The phrasing '90% confident' means that 90% of confidence intervals constructed from similarly collected samples will contain the true population mean."),
                choice("C", "The phrasing '90% confident' means that 90% of the sample data will fall between the bounds of the confidence interval."),
                choice("D", "The phrasing '90% confident' means that similarly collected samples will be approximately normal 90% of the time."),
            ]
        }
    },
    43: {
        "Part b": {
            "choices": [
                choice("A", "A confidence coefficient of 0.95 means that 95% of the values in the population will be contained in an interval estimator constructed using this coefficient."),
                choice("B", "A confidence coefficient of 0.95 means that there is a probability of 0.95 that an interval estimator constructed using this coefficient will contain all of the values in the relevant sample."),
                choice("C", "A confidence coefficient of 0.95 means that there is a probability of 0.95 that an interval estimator constructed using this coefficient will enclose the population parameter."),
                choice("D", "A confidence coefficient of 0.95 means that 95% of the values in any sample taken from the population will be contained in an interval estimator constructed using this coefficient."),
            ]
        },
        "Part e": {
            "choices": [
                choice("A", "No, the underlying distribution must be normal for the validity of these confidence intervals."),
                choice("B", "Yes, since the sample sizes are large (n ≥ 30), the condition guarantees that the sampling distribution of x̄ is approximately normal."),
                choice("C", "Yes, since the confidence level is at least 90%, the underlying distribution need not be normal."),
                choice("D", "Yes, since the sample sizes are large (n ≥ 30) and randomly selected from the target population, the condition guarantees that the sampling distribution of x̄ is approximately normal."),
                choice("E", "Yes, since the sample was randomly selected from the target population, the sampling distribution of x̄ is guaranteed to be approximately normal."),
            ]
        },
    },
    45: {
        "Part c": {
            "choices": [
                choice("A", "We are confident that 95% of the population do not use a cell phone while driving."),
                choice("B", "We are confident that 95% of the population use a cell phone while driving."),
                choice("C", "We are 95% confident that the true proportion of drivers using cell phones is inside this interval."),
                choice("D", "There is a 95% chance that the true proportion of drivers who use cell phones is outside this interval."),
            ]
        }
    },
    47: {
        "Question": {
            "choices": [
                choice("A", "There is insufficient evidence to reject H0 for α = 0.15."),
                choice("B", "There is sufficient evidence to reject H0 for α > 0.15."),
                choice("C", "There is insufficient evidence to reject H0 for α > 0.15."),
                choice("D", "There is sufficient evidence to reject H0 for α < 0.15."),
            ]
        }
    },
    48: {
        "Part a": {
            "choices": [
                choice("A", "H0: μ = 74; Ha: μ > 74"),
                choice("B", "H0: μ ≠ 74; Ha: μ = 74"),
                choice("C", "H0: μ = 74; Ha: μ < 74"),
                choice("D", "H0: μ = 74; Ha: μ ≠ 74"),
            ]
        },
        "Part b(1)": {
            "choices": [
                choice("A", "A Type I error would be to conclude that the sample mean level of support for sustainability is greater than 74 when, in fact, the sample mean is less than 74."),
                choice("B", "A Type I error would be to conclude that the true mean level of support for sustainability is not 74 when, in fact, the mean is equal to 74."),
                choice("C", "A Type I error would be to conclude that the sample mean level of support for sustainability is less than 74 when, in fact, the sample mean is greater than 74."),
                choice("D", "A Type I error would be to conclude that the true mean level of support for sustainability is 74 when, in fact, the mean is not equal to 74."),
            ]
        },
        "Part b(2)": {
            "choices": [
                choice("A", "A Type II error would be to conclude that the sample mean level of support for sustainability is less than 74 when, in fact, the sample mean is greater than 74."),
                choice("B", "A Type II error would be to conclude that the true mean level of support for sustainability is not 74 when, in fact, the mean is equal to 74."),
                choice("C", "A Type II error would be to conclude that the true mean level of support for sustainability is 74 when, in fact, the mean is not equal to 74."),
                choice("D", "A Type II error would be to conclude that the sample mean level of support for sustainability is greater than 74 when, in fact, the sample mean is less than 74."),
            ]
        },
        "Part d": {
            "choices": [
                choice("A", "Do not reject the null hypothesis. There is sufficient evidence at the α = 0.05 level of significance to conclude that the true mean level of support for sustainability is not equal to 74."),
                choice("B", "Do not reject the null hypothesis. There is sufficient evidence at the α = 0.05 level of significance to conclude that the true mean level of support for sustainability is greater than 74."),
                choice("C", "Reject the null hypothesis. There is sufficient evidence at the α = 0.05 level of significance to conclude that the true mean level of support for sustainability is not equal to 74."),
                choice("D", "Reject the null hypothesis. There is insufficient evidence at the α = 0.05 level of significance to conclude that the true mean level of support for sustainability is equal to 74."),
            ]
        },
        "Part e": {
            "choices": [
                choice("A", "One must assume that the distribution of support levels is normal because the sample size is very large."),
                choice("B", "One must assume that the distribution of support levels is symmetric because the test is two-tailed."),
                choice("C", "One must assume that the distribution of support levels is normal because the population standard deviation is not given."),
                choice("D", "No assumptions are necessary because the sample size is very large."),
            ]
        },
    },
    49: {
        "Part a": {
            "choices": [
                choice("A", "A random sample is selected from the target population."),
                choice("B", "The population from which the sample is selected has a distribution that is approximately normal."),
                choice("C", "The population standard deviation is approximately equal to the sample standard deviation."),
                choice("D", "No assumptions need to be made to perform the test."),
            ]
        }
    },
    50: {
        "Part b": {
            "choices": [
                choice("A", "H0: p < 0.7; Ha: p = 0.7"),
                choice("B", "H0: p = 0.7; Ha: p < 0.7"),
                choice("C", "H0: p > 0.7; Ha: p ≤ 0.7"),
                choice("D", "H0: p ≠ 0.7; Ha: p = 0.7"),
                choice("E", "H0: p = 0.7; Ha: p ≠ 0.7"),
                choice("F", "H0: p = 0.7; Ha: p > 0.7"),
            ]
        },
        "Part d": {
            "choices": [
                choice("A", "Reject H0 if z < -2.576 or z > 2.576."),
                choice("B", "Reject H0 if z = 2.326."),
                choice("C", "Reject H0 if z < -2.326."),
                choice("D", "Reject H0 if z > 2.326."),
            ]
        },
    },
    52: {
        "Part a": {
            "choices": [
                choice("A", "Do not reject H0. There is insufficient evidence that the means differ."),
                choice("B", "Reject H0. There is sufficient evidence that the means differ."),
                choice("C", "Do not reject H0. There is sufficient evidence that the means differ."),
                choice("D", "Reject H0. There is insufficient evidence that the means differ."),
            ]
        }
    },
    53: {
        "Part a": {
            "choices": [
                choice("A", "Since the given α value exceeds this p-value, there is sufficient evidence to indicate that the population means are different."),
                choice("B", "Since the given α value exceeds this p-value, there is insufficient evidence to indicate that the population means are different."),
                choice("C", "Since this p-value exceeds the given value of α, there is insufficient evidence to indicate that the population means are different."),
                choice("D", "Since this p-value exceeds the given value of α, there is sufficient evidence to indicate that the population means are different."),
            ]
        },
        "Part b": {
            "choices": [
                choice("A", "There is not enough information to determine the one-tailed p-value or its interpretation."),
                choice("B", "Since the given value of α exceeds the p-value for this one-tailed test, there is sufficient evidence to conclude that the mean for population 1 is significantly lower than the mean for population 2."),
                choice("C", "Since the p-value for this one-tailed test exceeds the given value of α, there is insufficient evidence to conclude that the mean for population 1 is significantly lower than the mean for population 2."),
            ]
        },
    },
    54: {
        "Part d": {
            "choices": [
                choice("A", "With 90% confidence, the confidence interval does not contain the true value of the proportion of milkshake-store coupons redeemed and the proportion of donut-store coupons redeemed."),
                choice("B", "With 90% confidence, the confidence interval does not contain the true value of the difference between the population proportions of redeemed milkshake-store coupons and redeemed donut-store coupons."),
                choice("C", "With 90% confidence, the confidence interval contains the true value of the difference between the population proportions of redeemed milkshake-store coupons and redeemed donut-store coupons."),
                choice("D", "With 90% confidence, the confidence interval contains the true value of the proportion of redeemed milkshake-store coupons and the proportion of redeemed donut-store coupons."),
            ]
        },
        "Part e": {
            "choices": [
                choice("A", "The probability that an interval estimator encloses both of the sample proportions is 0.90."),
                choice("B", "The probability that an interval estimator encloses at least one of the sample proportions is 0.90."),
                choice("C", "The probability that an interval estimator excludes the population parameter is 0.90."),
                choice("D", "The probability that an interval estimator encloses the population parameter is 0.90."),
            ]
        },
        "Part f": {
            "choices": [
                choice("A", "No, because the confidence interval does not contain 0."),
                choice("B", "Yes, because the confidence interval contains 0."),
                choice("C", "No, because the confidence interval contains 0."),
                choice("D", "Yes, because the confidence interval does not contain 0."),
            ]
        },
        "Part g": {
            "choices": [
                choice("A", "No, because 0.01 is contained within the confidence interval."),
                choice("B", "Yes, because the upper limit of the confidence interval is less than -0.01."),
                choice("C", "Yes, because 0.01 is contained within the confidence interval."),
                choice("D", "Yes, because the lower limit of the confidence interval is greater than 0.01."),
            ]
        },
    },
    55: {
        "Part a": {
            "choices": [
                choice("A", "H0: (p1 - p2) = 0; Ha: (p1 - p2) < 0"),
                choice("B", "H0: (p1 - p2) > 0; Ha: (p1 - p2) = 0"),
                choice("C", "H0: (p1 - p2) = 0; Ha: (p1 - p2) ≠ 0"),
                choice("D", "H0: (p1 - p2) < 0; Ha: (p1 - p2) = 0"),
                choice("E", "H0: (p1 - p2) ≠ 0; Ha: (p1 - p2) = 0"),
                choice("F", "H0: (p1 - p2) = 0; Ha: (p1 - p2) > 0"),
            ]
        }
    },
}


QUESTION_OVERRIDES: dict[int, dict[str, object]] = {
    51: {
        "intro": ["About the two populations: Select all that apply."],
        "parts": [
            {
                "id": "part-1",
                "label": "About the two populations",
                "prompt": ["About the two populations: Select all that apply."],
                "choices": [
                    choice("A", "Both sampled populations must have approximately equal population variances."),
                    choice("B", "Both sampled populations must be approximately normally distributed."),
                    choice("C", "There must be more than 30 samples selected from each population."),
                    choice("D", "Both populations must be selected independently of each other."),
                ],
                "answerKeys": ["A", "B"],
                "answerDetails": ["Correct answers: A, B"],
                "explanation": [
                    "For the pooled two-sample t-test with small samples, we assume the two populations are approximately normally distributed and have approximately equal variances."
                ],
            },
            {
                "id": "part-2",
                "label": "About the two samples",
                "prompt": ["About the two samples: Select all that apply."],
                "choices": [
                    choice("A", "The samples must be independent of each other."),
                    choice("B", "There must be more than 30 samples selected from each population."),
                    choice("C", "The samples themselves must be normally distributed."),
                ],
                "answerKeys": ["A"],
                "answerDetails": ["Correct answer: A"],
                "explanation": [
                    "The two samples must be independent of each other. There is no requirement here that each sample size exceed 30, and normality is assumed for the populations rather than the samples themselves."
                ],
            },
        ],
    }
}


def apply_manual_overrides(questions: list[dict[str, object]]) -> list[dict[str, object]]:
    by_id = {question["id"]: question for question in questions}

    for qid, replacement in QUESTION_OVERRIDES.items():
        question = by_id.get(qid)
        if not question:
            continue
        for field, value in replacement.items():
            question[field] = value

    for qid, overrides in PART_OVERRIDES.items():
        question = by_id.get(qid)
        if not question:
            continue
        parts_by_label = {part["label"]: part for part in question["parts"]}
        for label, updates in overrides.items():
            part = parts_by_label.get(label)
            if not part:
                continue
            for field, value in updates.items():
                part[field] = value

    return questions
