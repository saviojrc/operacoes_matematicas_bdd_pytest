Feature: Operações matemáticas básicas
  Todas as operações (soma, subtração, multiplicação e divisão) compartilham a mesma feature,
  cada caso de teste é um exemplo no mesmo Scenario Outline.

  Scenario Outline: <operacao> de dois números
    Given dois números "<a>" e "<b>"
    When eu <acao> os dois números
    Then o resultado deve ser "<resultado>"

  Examples:
    | operacao      | acao        | a  | b | resultado |
    | soma          | somar       | 1  | 2 | 3         |
    | subtração     | subtrair    | 5  | 3 | 2         |
    | multiplicação | multiplicar | 2  | 4 | 8         |
    | divisão       | dividir     | 10 | 2 | 5         |
