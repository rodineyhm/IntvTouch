# IntvTouch
**Protótipo controle para console Intellivision com direcional analógico e overlay na tela touch**

![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/001.jpg)
![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/002.jpg)
![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/003.jpg)
![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/004.jpg)
![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/005.jpg)
![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/006.jpg)

O projeto, sem fins comerciais, esta aberto para você construir o seu e, se puder, colaborar na melhoria desse desenvolvimento.

Baseado no hardware: Clone **Purple** da Raspberry Pi PICO RP2040, Display ILI9341 + XPT2046 (Touchscreen), Analógico direcional de 2 eixos e Optoacoplador.
Firmware CircuitPython
Imagens BMP dos overlays na pasta bmp nomeados com 3 digitos.
Botão de pressão do joystick para modo de Pausa e para novo overlay (3 digitos e Enter)

[![Veja o tutorial no YouTube](https://img.youtube.com/vi/SEU_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=SEU_VIDEO_ID)

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



**Lista de melhorias planejadas:**
- Alimentação com pilhas ou bateria recarregável
- Placa PCB
- Gabinete 3D
- Acionamento do direcional com alavanca, disco rotativo intercambiáveis
- Saída USB para emuladores
- Listagem de títulos para seleção do overlay
