# Диаграмма компонентов "Управления устройствами" WarmHouse

```plantuml
@startuml
title ToolService Component Diagram (Управление устройствами)

top to bottom direction

!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Component.puml

Container_Boundary(ToolService, "Tool Service") {
 Component(ApiHandler, "Device API", "Go (Gin)", "Обрабатывает входящие HTTP-запросы для управления устройствами: добавление, удаление, обновление")
  Component(CommandProcessor, "Command Processor", "Go", "Валидация и выполнение команд управления устройствами (включение, выключение, настройка)")
  Component(StateManager, "Device State Manager", "Go", "Хранение текущего состояния устройств, взаимодействие с базой данных")
  Component(DeviceCommunicator, "Device Communicator", "Go", "Низкоуровневое взаимодействие с устройствами через MQTT, TCP, или проприетарные протоколы")
  Component(DeviceRepository, "Device Repository", "Go + SQL", "Работа с базой данных устройств: загрузка и сохранение конфигураций")
}

' --- Внешние взаимодействия
Person(user, "Пользователь", "Пользователь системы Умный дом")
System_Ext(WebApp, "Web Application", "Go, Gin", "Web-интерфейс для пользователей и администраторов")
System_Ext(apiGateway, "API Gateway", "NGINX", "Единая точка входа в систему")
 
ContainerDb(deviceDb, "БД устройств", "PostgreSQL", "Состояние и конфигурация устройств")
System_Ext(Tools, "Устройства умного дома", "Датчики, камеры, реле и другое оборудование")

' --- Взаимодействия
Rel(user, WebApp, "Управление устройствами своего дома, в т.ч. подключение", "HTTPS")
Rel(WebApp, apiGateway, "Вызывает API", "REST / JSON")
Rel(apiGateway, ApiHandler, "Вызывает API", "REST / JSON")
Rel(ApiHandler, CommandProcessor, "Передаёт команды на исполнение","REST / JSON")
Rel(CommandProcessor, StateManager, "Получение состояния и обновление статуса устройства","REST / JSON")
Rel(StateManager, DeviceRepository, "Чтение/запись состояния", "SQL")
Rel(CommandProcessor, DeviceCommunicator, "Отправка управляющих команд устройствам","REST / JSON")
Rel(DeviceCommunicator, Tools, "MQTT / TCP")
Rel(DeviceRepository, deviceDb, "Чтение/запись конфигурации", "SQL")

@enduml
```