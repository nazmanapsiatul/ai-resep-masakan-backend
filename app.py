from flask import Flask, request, jsonify
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
print("API KEY:", os.getenv("GROQ_API_KEY"))
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

app = Flask(__name__)


@app.route("/")
def home():
    return "Ollama AI Aktif"
@app.route("/test")
def test():
    return "Backend Berhasil!"


@app.route("/extract", methods=["POST"])
def extract():

    text = request.json["text"]

    prompt = f"""
Anda adalah seorang chef Indonesia.

Buatkan 3 resep masakan sederhana untuk anak kos dari bahan berikut:

{text}

Aturan:
- Gunakan bahasa Indonesia.
- Jangan gunakan Markdown.
- Jangan gunakan tanda * atau #.
- Jangan gunakan kalimat pembuka.
- Langsung tampilkan resep.

Setiap resep WAJIB dipisahkan dengan:

=== RESEP ===

Format setiap resep:

=== RESEP ===

Nama Resep:
Deskripsi:

Estimasi Waktu:
Estimasi Biaya:
Tingkat Kesulitan:

Informasi Gizi:
Kalori:
Protein:
Karbohidrat:
Lemak:

Bahan:
- ...

Langkah:
1.
2.
3.
4.
5.

Tips:

Buat 3 resep yang berbeda.
"""

    response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.7,
)

    hasil = response.choices[0].message.content

    print("===== HASIL AI =====")
    print(hasil)
    print("====================")

    hasil = hasil.replace("**", "")
    hasil = hasil.replace("*", "")
    hasil = hasil.replace("#", "")
    hasil = hasil.replace("```", "")

    resep_list = hasil.split("=== RESEP ===")

    hasil_json = []

    for resep in resep_list:

        resep = resep.strip()

        if resep == "":
            continue

        lower = resep.lower()

        gambar = "chef.png"

        if "garang asem" in lower:
            gambar = "Garang_Asem_Ayam.jpeg"

        elif "ayam suwir" in lower:
            gambar = "Ayam_Suwir_Pedas_Manis.jpeg"

        elif "indomie carbonara" in lower:
            gambar = "Indomie_Carbonara.jpeg"

        elif "indomie telur" in lower:
            gambar = "Indomie_Telur.jpeg"

        elif "mie goreng sayur" in lower:
            gambar = "Mie_Goreng_Sayur.jpeg"

        elif "telur balado" in lower:
            gambar = "Telur_Balado.jpeg"

        elif "telur dadar" in lower:
            gambar = "Telur_Dadar.jpeg"

        elif "orak arik telur" in lower:
            gambar = "Orak_Arik_Telur_Sayur.jpeg"

        elif "tahu kecap" in lower:
            gambar = "Tahu_Kecap_Pedas.jpeg"

        elif "tempe bacem" in lower:
            gambar = "Tempe_Bacem.jpeg"

        elif "tempe goreng" in lower:
            gambar = "Tempe_Goreng.jpeg"

        elif "tumis kangkung" in lower:
            gambar = "Tumis_Kangkung.jpeg"

        elif "sayur bening bayam" in lower:
            gambar = "Sayur_Bening_Bayam.jpeg"

        elif "bakwan sayur" in lower:
            gambar = "Bakwan_Sayur.jpeg"

        elif "sarden" in lower:
            gambar = "Sarden_Simple.jpeg"

        hasil_json.append({
            "isi": resep,
            "gambar": gambar
        })

    return jsonify({
        "resep": hasil_json
    })

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )