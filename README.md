# IntvTouch
**Intellivision Touch, controlador para console e emulador Intellivision com direcional analógico e overlay na tela touch**

**Intellivision Touch, controller for console and Intellivision emulator with analog stick and overlay on the touch screen**

A versão comercial foi lançada em março de 2025, disponível no parceiro abcnetgames.com.br.

The commercial version was released in March 2025, available at the partner abcnetgames.com.br.

![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/Todos.jpg)

Intellivision Touch Available now

[![Veja no YouTube](https://img.youtube.com/vi/XqhcIi7sJF4/0.jpg)](https://youtu.be/XqhcIi7sJF4)

Intellivision Touch Controller Video User Manual Version 1.06

[![Veja no YouTube](https://img.youtube.com/vi/ugPp8pVRMoM/0.jpg)](https://youtu.be/ugPp8pVRMoM)

Intellivision Touch Controller Version 110 Update

[![Veja no YouTube](https://img.youtube.com/vi/3Wk6yGoCM5Y/0.jpg)](https://youtu.be/3Wk6yGoCM5Y)

**Protótipo controle para console e emulador Intellivision com direcional analógico e overlay na tela touch**

Versão final, pré-lançamento

![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/final.jpg)

**Vídeo no Youtube:**

[![Veja no YouTube](https://img.youtube.com/vi/a9IfyRDWwZY/0.jpg)](https://youtu.be/a9IfyRDWwZY)

Information about license of use:
This version is free for individual personal use, as long as it is not for commercial purposes and credits are attributed.
Replication for personal or commercial use of the pre-release or release version is prohibited, unless expressly authorized by the author.


Versão: 0.90

Agora com suporte para saída USB para emuladores, player 1 e player 2,
e menu de seleção de overlay com nomes de arquivos livres.

**Vídeo no Youtube:**

[![Veja no YouTube](https://img.youtube.com/vi/E4J67_oy-kw/0.jpg)](https://youtu.be/E4J67_oy-kw)


Versão: 0.12

O projeto, sem fins comerciais, esta aberto para você construir o seu e, se puder, colaborar na melhoria desse desenvolvimento.

Baseado no hardware: Clone **Purple** da Raspberry Pi PICO RP2040, Display ILI9341 + XPT2046 (Touchscreen), Analógico direcional de 2 eixos e Optoacoplador.
Firmware CircuitPython
Imagens BMP dos overlays na pasta bmp nomeados com 3 digitos.
Botão de pressão do joystick para modo de Pausa e para novo overlay (3 digitos e Enter)

![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/001.jpg)


**Vídeo no Youtube:**

[![Veja no YouTube](https://img.youtube.com/vi/FjTe33QmZQY/0.jpg)](https://youtu.be/FjTe33QmZQY)


![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/002.jpg)
![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/003.jpg)
![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/004.jpg)
![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/005.jpg)
![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/006.jpg)

Resumo das conexões:

**RP2040 - Purple**
![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/Pinos_Purple.jpg)

**Display ILI9341 + XPT2046** (JC2432S024R 2,4" resistor touch 240x320 RGB)
![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/Pinos_Display.jpg)

**Joystick** (2 eixos divisor resistivo 10K + chave pressão)
![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/Pinos_Joy.jpg)

**Botões**
![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/Pinos_Botoes.jpg)

**Optoacoplador** (8x EL817 ou 2x TLP281-4 + 8x 220R)
![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/Pinos_Opto.jpg)

**DB9** (Intellivision2 ou Sears, Intellivision1 com adaptador)
![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/Pinos_DB9.jpg)

Conector Intv Flashback:
A definir

**Acionamento**
![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/Pinos_Sinais.jpg)

