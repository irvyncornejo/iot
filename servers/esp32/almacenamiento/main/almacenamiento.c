#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "nvs_flash.h"
#include "nvs.h"

void app_main(void)
{
	printf("Start!!");

	// inicializar el driver de nvs
	esp_err_t err = nvs_flash_init();
	printf("NVS Init!!\n");
	printf((err != ESP_OK ? "Failed\n" : "Done"));

	nvs_handle_t my_storage;
	err = nvs_open("storage", NVS_READWRITE, &my_storage);
	printf("NVS Open");
	printf((err != ESP_OK ? "Failed\n" : "Done\n"));

	//escribir en nvs
	err = nvs_set_i32(my_storage, "number", 10);
	printf(("NVS Set"));
	printf((err != ESP_OK ? "Failed\n" : "Done\n"));

	//guardar en nvs
	err = nvs_commit(my_storage);
	printf(("NVS Commit"));
	printf((err != ESP_OK ? "Failed\n" : "Done\n"));

	//leer NVS
	int32_t number;
	err = nvs_get_i32(my_storage, "number", &number);
	printf(("NVS Get"));
	printf((err != ESP_OK ? "Failed\n" : "Done\n"));

	printf("El valor recuperado es: %ld \n", number);
	nvs_close(my_storage);

	printf("Terminó el programa\n");

}
