// Item forms (Found/Lost)
  const itemForms = document.querySelectorAll('.item-form');
  itemForms.forEach(form => {
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      showModal('บันทึกแบบฟอร์มสำเร็จ !');
      setTimeout(() => {
        closeModal();
        showPage('homepage');
      }, 2000);
    });
  });

