Feature: Test the expected relationship between room number and predicted median value.

  Scenario: Test the relationship is positive
     Given A trained model with training data
      When We perturbate the room number per dwelling
      Then The change in predicted median value should be positively correlated with the change.