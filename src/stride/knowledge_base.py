STRIDE_KNOWLEDGE_BASE = {
    "database": [
        {
            "category": "Tampering",
            "title": "Alteração indevida de dados",
            "description": "Um atacante pode tentar modificar dados armazenados no banco.",
            "mitigation": "Aplicar controle de acesso, criptografia e trilhas de auditoria.",
            "severity": "Alta",
        },
        {
            "category": "Information Disclosure",
            "title": "Exposição de dados sensíveis",
            "description": "Dados sensíveis podem ser acessados por usuários não autorizados.",
            "mitigation": "Usar criptografia em repouso, mascaramento de dados e políticas de acesso.",
            "severity": "Alta",
        },
    ],
    "api_gateway": [
        {
            "category": "Spoofing",
            "title": "Falsificação de identidade",
            "description": "Um atacante pode tentar acessar APIs se passando por um usuário legítimo.",
            "mitigation": "Utilizar autenticação forte, OAuth2, JWT e validação de tokens.",
            "severity": "Alta",
        },
        {
            "category": "Denial of Service",
            "title": "Sobrecarga do gateway",
            "description": "O gateway pode ser alvo de excesso de requisições.",
            "mitigation": "Aplicar rate limiting, throttling e proteção contra DDoS.",
            "severity": "Média",
        },
    ],
}