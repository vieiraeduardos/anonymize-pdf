# Anonymize PDF

O **Anonymize PDF** é uma ferramenta desenvolvida em Python para anonimizar nomes pessoais e outras informações sensíveis em documentos PDF. O objetivo principal do projeto é garantir a privacidade e a proteção de dados, especialmente em situações onde documentos precisam ser compartilhados sem expor informações pessoais, como nomes, CPFs, endereços ou outros dados identificáveis.

A ferramenta utiliza técnicas de processamento de linguagem natural (NLP) e reconhecimento de padrões para identificar e substituir automaticamente nomes e informações sensíveis por valores genéricos ou marcadores, como `[NOME]` ou `[REDACTED]`. Além disso, o projeto é capaz de preservar a formatação original do PDF, garantindo que o layout do documento não seja comprometido durante o processo de anonimização.

## Funcionalidades Principais

- **Identificação Automática de Nomes**:  
  Usa bibliotecas de NLP (como spaCy ou NLTK) para detectar nomes próprios no texto.

- **Redação de Informações Sensíveis**:  
  Substitui nomes, CPFs, endereços e outras informações por marcadores ou textos genéricos.

- **Preservação de Formatação**:  
  Mantém o layout original do PDF, incluindo imagens, tabelas e estilos de texto.

- **Interface Amigável**:  
  Pode ser utilizada via linha de comando (CLI) ou com uma interface gráfica simples (GUI) para facilitar o uso.

- **Suporte a Múltiplos Idiomas**:  
  Capaz de identificar e anonimizar nomes em diferentes idiomas, dependendo da configuração.

- **Exportação Segura**:  
  Gera um novo arquivo PDF com as informações sensíveis removidas, pronto para compartilhamento seguro.

## Casos de Uso

- Compartilhamento de documentos jurídicos ou médicos sem expor dados pessoais.
- Publicação de relatórios ou pesquisas que contenham informações confidenciais.
- Preparação de documentos para auditorias ou revisões, garantindo conformidade com leis de proteção de dados (como a LGPD ou GDPR).

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **PyPDF2 ou PDFMiner**: Para extração e manipulação de texto em PDFs.
- **spaCy ou NLTK**: Para identificação de nomes e entidades.
- **Regex (Expressões Regulares)**: Para detecção de padrões como CPFs, telefones, etc.
- **ReportLab ou fpdf**: Para gerar o novo PDF anonimizado (opcional).

## Objetivo Final

O **Anonymize PDF** visa ser uma solução eficiente e acessível para proteger a privacidade de indivíduos em documentos digitais, contribuindo para a segurança de dados e a conformidade com regulamentações de proteção à privacidade.
