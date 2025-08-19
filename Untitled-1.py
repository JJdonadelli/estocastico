import re
import json
from collections import defaultdict

def export_markov_model():
    """
    Processa o arquivo acile.txt e exporta o modelo Markov em diferentes formatos
    """
    
    print("🔄 Carregando e processando acile.txt...")
    
    # Carregar o texto
    try:
        with open("acile.txt", encoding="utf-8") as f:
            text = f.read().lower()
        print(f"✅ Arquivo carregado: {len(text)} caracteres")
    except FileNotFoundError:
        print("❌ Erro: arquivo 'acile.txt' não encontrado!")
        return
    
    # Quebrar em palavras
    words = re.findall(r"\b\w+\b", text)
    print(f"✅ Palavras extraídas: {len(words)} palavras")
    
    # Construir modelo de trigramas (Markov ordem 2)
    markov_model = defaultdict(list)
    for w1, w2, w3 in zip(words, words[1:], words[2:]):
        markov_model[(w1, w2)].append(w3)
    
    print(f"✅ Modelo construído: {len(markov_model)} trigramas únicos")
    
    # Converter defaultdict para dict normal (para JSON)
    markov_dict = {}
    for key, values in markov_model.items():
        # Usar string como chave para JSON: "palavra1|palavra2"
        key_str = f"{key[0]}|{key[1]}"
        markov_dict[key_str] = values
    
    # 1. EXPORTAR COMO JSON (para JavaScript)
    print("\n💾 Exportando modelo...")
    
    with open("markov_model.json", "w", encoding="utf-8") as f:
        json.dump(markov_dict, f, ensure_ascii=False, indent=2)
    print("✅ Salvo: markov_model.json")
    
    # 2. EXPORTAR COMO JAVASCRIPT (pronto para HTML)
    js_content = "// Modelo Markov gerado automaticamente\n"
    js_content += "const MARKOV_MODEL = " + json.dumps(markov_dict, ensure_ascii=False, indent=2) + ";\n\n"
    
    # Adicionar função auxiliar para usar o modelo
    js_content += """
// Função para gerar texto usando o modelo
function generateMarkovText(startWord, length = 50) {
    startWord = startWord.toLowerCase().trim();
    
    // Encontrar pares que começam com a palavra inicial
    const candidates = [];
    for (const key in MARKOV_MODEL) {
        const [w1, w2] = key.split('|');
        if (w1 === startWord) {
            candidates.push([w1, w2]);
        }
    }
    
    if (candidates.length === 0) {
        throw new Error(`Palavra "${startWord}" não encontrada no modelo.`);
    }
    
    // Escolher par inicial aleatório
    const [w1, w2] = candidates[Math.floor(Math.random() * candidates.length)];
    const result = [w1, w2];
    
    // Gerar texto
    let currentKey = `${w1}|${w2}`;
    for (let i = 2; i < length; i++) {
        if (!MARKOV_MODEL[currentKey] || MARKOV_MODEL[currentKey].length === 0) {
            break;
        }
        
        const nextWords = MARKOV_MODEL[currentKey];
        const nextWord = nextWords[Math.floor(Math.random() * nextWords.length)];
        result.push(nextWord);
        
        // Atualizar chave para próxima iteração
        const [, prevW2] = currentKey.split('|');
        currentKey = `${prevW2}|${nextWord}`;
    }
    
    return result.join(' ');
}

// Função para obter palavras iniciais disponíveis
function getAvailableStartWords() {
    const startWords = new Set();
    for (const key in MARKOV_MODEL) {
        const [w1] = key.split('|');
        startWords.add(w1);
    }
    return Array.from(startWords).sort();
}
"""
    
    with open("markov_model.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    print("✅ Salvo: markov_model.js")
    
    # 3. GERAR ESTATÍSTICAS
    stats = {
        "total_characters": len(text),
        "total_words": len(words),
        "unique_trigrams": len(markov_model),
        "unique_start_words": len(set(key[0] for key in markov_model.keys())),
        "most_common_starts": []
    }
    
    # Encontrar palavras iniciais mais comuns
    start_counts = defaultdict(int)
    for key in markov_model.keys():
        start_counts[key[0]] += len(markov_model[key])
    
    stats["most_common_starts"] = sorted(
        start_counts.items(), 
        key=lambda x: x[1], 
        reverse=True
    )[:20]
    
    with open("model_stats.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    print("✅ Salvo: model_stats.json")
    
    # 4. MOSTRAR EXEMPLOS
    print("\n🔤 Palavras iniciais mais comuns:")
    for word, count in stats["most_common_starts"][:10]:
        print(f"  • {word}: {count} continuações")
    
    print(f"\n📊 Resumo:")
    print(f"  • Texto original: {stats['total_characters']:,} caracteres")
    print(f"  • Total de palavras: {stats['total_words']:,}")
    print(f"  • Trigramas únicos: {stats['unique_trigrams']:,}")
    print(f"  • Palavras iniciais: {stats['unique_start_words']:,}")
    
    print("\n🎯 Arquivos gerados:")
    print("  • markov_model.json - Modelo em JSON")
    print("  • markov_model.js - Modelo pronto para JavaScript")
    print("  • model_stats.json - Estatísticas do modelo")
    print("\n✨ Pronto para usar no HTML!")

if __name__ == "__main__":
    export_markov_model()