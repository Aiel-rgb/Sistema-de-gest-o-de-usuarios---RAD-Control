import tkinter as tk
from tkinter import ttk, messagebox
from database import BancoRAD

class AppRAD:
    def __init__(self, root):
        self.root = root
        self.root.title("RAD Control")
        self.root.geometry("1400x1000")
        self.root.configure(bg="#1e293b")
        self.banco = BancoRAD()
        self.banco.conectar()
        self.criar_form()
        self.criar_tabela()
        self.recarregar()
        


    def criar_form(self):
        frame = tk.LabelFrame(self.root, text="Nova Solicitação", bg="#1e293b", fg="#38bdf8", font=("Segoe UI", 10, "bold"))
        frame.pack(side="left", fill="y", padx=10, pady=10)

        tk.Label(frame, text="Nome do Aluno:", bg="#1e293b", fg="#94a3b8").grid(row=0, column=0, sticky="w", pady=4)
        self.entry_nome = tk.Entry(frame, width=30, bg="#0f172a", fg="#e2e8f0", insertbackground="#38bdf8")
        self.entry_nome.grid(row=0, column=1, pady=4)

        tk.Label(frame, text = "Matricula:", bg="#1e293b", fg="#94a3b8").grid (row=1, column=0, sticky="w", pady=4)
        self.entry_matricula = tk.Entry(frame, width=30, bg="#0f172a", fg="#e2e8f0", insertbackground="#38bdf8")
        self.entry_matricula.grid(row=1, column=1, pady=4)

        tk.Label(frame, text="Tipo:", bg="#1e293b", fg="#94a3b8").grid(row=2, column=0, sticky="w", pady=4)
        self.combo_tipo = ttk.Combobox(frame, width=27, state = "readonly")
        self.combo_tipo["values"] = ["Dúvida", "Entrega", "Correção", "Orientação", "Revisão", "Outro"]
        self.combo_tipo.grid(row=2, column=1, pady=4)

        tk.Label(frame, text="Prioridade:", bg="#1e293b", fg="#94a3b8").grid(row=3, column=0, sticky="w", pady=4)
        self.combo_prioridade = ttk.Combobox(frame, width=27, state= "readonly")
        self.combo_prioridade["values"] = ["Baixa", "Média", "Alta"]
        self.combo_prioridade.grid(row=3,column=1, pady=4)

        tk.Label(frame, text="Status:", bg="#1e293b", fg="#94a3b8").grid(row=4, column=0, sticky="w", pady=4)
        self.combo_status = ttk.Combobox(frame, width=27, state= "readonly")
        self.combo_status["values"] = ["Aberto", "Em andamento", "Concluído", "Cancelado"]
        self.combo_status.grid(row=4, column=1, pady=4)

        tk.Label(frame, text="Prazo (AAAA-MM-DD):", bg="#1e293b", fg="#94a3b8").grid(row=5, column=0, sticky="w", pady=4)
        self.entry_prazo = tk.Entry(frame, width=30, bg="#0f172a", fg="#e2e8f0", insertbackground="#38bdf8")
        self.entry_prazo.grid(row=5, column=1, pady=4)

        tk.Label(frame, text="Descrição", bg="#1e293b", fg="#94a3b8").grid(row=6, column=0, sticky="nw", pady=4)
        self.text_descricao = tk.Text(frame, width=30, height=5)
        self.text_descricao.grid(row=6, column=1, pady=4)

        frame_botoes = tk.Frame(frame)
        frame_botoes.grid(row=7, column=0, columnspan=2, pady=10)

        tk.Button(frame_botoes, text="Cadastrar", width=12, command=self.cadastrar, bg="#0ea5e9", fg="white", relief="flat").pack(side="left", padx=4)
        tk.Button(frame_botoes, text="Atualizar", width=12 , command=self.atualizar, bg="#8b5cf6", fg="white", relief="flat").pack(side="left", padx=4)
        tk.Button(frame_botoes, text="Excluir", width=12, command=self.excluir, bg="#ef4444", fg="white", relief="flat").pack(side="left", padx=4)
        tk.Button(frame_botoes, text="Limpar", width=12, command=self.limpar, bg="#475569", fg="white", relief="flat").pack(side="left", padx=4)
        

    def criar_tabela(self):
        frame = tk.LabelFrame(self.root, text = "Solicitações", bg="#1e293b", fg="#38bdf8", font=("Segoe UI", 10, "bold"))
        frame.pack(side="right", fill = "both", expand=True, padx=10, pady=10)

        frame_pesquisa = tk.Frame(frame, bg="#1e293b")
        frame_pesquisa.pack(fill="x", pady=5)

        self.entry_pesquisa = tk.Entry(frame_pesquisa, width=30,bg="#0f172a", fg="#e2e8f0", insertbackground="#38bdf8")
        self.entry_pesquisa.pack(side="left", padx=4)

        tk.Button(frame_pesquisa, text="Pesquisar", command=self.pesquisar, bg="#0ea5e9", fg="white", relief="flat").pack(side="left", padx=4)
        tk.Button(frame_pesquisa, text="Recarregar", command=self.recarregar, bg="#475569", fg="white", relief="flat").pack(side="left", padx=4)

        colunas = ("id", "nome", "matricula", "tipo", "prioridade", "status", "descricao", "data", "prazo")
        self.tree = ttk.Treeview(frame, columns=colunas, show="headings", height=20)

        for col in colunas:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=90)
        
        self.tree.pack(fill="both", expand=True, padx=4, pady=4)
        self.tree.bind("<<TreeviewSelect>>", self.selecionar_registro)

        self.tree.tag_configure("alta", background="#fca5a5", foreground="#ef4444")
        self.tree.tag_configure("media", background="#fde68a", foreground="#b45309")
        self.tree.tag_configure("baixa", background="#bbf7d0", foreground="#15803d")
        
    
    def cadastrar(self):
        nome = self.entry_nome.get()
        matricula = self.entry_matricula.get()
        prazo = self.entry_prazo.get()

        descricao = self.text_descricao.get("1.0", tk.END).strip()

        prioridade = self.combo_prioridade.get()
        status = self.combo_status.get()
        tipo = self.combo_tipo.get()

        if not nome or not matricula or not tipo or not descricao:
            messagebox.showwarning("Atenção", "Preencha todos os campos obrigatorios!")
            return

        self.banco.inserir(nome, matricula, tipo, prioridade, status, descricao, prazo)
        self.recarregar()
        self.limpar()

    def atualizar(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um registro na tabela!")
            return 
        
        item = self.tree.item(selecionado[0])
        id_registro = item["values"][0]

        nome = self.entry_nome.get()
        matricula = self.entry_matricula.get()
        prazo = self.entry_prazo.get()

        descricao = self.text_descricao.get("1.0", tk.END).strip()

        prioridade = self.combo_prioridade.get()
        status = self.combo_status.get()
        tipo = self.combo_tipo.get()

        self.banco.atualizar(id_registro, nome, matricula, tipo, prioridade, status, descricao, prazo)
        self.recarregar()
        self.limpar()

    def excluir(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um registro na tabela!")
            return 
        
        item = self.tree.item(selecionado[0])
        id_registro = item["values"][0]
        confirmar = messagebox.askyesno("Confirmar", "Deseja excluir esse registro?")
        if not confirmar:
            return
        
        self.banco.excluir(id_registro)
        self.recarregar()

    def limpar(self):
        self.entry_matricula.delete(0,tk.END)
        self.entry_nome.delete(0,tk.END)
        self.entry_prazo.delete(0,tk.END)
        
        self.text_descricao.delete("1.0", tk.END)
        
        self.combo_prioridade.set("")
        self.combo_status.set("")
        self.combo_tipo.set("")

    def pesquisar(self):
        termo = self.entry_pesquisa.get()

        for item in self.tree.get_children():
            self.tree.delete(item)
        
        registros = self.banco.pesquisar(termo)
        for reg in registros:
            self.tree.insert("","end",values=reg)


    def recarregar(self):
        for item in self.tree.get_children():
           self.tree.delete(item)

        registros = self.banco.listar()
        for reg in registros:
            prioridade = reg[4].lower().strip()
            if "alta" in prioridade:
                tag = "alta"
            elif "média" in prioridade or "media" in prioridade:
                tag = "media"
            else:
                tag = "baixa"
            self.tree.insert("","end",values=reg, tags=(tag,))   
    
    def selecionar_registro(self, event):
        selecionado = self.tree.selection()
        if not selecionado:
            return
        
        item = self.tree.item(selecionado[0])
        valores = item["values"]

        self.limpar()
        self.entry_nome.insert(0, valores[1])
        self.entry_matricula.insert(0, valores[2])
        self.combo_tipo.set(valores[3])
        self.combo_prioridade.set(valores[4])
        self.combo_status.set(valores[5])
        self.text_descricao.insert("1.0", valores[6])
        self.entry_prazo.insert(0,valores[8])



if __name__ == "__main__":
    root = tk.Tk()
    app = AppRAD(root)
    root.mainloop()
