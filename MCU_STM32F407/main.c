#include "stm32f4xx.h"
#include "system_timetick.h"
#include "string.h"
#define		BUFF_SIZE			30

// Khai báo chân điều khiển động cơ
#define DIR_PIN_U GPIO_Pin_2
#define DIR_PORT_U GPIOA
#define STEP_PIN_U GPIO_Pin_3
#define STEP_PORT_U GPIOA

#define DIR_PIN_R GPIO_Pin_4
#define DIR_PORT_R GPIOA
#define STEP_PIN_R GPIO_Pin_5
#define STEP_PORT_R GPIOA

#define DIR_PIN_F GPIO_Pin_6
#define DIR_PORT_F GPIOA
#define STEP_PIN_F GPIO_Pin_7
#define STEP_PORT_F GPIOA

#define DIR_PIN_B GPIO_Pin_9
#define DIR_PORT_B GPIOD
#define STEP_PIN_B GPIO_Pin_10
#define STEP_PORT_B GPIOD

#define DIR_PIN_L GPIO_Pin_11
#define DIR_PORT_L GPIOD
#define STEP_PIN_L GPIO_Pin_12
#define STEP_PORT_L GPIOD

#define DIR_PIN_D GPIO_Pin_13
#define DIR_PORT_D GPIOD
#define STEP_PIN_D GPIO_Pin_14
#define STEP_PORT_D GPIOD

uint8_t 	rxbuff[BUFF_SIZE];
uint8_t txbuff[2];
//uint8_t 	a[4*BUFF_SIZE];
char a[100];
//#define BUFF_SIZE 30
//uint8_t 	rxbuff[BUFF_SIZE];
//uint8_t 	a[BUFF_SIZE];
uint16_t	index = 0;
uint16_t 	rcv_flag = 0;


void init_main(void);
void Delay(int t);
void delay_us(uint16_t period);
void delay_01ms(uint16_t period);

void stepU (int steps, uint8_t direction, uint16_t delay);
void stepR (int steps, uint8_t direction, uint16_t delay);
void stepF (int steps, uint8_t direction, uint16_t delay);
void stepD (int steps, uint8_t direction, uint16_t delay);
void stepL (int steps, uint8_t direction, uint16_t delay);
void stepB (int steps, uint8_t direction, uint16_t delay);
void step();
void sendto_PC();

void Delay(int t){
	int i;
	for (i=0; i<t; i++);
}

void stepU (int steps, uint8_t direction, uint16_t delay)
{
  int x;
  if (direction == 1) {
    GPIO_WriteBit(DIR_PORT_U, DIR_PIN_U, Bit_SET);} // theo chieu kim dong ho
  else if (direction == 0) {
    GPIO_WriteBit(DIR_PORT_U, DIR_PIN_U, Bit_RESET);} // nguoc chieu kim dong ho
  for(x=0; x<steps; x=x+1)
  {
    GPIO_WriteBit(STEP_PORT_U, STEP_PIN_U, Bit_SET);
    delay_us(delay);
    GPIO_WriteBit(STEP_PORT_U, STEP_PIN_U, Bit_RESET);
    delay_us(delay);
  }
}

void stepR (int steps, uint8_t direction, uint16_t delay)
{
  int x;
  if (direction == 1) {
    GPIO_WriteBit(DIR_PORT_R, DIR_PIN_R, Bit_SET);} // theo chieu kim dong ho
  else if (direction == 0) {
    GPIO_WriteBit(DIR_PORT_R, DIR_PIN_R, Bit_RESET);} // nguoc chieu kim dong ho
  for(x=0; x<steps; x=x+1)
  {
    GPIO_WriteBit(STEP_PORT_R, STEP_PIN_R, Bit_SET);
    delay_us(delay);
    GPIO_WriteBit(STEP_PORT_R, STEP_PIN_R, Bit_RESET);
    delay_us(delay);
  }
}

