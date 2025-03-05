# redes_ensp
Atividade final - Redes

Arquivos de configuração eNSP para criação de topologias.

Para a execução de cada topologia, basta:
  - instalar o eNSP 
  - baixar as pastas de cada topologia
  - salvá-las em eNSP/Examples
  - abrir o arquivo .topo


# Configuração de Vlan
![image](https://github.com/user-attachments/assets/3e132f93-5d97-42eb-b810-b07242a9cd1f)

# Configuração de Sub-redes
![image](https://github.com/user-attachments/assets/55c11153-c683-4fea-a417-783a162883a9)

# Configuração de Vlanif
![image](https://github.com/user-attachments/assets/0c8abd9d-9b12-4bb5-9fc0-e31093393e39)


# Configuração de WLAN
![image](https://github.com/user-attachments/assets/12fb16c1-77e8-4fdd-b32e-7ada1cdf0f88)

# Socket Python
### Lista de Comandos

| Comando          | Descrição                                      | Exemplo                          |
|------------------|-----------------------------------------------|----------------------------------|
| `<mensagem>`     | Envia uma mensagem para todos os clientes.     | `Olá, pessoal!`                 |
| `/list`          | Lista todos os clientes conectados.            | `/list`                         |
| `/msg <user> <msg>` | Envia uma mensagem privada para um usuário. | `/msg Bob Olá, Bob!`            |
| `/exit`          | Desconecta o cliente do servidor.              | `/exit`                         |

---

## Exemplo de Uso

### Cliente 1 (Alice):
```bash
Enter your username: Alice
Olá, pessoal!
/list
Current clients:
Alice
Bob
/msg Bob E aí, Bob! Tudo bem?
/exit
