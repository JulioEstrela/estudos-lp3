# Comandos git:

git init - Inicializa o repositório git

git clone - Faz o download do repositorio git remoto

git status - Apresenta o status do repositorio local

git add \<nome do arquivo> - Adiciona o arquivo modificado ou untracked para o próximo commit

git add . - Adiciona todos os arquivos modificados ou untracked para o próximo commit

git stage - Sinônimmo de git add

git reset - Remove todas as modificações adicionadas ao próximo commit

git commit -m "mensagem" - Realiza o commit com a mensagem

git branch - Mostra a branch atual

git checkout \<nome da branch> - Muda de branch

git diff - Mostra a diferença do código atual em relação ao último commit

git fetch - Atualiza os commits do repositório remoto no repositório local

git merge - Mescla o repositório remoto no workspace local

git pull "Puxa" - git fetch + git merge

git push "Empurra" - Envia todos os commits locais para o repositório remoto

git log - Mostra o histórico de commits: título, descrição, hash, autor e data. (Com alguns argumentos é possível mudar a aparência da saída: https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)

git restore \<hash> - Reverte o projeto à como estava antes do commit passado (hash)
