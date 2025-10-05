function goHome() {
  window.location.href = "index.html";
}

function logout() {
  alert("ออกจากระบบเรียบร้อยแล้ว");
  window.location.href = "login.html";
}

// เปลี่ยนรูปโปรไฟล์
function previewPhoto(event) {
  const photo = document.getElementById('photoPreview');
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = e => {
      photo.style.backgroundImage = `url(${e.target.result})`;
    };
    reader.readAsDataURL(file);
  }
}

// สลับโหมดแก้ไข / ดูข้อมูล
function toggleEdit() {
  const inputs = document.querySelectorAll('#profileForm input');
  const editBtn = document.getElementById('editBtn');

  const isEditing = editBtn.textContent === "แก้ไขโปรไฟล์";

  if (isEditing) {
    // เปิดให้แก้ไข
    inputs.forEach(i => i.disabled = false);
    editBtn.textContent = "เสร็จสิ้น";
    editBtn.style.backgroundColor = "#00b300";
  } else {
    // กลับสู่โหมดดูข้อมูล
    inputs.forEach(i => i.disabled = true);
    editBtn.textContent = "แก้ไขโปรไฟล์";
    editBtn.style.backgroundColor = "#10b32d";
    alert("บันทึกข้อมูลเรียบร้อย ✅");
  }
}
