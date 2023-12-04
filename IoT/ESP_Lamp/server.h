#include <ESP8266WebServer.h>

ESP8266WebServer server(80);

void handle_root(){
String page_code = "<form action=\"/LED\" method=\"POST\">";
page_code += "<input type=\"submit\" style=\"color: red; padding: 15px 20px; border: 2px solid black; width: 50%; height: 100px; font-size: 100px; align-items: center; text-align: center; margin: 0 auto; \">";
page_code += "</form>";

  server.send(200, "text/html", page_code);
}

void handle_wifi_setup() {
  String wifi_setup_page = "<form action=\"/set_wifi\" method=\"POST\">";
  wifi_setup_page += "SSID: <input type=\"text\" name=\"ssid\"><br>";
  wifi_setup_page += "Pass: <input type=\"password\" name=\"password\"><br>";
  wifi_setup_page += "<input type=\"submit\" value=\"Set Wi-Fi\" style=\"color: red; padding: 15px 20px; border: 2px solid black;\">";
  wifi_setup_page += "</form>";

  server.send(200, "text/html", wifi_setup_page);
}

void handle_set_wifi() {
  if (server.hasArg("ssid") && server.hasArg("password")) {
    String new_ssid = server.arg("ssid");
    String new_password = server.arg("password");

    WiFi.begin(new_ssid.c_str(), new_password.c_str());

    server.send(200, "text/html", "complete");
    delay(2000);
    ESP.restart();
}
}


void handle_led(){
  digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));
  server.sendHeader("Location", "/");
  server.send(303);
}

void handle_not_found(){
  server.send(404, "text/html", "404 ERROR");
}

void server_init(){
  server.on("/", HTTP_GET, handle_root);
  server.on("/LED", HTTP_POST, handle_led);
  server.on("/wifi_setup", HTTP_GET, handle_wifi_setup);
  server.on("/set_wifi", HTTP_POST, handle_set_wifi);
  server.onNotFound(handle_not_found);

  server.begin();
  Serial.println("HTTP server started");
}
