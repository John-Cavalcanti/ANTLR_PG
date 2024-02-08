# ANTLR_PG
Atividade para o uso de um gerador de parser para a cadeira de Compiladores

## Como gerar parser e lexer 

Antes de usar o código de geração do parser e lexer é necessário adicionar o arquivo
do antlr4 ao PATH pois mesmo rodando uma vez o código ele apenas funciona temporariamente.

```bash
export CLASSPATH="C:\ANTLR\antlr-4.13.1-complete.jar"
alias antlr4='java -Xmx500M -cp "C:\ANTLR\antlr-4.13.1-complete.jar" org.antlr.v4.Tool'
alias grun='java -Xmx500M -cp "C:\ANTLR\antlr-4.13.1-complete.jar" org.antlr.v4.gui.TestRig'

```

Após isso só usar o código abaixo para gerar os lexers e parsers.

```bash
antlr4 -Dlanguage=Python3 ./Grammar/Arithmetic.g4
```