void stepF (int steps, uint8_t direction, uint16_t delay)
{
  int x;
  if (direction == 1) {
    GPIO_WriteBit(DIR_PORT_F, DIR_PIN_F, Bit_SET);} // theo chieu kim dong ho
  else if (direction == 0) {
    GPIO_WriteBit(DIR_PORT_F, DIR_PIN_F, Bit_RESET);} // nguoc chieu kim dong ho
  for(x=0; x<steps; x=x+1)
  {
    GPIO_WriteBit(STEP_PORT_F, STEP_PIN_F, Bit_SET);
    delay_us(delay);
    GPIO_WriteBit(STEP_PORT_F, STEP_PIN_F, Bit_RESET);
    delay_us(delay);
  }
}

void stepB (int steps, uint8_t direction, uint16_t delay)
{
  int x;
  if (direction == 1) {
    GPIO_WriteBit(DIR_PORT_B, DIR_PIN_B, Bit_SET);} // theo chieu kim dong ho
  else if (direction == 0) {
    GPIO_WriteBit(DIR_PORT_B, DIR_PIN_B, Bit_RESET);} // nguoc chieu kim dong ho
  for(x=0; x<steps; x=x+1)
  {
    GPIO_WriteBit(STEP_PORT_B, STEP_PIN_B, Bit_SET);
    delay_us(delay);
    GPIO_WriteBit(STEP_PORT_B, STEP_PIN_B, Bit_RESET);
    delay_us(delay);
  }
}

void stepL (int steps, uint8_t direction, uint16_t delay)
{
  int x;
  if (direction == 1) {
    GPIO_WriteBit(DIR_PORT_L, DIR_PIN_L, Bit_SET);} // theo chieu kim dong ho
  else if (direction == 0) {
    GPIO_WriteBit(DIR_PORT_L, DIR_PIN_L, Bit_RESET);} // nguoc chieu kim dong ho
  for(x=0; x<steps; x=x+1)
  {
    GPIO_WriteBit(STEP_PORT_L, STEP_PIN_L, Bit_SET);
    delay_us(delay);
    GPIO_WriteBit(STEP_PORT_L, STEP_PIN_L, Bit_RESET);
    delay_us(delay);
  }
}

void stepD (int steps, uint8_t direction, uint16_t delay)
{
  int x;
  if (direction == 1) {
    GPIO_WriteBit(DIR_PORT_D, DIR_PIN_D, Bit_SET);} // theo chieu kim dong ho
  else if (direction == 0) {
    GPIO_WriteBit(DIR_PORT_D, DIR_PIN_D, Bit_RESET);} // nguoc chieu kim dong ho
  for(x=0; x<steps; x=x+1)
  {
    GPIO_WriteBit(STEP_PORT_D, STEP_PIN_D, Bit_SET);
    delay_us(delay);
    GPIO_WriteBit(STEP_PORT_D, STEP_PIN_D, Bit_RESET);
    delay_us(delay);
  }
}

void delay_us(uint16_t period){

  	RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM6, ENABLE);
  	TIM6->PSC = 83;		// clk = SystemCoreClock /2/(PSC+1) = 1MHz
  	TIM6->ARR = period-1;
  	TIM6->CNT = 0;
  	TIM6->EGR = 1;		// update registers;

  	TIM6->SR  = 0;		// clear overflow flag
  	TIM6->CR1 = 1;		// enable Timer6

  	while (!TIM6->SR);
    
  	TIM6->CR1 = 0;		// stop Timer6
  	RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM6, DISABLE);
}

void delay_01ms(uint16_t period){

  	RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM6, ENABLE);
  	TIM6->PSC = 8399;		// clk = SystemCoreClock /2 /(PSC+1) = 10KHz
  	TIM6->ARR = period-1;
  	TIM6->CNT = 0;
  	TIM6->EGR = 1;		// update registers;

  	TIM6->SR  = 0;		// clear overflow flag
  	TIM6->CR1 = 1;		// enable Timer6

  	while (!TIM6->SR);
    
  	TIM6->CR1 = 0;		// stop Timer6
  	RCC_APB1PeriphClockCmd(RCC_APB1Periph_TIM6, DISABLE);
}



