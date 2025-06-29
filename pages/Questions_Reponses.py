import streamlit as st
# Configuration de la page
st.set_page_config(page_title="Questions_Réponses", layout="wide")
# EN-TÊTE
st.markdown("""
<div style="background-color:#00a3a6;padding:10px;border-radius:8px;">
    <h2 style="color:white;text-align:center;">Les interrogations des éleveurs et éleveuses face au changement climatique</h2>
</div>
<div style='text-align:center;margin-top:10px;margin-bottom:20px;'>
    <p style='color:#4d4d4d;font-size:16px;'>
        🧑‍🏫 <strong>Yves Richard</strong> (Université de Bourgogne Europe);
        🧑‍🔬 <strong>Thierry Castel</strong> (institut Agro Dijon)
    </p>       
</div>
""", unsafe_allow_html=True)

st.markdown("#### Les réponses aux vingtaines de questions posées par les éléveurs et éleveuses sur le climat et la météo, " \
"rencontrés lors des enquêtes de terrain  ont été regroupées en quatre grandes familles et sous-familles.")
# Tabs
tabs = st.tabs(["🌦️ Météorologie et Climat", "🌍 Changement climatique", "🌱 Milieux", "👨‍🌾 Les humains"])

# Onglet 1
with tabs[0]:
    st.markdown("### 1. Météorologie et Climat")

     # 🔵 Bloc des questions (texte intact)
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 20px; border-left: 5px solid #2196F3; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
        Manque de fiabilité de la météo « Pouvez-vous améliorer votre logiciel pour avoir une météo plus fiable ? » 
        « J’ai une vraie question actuelle sur la fiabilité de la météo ? Cette année (2024) on avait l’impression de ne jamais pouvoir faire confiance à la météo ». 
        « La météo change tout le temps, est-ce qu’on pourrait avoir des prévisions fiables ? On est en 2024, on a des satellites partout et j’ai l’impression que le baromètre nous disait mieux le temps qu’il allait faire que la météo actuelle » 
        « Avoir la météo à l’année » 
        « Qu’ils arrivent à nous annoncer des météos précises »
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 🟢 Bloc de réponse (vert clair, texte continu)
    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-left: 5px solid #43a047; border-radius: 8px; text-align: justify;">
        Le battement de l'aile d'un papillon peut... Il n'est pas prévisible. Les mouvements qui animent l'atmosphère ne sont pas tous déterministes. 
        Ils sont en partie <b>chaotiques</b>. Ainsi, <b>prévoir avec précision le temps qu'il fera en un lieu donné au-delà de 15 jours est, et sera à tout jamais, impossible</b>.
        Pour autant, une part des phénomènes et mouvements qui animent l'atmosphère est <b>déterministe</b> et aisément <b>prévisible</b>. 
        Par exemple, ceux associés à l'astronomie et à la composition chimique de l'atmosphère. 
        Le jour sera plus ensoleillé que la nuit et l'été sera plus chaud que l'hiver. 
        Lorsque les hommes émettent des gaz à effet de serre, le climat devient plus chaud.
        <br><br>
        En <b>météorologie</b>, on parle de <i>prévision</i>, ce qui va se passer à l'horizon de l'heure, du jour ou des 15 prochains jours. 
        En <b>climatologie</b>, on parle de <i>projection</i>, ce qui peut se passer pour la saison, l'année ou les décennies prochaines.
    </div>
    """, unsafe_allow_html=True)

with tabs[1]:
    st.markdown("### 2 Changement climatique")

    st.markdown("#### 2.1 Comprendre")
    st.markdown("""
        <div style="background-color: #e3f2fd; padding: 20px; border-left: 5px solid #2196F3; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
        - Avoir des informations sur le CC ; comprendre ; avoir des éléments précis ; de long terme ; ce qui est certain et ce qui reste non connu. Est-ce que les climatologues sont sûrs de ce qu’ils disent, parce que c’est inquiétant ?<br><br>
        « C'est un peu du genre, qu'est-ce qu'ils [les climatologues] font quand les États-Unis refusent tous les... Je veux dire, c'est des choses comme ça. Quand je disais qu'on a tout sur les épaules, en face, il y a des gros producteurs, qui aujourd'hui s'en foutent. Je ne dis pas que pour autant, on ne doit rien faire non plus, au contraire. Mais c'est ce qui pose question et c'est ce qui peut aussi bloquer peut-être dans certaines réflexions. C'est qu'on se rend compte que d'un point de vue mondial, le constat du changement climatique n'est pas partagé. Déjà une chose, c'est qu'on peut nous l’acter, mais il n'est pas partagé partout ».
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- Bloc Réponse (fond vert clair, texte rédigé fluide) ---
    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-left: 5px solid #43a047; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    Les sciences du climat sont complexes, mais pas plus que les autres disciplines scientifiques. Leur spécificité réside dans leur capacité à produire de vastes synthèses collectives. Tous les cinq à huit ans, le GIEC (Groupe d’experts intergouvernemental sur l’évolution du climat) publie un rapport fondé sur des milliers d'études scientifiques évaluées par les pairs. Ces rapports sont accompagnés de résumés clairs, traduits dans de nombreuses langues, et accessibles à tous. Peu de domaines scientifiques offrent une telle transparence et rigueur méthodologique.<br><br>
    Il est essentiel de comprendre que le GIEC n’est ni un lobby ni un groupe militant. Il s’agit d’une structure qui regroupe des scientifiques de haut niveau venant du monde entier, et appartenant à de nombreuses disciplines : mathématiques appliquées, physique de l’atmosphère, modélisation, géographie, science des données, économie, sociologie, etc. Leur objectif commun est de synthétiser les connaissances disponibles sur l’évolution du climat, ses causes, ses conséquences, et les trajectoires possibles selon les choix humains.<br><br>
    Le fait que certains États ou producteurs n’adhèrent pas pleinement à ces constats ne remet pas en cause la qualité ni la fiabilité du travail scientifique mené. L'incertitude ne signifie pas ignorance : elle est mesurée, encadrée, et rendue explicite dans les publications du GIEC. La science du climat n’est pas figée, mais elle repose sur des fondements solides que la communauté internationale actualise en permanence.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("#### 2.2 « Ici et maintenant » ou la relation au temps long et à l’espace")
                
    st.markdown("""
        <div style="background-color: #e3f2fd; padding: 20px; border-left: 5px solid #2196F3; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    • Cycles ? sommes-nous dans des cycles (retour année humide 2024) ?   Année de 13 lunes.<br>
        « on entend dire avec les lunes, avec les marées, toutes ces choses-là, les années de 13 lunes, les années bissextiles, ça influe sur le climat, cette année de 13 lunes et bissextile, il paraît que les deux-là associées c’est pas bon » « el Niño ils parlaient bien des cycles » « puis il [le véto] nous dit que c’est des cycles »
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- Bloc Réponse (fond vert clair, texte rédigé fluide) ---
    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-left: 5px solid #43a047; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    Un cycle, à l'image d'une roue, signifie « tourner en rond ». La Terre tourne sur elle-même. C'est le cycle diurne qui régit l'alternance nuit jour. 
    La Terre tourne autour du soleil. C'est le cycle annuel qui régit les saisons. La trajectoire que la Terre effectue autour du soleil est modulée 
    selon 3 éléments qui forment 3 familles de cycles :<strong> 1. Excentricité (de l'ordre de 100 000 ans), 2. Obliquité (de l'ordre de 40 000 ans), 
    et 3. Précession des équinoxes (de l'ordre de 18 000 ans)</strong>. La combinaison de ces 3 familles de cycles régit, a minima depuis 1 million d'années,
    les alternances observées entre périodes glaciaires et périodes interglaciaires. Depuis 12 000 ans, nous sommes dans une période interglaciaire, nommée Holocène. 
    Il existe d'autres cycles, comme par exemple l'activité solaire, cycle de 11 ans, ou encore les cycles de la lune (environ 29 jours). L'influence de ces cycles 
    sur le climat de la Terre ou les climats régionaux n'a jamais pu être démontrée. On ne retrouve pas de telles cyclicités sur les climats de la Terre.<br><br>
    Le phénomène <strong>El Niño </strong>est parfois associé à la notion de cycle. De manière simple, dans le Pacifique équatorial, les eaux sont plus fraîches
    le long des côtes sud-américaines que sur les côtes asiatiques et australiennes. Ceci est lié aux <strong>alizés</strong> qui poussent les eaux de surface de l’est vers l’ouest.
    Certaines années, cette situation se renforce. On parle alors de <strong>La Niña</strong>. D’autres années, cette situation s’affaiblit. Des eaux chaudes atteignent alors les côtes sud-américaines.
    Ce phénomène a été nommé <strong>El Niño </strong>par les pêcheurs péruviens car il survient le plus souvent aux alentours de Noël. Les événements El Niño reviennent tous les 2 à 7 ans. Ce ne sont donc pas des cycles réguliers. À l’échelle de la planète, les années El Niño sont plus chaudes que les années La Niña. Les anomalies climatiques associées à El Niño et à La Niña sont nombreuses sous les tropiques comme en Amérique du Nord. L’impact sur le climat de l’Europe reste à démontrer.
    <br><br>
    Enfin, il existe des phénomènes non cycliques, comme l'activité volcanique, qui influencent également climat. Ces derniers sont aujourd'hui globalement imprévisibles.   
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("#### - 2024 : une année de records ?")
    # --- Bloc Question (fond bleu clair) ---
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 20px; border-left: 5px solid #2196F3; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    • 2024 : une année de records ?<br>
    « enfin on prend cette année-là ou enfin on est sur une année qui semble climatiquement un peu particulière…. »<br>
    « il faudrait demander aux météorologues ou à vos climatologues mais je jouerais qu’on a explosé tous les records, entre octobre et février, de pluviométrie et de température.
    Je pense que c’est l’hiver le plus chaud qu’on ait connu » (éleveur.se du Doubs)
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- Bloc Réponse (fond vert clair) ---
    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-left: 5px solid #43a047; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    En France, l'année 2024, par comparaison à la normale récente, à savoir 1991-2020, fut chaude, pluvieuse et peu ensoleillée. Ainsi les sols sont souvent restés humides voire très humides. 2024 diffère de ce qui avait été observé les années précédentes, en particulier en 2022.

    Pour autant, ce n’est pas une année de records. Bien que chaude, elle le fut moins que 2022 et 2023. Bien que pluvieuse, elle le fut moins que 2013 ou 2001, par exemple en Bourgogne-Franche-Comté.

    Si 2024 a surpris, c’est surtout par contraste avec les années qui ont précédé. Si 2024 était survenue dans les années 1970, tout le monde l’aurait trouvée exceptionnellement chaude — en vérité du jamais vu — mais assez habituelle en termes de précipitations, d’ensoleillement et d’humidité des sols.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("#### - Moyenne France : ce n’est pas une donnée pertinente pour nous")
     # --- Bloc Question (fond bleu clair) ---
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 20px; border-left: 5px solid #2196F3; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    • Moyenne France : ce n'est pas une donnée pertinente pour nous.<br>
    « la moyenne de la France ça ne veut rien dire — vous voulez que ce soit plus localisé ? oui c’est comme ça qu’on va réfléchir, c’est comme ça qu’on va se poser des questions,
    nous agriculteurs, sur l’avenir, comment s’adapter »
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- Bloc Réponse (fond vert clair) ---
    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-left: 5px solid #43a047; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    En France métropolitaine — les climats d’outre-mer étant très variés et tous très différents — on distingue deux grands types de climats : le climat tempéré et le climat méditerranéen. 
    Les évolutions de ces deux climats sont distinctes.
    Par exemple, les régions méditerranéennes françaises ont commencé à se réchauffer de manière significative dès le début des années 1980, alors que les régions à climat tempéré n’ont observé un réchauffement marqué qu’à partir de 1988.
    Au sein même du climat tempéré, entre le Pays Basque, la Bretagne, l’Alsace ou encore le centre de la France, il existe de nombreuses nuances. Mais cet ensemble évolue globalement à l’unisson. Ainsi, les grands froids de février 1956, 
    la grande sécheresse de 1976 ou encore l’année chaude et sèche de 2022 furent partagés par ces régions.
    Partout également, dans ces régions à climat tempéré, l’année 2024 fut chaude, pluvieuse et peu ensoleillée.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("#### - Sur l’évolution précise des températures")
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 20px; border-left: 5px solid #2196F3; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    « on entend beaucoup dire que les températures vont être …voilà j’entends dire plein de choses : plus hautes l’été, plus basses l’hiver. Ce serait de savoir pas exactement 
    mais de combien, et puis petit à petit savoir jusqu’à quand quoi , jusqu’à quel point ça va aller avec les années pour qu’on puisse s’adapter un peu en amont et ne pas se retrouver un jour à dire oh làlà, ça ne va plus »<br>
    « la terre elle a déjà été plus chaude ; il y a un réchauffement est ce qu’on est réellement capable de dire ça ou pas »
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-left: 5px solid #43a047; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    Avec la pression atmosphérique, la température est la variable météorologique la plus facile à mesurer. Les thermomètres sont des instruments qui existent depuis des siècles.
    Ils sont très fiables. Ainsi la connaissance de l'évolution des températures est-elle fiable et précise. A l'échelle de la planète, la température de la dernière décennie a 
    augmenté de +1.2 0 C depuis 1850. En 2024, elle fut même supérieure de 1,5 0 C. A l'échelle de la France, cette augmentation est de l'ordre de 2 o c. Comme sur tous les continents, 
    c'est supérieur à la moyenne mondiale. Ce réchauffement, est un peu moindre à proximité de l'océan, par exemple en Bretagne, un peu plus fort lorsque l'on s'éloigne de l'océan,
    par exemple dans les Alpes.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("#### - Sur l’évolution du vent")
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 20px; border-left: 5px solid #2196F3; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    « le vent. Parce que maintenant…On trouve qu’on a plus de vent ».
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-left: 5px solid #43a047; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    Le vent est peut-être la variable météorologique la plus difficile à mesurer car, il est fortement affecté par la turbulence notamment à proximité de la surface de la Terre. Les instruments, des anémomètres, évoluent avec les progrès technologiques. Aujourd'hui, on utilise parfois des anémomètres 3D à ultrasons ! Ainsi, il est difficile de produire des séries longues (plusieurs décennies) et fiables. En outre, ces instruments sont coûteux et demandent beaucoup de maintenance. En conséquence, les points de mesure sont peu nombreux. Enfin, l'environnement immédiat des stations météorologiques est très impactant. La construction d'un bâtiment ou la suppression d'une haie non loin d'une station météorologique affecte ce que l'on appelle la rugosité de surface (la surface des continents n’est pas aussi lisse que celle des océans) ce qui modifie la direction et la vitesse du vent et sa mesure. Au final, la connaissance de l'évolution du vent sur plusieurs décennies, qu'il s'agisse de sa vitesse moyenne, de ses directions ou des vitesses lors des rafales, est globalement méconnue. Chacun a son ressenti. Selon que l'on pratique, la voile, le cerf-volant, le vélo ou l'agriculture, on ne sera peut-être pas sensible aux mêmes caprices du vent ! D'autre part notre mémoire concernant l'ensemble des variables climatiques et le vent en particulier est médiocre et très sélective. Elle n'enregistre en général que les épisodes dits marquants ou extrêmes (tempêtes, vagues de froids ou de chaleurs intenses et persistantes...).
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 2.3 Intensité et fréquence d’événements météorologique ou la question des extrêmes")
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 20px; border-left: 5px solid #2196F3; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    • Des extrêmes ?
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-left: 5px solid #43a047; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    Le changement climatique est dû à l'augmentation des concentrations atmosphériques en gaz de faible concentration dit ‘trace’, à effet de serre. Ces gaz, en particulier le dioxyde de carbone, le méthane et le protoxyde d'azote, à l'image du plastique d'une serre ou d'une couette sur un lit, piègent le rayonnement sortant. Comme dans une serre ou sous la couette, Il fait plus chaud ! Il y a plus d'énergie piégée dans l'atmosphère. Il fait donc plus chaud partout sur la planète. Les glaciers et la banquise fondent. Ce sont les conséquences les plus directes. Mais, sachant que l'air chaud peut contenir plus de vapeur d'eau que l'air froid (+7 % à chaque degré supplémentaire), il y a aussi plus de vapeur d'eau dans l'atmosphère qui renforce l'effet de serre car la vapeur d'eau est le premier gaz à effet de serre. Mais plus de vapeur d'eau c'est également plus de nuages qui bloquent le rayonnement solaire et atténuent le réchauffement. Il y a donc un équilibre subtil qui est déstabilisé avec la modification des concentrations de Gaz à Effet de Serre (GES) et notamment des gaz traces. Potentiellement les pluies peuvent être plus intenses qu'auparavant. C'est par exempte ce qui s'est produit à Valence en automne 2024. Les cyclones tropicaux, comme tes tempêtes des latitudes tempérées et froides, peuvent, à défaut d'être nécessairement plus fréquents, devenir plus violents. Les vagues de chaleur donnent lieu à des températures plus élevées. Pour autant, tous les événements extrêmes n'augmentent pas : les vagues de froids et les grandes gelées sont plus rares et moins sévères.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("#### - C’est normal le sirocco en février ? sur vents avec poussières qui arrivent chez nous")
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 20px; border-left: 5px solid #2196F3; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    • « Et maintenant le sirocco, enfin dans les années 80, le sirocco on le constatait dans l’été maintenant c’est au mois de février ! est-ce que c’est normal ? » sur vents avec poussières qui arrivent chez nous
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-left: 5px solid #43a047; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    Lorsqu'une dépression est positionnée au large du Portugal, un fort flux de sud s'établit entre l'Afrique du Nord et l'Europe de l'Ouest. Les vents peuvent soulever 
    du sable sur le Sahara et le transporter par-delà la Méditerranée. Ce phénomène se produit le plus souvent aux saisons intermédiaires. Les poussières qui se déposent en Europe 
    fertilisent les sols, mais accélèrent la fonte des neiges. Il est important de mieux étudier ces événements, ce dans la durée, avant de pouvoir identifier d'éventuelles tendances.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("#### - Phénomènes d’orages ")
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 20px; border-left: 5px solid #2196F3; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
     J’observe des couloirs d’orages (les 4 fois d’orages sur le même couloir), c’est bizarre ?
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-left: 5px solid #43a047; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    Pour qu'un orage se forme, il faut beaucoup d'énergie. Ainsi les orages sont-ils fréquents dans les pays tropicaux ou en saison chaude dans les pays tempérés. 
    Avec l'augmentation des concentrations en gaz à effet de serre dans l'atmosphère, il y a plus d'énergie dans les basses couches de l'atmosphère, les surfaces continentales
    et de l'océan. Dans nos régions, cela peut favoriser l'intensité des orages et étendre leur saison. A noter également que le réchauffement généré par les gaz à effet de serre 
    est très marqué près de la surface. Au sommet de la troposphère, à ta tropopause, là où se dessinent les « enclumes » qui coiffent les cumulonimbus, nuages pourvoyeurs au sein
    desquels se forment les orages, l'atmosphère ne se réchauffe pas. Le gradient/différence thermique vertical est donc de plus en plus prononcé. Cela favorise la convection ou 
    mouvements ascendants de masse d'air plus humide avec des vitesses verticales plus grandes et donc les orages et la grêle plus violente qui parfois les accompagne.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("#### - Evapotranspiration (pas assez connue) ")
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 20px; border-left: 5px solid #2196F3; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
     Evapotranspiration (pas assez connue). Il faut qu’on parle plus du phénomène d’évapotranspiration. (…) parce que là ils se plaignant « il pleut mais il ne fait rien » « il n’arrête pas de pleuvoir et je trouve que le sol est quand même super sec »
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-left: 5px solid #43a047; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    L'évaporation peut être potentielle (ETP) ou réelle (ET R). Potentielle (ETP), c'est la demande évaporative de l'atmosphère (ensemble des facteurs climatiques qui influent 
    sur les pertes d'eau par évaporation au niveau du sol ou d'une nappe d'eau libre, et par transpiration au niveau des plantes). Plus il est fait chaud, plus il y a de soleil 
    et plus il y a de vent, plus I'ETP augmente. Réelle (ET R), c'est le flux de vapeur d'eau depuis le sol vers l'atmosphère. Si la 'soif' de l'atmosphère est supérieure à ce que 
    le sol peut donner, avec l'aide des plantes, alors ETP > ET R. Les plantes entrent en contrainte pouvant aller jusqu'au stress hydrique plus ou moins intense et persistant et 
    conduire à leur dépérissement. Dans un climat plus chaud, ETP augmente mécaniquement, et ETR ne suit pas toujours. Même si les précipitations restent constantes, 
    les sécheresses hydriques (sols) et hydrologiques (nappes et cours d'eau) sont plus fréquentes, intenses et longues que dans les années 1960, 70 ou 80.
    </div>
    """, unsafe_allow_html=True)
    
