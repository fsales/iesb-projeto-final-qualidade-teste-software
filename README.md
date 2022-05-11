# Projeto Final da disciplina Qualidade e Testes de Software.

## Curso

    Pós Graduação Lato Sensu - Especialização em Análise e Desenvolviemento de Sistemas.

## Instituição

Centro Universitário IESB.

## Disciplina

Qualidade e Testes de Software.

## Professor

Ana Cristina Fernandes Lima

## Turma

    RMTADSA

## Aluno(s)
   * Alex de Oliveira Moreira
   * Davidson Pereira Campos
   * Fábio de Oliveira Sales
   * Gabriel Dennis Pereira de Faria
   * Natana Felix da Rocha 
     

## Objetivo

Teste de Perfomance/Carga/Stress da API [Serverest](https://serverest.dev/)

## Tecnologias

- [Python](https://www.python.org/)
- [Poetry](https://python-poetry.org/)
- [Locust](https://locust.io/)

### Mão no código

- [x] Instalar [Python](https://www.python.org/downloads/)
- [x] Instalar [Poetry](https://github.com/python-poetry/poetry#Installation)

### Instando o ambiente

- Comando a seguir instala as dependências do projeto.

```sh
    poetry install
```

- Comando a seguir ativa o ambiente virtual do poetry.

```sh
    poetry shell
```

- Comando a seguir adicina as dependências no projeto.

```sh
    poetry add {nome-dependência}
```

### Executando o programa

```sh
    poetry run locust --locustfile estudo_caso/tests/teste_suite.py --csv serveres_test --logfile serverest_test.log --host https://serverest.dev 
```

### Executando o programa com a configuração do "locust.conf"
```sh
    poetry run locust  
```
ou 

```sh
    poetry shell
    locust  
```

Acesse o projeto no endereço  http://localhost:8089.

