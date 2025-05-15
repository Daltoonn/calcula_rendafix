import tkinter as tk
from tkinter import messagebox

def calcular_porcentagem():
    try:
        porcentagem = float(entry_porcentagem.get())
        valor = float(entry_valor.get())
        resultado = (porcentagem / 100) * valor
        label_resultado.config(text=f"Renda Mensal: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Configuração da janela principal
root = tk.Tk()
root.title("Conversor de Renda Fixa")

# Label e Entry para a porcentagem
label_porcentagem = tk.Label(root, text="Por favor insira a porcentagem do rendimento do investimento (%):")
label_porcentagem.pack(pady=25)
entry_porcentagem = tk.Entry(root)
entry_porcentagem.pack(pady=25)

# Label e Entry para o valor base
label_valor = tk.Label(root, text="Por favor insira o Valor que você gostaria de investir:")
label_valor.pack(pady=25)
entry_valor = tk.Entry(root)
entry_valor.pack(pady=25)

# Botão para calcular a porcentagem
botao_calcular = tk.Button(root, text="Calcular", command=calcular_porcentagem)
botao_calcular.pack(pady=40)

# Label para exibir o resultado
label_resultado = tk.Label(root, text="Renda Mensal:")
label_resultado.pack(pady=40)

# Iniciar o loop da interface
root.mainloop()
