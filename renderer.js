window.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("captureBtn");
  const output = document.getElementById("output");

  btn.addEventListener("click", async () => {
    output.innerText = "lendo a tela...";
    try {
      const res = await fetch("http://localhost:5000/captura", {
        method: "POST",
      });
      const data = await res.json();
      output.innerText = `\n Assistente:\n${data.interpretacao}`;
    } catch (err) {
      output.innerText = " Erro ao conectar ao servidor Python.";
    }
  });
});