void step()
{
	for (int i = 0; i<50; i++)
				{
					switch (a[i])
					{
						case 'U':
							stepU(100, 0, 500); // delay 500us
							delay_01ms(5000); // delay 500ms
							break;
						case 'u': // U'
							stepU(100, 1, 500);
							delay_01ms(5000);
							break;
						case 'Z': // U2
							//stepU(200, 0, 500);
							stepU(200, 0, 500);
							delay_01ms(5000);
							break;
						
						case 'R':
							stepR(100, 0, 500);
							delay_01ms(5000);
							break;
						case 'r': // R'
							stepR(100, 1, 500);
							delay_01ms(5000);
							break;
						case 'X': // R2
							//stepR(200, 0, 500);
							stepR(200, 0, 500);
							delay_01ms(5000);
							break;
						
						case 'F':
							stepF(100, 0, 500);
							delay_01ms(5000);
							break;
						case 'f': // U'
							stepF(100, 1, 500);
							delay_01ms(5000);
							break;
						case 'C': // U2
							//stepF(200, 0, 500);
							stepF(200, 0, 500);
							delay_01ms(5000);
							break;
						
						case 'B':
							stepB(100, 0, 500);
							delay_01ms(5000);
							break;
						case 'b': // R'
							stepB(100, 1, 500);
							delay_01ms(5000);
							break;
						case 'V': // R2
							//stepB(200, 0, 500);
							stepB(200, 0, 500);
							delay_01ms(5000);
							break;
						
						case 'L':
							stepL(100, 0, 500);
							delay_01ms(5000);
							break;
						case 'l': // U'
							stepL(100, 1, 500);
							delay_01ms(5000);
							break;
						case 'N': // U2
							//stepL(200, 0, 500);
							stepL(200, 0, 500);
							delay_01ms(5000);
							break;
						
						case 'D':
							stepD(100, 0, 500);
							delay_01ms(5000);
							break;
						case 'd': // R'
							stepD(100, 1, 500);
							delay_01ms(5000);
							break;
						case 'M': // R2
							//stepD(200, 0, 500);
							stepD(200, 0, 500);
							delay_01ms(5000);
							break;
					}
				}
}
int main(void)
{
	/* Enable SysTick at 10ms interrupt */
	SysTick_Config(SystemCoreClock/100);

	init_main();

	GPIO_InitTypeDef  GPIO_InitStructure;
	
	/* Enable SysTick at 10ms interrupt */
	//SysTick_Config(SystemCoreClock/100);
	
	/* GPIOD Peripheral clock enable */
  RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOA, ENABLE); 
	RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOD, ENABLE);

  /* Configure PD12, PD13 in output pushpull mode */
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_2 | GPIO_Pin_3 | GPIO_Pin_4 | GPIO_Pin_5 | GPIO_Pin_6 | GPIO_Pin_7;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_OUT;
  GPIO_InitStructure.GPIO_OType = GPIO_OType_PP; 
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_100MHz;
  GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_NOPULL;
  GPIO_Init(GPIOA, &GPIO_InitStructure);
  
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_9 | GPIO_Pin_10 | GPIO_Pin_11 | GPIO_Pin_12 | GPIO_Pin_13 | GPIO_Pin_14;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_OUT;
  GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_100MHz;
  GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_NOPULL;
  GPIO_Init(GPIOD, &GPIO_InitStructure);


	while(1){
//		stepU(200, 0, 500);
//		delay_01ms(5000);
//		stepR(200, 1, 500);
//		delay_01ms(5000);
//		stepF(200, 1, 500);
//		delay_01ms(5000);
//		stepD(200, 1, 500);
//		delay_01ms(5000);
//		stepL(200, 1, 500);
//		delay_01ms(5000);
//		stepB(200, 1, 500);
//		delay_01ms(5000);

	}
	
}

