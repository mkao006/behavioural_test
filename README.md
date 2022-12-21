# Behavioural Testing for ML models

This is an example for this blogpost to illustrate how we can use [behave](https://behave.readthedocs.io/en/stable/index.html) to perform behavioural tests on our ML model for non-NLP use cases to ensure that the model is behaving as expected.

For example, if we build a housing price prediction model using a gradient boosted tree, while it may be difficult to explain the relationships, we know on average that when you increase the number of rooms, the predicted price should on average increase. 

This is an example of the 'Expected Directional Test', if this relatinrelationship does not hold, then there is perhaps something wrong with the model.

[Beyond Accuracy: Behavioral Testing of NLP models with CheckList](https://arxiv.org/abs/2005.04118)
