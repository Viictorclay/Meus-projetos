# Copilot Instructions for AI Agents

## Visão Geral do Projeto
Este repositório contém múltiplos projetos pequenos, organizados por tipo e finalidade. Os principais componentes são:
- Scripts Python para controle de estoque, geração de histogramas e placar de basquete (`scripts/`)
- Projetos web estáticos, com HTML, CSS e JavaScript, organizados em subpastas de `WEBs/`

## Estrutura e Fluxos
- **scripts/**: Scripts Python independentes, cada um com sua própria lógica e, em alguns casos, arquivos de dados (ex: `Estoque.json`).
  - `Controle_de_estoque_simples.py`: Manipula estoque usando um arquivo JSON.
  - `histograma.py`: Provavelmente gera histogramas a partir de dados.
  - `Placar_de_basket.py`: Gerencia placar de partidas de basquete.
- **WEBs/web-01/**: Projeto web estático com estrutura típica de front-end:
  - `index.html`: Página principal.
  - `assets/css/style.css`: Estilos customizados.
  - `assets/js/script.js`: Scripts JS para interatividade.
  - `assets/imgs/`: Imagens usadas no site.
  - `templates/`: Possível uso futuro para páginas HTML reutilizáveis.

## Convenções e Padrões
- **Python**: Scripts não seguem um padrão de pacote, mas usam arquivos de dados locais (JSON). Não há estrutura de testes automatizados detectada.
- **Web**: Estrutura de pastas separa claramente CSS, JS e imagens. Use caminhos relativos para assets.
- **Nomes de arquivos**: Use nomes descritivos e evite espaços; preferir underscores ou kebab-case.

## Fluxos de Desenvolvimento
- Não há automação de build/teste detectada. Execute scripts Python diretamente pelo interpretador.
- Para desenvolvimento web, edite arquivos em `WEBs/web-01/` e abra `index.html` no navegador para visualizar mudanças.

## Integrações e Dependências
- **Python**: Dependências externas não detectadas (exceto possível uso de bibliotecas padrão).
- **Web**: Não há dependências externas explícitas (ex: npm, frameworks JS).

## Exemplos de Uso
- Para rodar o controle de estoque: `python scripts/Controle_de_estoque_simples.py`
- Para editar o site: modifique arquivos em `WEBs/web-01/assets/` e recarregue o navegador.

## Recomendações para Agentes
- Respeite a separação entre scripts Python e projetos web.
- Mantenha a organização de assets em subpastas.
- Documente scripts ou fluxos novos diretamente no README ou em comentários nos arquivos relevantes.

Se detectar padrões novos ou fluxos automatizados, atualize este arquivo para refletir as melhores práticas do repositório.