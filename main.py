from antlr4 import *
from ArithmeticLexer import ArithmeticLexer
from ArithmeticParser import ArithmeticParser

class ArithmeticVisitor:
    
    variablesDict = {}
    
    def visit(self, ctx):
        if isinstance(ctx, ArithmeticParser.ExprContext):
            return self.visitExpr(ctx)
    
        elif isinstance(ctx, ArithmeticParser.TermContext):
            return self.visitTerm(ctx)
    
        elif isinstance(ctx, ArithmeticParser.FactorContext):
            return self.visitFactor(ctx)
        
        elif isinstance(ctx, ArithmeticParser.ProgramContext):
            pass
        
        elif isinstance(ctx, ArithmeticParser.StatementContext):
            pass
        
        elif isinstance(ctx, ArithmeticParser.AssignmentContext):
            pass

    def visitExpr(self, ctx):
    
        result = self.visit(ctx.term(0))
    
        for i in range(1, len(ctx.term())):
            
            if ctx.getChild(i * 2 - 1).getText() == '+':
                result += self.visit(ctx.term(i))
            else:
                result -= self.visit(ctx.term(i))
        
        return result

    def visitTerm(self, ctx):
    
        result = self.visit(ctx.factor(0))
    
        for i in range(1, len(ctx.factor())):
            
    
            if ctx.getChild(i * 2 - 1).getText() == '*':
                result *= self.visit(ctx.factor(i))
            else:
                result /= self.visit(ctx.factor(i))
    
        return result

    def visitFactor(self, ctx):
    
        if ctx.INT():
            return int(ctx.INT().getText())
        else:
            return self.visit(ctx.expr())
    
    # criar visits
    
    ## visitProgram
    def visitProgram(self, ctx):
        result = self.visit(ctx.statement(0))
        
        for i in range(1, len(ctx.statement())):
            if ctx.getChild(i * 2 - 1).statement():
                result += self.visit(ctx.statement(i))
            else:
                result -= self.visit(ctx.statement(i))
    
    ## visitStatement
    def visitStatement(self, ctx):
        if(ctx.assignment()):
            return self.visit(ctx.assignment())
        elif(ctx.expr()):
            return self.visit(ctx.expr())
        
    
    ## visitAssignment
    def visitAssignment(self, ctx):
        variable_name = ctx.VAR().getText()
        value = ctx.visit(ctx.expr())
    

def main():
    expression = input("Digite uma expressão aritmética: ")
    lexer = ArithmeticLexer(InputStream(expression))
    stream = CommonTokenStream(lexer)
    parser = ArithmeticParser(stream)
    tree = parser.expr()
    visitor = ArithmeticVisitor()
    result = visitor.visit(tree)
    print("Resultado:", result)

if __name__ == '__main__':
    main()