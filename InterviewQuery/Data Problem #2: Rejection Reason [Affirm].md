Data Problem #2: Rejection Reason [Affirm]

If we had access to feature weights, we would 
- know how much each [feature contributes](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) to final classification.
- have plotted [feature importances](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html) to know what features are important in case of Decision Tree/Random Forest. 
- have plotted the decision tree rules [sklearn.tree](https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html) for better understanding.

Given that we don't have access to the feature weigths, we would have to find some other ways to give reasons to customers for their rejection. 
- As we are a financial company, we could leverage domain experts(who also might have helped in creating this model) to get some intuition about the features of rejected customer(s). 
- We could take the features of a rejected customer. Find similar customers(who also got rejected) and make a correlation between them. If we find certain common pattern / data point in this (rejected) population, we could find a mapping of the customers based on that. 
- Visually explaining the reasons to stakeholders, *if feasible*, is a better way than writing in text format. For this we could find a few buckets/population from point#2 and show customers to which bucket they belong to.
