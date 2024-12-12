#        intvTouch
#    github.com/rodineyhm    
versao = "Protótipo Versão 0.12"

import board, time, analogio, busio
from digitalio import DigitalInOut, Direction, Pull
import math, displayio #, terminalio, vectorio
#from adafruit_display_shapes.circle import Circle
#from adafruit_display_shapes.line import Line
import adafruit_ili9341
from cpy_xpt2046 import Touch
from os import stat

from adafruit_display_text import label
import terminalio

# Configuração do teclado
KEYBOARD_LAYOUT = [
    "123",
    "456",
    "789",
    "C0E"
]
# Dimensões da tela e teclado
TFT_WIDTH = 240  # Largura da tela após rotação
TFT_HEIGHT = 320  # Altura da tela após rotação
NUM_ROWS = len(KEYBOARD_LAYOUT)
NUM_COLS = max(len(row) for row in KEYBOARD_LAYOUT)
# Ajustando o cálculo da largura e altura das teclas
KEY_WIDTH = TFT_WIDTH // NUM_COLS  # Calculando largura das teclas
KEY_HEIGHT = TFT_HEIGHT // NUM_ROWS  # Calculando altura das teclas
# Limites do touch
touch_x_min = 64
touch_x_max = 1847
touch_y_min = 148
touch_y_max = 2047
# Ajustes de calibração - altere conforme necessário
CALIBRATION_OFFSET_X = -5  # Deslocamento em X
CALIBRATION_OFFSET_Y = 50  # Deslocamento em Y
CALIBRATION_SCALE_X = 1.0  # Escala em X
CALIBRATION_SCALE_Y = 1.05  # Escala em Y (ajuste para corrigir alongamento/compressão)

# Configuração da conexão do display
tft_cs  = board.GP17
tft_res = board.GP16
tft_dc  = board.GP15
tft_spi_mosi = board.GP7
tft_spi_clk = board.GP6
touch_spi_clk = board.GP10
touch_cs = board.GP12
touch_spi_mosi = board.GP11
touch_spi_miso = board.GP8

# Inicialização de SPI e display
displayio.release_displays()
touch_spi = busio.SPI(touch_spi_clk, MOSI=touch_spi_mosi, MISO=touch_spi_miso)
touch = Touch(touch_spi, cs=touch_cs,
              x_min=touch_x_min, x_max=touch_x_max,
              y_min=touch_y_min, y_max=touch_y_max)
tft_spi = busio.SPI(tft_spi_clk, MOSI=tft_spi_mosi)
display_bus = displayio.FourWire(tft_spi, command=tft_dc, chip_select=tft_cs, reset=tft_res)
# Inicialização do display com rotação
display = adafruit_ili9341.ILI9341(display_bus, width=TFT_HEIGHT, height=TFT_WIDTH)
display.rotation = 90  # Garante que a tela seja rotacionada corretamente
scrWidth = display.width
scrHeight = display.height

#ledOnBoard = board.GP25
ledOnBoard = DigitalInOut(board.LED)
ledOnBoard.direction = Direction.OUTPUT

# Configuração dos botões
b01 = DigitalInOut(board.GP18)
b01.direction = Direction.INPUT
b01.pull = Pull.UP
b02 = DigitalInOut(board.GP19)
b02.direction = Direction.INPUT
b02.pull = Pull.UP
b03 = DigitalInOut(board.GP20)
b03.direction = Direction.INPUT
b03.pull = Pull.UP

# Configuração do Joystick
hJoy = analogio.AnalogIn(board.GP26)
vJoy = analogio.AnalogIn(board.GP27)
bJoy = DigitalInOut(board.GP24)
bJoy.direction = Direction.INPUT
bJoy.pull = Pull.UP #Pull.DOWN

# Configuração dos pinos GPIO para os octoacopladores
pinosDB = [
    DigitalInOut(board.GP9),
    DigitalInOut(board.GP1),
    DigitalInOut(board.GP2),
    DigitalInOut(board.GP3),
    DigitalInOut(board.GP4),
    DigitalInOut(board.GP5),
    DigitalInOut(board.GP13),
    DigitalInOut(board.GP14),
]

# Configura todos os pinos como saída
for pino in pinosDB:
    pino.direction = Direction.OUTPUT
    pino.value = 0  # Inicializa os pinos em nível baixo (desativa os octoacopladores)  
 
