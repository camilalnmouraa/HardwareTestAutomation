# Automated Testing for Electronic Hardware System

This project consists of a set of automated tests for an electronic hardware system with one input and one output. When the input state changes, the output pin toggles on for one second.

## Testing Strategy

To test the electronic hardware system, the following test cases were implemented:

1. **Activation and Deactivation of Output Pin Test:**
   - Verifies if it is possible to activate and deactivate the output pin correctly.

2. **Input Pin State Reading Test:**
   - Confirms if the system can correctly read the state of the input pin after a change.

3. **Simulated Change in Output Pin Test:**
   - Tests the simulation of a change in the state of the output pin and verifies if the input pin responds appropriately.

## CI/CD Pipeline Configuration

The continuous integration (CI/CD) pipeline is configured to run the automated tests in a simulated hardware environment. The strategy to perform the tests is as follows:

1. **Environment Setup:**
   - Installation of project dependencies.
   - Configuration of the hardware simulation environment.

2. **Test Execution:**
   - Activation of automated tests to verify the behavior of the hardware system.
   - The tests include activation and deactivation of the output pin, reading the state of the input pin, and simulating a change in the output pin.

3. **Failure Notification:**
   - In case of test failures, an alert is sent to the configured Slack channel.

## Observations

Due to the nature of the project, where the hardware is not available for testing, the execution of the tests may not fully reflect the real behavior of the system. However, the tests provide an initial validation of the implemented logic and serve as a basis for future testing in a real hardware environment.

## References

- Pytest Documentation: [link](https://docs.pytest.org/en/latest/)
- GitLab CI/CD Documentation: [link](https://docs.gitlab.com/ee/ci/yaml/)
