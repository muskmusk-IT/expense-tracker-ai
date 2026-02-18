async function loadExpenses() {
  const response = await fetch("PASTE_LINK_CSV_DISINI");
  const data = await response.text();

  const rows = data.split("\n").slice(1); // skip header

  let total = 0;

  rows.forEach(row => {
    const cols = row.split(",");
    const amount = parseInt(cols[2]) || 0; // kolom Total
    total += amount;
  });

  document.getElementById("totalAmount").innerText =
    "Rp " + total.toLocaleString("id-ID");
}

loadExpenses();