void init_main(void)
{
  GPIO_InitTypeDef 	GPIO_InitStructure; 
	USART_InitTypeDef USART_InitStructure;  
	DMA_InitTypeDef   DMA_InitStructure;
  NVIC_InitTypeDef  NVIC_InitStructure;	
   
  /* Enable GPIO clock */
  RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOA, ENABLE);
  /* Enable UART clock */
  RCC_APB1PeriphClockCmd(RCC_APB1Periph_UART4, ENABLE);
	/* Enable DMA1 clock */
  RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_DMA1, ENABLE);

  /* Connect UART4 pins to AF2 */  
  GPIO_PinAFConfig(GPIOA, GPIO_PinSource0, GPIO_AF_UART4);
  GPIO_PinAFConfig(GPIOA, GPIO_PinSource1, GPIO_AF_UART4); 

  /* GPIO Configuration for UART4 Tx */
  GPIO_InitStructure.GPIO_Pin   = GPIO_Pin_0;
  GPIO_InitStructure.GPIO_Mode  = GPIO_Mode_AF;
  GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;
  GPIO_InitStructure.GPIO_PuPd  = GPIO_PuPd_UP;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_Init(GPIOA, &GPIO_InitStructure);

  /* GPIO Configuration for USART Rx */
  GPIO_InitStructure.GPIO_Pin   = GPIO_Pin_1;
  GPIO_InitStructure.GPIO_Mode  = GPIO_Mode_AF;
  GPIO_Init(GPIOA, &GPIO_InitStructure);
       
  /* USARTx configured as follow:
		- BaudRate = 115200 baud  
    - Word Length = 8 Bits
    - One Stop Bit
    - No parity
    - Hardware flow control disabled (RTS and CTS signals)
    - Receive and transmit enabled
  */
  USART_InitStructure.USART_BaudRate = 115200;
  USART_InitStructure.USART_WordLength = USART_WordLength_8b;
  USART_InitStructure.USART_StopBits = USART_StopBits_1;
  USART_InitStructure.USART_Parity = USART_Parity_No;
  USART_InitStructure.USART_HardwareFlowControl = USART_HardwareFlowControl_None;
  USART_InitStructure.USART_Mode = USART_Mode_Rx | USART_Mode_Tx;
  USART_Init(UART4, &USART_InitStructure);

  /* Enable USART */
  USART_Cmd(UART4, ENABLE);
	/* Enable UART4 DMA */
  USART_DMACmd(UART4, USART_DMAReq_Rx, ENABLE);
  USART_DMACmd(UART4,USART_DMAReq_Tx,ENABLE);
  
	/* DMA1 Stream2 Channel4 for USART4 Rx configuration */			
  DMA_InitStructure.DMA_Channel = DMA_Channel_4;  
  DMA_InitStructure.DMA_PeripheralBaseAddr = (uint32_t)&UART4->DR;
  DMA_InitStructure.DMA_Memory0BaseAddr = (uint32_t)rxbuff;
  DMA_InitStructure.DMA_DIR = DMA_DIR_PeripheralToMemory;
  DMA_InitStructure.DMA_BufferSize = BUFF_SIZE;
  DMA_InitStructure.DMA_PeripheralInc = DMA_PeripheralInc_Disable;
  DMA_InitStructure.DMA_MemoryInc = DMA_MemoryInc_Enable;
  DMA_InitStructure.DMA_PeripheralDataSize = DMA_PeripheralDataSize_Byte;
  DMA_InitStructure.DMA_MemoryDataSize = DMA_MemoryDataSize_Byte;
  DMA_InitStructure.DMA_Mode = DMA_Mode_Normal;//DMA_Mode_Circular;
  DMA_InitStructure.DMA_Priority = DMA_Priority_High;
  DMA_InitStructure.DMA_FIFOMode = DMA_FIFOMode_Disable;         
  DMA_InitStructure.DMA_FIFOThreshold = DMA_FIFOThreshold_HalfFull;
  DMA_InitStructure.DMA_MemoryBurst = DMA_MemoryBurst_Single;
  DMA_InitStructure.DMA_PeripheralBurst = DMA_PeripheralBurst_Single;
  DMA_Init(DMA1_Stream2, &DMA_InitStructure);
  DMA_Cmd(DMA1_Stream2, ENABLE);
  
  
  DMA_DeInit(DMA1_Stream4);
	// Cau hinh DMA UART4 Tx: DMA1, Channel4, Stream 4	
	DMA_InitStructure.DMA_Channel = DMA_Channel_4;  
	DMA_InitStructure.DMA_PeripheralBaseAddr = (uint32_t)&(UART4->DR);
	DMA_InitStructure.DMA_Memory0BaseAddr = (uint32_t)txbuff;
	DMA_InitStructure.DMA_DIR = DMA_DIR_MemoryToPeripheral;
	DMA_InitStructure.DMA_BufferSize = BUFF_SIZE;
	DMA_InitStructure.DMA_PeripheralInc = DMA_PeripheralInc_Disable;
	DMA_InitStructure.DMA_MemoryInc = DMA_MemoryInc_Enable;
	DMA_InitStructure.DMA_PeripheralDataSize = DMA_PeripheralDataSize_Byte;
	DMA_InitStructure.DMA_MemoryDataSize = DMA_MemoryDataSize_Byte;
	DMA_InitStructure.DMA_Mode = DMA_Mode_Normal;
	DMA_InitStructure.DMA_Priority = DMA_Priority_High;
	DMA_InitStructure.DMA_FIFOMode = DMA_FIFOMode_Disable;         
	DMA_InitStructure.DMA_FIFOThreshold = DMA_FIFOThreshold_HalfFull;
	DMA_InitStructure.DMA_MemoryBurst = DMA_MemoryBurst_Single;
	DMA_InitStructure.DMA_PeripheralBurst = DMA_PeripheralBurst_Single;
	DMA_Init(DMA1_Stream4, &DMA_InitStructure);
	DMA_Cmd(DMA1_Stream4, ENABLE);
	
	/* Enable DMA Interrupt to the highest priority */
  NVIC_InitStructure.NVIC_IRQChannel = DMA1_Stream2_IRQn;
  NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 0;
  NVIC_InitStructure.NVIC_IRQChannelSubPriority = 0;
  NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;
  NVIC_Init(&NVIC_InitStructure);

  /* Transfer complete interrupt mask */
  DMA_ITConfig(DMA1_Stream2, DMA_IT_TC, ENABLE);
}

void sendto_PC(void)
{
	txbuff[0] = 'e';
	txbuff[1] = '0';
	DMA_ClearFlag(DMA1_Stream4, DMA_FLAG_TCIF4);
	DMA1_Stream4->NDTR = 2; // BUFF_SIZE_TX = 2
	DMA_Cmd(DMA1_Stream4, ENABLE);
}

void DMA1_Stream2_IRQHandler(void)
{
  uint16_t i;

  /* Clear the DMA1_Stream2 TCIF2 pending bit */
  DMA_ClearITPendingBit(DMA1_Stream2, DMA_IT_TCIF2);

//  for(i=0; i<BUFF_SIZE; i++)
//    a[index + i] = rxbuff[i];
//	index = index + BUFF_SIZE;
//  rcv_flag = 1;
	//sangled();
	for(uint8_t i=0; i<BUFF_SIZE; i++)	a[i]=rxbuff[i];
	step();
	sendto_PC();
	DMA_Cmd(DMA1_Stream2, ENABLE);
}