# Mapeamento de números para combinações de estados
combinacoesDB = {
    #número/PinosDB: 1 2 3 4 _ 6 7 8 9
    0: [0, 0, 0, 0, 0, 0, 0, 0],
    1: [0, 1, 0, 0, 0, 0, 0, 0],
    2: [0, 1, 0, 0, 0, 0, 0, 1],
    3: [0, 1, 1, 0, 0, 0, 0, 1],
    4: [0, 1, 1, 0, 0, 0, 0, 0],
    5: [0, 0, 1, 0, 0, 0, 0, 0],
    6: [0, 0, 1, 0, 0, 0, 0, 1],
    7: [0, 0, 1, 1, 0, 0, 0, 1],
    8: [0, 0, 1, 1, 0, 0, 0, 0],
    9: [0, 0, 0, 1, 0, 0, 0, 0],
    10: [0, 0, 0, 1, 0, 0, 0, 1],
    11: [1, 0, 0, 1, 0, 0, 0, 1],
    12: [1, 0, 0, 1, 0, 0, 0, 0],
    13: [1, 0, 0, 0, 0, 0, 0, 0],
    14: [1, 0, 0, 0, 0, 0, 0, 1],
    15: [1, 1, 0, 0, 0, 0, 0, 1],
    16: [1, 1, 0, 0, 0, 0, 0, 0],
    17: [1, 0, 0, 0, 0, 1, 0, 0],
    18: [0, 0, 0, 1, 1, 0, 0, 0],
    19: [0, 0, 0, 1, 0, 1, 0, 0],
    20: [0, 0, 0, 1, 0, 0, 1, 0],
    21: [0, 0, 1, 0, 1, 0, 0, 0],
    22: [0, 0, 1, 0, 0, 1, 0, 0],
    23: [0, 0, 1, 0, 0, 0, 1, 0],
    24: [0, 1, 0, 0, 1, 0, 0, 0],
    25: [0, 1, 0, 0, 0, 1, 0, 0],
    26: [0, 1, 0, 0, 0, 0, 1, 0],
    27: [1, 0, 0, 0, 1, 0, 0, 0],
    28: [1, 0, 0, 0, 0, 0, 1, 0],
    29: [0, 0, 0, 0, 1, 0, 1, 0],
    30: [0, 0, 0, 0, 0, 1, 1, 0],
    31: [0, 0, 0, 0, 1, 1, 0, 0],
    91: [0, 1, 0, 1, 1, 0, 1, 0],
}

# Controla saídas DB
def controlar_saidasDB(saidaDB_1B,saidaDB_3D,saidaDB_2T):
    saidas_simultaneas = [saidaDB_1B,saidaDB_3D,saidaDB_2T]
    saidas_resultado = [max(combinacoesDB[k][i] for k in saidas_simultaneas) for i in range(len(combinacoesDB[0]))]    
    for i, estado in enumerate(saidas_resultado):
        if estado == 1:
            if not pinosDB[i].value:  # Apenas altere se necessário
                pinosDB[i].value = estado  # Atualiza o estado de cada pino
        else: #estado == 0
            if pinosDB[i].value:
                pinosDB[i].value = estado
    #time.sleep(0.01)  # 10 ms 

