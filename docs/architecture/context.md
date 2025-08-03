# Контекстная диаграмма WarmHouse

```plantuml
@startuml context-diagram
!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Context.puml

title WarmHouse Context Diagram AS IS
top to bottom direction

Person(user, "Пользователь", "Пользователь системы Умный дом")
Person(admin, "Выездной специалист", "Устанавливает оборудование и подключает его к системе")
System(WarmHouse, "Умный дом", "Система управления отоплением в доме и проверки температуры")

System_Ext(warm,"Система отопления", "Набор датчиков, установленных в домах")

Rel(user, WarmHouse, "Управление (вкл/выкл) отоплением в своем доме")
Rel(user, WarmHouse, "Просмотр текущей температуры в своих домах")
Rel(admin, WarmHouse, "Подключение системы отопления к системе Умный дом")
Rel(WarmHouse, warm, "Запрос данных о температуре с датчиков, установленных в домах", "HTTPS / JSON")

@enduml
```
