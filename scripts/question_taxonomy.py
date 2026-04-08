from __future__ import annotations

import re


QUESTION_CLASSIFICATIONS: dict[int, dict[str, object]] = {
    1: {
        "family": "Foundations",
        "module": "Statistical thinking",
        "concept": "Descriptive vs inferential statistics",
        "tags": ["descriptive statistics", "inferential statistics", "sampling"],
    },
    2: {
        "family": "Foundations",
        "module": "Sampling",
        "concept": "Representative samples",
        "tags": ["representative sample", "population", "inference"],
    },
    3: {
        "family": "Foundations",
        "module": "Data types",
        "concept": "Qualitative vs quantitative data",
        "tags": ["categorical data", "coded data", "qualitative vs quantitative"],
    },
    4: {
        "family": "Foundations",
        "module": "Study design",
        "concept": "Population, sample, variable, and inference",
        "tags": ["population", "sample", "variable of interest", "survey bias"],
    },
    5: {
        "family": "Descriptive statistics",
        "module": "Categorical displays",
        "concept": "Pareto charts",
        "tags": ["Pareto diagram", "categorical frequency", "interpretation"],
    },
    6: {
        "family": "Descriptive statistics",
        "module": "Data displays",
        "concept": "Stem-and-leaf plots and dot plots",
        "tags": ["stem-and-leaf", "dot plot", "raw data reconstruction"],
    },
    7: {
        "family": "Descriptive statistics",
        "module": "Center and shape",
        "concept": "Mean, median, mode, and skewness",
        "tags": ["mean", "median", "mode", "skewness"],
    },
    8: {
        "family": "Descriptive statistics",
        "module": "Variability",
        "concept": "Range, variance, and standard deviation",
        "tags": ["range", "variance", "standard deviation", "spread"],
    },
    9: {
        "family": "Descriptive statistics",
        "module": "Position measures",
        "concept": "Percentiles and quartile interpretation",
        "tags": ["percentiles", "quartiles", "interpretation"],
    },
    10: {
        "family": "Descriptive statistics",
        "module": "Standardized values",
        "concept": "Z-scores and unusual observations",
        "tags": ["z-score", "outlier", "unusual value"],
    },
    11: {
        "family": "Categorical analysis",
        "module": "Contingency tables",
        "concept": "Expected counts, chi-square, and Cramer's V",
        "tags": ["expected count", "chi-square", "Cramer's V", "independence"],
    },
    12: {
        "family": "Categorical analysis",
        "module": "Comparing groups",
        "concept": "Conditional proportions in two-way tables",
        "tags": ["conditional proportion", "gender comparison", "two-way table"],
    },
    13: {
        "family": "Functions and graphs",
        "module": "Linear equations",
        "concept": "Graphing lines from slope-intercept form",
        "tags": ["line graph", "slope", "y-intercept"],
    },
    14: {
        "family": "Regression",
        "module": "Model setup",
        "concept": "Explanatory and response variables",
        "tags": ["predictor", "response", "regression setup"],
    },
    15: {
        "family": "Regression",
        "module": "Scatterplots and fit",
        "concept": "Scatterplot trend and least-squares line",
        "tags": ["scatterplot", "least squares", "fit interpretation"],
    },
    16: {
        "family": "Regression",
        "module": "Simple linear regression",
        "concept": "Regression equation, intercept, slope, and scope",
        "tags": ["regression equation", "intercept", "slope", "practical interpretation"],
    },
    17: {
        "family": "Regression",
        "module": "Prediction",
        "concept": "Fit a line and predict a response",
        "tags": ["prediction", "least squares", "software millionaires"],
    },
    18: {
        "family": "Regression",
        "module": "Scatterplot association",
        "concept": "Linear trend direction and slope sign",
        "tags": ["linear trend", "scatterplot", "positive/negative slope"],
    },
    19: {
        "family": "Probability",
        "module": "Basic rules",
        "concept": "Complements and unions",
        "tags": ["complement", "union", "intersection"],
    },
    20: {
        "family": "Probability",
        "module": "Two-way tables",
        "concept": "Joint, marginal, and union probabilities",
        "tags": ["joint probability", "marginal probability", "union"],
    },
    21: {
        "family": "Probability",
        "module": "Venn diagrams",
        "concept": "Visualizing overlap with unions and complements",
        "tags": ["Venn diagram", "union", "complement"],
    },
    22: {
        "family": "Probability",
        "module": "Conditional probability",
        "concept": "Conditional probability and independence",
        "tags": ["P(A|B)", "independence", "conditional probability"],
    },
    23: {
        "family": "Probability",
        "module": "Bayes theorem",
        "concept": "Posterior probability from diagnostic information",
        "tags": ["Bayes theorem", "tree diagram", "posterior probability"],
    },
    24: {
        "family": "Probability",
        "module": "Event relationships",
        "concept": "Mutually exclusive events vs independent events",
        "tags": ["mutually exclusive", "independence", "conditional probability"],
    },
    25: {
        "family": "Random variables",
        "module": "Discrete distributions",
        "concept": "Profit distributions from uncertain demand",
        "tags": ["discrete random variable", "profit", "distribution table"],
    },
    26: {
        "family": "Random variables",
        "module": "Expected value",
        "concept": "Expected price and long-run budgeting",
        "tags": ["expected value", "budgeting", "weighted average"],
    },
    27: {
        "family": "Random variables",
        "module": "Discrete distributions",
        "concept": "Read probabilities from a histogram",
        "tags": ["discrete distribution", "histogram", "probability"],
    },
    28: {
        "family": "Random variables",
        "module": "Poisson distribution",
        "concept": "Poisson probabilities and moments",
        "tags": ["Poisson", "mean", "standard deviation", "P(X=x)"],
    },
    29: {
        "family": "Random variables",
        "module": "Poisson distribution",
        "concept": "Interpreting the Poisson mean",
        "tags": ["Poisson mean", "expected value", "interpretation"],
    },
    30: {
        "family": "Normal model",
        "module": "Normal probabilities",
        "concept": "Probabilities and quantiles under a normal distribution",
        "tags": ["normal distribution", "z-score", "percentile", "quantile"],
    },
    31: {
        "family": "Normal model",
        "module": "Normality checks",
        "concept": "Identify evidence against approximate normality",
        "tags": ["normality", "QQ plot", "empirical rule", "IQR/s"],
    },
    32: {
        "family": "Normal model",
        "module": "Normality checks",
        "concept": "IQR-to-standard-deviation diagnostic",
        "tags": ["IQR/s", "normality check", "approximate normal"],
    },
    33: {
        "family": "Normal model",
        "module": "Model choice",
        "concept": "Use a histogram to decide whether a normal model is appropriate",
        "tags": ["histogram", "model choice", "normal approximation"],
    },
    34: {
        "family": "Sampling distributions",
        "module": "Normal approximation",
        "concept": "Approximating a binomial distribution with a normal curve",
        "tags": ["normal approximation", "binomial", "continuity correction"],
    },
    35: {
        "family": "Sampling distributions",
        "module": "Central Limit Theorem",
        "concept": "When the sampling distribution of x-bar is approximately normal",
        "tags": ["CLT", "sampling distribution", "x-bar"],
    },
    36: {
        "family": "Sampling distributions",
        "module": "Central Limit Theorem",
        "concept": "How sample size changes the shape of the x-bar distribution",
        "tags": ["CLT", "histogram", "sample size effect"],
    },
    37: {
        "family": "Sampling distributions",
        "module": "Comparing populations",
        "concept": "Use sample-mean behavior to infer which population is more plausible",
        "tags": ["sampling distribution", "x-bar", "compare populations"],
    },
    38: {
        "family": "Sampling distributions",
        "module": "Sample mean",
        "concept": "Mean, standard error, z-score, and probability for x-bar",
        "tags": ["standard error", "z-score", "sample mean"],
    },
    39: {
        "family": "Sampling distributions",
        "module": "Sample proportion",
        "concept": "Mean, standard deviation, z-score, and probability for p-hat",
        "tags": ["sample proportion", "p-hat", "standard deviation", "z-score"],
    },
    40: {
        "family": "Estimation",
        "module": "Estimator concepts",
        "concept": "Point estimators vs interval estimators",
        "tags": ["point estimate", "interval estimate", "parameter"],
    },
    41: {
        "family": "Estimation",
        "module": "Confidence interval assumptions",
        "concept": "Large-sample confidence intervals and the Central Limit Theorem",
        "tags": ["confidence interval", "large sample", "CLT"],
    },
    42: {
        "family": "Estimation",
        "module": "Confidence interval interpretation",
        "concept": "Confidence coefficients, interpretation, and width",
        "tags": ["confidence coefficient", "confidence interval", "margin of error"],
    },
    43: {
        "family": "Estimation",
        "module": "Confidence intervals for a mean",
        "concept": "Construct and compare 95% and 99% intervals for mu",
        "tags": ["mean CI", "95%", "99%", "critical value"],
    },
    44: {
        "family": "Estimation",
        "module": "Margin of error",
        "concept": "How sample size changes confidence-interval width",
        "tags": ["sample size", "confidence interval width", "margin of error"],
    },
    45: {
        "family": "Estimation",
        "module": "Confidence intervals for a proportion",
        "concept": "Point estimate and 95% confidence interval for p",
        "tags": ["proportion CI", "point estimate", "interpretation"],
    },
    46: {
        "family": "Estimation",
        "module": "Confidence intervals for a proportion",
        "concept": "Recover sample size from a confidence interval for p",
        "tags": ["sample size", "proportion CI", "margin of error"],
    },
    47: {
        "family": "Hypothesis testing",
        "module": "One-sample mean tests",
        "concept": "Two-tailed p-value and decision for a mean",
        "tags": ["p-value", "two-tailed test", "mean hypothesis test"],
    },
    48: {
        "family": "Hypothesis testing",
        "module": "One-sample z tests",
        "concept": "Null and alternative hypotheses, Type I/II errors, and assumptions",
        "tags": ["one-sample z test", "Type I error", "Type II error", "assumptions"],
    },
    49: {
        "family": "Hypothesis testing",
        "module": "One-sample t tests",
        "concept": "One-tailed vs two-tailed p-values with a t statistic",
        "tags": ["one-sample t test", "one-tailed", "two-tailed", "p-value"],
    },
    50: {
        "family": "Hypothesis testing",
        "module": "One-sample proportion tests",
        "concept": "Upper-tailed z test for a population proportion",
        "tags": ["proportion test", "upper-tailed", "z test", "rejection region"],
    },
    51: {
        "family": "Hypothesis testing",
        "module": "Two-sample mean tests",
        "concept": "Assumptions for the pooled small-sample t procedure",
        "tags": ["pooled t test", "equal variances", "assumptions"],
    },
    52: {
        "family": "Hypothesis testing",
        "module": "Two-sample mean tests",
        "concept": "Pooled t test and confidence interval for mu1 minus mu2",
        "tags": ["pooled t test", "mu1 - mu2", "confidence interval"],
    },
    53: {
        "family": "Hypothesis testing",
        "module": "Two-sample mean tests",
        "concept": "Interpret a p-value for two-sided and one-sided mean comparisons",
        "tags": ["two-sample means", "p-value", "one-sided vs two-sided"],
    },
    54: {
        "family": "Hypothesis testing",
        "module": "Two-proportion inference",
        "concept": "Confidence interval plus statistical and practical significance for p1 minus p2",
        "tags": ["two-proportion CI", "practical significance", "statistical significance"],
    },
    55: {
        "family": "Hypothesis testing",
        "module": "Two-proportion tests",
        "concept": "Upper-tailed test for whether p1 exceeds p2",
        "tags": ["two-proportion test", "upper-tailed", "p1 - p2"],
    },
}


def _slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def classification_for(question_id: int) -> dict[str, object]:
    if question_id not in QUESTION_CLASSIFICATIONS:
        raise KeyError(f"Missing classification for question {question_id}")

    base = QUESTION_CLASSIFICATIONS[question_id]
    family = str(base["family"])
    module = str(base["module"])
    concept = str(base["concept"])

    return {
        **base,
        "conceptPath": f"{family} / {module} / {concept}",
        "familyId": _slugify(family),
        "conceptId": _slugify(f"{family}-{module}-{concept}"),
    }
