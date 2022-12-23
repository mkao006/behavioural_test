Feature: Test the expected relationship using scenario outline

Scenario Outline: Test the directional relationship
   Given A trained model with training data
    when We <perturbation_change> the room number per dwelling
    then The average predicted median value should <expected_output_direction>

 Examples:
   | perturbation_change | expected_output_direction |
   | increase            | increase                  |
   | decrease            | decrease                  |