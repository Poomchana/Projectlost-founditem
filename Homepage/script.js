<<<<<<< HEAD
// ฟังก์ชันกลับไปหน้าแรก
function goHome() {
  // ใส่ลิงก์หรือโค้ดเพื่อกลับหน้าแรกได้ที่นี่
  // ตัวอย่าง: window.location.href = "home.html";
  alert("กลับไปหน้าแรก (ตัวอย่าง)"); 
}

// หากต้องการเพิ่มข้อมูลด้วย JS ภายหลัง สามารถใช้โค้ดนี้เป็นแนวทาง
/*
function addRow(id, date, detail, status) {
  const tbody = document.getElementById('lost-data');
  const row = document.createElement('tr');
  row.innerHTML = `
    <td>${id}</td>
    <td>${date}</td>
    <td>${detail}</td>
    <td>${status}</td>
  `;
  tbody.appendChild(row);
}
*/
=======
document.addEventListener('DOMContentLoaded', () => {
  // ปุ่มติดต่อ
  document.querySelectorAll('.contact-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      alert('ติดต่อเจ้าของสิ่งของ\nFacebook: ***\nLine: ***\nเบอร์โทร: ***');
    });
  });

  // hover การ์ด
  document.querySelectorAll('.item-card').forEach(card => {
    card.addEventListener('mouseenter', () => {
      card.style.transform = 'translateY(-5px)';
      card.style.boxShadow = '0px 8px 16px rgba(0,0,0,0.3)';
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = 'translateY(0)';
      card.style.boxShadow = '0px 4px 4px rgba(0,0,0,0.25)';
    });
  });
});


>>>>>>> HomePage