# Direção do Joystick (1 a 16)
def calcular_direcao(x, y):
    # Calcula o ângulo ajustado de 0 a 360 começando do topo
    if x == 0 and y == 0:
        return 0  # Ângulo indefinido, retorna 0 como padrão
    angulo_radianos = math.atan2(y, x)
    angulo_graus = (90 - math.degrees(angulo_radianos)) % 360        
    # Determina a Direção (1 a 16)
    direcao_calculada = int((angulo_graus // 22.5) + 1)
    return direcao_calculada   

def get_pressed_key(touch_x, touch_y):
    #Retorna a tecla correspondente ao toque, levando em consideração a rotação da tela.
    # Ajustando a leitura após rotação
    col = touch_x // KEY_WIDTH
    row = touch_y // KEY_HEIGHT
    # Garantir que o toque está dentro dos limites das teclas
    if 0 <= row < NUM_ROWS and 0 <= col < NUM_COLS:
        return KEYBOARD_LAYOUT[row][col]
    return None

# Função de validação de toque
def validTouch():
    xy = touch.raw_touch()    
    if xy is None:
        return None    
    normailzedX, normailzedY = touch.normalize(*xy)
    # Troca X e Y (corrigir orientação invertida)
    normailzedX, normailzedY = normailzedY, normailzedX
    # Aplicar ajuste baseado na rotação do display
    if display.rotation == 90:
        normailzedX, normailzedY = normailzedY, scrWidth - 1 - normailzedX
    elif display.rotation == 180:
        normailzedX, normailzedY = scrWidth - 1 - normailzedX, scrHeight - 1 - normailzedY
    elif display.rotation == 270:
        normailzedX, normailzedY = scrHeight - 1 - normailzedY, normailzedX
    # Aplicar calibração de escala e deslocamento
    normailzedX = int((normailzedX + CALIBRATION_OFFSET_X) * CALIBRATION_SCALE_X)
    normailzedY = int((normailzedY + CALIBRATION_OFFSET_Y) * CALIBRATION_SCALE_Y)
    # Garantir que as coordenadas estejam dentro dos limites da tela
    if (normailzedX < 0 or normailzedX >= scrWidth
            or normailzedY < 0 or normailzedY >= scrHeight):
        return None        
    return (normailzedX, normailzedY)

# Grupo principal
tela = displayio.Group()
display.show(tela)

#Atualiza Overlay
def carrega_overlay(overlay):
    imagem = f"/bmp/{overlay}.bmp"
    try:
        if not stat(imagem):  # Verifica se o arquivo existe
            draw_label(f"Erro Arquivo {imagem} não encontrado.")
            overlay = "000"
        else:
            bitmap = displayio.OnDiskBitmap(imagem)
            face = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
            tela.append(face)
    except:
        draw_label(f"Erro Arquivo {imagem} não encontrado.")
        overlay = "000"

# Draw a label
text_atual = None  # Armazenará o grupo de texto atual
def draw_label(text):
    global text_atual  # Permite acessar e modificar o texto atual
    if text_atual:
        tela.remove(text_atual)  # Remove o texto anterior da tela
    # Cria o novo texto
    text_group = displayio.Group(scale=1, x=11, y=11)
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
    text_group.append(text_area)
    tela.append(text_group)  # Adiciona o texto à tela
    text_atual = text_group  # Atualiza o texto atual    

#Posição Direcional
def posicao_direcional():
    #Posição angular Joystick
    hVal=hJoy.value #hVal=hJoy.read_u16()
    hCal=int(-.00306*hVal+100.766) #* -1 Caso precise inverter os eixos
    vVal=vJoy.value    
    vCal=int(.00306*vVal-100.766) #* -1 Caso precise inverter os eixos
    mag=math.sqrt(hCal**2+vCal**2)
    if mag <= 6: #Margem do centro a desconsiderar
        hCal=0
        vCal=0
    posicao = calcular_direcao(hCal, vCal)
    return posicao

#Apresenta a splash
overlay = "sphash"
carrega_overlay(overlay)
draw_label(versao)
time.sleep(5.00)
   
#Carrega overlay padrão
overlay = "000"
carrega_overlay(overlay)

pause = 0
overlay_novo = ""
saidaDB_1B = 0
saidaDB_2T = 0
saidaDB_3D = 0
while True: 
    bVal = bJoy.value
    if bVal == 0: #Pressionado
        if pause == 0:
            pause = 1
            ledOnBoard.value = True #Acende
            draw_label("Em PAUSA")       
            controlar_saidasDB(91,0,0)
        else:
            pause = 0
            ledOnBoard.value = False #Apaga
            draw_label("")
        time.sleep(0.30)
    elif b01.value == 0:
        saidaDB_1B = 29
    elif b02.value == 0:
        saidaDB_1B = 30
    elif b03.value == 0:
        saidaDB_1B = 31
    else:
        saidaDB_1B = 0

    xy = validTouch()
    if xy:
        touchedX, touchedY = xy
        key = get_pressed_key(touchedX, touchedY)
        if key:
            if pause == 0:
                if key == "C":
                    saidaDB_2T = 27
                elif key == "E":
                    saidaDB_2T = 28
                if key <= "9":
                    saidaDB_2T = 17 + int(key)
            else:
                if key == "C":
                    overlay_novo = ""
                elif key == "E" and len(overlay_novo) == 3:
                    carrega_overlay(overlay_novo)
                else:              
                    if len(overlay_novo) >= 3:
                        overlay_novo = overlay_novo[1:]
                    overlay_novo = overlay_novo + key
                draw_label(f"Entrando novo Overlay: {overlay_novo}")           
            time.sleep(0.10)
    else:
        saidaDB_2T = 0
            
    direcao = posicao_direcional()    
    if direcao != 0:
        saidaDB_3D = direcao
    else:
        saidaDB_3D = 0

    controlar_saidasDB(saidaDB_1B,saidaDB_2T,saidaDB_3D)
    #time.sleep(0.02)
