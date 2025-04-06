document.getElementById("form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const nome = document.getElementById("nome").value;
  const endereco = document.getElementById("endereco").value;
  const horario = document.getElementById("horario").value;
  const promocao = document.getElementById("promocao").value;

  const data = { nome, endereco, horario, promocao };

  try {
    const res = await fetch("http://localhost:5000/estabelecimentos", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    if (res.ok) {
      alert("Estabelecimento cadastrado com sucesso!");
      document.getElementById("form").reset();
    } else {
      alert("Erro ao cadastrar.");
    }
  } catch (err) {
    console.error(err);
    alert("Erro na comunicação com o servidor.");
  }
});