#------------------------------------------------------#
print("\nExercício 03 Estrutura de repetição\n")
numero = int(input("Digite o número para a tabuada: "))
for sequencia in range(1,11):
  print("%2d x %2d = %3d" %(sequencia,numero,sequencia*numero))
  #%2d -> serve para criar um alinhamento de colunas entre os valores