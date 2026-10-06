# Calculadora de Peso de Chapa

Aplicação desktop desenvolvida em **Python** para calcular de forma rápida o peso de chapas de aço a partir das dimensões informadas pelo usuário.

A interface foi construída com **Tkinter** e utiliza **Pillow** para tratamento e redimensionamento dinâmico da imagem de fundo.

## Funcionalidades

- Cálculo automático do peso da chapa.
- Entrada de largura, comprimento e espessura.
- Aceita valores com vírgula ou ponto decimal.
- Resultado apresentado em quilogramas (kg).
- Validação de valores numéricos.
- Navegação entre os campos utilizando a tecla `Enter`.
- Interface redimensionável.
- Imagem de fundo com desfoque e tratamento visual.

## Fórmula utilizada

O cálculo considera a densidade aproximada do aço de **7.850 kg/m³**.

```text
Peso (kg) = Largura × Comprimento × Espessura × 0,00000785
```

> As dimensões devem ser informadas em **milímetros (mm)**.

### Exemplo

Para uma chapa com:

- Largura: `1200 mm`
- Comprimento: `3000 mm`
- Espessura: `6,30 mm`

O cálculo será:

```text
1200 × 3000 × 6,30 × 0,00000785
```

Resultado aproximado:

```text
178,04 kg
```

## Tecnologias utilizadas

- Python
- Tkinter
- Pillow (PIL)

## Estrutura do projeto

```text
PROJETO CALCULO DE CUSTO/
├── custos.py
├── grunge-wall-texture.jpg
└── README.md
```

## Requisitos

Para executar o projeto, tenha instalado:

- Python 3.10 ou superior
- Pillow

O Tkinter normalmente já acompanha a instalação padrão do Python no Windows.

## Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/calculadora-peso-chapa.git
```

Entre na pasta do projeto:

```bash
cd calculadora-peso-chapa
```

Instale a dependência necessária:

```bash
pip install pillow
```

## Como executar

Execute:

```bash
python custos.py
```

No Windows, dependendo da instalação do Python, também pode ser utilizado:

```bash
py custos.py
```

## Arquivo de imagem

O arquivo:

```text
grunge-wall-texture.jpg
```

deve permanecer na mesma pasta do arquivo `custos.py`, pois ele é carregado diretamente pela aplicação como imagem de fundo.

## Interface

A aplicação possui uma interface simples e responsiva com três campos principais:

1. Largura da chapa
2. Comprimento da chapa
3. Espessura da chapa

Após preencher os valores, basta clicar em **Calcular** ou pressionar `Enter` no campo de espessura.

## Possíveis melhorias futuras

- Seleção de diferentes materiais e densidades.
- Histórico de cálculos.
- Cálculo do custo da chapa por kg.
- Cálculo de aproveitamento e desperdício.
- Exportação dos resultados para Excel ou PDF.
- Empacotamento do programa em `.exe`.
- Interface com identidade visual personalizada.

## Licença

Este projeto pode ser utilizado para fins de estudo, desenvolvimento e uso interno.
