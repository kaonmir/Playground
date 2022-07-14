#!/usr/bin/python3

from dataclasses import dataclass
from datetime import datetime


class FieldFormat:
    @classmethod
    def hide_field(self, field) -> str:
        return "** 민감한 정보 삭제 **"

    @classmethod
    def fromat_time(self, field_timestamp: datetime) -> str:
        return field_timestamp.strftime("%Y-%m-%d %H:%M")

    @classmethod
    def show_original(self, field):
        return field


class EventSerializer:
    def __init__(self, serialization_fields: dict) -> None:
        self.serialization_fields = serialization_fields

    def serialize(self, event):
        return {
            field: transformation(getattr(event, field))
            for field, transformation in self.serialization_fields.items()
        }


class Serialization:
    def __init__(self, **transformations) -> None:
        self.serializer = EventSerializer(transformations)

    def __call__(self, event_class):
        def serialize_method(event_instance):
            return self.serializer.serialize(event_instance)

        event_class.serialize = serialize_method
        return event_class


@Serialization(
    username=FieldFormat.show_original,
    password=FieldFormat.hide_field,
    ip=FieldFormat.show_original,
    timestamp=FieldFormat.fromat_time,
)
@dataclass
class LogEvent:
    username: str
    password: str
    ip: str
    timestamp: str


def main():
    log = LogEvent("kaonmir", "1234", "192.168.43.232", datetime.now())
    serialized = log.serialize()
    print(serialized)


if __name__ == "__main__":
    main()
