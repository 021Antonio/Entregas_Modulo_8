# Ponderada 8

Para ver o video, clique no link por favor, não consegui colocar o video aqui no README

https://www.loom.com/embed/9636b9b4e7754a12a6a825349610756a?sid=6635d308-607d-49bb-bed3-d7d2e795e606

## Como executar

Entre na pasta do projeto e execute o comando:

```bash
python3 tts_tradutor.py
```
O codigo irá rodar certo apenas com esse comando. Mas lembre-se de instalar as bibliotecas necessarias. 

```bash 
pip install pip install SpeechRecognition googletrans gtts
```
E outra coisa muito importante. Para a leitura dos audios, é necessario estar no formato `.wav`. Caso deseje botar seu proprio audio, [clique aqui!](https://cloudconvert.com/mp3-to-wav)

## Sobre o codigo 

Este código em Python realiza a transcrição de áudio para texto, traduz o texto para outro idioma e, em seguida, converte a tradução em um arquivo de áudio usando as seguintes bibliotecas:

### Bibliotecas utilizadas

<h4>SpeechRecognition</h4>

Objetivo: Reconhecimento de fala.

Uso no código: Usado para transcrever o áudio para texto por meio do serviço de reconhecimento de fala do Google.

<h4>googletrans</h4>

Objetivo: Tradução de texto entre idiomas.

Uso no código: Utilizado para traduzir o texto reconhecido para outro idioma.

<h4>gTTS (Google Text-to-Speech)</h4>

Objetivo: Síntese de fala a partir de texto.

Uso no código: Usado para converter o texto traduzido em um arquivo de áudio.


### Funcionamento do Código
x
Transcrição de Áudio para Texto

Utiliza a biblioteca SpeechRecognition para transcrever um arquivo de áudio fornecido para texto, utilizando o serviço de reconhecimento de fala do Google.
Tradução de Texto

Usa a biblioteca googletrans para traduzir o texto reconhecido para outro idioma (por padrão, inglês).
Conversão de Texto Traduzido em Áudio

Utiliza a gTTS para criar um arquivo de áudio a partir do texto traduzido.
