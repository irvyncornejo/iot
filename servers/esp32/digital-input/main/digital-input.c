#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "driver/gpio.h"

#define LED_PIN 2
#define INPUT_PIN 15

void app_main(void)
{
    int led_state = 0;
    gpio_reset_pin(LED_PIN);
    gpio_set_direction(LED_PIN, GPIO_MODE_OUTPUT);
    gpio_set_direction(INPUT_PIN, GPIO_MODE_INPUT);

    gpio_set_level(LED_PIN, led_state);

    while (1)
    {   
        led_state = gpio_get_level(INPUT_PIN);
        gpio_set_level(LED_PIN, led_state);
    }
}
