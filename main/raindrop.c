
#include "app_prov.h"
#include "driver/rmt.h"
#include "esp_event_loop.h"
#include "esp_http_client.h"
#include "esp_log.h"
#include "esp_sleep.h"
#include "esp_wifi.h"
#include "freertos/FreeRTOS.h"
#include "freertos/event_groups.h"
#include "freertos/task.h"
#include "math.h"
#include "nvs_flash.h"
#include "string.h"
#include <esp_system.h>
#include <lwip/err.h>
#include <lwip/sys.h>

static const char *RAINDROP_TAG = "RAINDROP";

#define RMT_TX_CHANNEL RMT_CHANNEL_0
#define RMT_TX_GPIO 19

#define num_leds 3

/* FreeRTOS event group to signal when we are connected & ready to make a request */
static EventGroupHandle_t wifi_event_group;

/* The event group allows multiple bits for each event,
   but we only care about one event - are we connected
   to the AP with an IP? */
const int CONNECTED_BIT = BIT0;

RTC_DATA_ATTR int boot_cnt = 0;

float *precipitationdata;

/*
 * Initialize the RMT Tx channel
 */
static void rmt_tx_int()
{
    rmt_config_t config;
    config.rmt_mode = RMT_MODE_TX;
    config.channel = RMT_TX_CHANNEL;
    config.gpio_num = RMT_TX_GPIO;
    config.mem_block_num = 1;
    config.tx_config.loop_en = 0;
    // set the maximum clock divider to be able to output
    // RMT pulses in range of about one hundred milliseconds
    config.clk_div = 8;

    ESP_ERROR_CHECK(rmt_config(&config));
    ESP_ERROR_CHECK(rmt_driver_install(config.channel, 0, 0));
}

static void wifi_init_sta()
{
    /* Start wifi in station mode with credentials set during provisioning */
    wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
    ESP_ERROR_CHECK(esp_wifi_init(&cfg));
    ESP_ERROR_CHECK(esp_wifi_set_mode(WIFI_MODE_STA) );
    ESP_ERROR_CHECK(esp_wifi_start() );
}

esp_err_t _http_event_handle(esp_http_client_event_t *evt)
{
    switch(evt->event_id) {
        case HTTP_EVENT_ERROR:
            ESP_LOGI(RAINDROP_TAG, "HTTP_EVENT_ERROR");
            break;
        case HTTP_EVENT_ON_CONNECTED:
            ESP_LOGI(RAINDROP_TAG, "HTTP_EVENT_ON_CONNECTED");
            break;
        case HTTP_EVENT_HEADER_SENT:
            ESP_LOGI(RAINDROP_TAG, "HTTP_EVENT_HEADER_SENT");
            break;
        case HTTP_EVENT_ON_HEADER:
            ESP_LOGI(RAINDROP_TAG, "HTTP_EVENT_ON_HEADER");
            break;
        case HTTP_EVENT_ON_DATA:
            ESP_LOGI(RAINDROP_TAG, "HTTP_EVENT_ON_DATA, len=%d", evt->data_len);
            *precipitationdata = atof(evt->data);

            break;
        case HTTP_EVENT_ON_FINISH:
            ESP_LOGI(RAINDROP_TAG, "HTTP_EVENT_ON_FINISH");
            break;
        case HTTP_EVENT_DISCONNECTED:
            ESP_LOGI(RAINDROP_TAG, "HTTP_EVENT_DISCONNECTED");
            break;
    }
    return ESP_OK;
}

void app_wifi_wait_connected()
{
    xEventGroupWaitBits(wifi_event_group, CONNECTED_BIT, false, true, portMAX_DELAY);
}

void precipitationdatadownload(){
    ESP_LOGI(RAINDROP_TAG, "Start data download");
    free(precipitationdata);

    char *url = "https://dwd:dwdaccount@ladikas.de/dwd/simple/relative/DRESDEN/0-12h/precipitation";

    precipitationdata = malloc(5);
    esp_http_client_config_t config = {
        .url = url,
        .auth_type = HTTP_AUTH_TYPE_BASIC,
        .event_handler = _http_event_handle,
    };
    esp_http_client_handle_t client = esp_http_client_init(&config);
    esp_http_client_set_method(client, HTTP_METHOD_GET);
    esp_err_t err = esp_http_client_perform(client);

    ESP_LOGI(RAINDROP_TAG, "Downloading weather data");
    if (err == ESP_OK) {
        ESP_LOGI(RAINDROP_TAG, "Status = %d, content_length = %d",
                esp_http_client_get_status_code(client),
                esp_http_client_get_content_length(client));
    }
     else {
        ESP_LOGE(RAINDROP_TAG, "HTTP POST request failed: %s", esp_err_to_name(err));
    }
    esp_http_client_cleanup(client);
}

