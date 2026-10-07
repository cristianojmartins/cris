#!/data/data/com.termux/files/usr/bin/bash

echo "=============================================="
echo "      DIAGNÓSTICO DE APLICATIVOS ANDROID"
echo "=============================================="
echo
echo "Este diagnóstico NÃO altera nem desinstala nada."
echo

echo "APLICATIVOS INSTALADOS PELO USUÁRIO"
echo "----------------------------------------------"
echo

for pacote in $(pm list packages -3 | sed 's/package://'); do

    nome="$pacote"
    tamanho="N/D"

    apk=$(pm path "$pacote" 2>/dev/null | head -n 1 | sed 's/package://')

    if [ -n "$apk" ] && [ -f "$apk" ]; then
        tamanho=$(du -h "$apk" 2>/dev/null | awk '{print $1}')
    fi

    printf "%-55s %8s\n" "$nome" "$tamanho"

done

echo
echo "=============================================="
echo "Fim do diagnóstico"
echo "=============================================="
echo
echo "N/D = informação não disponível para o Termux."
