"""
Tugas 4 - Jalur B: Publisher (simulasi modul Pembayaran)
Author: FARRELLINO ULUNG SATYA AMANDO - 103072400005
Pastikan `docker compose up -d` sudah jalan sebelum menjalankan file ini.
"""

import pika
import json
import time

QUEUE_NAME = "pembayaran_berhasil"

def main():
    print("[1] Menghubungkan ke RabbitMQ...")
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost")
    )
    channel = connection.channel()
    print("[OK] Terhubung ke RabbitMQ")

    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    print(f"[OK] Queue '{QUEUE_NAME}' siap (durable)")

    print("\n[2] Mengirim event pembayaran...")
    for i in range(1, 4):
        pesan = {
            "user_id": f"user{i}",
            "jumlah": 20000 * i,
            "timestamp": time.time(),
            "status": "lunas"
        }
        
        channel.basic_publish(
            exchange='',
            routing_key=QUEUE_NAME,
            body=json.dumps(pesan),
            properties=pika.BasicProperties(
                delivery_mode=2  
            )
        )
        print(f"  ✓ Event terkirim: {pesan['user_id']} - Rp {pesan['jumlah']:,}")
        time.sleep(0.5)

    connection.close()
    print("\n[OK] Publisher selesai. Semua event telah dikirim.")

if __name__ == "__main__":
    main()