void loop(){

    esp_sleep_enable_timer_wakeup(30 * 1000000);

    boot_cnt++;
    printf("boot_cnt: %d\n", boot_cnt);


    //init wifi
    //Initialize NVS
    //esp_err_t ret = nvs_flash_init();
    //if (ret == ESP_ERR_NVS_NO_FREE_PAGES || ret == ESP_ERR_NVS_NEW_VERSION_FOUND) {
    //  ESP_ERROR_CHECK(nvs_flash_erase());
    //  ret = nvs_flash_init();
    //}
    //ESP_ERROR_CHECK(ret);

    // green, red, blue
    int colors[num_leds][3];

    precipitationdatadownload();
    if(*precipitationdata <= 33){
        for(int led = 0; led < num_leds; led++){
            colors[led][0]=165;
            colors[led][1]=255;
            colors[led][2]=0;
        }
    }
    if(*precipitationdata > 33 && *precipitationdata <= 66){
        for(int led = 0; led < num_leds; led++){
            colors[led][0]=255;
            colors[led][1]=0;
            colors[led][2]=0;
        }
    }
    if(*precipitationdata > 66){
        for(int led = 0; led < num_leds; led++){
            colors[led][0]=0;
            colors[led][1]=255;
            colors[led][2]=0;
        }
    }
    //end wifi

    rmt_item32_t items[num_leds * 3 * 8 + 1];
    rmt_item32_t *items_pointer = items;
    // reset pulse
    items_pointer -> level0 = 1;
    items_pointer -> duration0 = 1;
    items_pointer -> level1 = 0;
    items_pointer -> duration1 = 1050;
    items_pointer++;

    for(int led_index = 0; led_index < num_leds; led_index++){
        for(uint8_t color_index = 0; color_index < 3; color_index++){
            for(uint8_t bit_index = 8; bit_index != 0; bit_index--){
                uint8_t bit_set = (colors[led_index][color_index] >> (bit_index-1)) & 1;
                if(bit_set) {
                    printf("1");
                    items_pointer -> level0 = 1;
                    items_pointer -> duration0 = 14;
                    items_pointer -> level1 = 0;
                    items_pointer -> duration1 = 3;
                }
                else {
                    printf("0");
                    items_pointer -> level0 = 1;
                    items_pointer -> duration0 = 3;
                    items_pointer -> level1 = 0;
                    items_pointer -> duration1 = 14;
                }
                items_pointer++;
            }
        }
        printf("\n");
    }

    ESP_ERROR_CHECK(rmt_write_items(RMT_TX_CHANNEL, items, num_leds * 3 * 8 + 1, true));
    ESP_LOGI(RAINDROP_TAG, "Transmission complete");

    ESP_LOGI(RAINDROP_TAG, "Entering deep sleep");
    esp_wifi_stop();
    esp_deep_sleep_start();
}

static esp_err_t event_handler(void *ctx, system_event_t *event)
{
    /* Invoke Provisioning event handler first */
    app_prov_event_handler(ctx, event);

    switch(event->event_id) {
    case SYSTEM_EVENT_STA_START:
        ESP_LOGI(RAINDROP_TAG, "Starting wifi station event");
        esp_wifi_connect();
        break;
    case SYSTEM_EVENT_STA_GOT_IP:
        ESP_LOGI(RAINDROP_TAG, "got ip:%s",
                 ip4addr_ntoa(&event->event_info.got_ip.ip_info.ip));

        xEventGroupSetBits(wifi_event_group, CONNECTED_BIT);

        break;
    case SYSTEM_EVENT_AP_STACONNECTED:
        ESP_LOGI(RAINDROP_TAG, "station:"MACSTR" join, AID=%d",
                 MAC2STR(event->event_info.sta_connected.mac),
                 event->event_info.sta_connected.aid);
        break;
    case SYSTEM_EVENT_STA_DISCONNECTED:
        ESP_LOGI(RAINDROP_TAG, "Disconnecting wifi station event");
        xEventGroupClearBits(wifi_event_group, CONNECTED_BIT);

        break;
    default:
        break;
    }
    return ESP_OK;
}

void app_main() {
    wifi_event_group = xEventGroupCreate();

    ESP_LOGI(RAINDROP_TAG, "Configuring transmitter");
    rmt_tx_int();

    int security = 1;

    const static protocomm_security_pop_t app_pop = {
        .data = (uint8_t *) CONFIG_POP,
        .len = (sizeof(CONFIG_POP)-1)
    };
    const static protocomm_security_pop_t *pop = &app_pop;

    /* Initialize networking stack */
    tcpip_adapter_init();

    /* Set our event handling */
    ESP_ERROR_CHECK(esp_event_loop_init(event_handler, NULL));

    /* Check if device is provisioned */
    bool provisioned;
    esp_err_t ret = nvs_flash_init();
    if (ret == ESP_ERR_NVS_NO_FREE_PAGES || ret == ESP_ERR_NVS_NEW_VERSION_FOUND) {
      ESP_ERROR_CHECK(nvs_flash_erase());
      ret = nvs_flash_init();
    }
    if (app_prov_is_provisioned(&provisioned) != ESP_OK) {
        ESP_LOGI(RAINDROP_TAG, "Error getting device provisioning state");
        return;
    }

    if (provisioned == false) {
        /* If not provisioned, start provisioning via BLE */
        ESP_LOGI(RAINDROP_TAG, "Starting BLE provisioning");
        app_prov_start_ble_provisioning(security, pop);

        app_wifi_wait_connected();
        loop();
    }
    else {
        /* Else start as station with credentials set during provisioning */
        ESP_LOGI(RAINDROP_TAG, "Starting WiFi station");
        wifi_init_sta(NULL);

        app_wifi_wait_connected();
        loop();
    }
}
