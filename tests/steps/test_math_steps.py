from pytest_bdd import scenarios, given, when, then, parsers

# aponta para todas as scenarios dentro de math_operations.feature
scenarios('../features/math_operations.feature')


@given(parsers.cfparse('dois números "{a:d}" e "{b:d}"'))
def given_numeros(nums, a, b):
    # sobrescreve zeros iniciais
    nums["a"] = a
    nums["b"] = b
    return nums


@when('eu somar os dois números')
def step_somar(nums):
    nums["resultado"] = nums["a"] + nums["b"]


@when('eu subtrair os dois números')
def step_subtrair(nums):
    nums["resultado"] = nums["a"] - nums["b"]


@when('eu multiplicar os dois números')
def step_multiplicar(nums):
    nums["resultado"] = nums["a"] * nums["b"]


@when('eu dividir os dois números')
def step_dividir(nums):
    # divisão inteira ou float de acordo com necessidade
    nums["resultado"] = nums["a"] / nums["b"]


@then(parsers.cfparse('o resultado deve ser "{resultado:d}"'))
def step_verificar(nums, resultado):
    assert nums["resultado"] == resultado