with tabs[2]:
    st.markdown("### 3. Milieux")

    st.markdown("#### - Température du sol car très corrélée à la pousse de l’herbe")
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 20px; border-left: 5px solid #2196F3; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    « mais je pense que le sol par exemple la température du sol est bien plus élevée …les degrés cumulés du sols sont bien plus élevés que la même année en 1977, 
    on compare par rapport à 1977 parce que c’était une année exceptionnelle » (Nièvre)<br>
    « s’il y a des mesures par exemple de température du sol, je serai curieux, c’est des choses qui nous serviraient »<br>
    « nous on a besoin des températures du sol pour savoir quoi planter »<br>
    « la somme des températures sur une année elle a tendance à augmenter »
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-left: 5px solid #43a047; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    Le sol a une plus forte inertie que l'air. Les variations de température y sont moins rapides. L'amplitude thermique diurne est moins forte. Au printemps, le sol est un peu plus frais que l'air. En été, le sol atteint sa température maximale en décalé et plus tardivement que l'atmosphère. Il en est de même pour la température minimale en hiver. Enfin, à l'automne il est un peu plus chaud. Tout ceci est d'autant plus marqué que l'on mesure la température profondément (10 cm, 50 cm, 100 cm). À 100 cm, seul le cycle annuel subsiste. Les variations plus rapides disparaissent. À l'échelle de l'année, la température moyenne du sol est égale à la température moyenne de l'air.<br><br>
    - <strong>Evolution de la végétation ?</strong>
    <br>
    La végétation est sensible à la température, à l'eau et à la lumière. En Bourgogne-Franche-Comté, et ce de manière plus nette en altitude, 
    le principal facteur limitant est la température. Ainsi, avec le changement climatique, la saison végétative s'allonge. 
    Tous les stades phrénologiques gagnent en précocité. Tant que la disponibilité en eau est suffisante, la production de biomasse progresse.
    C'est ce qui a été observé dans les années 1990 et 2000. Depuis quelques années, la courbe s'est inversée car la disponibilité en eau 
    est devenue un facteur de plus en plus limitant. Cultures et forêts poussent moins bien. Par endroits la forêt dépérit. 
    La capacité des écosystèmes et des agrosystèmes à stocker du carbone diminue. Les rendements baissent. Il est important d'intégrer 
    dans cette évolution la notion d'acclimatation que les végétaux ont développée pour s'adapter au climat de la région. 
    Cette acclimatation est grandement déterminée par les conditions climatiques qui, étant déréglées avec le changement climatique, 
    perturbent ce mécanisme et modifient la vulnérabilité de la végétation qui devient plus fragile vis-à-vis de certains aléas (e.g.
    températures négatives).
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### • Plantes et races adaptées")
    
     # --- Bloc : Plantes et races adaptées ---
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 20px; border-left: 5px solid #2196F3; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    « savoir au niveau des animaux, voir s’il y a des races adaptées »
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-left: 5px solid #43a047; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    À moyen terme les peuplements commencent à changer et vont radicalement changer. Certaines espèces progressent en gagnant en altitude. Mais les sommets sont vite 
    atteints en Bourgogne-Franche-Comté. D'autres trouvent un refuge provisoire dans des fonds de vallées étroites où les inversions thermiques sont fréquentes. 
    C'est l'idée de niche ou de refuge. Enfin, certaines migrent du sud vers le nord. Mais le rythme du changement climatique apparaît comme trop rapide en termes 
    de capacité des écosystèmes à s'adapter. Chez les animaux, les espèces généralistes semblent plus résilientes que les spécialistes.
    </div>
    """, unsafe_allow_html=True)

with tabs[3]:
    st.markdown("### 4. Les hommes")

    st.markdown("#### • Ce qui s’est passé avant nous")
    # --- Bloc : Ce qui s'est passé avant nous ---
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 20px; border-left: 5px solid #2196F3; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    « qu’est ce qui fait l’homme qui impacte le climat ? »
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-left: 5px solid #43a047; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    À l’échelle de dizaines ou de centaines de millions d'années, les climats de la Terre ont beaucoup changé. Ils furent parfois beaucoup plus froids, parfois beaucoup plus chauds. Cette planète n'était peuplée ni d'hommes ni de grands singes. À cette échelle, la tectonique des plaques est le facteur principal des changements.<br><br>
    À l’échelle de dizaines ou de centaines de milliers d'années, des périodes cycliques glaciaires et interglaciaires ont alterné. À cette échelle, ce sont les paramètres adossés aux mouvements de la Terre et du Soleil qui régissent ces grands cycles. Les hommes du paléolithique ont su s'adapter à ces changements. Pendant les périodes glaciaires, les glaciers du Jura descendaient jusqu'en Bresse et les hommes chassaient une faune arctique dans des paysages de toundra.<br><br>
    Depuis 10 000 ans, nous étions « confortablement » installés dans un interglaciaire, nommé l'Holocène. Les hommes se sont progressivement sédentarisés. C'est la révolution néolithique. Les éleveurs et agriculteurs de notre région n'ont connu que ce climat dont les variations étaient minimes (optimum médiéval puis petit âge de glace par exemple) au regard des changements actuels.<br><br>
    Les agriculteurs d'aujourd'hui, alors que les activités humaines (émissions de gaz à effet de serre) nous font quitter l'Holocène, sont les premiers à connaître un changement si rapide (vitesse inconnue à l'échelle de l'humanité voire au-delà) et un climat si chaud. Le défi est immense pour eux.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("#### 4.1 Changer le climat ou la question de l’atténuation")
    # --- Bloc : Vitesse du dérèglement climatique et avenir ---
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 20px; border-left: 5px solid #2196F3; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    • « s’ils savent vraiment à quelle vitesse le climat va continuer de se dérégler ? en fait savoir si ça va aller beaucoup plus vite que ce que l’on a connu ? (…) pour savoir s’il faut se projeter sur quelque chose de court terme ou de très long terme »<br>
    « si nos enfants vont pouvoir encore vivre sur la planète ? (…) si on peut faire un peu machine arrière, aussi ? »
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-left: 5px solid #43a047; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    Cela dépend de nous, les 8 milliards d'humains. Si l'humanité suit les accords de Paris, le réchauffement planétaire pourrait se stabiliser vers +3 °C par rapport au climat préindustriel (1850). Nous aurions donc déjà fait une moitié du chemin (+1,5 °C en 2024).<br><br>
    Si nous sortons des accords de Paris, à l'image des États-Unis, le réchauffement pourrait être beaucoup plus marqué. Les climatologues ne savent jusqu'où peut aller ta folie (à l'image du slogan mortifère « drill baby drill ») des hommes. Cela ne relève pas de leurs compétences. Ils ne peuvent qu'informer, communiquer, en espérant être réellement entendus.<br><br>
    De plus en plus de scientifiques et de climatologues s'engagent dans des mouvements et passent à l'action pour alerter.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
        # --- Bloc : Scénarios / vision à 5–50 ans ---
    st.markdown(""" - **Scénarios / vision à 5-10-15-50 ans / tendances 10-20 prochaines années.** """)
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 20px; border-left: 5px solid #2196F3; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    « Sur les scénarios sur le long terme…je me dis que cette année est peut-être une année anecdotique, peut-être qu’El Niño va nous préserver un ou deux ans, nous ramener de la pluie régulièrement… »<br>
    « Je me dis comment on arrive à être précis sur le long terme si on n’arrive pas à être précis sur aujourd’hui ? »<br>
    « si eux ils ont une vision dans les 5 ou 10 ou 15 ans ou même dans les 50 ans à venir »<br>
    « ce dont j’ai besoin c’est sur le long terme, de regarder vraiment ce qui s’est passé avant nous, et ce qui pourrait se passer après nous, (…) plutôt la tendance, parce que la terre on sait qu’elle se réchauffe tout doucement depuis longtemps »<br>
    « est-ce que dans les 10 ans, 15 ans, 20 ans à venir est ce qu’il aura vraiment un changement ? (…) que même si on stoppe toutes les émissions de gaz à effet de serre c’est déjà trop tard ? »<br>
    « comment est-ce que ça va évoluer ? si eux ils ont des pistes pour nous dire ‘ça risque d’aller dans tel sens’, si on a ces infos là ça nous permet d’anticiper. (..) qu’on nous explique vraiment comment ça se passe le réchauffement climatique, moi j’aimerais comprendre »<br>
    « qu’ils nous prédisent pour les années à venir. Est-ce qu’ils le savent déjà ? »<br>
    « qu’ils nous disent ce qui va arriver dans les 10 prochaines années, les 20 prochaines »
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-left: 5px solid #43a047; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    De 2025 à 2050, due à l'inertie du système, l'histoire est écrite et le climat va continuer à changer, principalement à se réchauffer, et ce à un rythme plus rapide que ce que nous venons de vivre depuis l'an 2000 (25 ans aussi).<br><br>
    Au-delà de 2050, cela dépendra des politiques de réduction des émissions de gaz à effet de serre que nous menons (ou non) dès aujourd'hui. Il y a une forte inertie du système climatique liée notamment à l'océan et à la persistance du dioxyde de carbone dans l'atmosphère. Il n'y a pas de mécanisme d'auto-épuration du dioxyde de carbone (CO₂, molécule très stable), et seul l'océan et la végétation sont en capacité de le capter pour le fixer. Cette inertie est maximale pour des compartiments comme l'océan ou les glaciers.<br><br>
    Quoiqu'il advienne, nous ne retrouverons pas dans les siècles à venir le climat préindustriel (1850) ni même celui de notre enfance (1950–2000). L'enjeu est que le climat de nos enfants et petits-enfants leur permette de vivre sur notre planète. L'habitabilité de la planète ne sera pas intégralement remise en question. Mais de nombreuses parties aujourd'hui très peuplées (par exemple l'Asie du Sud-Est où vivent 2 milliards d'humains) et les littoraux de très faible altitude pourraient devenir impropres à la vie humaine.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
     # --- Bloc : Peut-on modifier la météo ? ---
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 20px; border-left: 5px solid #2196F3; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    • « Une question qui me turlupine : est-ce qu’il y a des personnes qui sont capables de modifier la météo ? Des fois on a des nuages bizarres qu’on n’a pas l’habitude voir. Je sais qu’il existe des trucs anti-grêle par exemple ? »
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-left: 5px solid #43a047; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    C'est ce que les hommes font en émettant des gaz à effet de serre. C'est très efficace. Trouver un antidote est comme penser que l'on peut fumer deux paquets de cigarettes par jour et qu'un médicament va miraculeusement soigner nos poumons et nos artères.<br><br>
    Certains industriels soutiennent ces pistes que l'on qualifie de géo-ingénierie ou techno-solutionnisme. Il y a en effet beaucoup d'argent à gagner s'ils convainquent dirigeants et peuples.<br><br>
    Les générateurs anti-grêle ne modifient ni les températures ni les précipitations. Modifient-ils la grêle ? Il n'y a pas de consensus ou accord scientifique sur ce sujet.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # --- Bloc : Injustices, efforts à fournir, jets privés ---
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 20px; border-left: 5px solid #2196F3; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    • « on pointe souvent du doigt certaines catégories. Nous on est pointés du doigt par rapport aux gaz à effet de serre »<br>
    « et donc l’effort qu’il faut faire, c’est tout le monde. C’est l’industrie, c’est l’agriculture. Et c’est le particulier en premier, qu’il faut qu’il fasse des efforts (…) limiter les jets privés, (…) je ne voudrais que ce soit les pauvres qui subissent. »
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-left: 5px solid #43a047; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    La question de l'équité est centrale. On peut l'envisager selon une perspective historique (anciens versus nouveaux pays industriels et riches), selon une perspective géographique (pays fortement versus faiblement émetteurs de gaz à effet de serre), selon une perspective sociologique (catégories sociales aisées très émettrices versus personnes modestes faiblement émettrices) ou philosophique en lien avec l'éthique et la justice.<br><br>
    Combiner ces perspectives est indispensable pour que tous se mettent en mouvement, à hauteur de leurs émissions et de leurs moyens.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("#### 4.2 Changer nos vies ou la question de l’adaptation")
    # --- Bloc : Comment peut-on s'adapter ? ---
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 20px; border-left: 5px solid #2196F3; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    • Comment peut-on s'adapter à ce qui va arriver ?<br>
    « Ce qui serait bien de savoir, c’est comment nous on peut s’adapter à ce qui va arriver car on ne va pouvoir l’empêcher de toute façon »
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-left: 5px solid #43a047; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    La première étape consiste à sortir du tout déni. Accepter le fait et les faits que le changement climatique est là et que son origine est exclusivement liée aux activités humaines (émissions de gaz à effet de serre).<br><br>
    La seconde étape est de mettre en œuvre une kyrielle de solutions largement listées dans le dernier rapport du GIEC. Cela demande de la concertation, de l'écoute, de la solidarité, de l'imagination. Ces solutions sont à décliner dans chaque territoire, avec l'ensemble des acteurs économiques et des habitants.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
  # --- Bloc : Échanges avec d'autres régions, recherche de solutions concrètes ---
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 20px; border-left: 5px solid #2196F3; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    • « qu’est ce qu’on pourrait bien mettre en place, quelle culture on pourrait mettre en place, comment on pourrait changer les choses, on y réfléchit, on en discute avec nos enfants, on ne voit pas vraiment de solution, et là c’est clair on aurait besoin de rencontrer des gens qui viennent d'ailleurs, d’autres régions, de régions où il fait chaud de savoir comment eux ils fonctionnent, quelles dispositions ils ont prises, quelles essences ils ont planté »<br>
    « aller voir un peu comment ils travaillent dans le sud. Ici ils nous disent que dans 10 ans on aura le climat de Lyon je crois ? (…) parce qu’il y a des choses auxquelles on ne pense pas parce que l’on n’y est pas confronté aujourd’hui »
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-left: 5px solid #43a047; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    Rencontrer des gens qui ont commencé à expérimenter des solutions est très stimulant. Cela montre que c'est possible. S'inspirer de leurs réussites, et prendre en compte leurs échecs, réussites et échecs des pistes déjà empruntées par d'autres, permet d'être plus efficace et de gagner du temps.<br><br>
    Les solutions fondées sur la nature, expérimentées ou déclinées par d'autres en d'autres lieux sont des voies à creuser et possiblement à généraliser.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- Bloc : Replanter, essences adaptées, transformation agricole ---
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 20px; border-left: 5px solid #2196F3; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    • « C’est quels moyens on peut mettre en œuvre au niveau des plantes, des arbres qui se sont renversés, on voudrait bien replanter aussi. Mettre des essences moins sensibles au vent, à la sécheresse par exemple. »
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #e8f5e9; padding: 20px; border-left: 5px solid #43a047; border-radius: 8px; font-family: Arial, sans-serif; text-align: justify;">
    Regarder les vidéos de Serge Zaka est une clé d'entrée. Il y a beaucoup d'informations disponibles. Il convient d'être curieux, de s'en emparer, d'être audacieux. Cela demande d'être conseillé, d'être accompagné.<br><br>
    L'agriculture française a su répondre aux défis des années d'après-guerre. En quelques décennies, elle a su se transformer en profondeur et faire de la France une grande puissance agricole. Un défi analogue est à nouveau à relever aujourd'hui. Les causes et symptômes ne sont pas les mêmes. Mais on peut s'inspirer de cette histoire pour relever ensemble le défi actuel : transformer l'agriculture pour que les agriculteurs vivent dignement de leur production selon des modalités en équilibre avec notre environnement.<br><br>
    Ce sont les habitudes des consommateurs qui nécessitent également de profondes évolutions. Les assiettes de demain ne seront ni celles de l'après-guerre, ni celles des trente glorieuses.
    </div>
    """, unsafe_allow_html=True)
