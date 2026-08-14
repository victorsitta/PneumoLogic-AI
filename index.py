# ==============================================================================
# PASSO 1: A BASE DE CONHECIMENTO (Memória do Sistema)
# ==============================================================================
class BaseDeConhecimento:
    """
    Esta classe funciona como o 'banco de dados' do nosso especialista.
    Ela armazena o que o sistema JÁ SABE (fatos) e como ele PENSA (regras).
    """
    def __init__(self):
        # Lista onde guardaremos os fatos conhecidos (sintomas e diagnósticos deduzidos)
        self.fatos = []
        
        # Lista onde guardaremos as regras do tipo: ( [LISTA_DE_CONDICOES], CONCLUSÃO )
        self.regras = []

    def adicionar_fato(self, fato):
        """Adiciona uma nova informação à nossa lista de verdades."""
        if fato not in self.fatos:
            self.fatos.append(fato)

    def adicionar_regra(self, condicao, conclusao):
        """
        Adiciona uma regra lógica. 
        Exemplo: condicao = ["febre alta", "tosse"], conclusao = "infecção respiratória"
        Representação lógica: (febre alta ∧ tosse) -> infecção respiratória
        """
        self.regras.append((condicao, conclusao))


# ==============================================================================
# PASSO 2: O MECANISMO DE INFERÊNCIA (O "Cérebro" do Sistema)
# ==============================================================================
class SistemaEspecialista:
    """
    Esta classe é o motor de inferência. 
    Ela pega os fatos e as regras da Base de Conhecimento e usa Lógica Proposicional
    para deduzir novas conclusões através do encadeamento para frente (Forward Chaining).
    """
    def __init__(self, base_conhecimento):
        # O sistema precisa ter acesso à base para ler e atualizar dados
        self.base_conhecimento = base_conhecimento

    def inferir(self):
        """
        Analisa as regras repetidamente. Se TODAS as condições de uma regra forem
        satisfeitas pelos fatos atuais, a conclusão é adicionada como um NOVO fato.
        """
        novos_fatos_encontrados = True

        # O loop roda enquanto estivermos descobrindo coisas novas
        while novos_fatos_encontrados:
            novos_fatos_encontrados = False

            # Passa por CADA regra cadastrada
            for condicao, conclusao in self.base_conhecimento.regras:
                
                # 1. VERIFICAÇÃO LÓGICA (Operador AND / ∧):
                # 'all()' verifica se TODOS os sintomas exigidos pela regra estão na lista de fatos.
                todas_condicoes_satisfeitas = all(
                    sintoma in self.base_conhecimento.fatos for sintoma in condicao
                )

                # 2. DEDUÇÃO:
                # Se o paciente tem TODOS os sintomas E a conclusão ainda não foi anotada:
                if todas_condicoes_satisfeitas and conclusao not in self.base_conhecimento.fatos:
                    # Adicionamos a nova conclusão aos fatos do paciente
                    self.base_conhecimento.adicionar_fato(conclusao)
                    
                    # Avisamos ao sistema o raciocínio seguido
                    print(f" -> [DEDUÇÃO]: Como o paciente apresenta {condicao}, deduziu-se: '{conclusao}'.")
                    
                    # Marcamos como True para o 'while' rodar mais uma vez e testar
                    # se essa nova conclusão ativa NENHUMA OUTRA regra em cadeia!
                    novos_fatos_encontrados = True


# ==============================================================================
# PASSO 3 & 4: TESTANDO O SISTEMA COM CASOS REAIS
# ==============================================================================
if __name__ == "__main__":
    print("==================================================")
    print("   SISTEMA ESPECIALISTA DE DIAGNÓSTICO MÉDICO    ")
    print("==================================================\n")

    # 1. Instanciando a Base de Conhecimento
    base = BaseDeConhecimento()

    # 2. Cadastrando as Regras de Negócio (Conhecimento Médico)
    # Regra 1: (febre alta ∧ tosse) -> infecção respiratória
    base.adicionar_regra(["febre alta", "tosse"], "infecção respiratória")
    
    # Regra 2: (infecção respiratória ∧ dificuldade para respirar) -> pneumonia
    base.adicionar_regra(["infecção respiratória", "dificuldade para respirar"], "pneumonia")

    # 3. Inserindo os Fatos Iniciais (Sintomas relatados pelo Paciente)
    print("--- 1. Sintomas Relatados pelo Paciente ---")
    sintomas_paciente = ["febre alta", "tosse", "dificuldade para respirar"]
    for sintoma in sintomas_paciente:
        base.adicionar_fato(sintoma)
        print(f" • Sintoma registrado: {sintoma}")

    print("\n--- 2. Executando o Mecanismo de Inferência ---")
    sistema = SistemaEspecialista(base)
    sistema.inferir()

    print("\n--- 3. Diagnóstico Final ---")
    print("Lista completa de fatos mantidos no prontuário do paciente:")
    for fato in base.fatos:
        print(f" ✓ {fato}")