# Projeto Universidade

Modelagem em orientação à Objetos das Entidades Alunos, Cursos e Turmas

##  Caso de Uso
```mermaid
flowchart LR 
    Usuario([secretaria])

    UC1((Cadastrar Alunos))
    UC2((Editar Alunos))
    UC3((Transferir Aluno))

    Usuario --> UC1
    Usuario --> UC2
    Usuario --> UC3
```

## Diagrama de Classes 
```mermaid
classDiagram
    class aluno{
        - nome 
        - email
        - cpf
        - telefone
        - endereço 
        - matrícula 
        + cadastrar()
        + editar()
        + transferir()    
    }
```
# Funções MySQL

- CREATE - Cria tabelas dentro da base de dados.
- INSERT - Cria registros dentro das tabelas.

- SELECT - Permite visualizar os dados dentro das tabelas. Também permite filtrar os dados que quer visualizar.

- ALTER - Altera a estrutura das tabelas, adicionando ou removendo atributos(campos).
- UPDATE - Atualiza regristros dentro da tabela.

- DROP - Exclui a tabela ou a base de dados inteira.
- DELETE - Exclui registros dentro das tabelas.

#  Conceitos MySQL

- Banco de Dados: Programa hospedado na máquina, com objetivo de persistir os dados fisicamente no HD.

- Base de Dados: Conjunto de tabelas.

- Tabelas: Conjunto de registros.

- Registros: Uma linha na tabela, contendo a informação dos seus atributos.

- Atributos: Uma das caracteristicas da tabela (Colunas).

# Bibliotecas Python

- Python
- PySide6
- PyInstaller

## Dependências
- **VSCode**: IDE(Interface de Desenvolvimento)

- **Mermaid**: Linguagem para 
confecção de Diagramas em 
documentos MD (Mark Down) 

- **Material Icon Theme**: Tema para colorir
 as pastas.

 - **Git Lens**: Interface gráfica para o versionamento .git integrada 
 ao VSCode. 

 - **MySQL**: SGB (Sistema Gerenciado de Banco de Dados). Permite conectar o usuário como servidor MySQL, possibilitando criar bases de dados, tabelas, incluir e modificar atributos e registros. 