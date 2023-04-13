# STEAM-KANISIUS

Library yang dibutuhkan:
<ol>
<li>requests</li>
<li>cv2</li>
<li>numpy</li>
<li>matplotlib</li>
<li>time (sudah otomatis terinstall)</li>
<li>serial</li>
</ol>
Dibutuhkan pula instalasi python terbaru dan arduino IDE. <br>
Penjelasan file: <br>
image-recog/make-model.py : kode untuk membuat model machine learning, hanya untuk dijalankan tepat 1 kali.
<br>
image-recog/communicator.py : untuk alat komunikasi dengan handphone dan arduino <br>
arduino-part/main.ino : kode utama arduino untuk membaca sensor dan menggerakan motor servo. <br><br>

Catatan: jalankan terlebih dahulu main.ino sebelum communicator.py. <br>
Kedua file harus selalu berjalan selama tong sampah berjalan.
