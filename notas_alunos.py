nota_port=float(input("digite a nota do aluno"))
nota_mat=float(input("digite a nota do aluno"))
nota_P_A=float(input("digite a nota do aluno"))
media=(nota_port + nota_mat + nota_P_A)/3
print(media)
nota_aprovacao=7
if media >= 7:
    print("voce passou")
else:
    print("voce nao passou")
   
