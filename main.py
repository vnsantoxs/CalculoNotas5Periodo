import streamlit as st

if __name__ == '__main__':
    st.title("Notas")
    st.divider()
    st.subheader("INTRODUÇÃO A ECONOMIA (MEE = (N1 + N2 + N3) /3)")
    c1, c2, c3, c4, c5 = st.columns(5)
    eco_nota1 = c1.number_input('Nota1', 0.0, 10.0, key='eco1')
    eco_nota2 = c2.number_input('Nota2', 0.0, 10.0, key='eco2')
    eco_nota3 = c3.number_input('Nota3', 0.0, 10.0, key='eco3')
    eco_media = (eco_nota1 + eco_nota2 + eco_nota3) / 3
    c4.write("Media")
    c4.write(eco_media)
    c5.write("Prova Final(Min)")
    if eco_media >= 8.0:
        c5.text("AP")
    else:
        nota_minima_prova_final_eco = (15 - (eco_media * 2)) / 3
        if nota_minima_prova_final_eco >= 10.0:
            c5.text("RP")
        else:
            if nota_minima_prova_final_eco == 0:
                c5.text("AP MF=5")
            else:
                c5.write(nota_minima_prova_final_eco)

    st.divider()
    st.subheader("PROBABILIDADE E ESTATÍSTICA")
    st.write("Sem plano de Ensino")
    st.divider()
    st.subheader("INSTITUIÇÕES DE DIREITO PÚBLICO E PRIVADO(MEE = (EE1 + EE2) / 2)")
    c6, c7, c8, c9 = st.columns(4)
    dir_nota1 = c6.number_input('Nota1', 0.0, 10.0, key='dir1')
    dir_nota2 = c7.number_input('Nota2', 0.0, 10.0, key='dir2')
    dir_media = (dir_nota1 + dir_nota2) / 2
    c8.write("Media")
    c8.write(dir_media)
    c9.write("Prova Final(Min)")
    if dir_media >= 8.0:
        c9.text("AP")
    else:
        nota_minima_prova_final_dir = (15 - (dir_media * 2)) / 3
        if nota_minima_prova_final_dir >= 10.0:
            c9.text("RP")
        else:
            if nota_minima_prova_final_dir == 0:
                c9.text("AP MF=5")
            else:
                c9.write(nota_minima_prova_final_dir)

    st.divider()
    st.subheader("GESTÃO DA QUALIDADE DE SOFTWARE (MEE = (AV1 + AV2 + AV3) / 3) ")
    c10, c11, c12, c13, c14 = st.columns(5)
    ges_nota1 = c10.number_input('Nota1', 0.0, 10.0, key='ges1')
    ges_nota2 = c11.number_input('Nota2', 0.0, 10.0, key='ges2')
    ges_nota3 = c12.number_input('Nota3', 0.0, 10.0, key='ges3')
    ges_media = (ges_nota1 + ges_nota2 + ges_nota3) / 3
    c13.write("Media")
    c13.write(ges_media)
    c14.write("Prova Final(Min)")
    if ges_media >= 8.0:
        c14.text("AP")
    else:
        nota_minima_prova_final_ges = (15 - (ges_media * 2)) / 3
        if nota_minima_prova_final_ges >= 10.0:
            c14.text("RP")
        else:
            if nota_minima_prova_final_ges == 0:
                c14.text("AP MF=5")
            else:
                c14.write(nota_minima_prova_final_ges)
    st.divider()
    st.subheader("PROGRAMAÇÃO PARA COMPUTAÇÃO MÓVEL(MEE = (3MTP + 5TF + 2DTF) / 10)")
    c15, c16, c17, c18, c19 = st.columns(5)
    mol_nota1 = c15.number_input('Nota1', 0.0, 10.0, key='mol1')
    mol_nota2 = c16.number_input('Nota2', 0.0, 10.0, key='mol2')
    mol_nota3 = c17.number_input('Nota3', 0.0, 10.0, key='mol3')
    mol_media = ((mol_nota1*3) + (mol_nota2*5) + (mol_nota3*2)) / 10
    c18.write("Media")
    c18.write(mol_media)
    c19.write("Prova Final(Min)")
    if mol_media >= 8.0:
        c19.text("AP")
    else:
        nota_minima_prova_final_mol = (15 - (mol_media * 2)) / 3
        if nota_minima_prova_final_mol >= 10.0:
            c19.text("RP")
        else:
            if nota_minima_prova_final_mol == 0:
                c19.text("AP MF=5")
            else:
                c19.write(nota_minima_prova_final_mol)
    st.divider()
    st.subheader("REDES DE COMPUTADORES (MEE = (P1 + TP1 + P2 + TP2) / 4)")
    c20, c21, c22, c23, c24, c25 = st.columns(6)
    red_nota1 = c20.number_input('Nota1', 0.0, 10.0, key='red1')
    red_nota2 = c21.number_input('Nota2', 0.0, 10.0, key='red2')
    red_nota3 = c22.number_input('Nota3', 0.0, 10.0, key='red3')
    red_nota4 = c23.number_input('Nota4', 0.0, 10.0, key='red4')
    red_media = (red_nota4+red_nota3+red_nota2+red_nota1)/4
    c24.write("Media")
    c24.write(red_media)
    c25.write("Prova Final(Min)")
    if red_media >= 8.0:
        c25.text("AP")
    else:
        nota_minima_prova_final_red = (15 - (red_media * 2)) / 3
        if nota_minima_prova_final_red >= 10.0:
            c25.text("RP")
        else:
            if nota_minima_prova_final_red == 0:
                c25.text("AP MF=5")
            else:
                c25.write(nota_minima_prova_final_red)
    st.divider()
    st.subheader("MODELOS DE GESTÃO  (MEE = (EE1 + EE2 + EE3) / 3)")
    c26, c27, c28, c29, c30 = st.columns(5)
    mod_nota1 = c26.number_input('Nota1', 0.0, 10.0, key='mod1')
    mod_nota2 = c27.number_input('Nota2', 0.0, 10.0, key='mod2')
    mod_nota3 = c28.number_input('Nota3', 0.0, 10.0, key='mod3')
    mod_media = (mod_nota1 + mod_nota2 + mod_nota3) / 3
    c29.write("Media")
    c29.write(mod_media)
    c30.write("Prova Final(Min)")
    if mod_media >= 8.0:
        c30.text("AP")
    else:
        nota_minima_prova_final_mod = (15 - (mod_media * 2)) / 3
        if nota_minima_prova_final_mod >= 10.0:
            c30.text("RP")
        else:
            if nota_minima_prova_final_mod == 0:
                c30.text("AP MF=5")
            else:
                c30.write(nota_minima_prova_final_mod)
