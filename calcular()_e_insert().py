tam = 30
operacoes = {
    "+": "soma",
    "-": "subtração",
    "x": "multiplicação",
    "/": "divisão",
    "^": "potência",
    "00": "fechar calculadora"
}



def insert():

  
    while True:
        print(f"+{'-' * tam}+")
        print(f"|{'calculadora':^{tam}}|")
        print(f"+{'-' * tam}+")

        for i in operacoes.values():
            print(f"|{f' {i} ':{tam}}|")

        print(f"+{'-' * tam}+")

        print("Orientação: aperte 00 para fechar a calculadora")

        

        A0 = input('Digite o primeiro valor: ')
        if A0 == "00":
          print("Calculadora fechada.")
          break

        try:
          A0 = float(A0)
        except ValueError:
          print("Entrada inválida. Certifique-se de inserir números.")
          continue  

        op = input('Selecione a operação: ')
        if op == "00":
          print("Calculadora fechada.")
          break

        B0 = input('Digite o segundo valor: ')
        if B0 == "00":
          print("Calculadora fechada.")
          break

        try:
          B0 = float(B0)
        except ValueError:

          print("Entrada inválida. Certifique-se de inserir números.")
          continue 
        return A0, op, B0

def calcular(A0, op, B0):
  
  if op in operacoes:
    if op == "+":
      print(A0 + B0)
    elif op == "-":
        print(A0 - B0)
    elif op == "x":
        print(A0 * B0)
    elif op == "/":
        print(A0 / B0)
    elif op == "^":
      print(A0 ** B0)
          
  else:
      print("Operação inválida. Tente novamente.")

valores = insert()
if valores is not None:
  calcular(*valores)