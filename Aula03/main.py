from Aluno import Aluno
from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

print("--------PESSOA-------")

p1 = Pessoa("Luiz", "(51) 992617905")
p1.imprimir()

print("--------PESSOA FISICA-------")

pf = PessoaFisica("João", "(52) 992617905", "01961258048")
pf.imprimir()

print("--------PESSOA JURIDICA-------")

pj = PessoaJuridica("SENAC","(53) 123456789","00.000.0000")
pj.imprimir()

print("--------ALUNO-------")

A = Aluno("Aluno1","(54) 12345678","123.456.789.00","1865")
A.imprimir()