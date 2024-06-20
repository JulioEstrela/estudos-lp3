import json
from flask import Flask, render_template
from validate_docbr import CPF, CNPJ

# instancia o objeto flask que representa a aplicação
app = Flask("minha aplicação")

@app.route("/")
def home():
    return render_template('home.html')

# página lojas
@app.route("/lojas")
def lojas():
    
    with open('projeto_lp3/lojas.json', 'r', encoding='utf8') as lojas_json:
        lista_lojas = json.load(lojas_json)
        lojas = [{**loja} for loja in lista_lojas]
        

        return render_template('lojas.html', lojas=lojas)

# página de produtos
@app.route("/produtos")
def produtos(): 

    with open('projeto_lp3/produtos.json', 'r', encoding='utf8') as produtos:
        lista_produtos = json.load(produtos)
        produtos = [{**produto, 'preco': format(produto['preco'], '.2f')} for produto in lista_produtos]

        # dá um nome pra acessar no html
        return render_template('produtos.html', produtos=produtos)




@app.route("/servicos")
def servicos(): 
    return render_template('servicos.html')


@app.route("/gerar-cpf")
def cpf(): 
    cpf = CPF()
    return render_template('gerar-cpf.html', cpf_gerado = cpf.generate(True))

@app.route("/gerar-cnpj")
def cnpj(): 
    cnpj = CNPJ()
    return render_template('gerar-cnpj.html', cnpj_gerado = cnpj.generate(True))


if __name__ == "__main__":
    app.run()