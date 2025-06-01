Feature: Facebook Login Functionality

  @logincase
  Scenario Outline: Test login with incorrect credentials
    When we input '<login_id>' and '<password>'
    Examples: Credentials
      | login_id            | password      |
      | vishal4128           | Universe234@# |
    Then Program tries to run
