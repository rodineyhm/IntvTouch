# IntvTouch
**Protótipo controle para console Intellivision com direcional analógico e overlay na tela touch**

![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/001.jpg)
![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/002.jpg)
![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/003.jpg)
![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/004.jpg)
![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/005.jpg)
![ScreenShot](https://raw.githubusercontent.com/rodineyhm/IntvTouch/main/Pictures/006.jpg)

Este é um projeto não comercial, disponível para você construir o seu e, se puder, colaborar na melhoria desse desenvolvimento.

Baseado no hardware: Clone **Purple** da Raspberry Pi PICO RP2040, Display ILI9341 + XPT2046 (Touchscreen), Analógico direcional de 2 eixos e Optoacoplador.
Firmware CircuitPython
Imagens BMP dos overlays na pasta bmp nomeados com 3 digitos.
Botão de pressão do joystick para modo de Pausa e para novo overlay (3 digitos e Enter)

[![Veja o tutorial no YouTube](https://img.youtube.com/vi/SEU_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=SEU_VIDEO_ID)

Resumo das conexões:

**RP2040 - Purple**
0-GP0 
1-GP1 => 220R-OptoA-IN2
2-GP2 => 220R-OptoA-IN3
3-GP3 => 220R-OptoA-IN4
4-GP4 => 220R-OptoB-IN1
G-GND
5-GP5 => 220R-OptoB-IN2
6-GP6 => Display-SCK
7-GP7 => Display-SDI(MOSI)
8-GP8 => Display-Touch T_DO
9-GP9 => 220R-OptoA-IN1
10-GP10 => Display-Touch T_CLK
11-GP11 => Display-Touch T_DIN
12-GP12 => Display-Touch T_CS
G-GND
13-GP13 => 220R-OptoB-IN3
14-GP14 => 220R-OptoB-IN4
15-GP15 => Display-D/C
16-GP16 => Display-RESET
17-GP17 => Display-CS

O-VBUS
O-VN
O-GND
O-3V3_EN
O-3V3 => 
O-GND
RUN-RUN
A3-GP29_A3
A2-GP28_A2
A1-GP27_A1 <= Joystick VRY
A0-GP26_A0 <= Joystick VRX
AG-AGND
25-GP25
24-GP24 <= Joystick SW
23-GP23
22-GP22
21-GP21
20-GP20 <= SW_B03
19-GP19 <= SW_B02
18-GP18 <= SW_B01

**Display ILI9341 + XPT2046** (JC2432S024R 2,4" resistor touch 240x320 RGB)
Display-VCC <= 3V3
Display-GND <= GND
Display-CS <= GP17
Display-RESET <= GP16
Display-D/C <= GP15
Display-SDI(MOSI) <= GP7
Display-SCK <= GP6
Display-LED <= 3V3
Display-SDO(MISO) = Sem Uso
Display-Touch T_CLK <= GP10
Display-Touch T_CS <= GP12
Display-Touch T_DIN <= GP11
Display-Touch T_DO <= GP8
Display-Touch T_IRQ = Sem Uso

**Joystick** (2 eixos divisor resistivo 10K + chave pressão)
Joystick GND <= GND
Joystick +5V <= 3V3
Joystick VRX => GP26-A0
Joystick VRY => GP27-A1
Joystick SW => GP24

**Botões**
B01(x2) => GP18
B02 => GP19
B03 => GP20
<= GND
------
1    1
2    3
E----D

**Optoacoplador** (8x EL817 ou 2x TLP281-4 + 8x 220R)
A-NC = Sem uso
OptoA-IN1 <= 220R-GP9
OptoA-IN2 <= 220R-GP1
OptoA-IN3 <= 220R-GP2
OptoA-IN4 <= 220R-GP3
OptoA-GND <= GND
OptoA-OUT1 => DB1
OptoA-OUT2 => DB2
OptoA-OUT3 => DB3
OptoA-OUT4 => DB4
OptoA-HVCC = Sem uso
OptoA-HGND => DB5
OptoB-NC = Sem uso
OptoB-IN1 <= 220R-GP4
OptoB-IN2 <= 220R-GP5
OptoB-IN3 <= 220R-GP13
OptoB-IN4 <= 220R-GP14
OptoB-GND <= GND
OptoB-OUT1 => DB6
OptoB-OUT2 => DB7
OptoB-OUT3 => DB8
OptoB-OUT4 => DB9
OptoB-HVCC = Sem uso
OptoB-HGND => DB5

**DB9** (Intellivision2 ou Sears, Intellivision1 com adaptador)
DB1 <= OptoA-OUT1
DB2 <=Opto A-OUT3
DB3 <=Opto A-OUT4
DB4 <= OptoA-OUT5
DB5 => OptoA-HGND/OptoB-HGND
DB6 <= OptoB-OUT1
DB7 <=Opto B-OUT2
DB8 <= OptoB-OUT3
DB9 <= OptoB-OUT4

Conector Intv2 fêmea visto de frente:
 -----------
  5 4 3 2 1
   9 8 7 6
   -------

Conector Intv1 para adaptação:
verde---------------branco
    5 4 3 2 1 9 8 7 6 

Conector Intv Flashback:
A definir

Acionamento:
				Pino DB								
		Seq		1	2	3	4	5	6	7	8	9
Disco		1	1	0	1	0	0	T	0	0	0	0
		2	2	0	1	0	0	T	0	0	0	1
		3	3	0	1	1	0	T	0	0	0	1
		4	4	0	1	1	0	T	0	0	0	0
		5	5	0	0	1	0	T	0	0	0	0
		6	6	0	0	1	0	T	0	0	0	1
		7	7	0	0	1	1	T	0	0	0	1
		8	8	0	0	1	1	T	0	0	0	0
		9	9	0	0	0	1	T	0	0	0	0
		10	10	0	0	0	1	T	0	0	0	1
		11	11	1	0	0	1	T	0	0	0	1
		12	12	1	0	0	1	T	0	0	0	0
		13	13	1	0	0	0	T	0	0	0	0
		14	14	1	0	0	0	T	0	0	0	1
		15	15	1	1	0	0	T	0	0	0	1
		16	16	1	1	0	0	T	0	0	0	0
Teclado		0	17	1	0	0	0	T	0	1	0	0
		1	18	0	0	0	1	T	1	0	0	0
		2	19	0	0	0	1	T	0	1	0	0
		3	20	0	0	0	1	T	0	0	1	0
		4	21	0	0	1	0	T	1	0	0	0
		5	22	0	0	1	0	T	0	1	0	0
		6	23	0	0	1	0	T	0	0	1	0
		7	24	0	1	0	0	T	1	0	0	0
		8	25	0	1	0	0	T	0	1	0	0
		9	26	0	1	0	0	T	0	0	1	0
		C	27	1	0	0	0	T	1	0	0	0
		E	28	1	0	0	0	T	0	0	1	0
Botão		1	29	0	0	0	0	T	1	0	1	0
		2	30	0	0	0	0	T	0	1	1	0
		3	31	0	0	0	0	T	1	1	0	0
Pause			91	0	1	0	1	T	1	0	1	0



**Lista de melhorias planejadas:**
- Alimentação com pilhas ou bateria recarregável
- Placa PCB
- Gabinete 3D
- Acionamento do direcional com alavanca, disco rotativo intercambiáveis
- Saída USB para emuladores
- Listagem de títulos para seleção do overlay
