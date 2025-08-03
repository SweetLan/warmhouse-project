# Диаграмма кода компонента управления устройствами
```plantuml
@startuml CodeDiagram
title Классы: Устройство и управление


class Device {
  - id: string
  - name: string
  - type: DeviceType
  - state: DeviceState
  --
  + turnOn(): void
  + turnOff(): void
  + isOn(): bool
}

class Module {
  - id: string
  - name: string
  - version: string
  - type: ModuleType
}

enum DeviceType {
  LIGHT
  WARM
  CAMERA
  GATE
}

enum DeviceState {
  ON
  OFF
  UNKNOWN
}

enum ModuleType {
  TemperatureSensor
  HumiditySensor
  SwitchModule
  DimmingControl
  GateMotorControl
  PositionSensor
}
 
DeviceType "1" -- "1..N" Device  : has
Device "1" -- "1" DeviceState : has
Device "1" -- "1..N" Module : has
ModuleType "1" -- "1..N" Module  : has

@enduml

```