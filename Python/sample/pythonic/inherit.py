#!/usr/bin/python3
from abc import ABC, abstractmethod


class TransactionalPolicy:
    def __init__(self, policy_data, **extra_data):
        self._data = {**policy_data, **extra_data}

    def __getitem__(self, customer_id):
        return self._data[customer_id]

    def __len__(self):
        return len(self._data)

    def change_in_policy(self, customer_id, **new_policy_data):
        self._data[customer_id].update(**new_policy_data)


def main():
    policy = TransactionalPolicy()
    policy.change_in_policy(2, {"a": 3})
    return policy[2]


if __name__ == "__main__":
    main()
