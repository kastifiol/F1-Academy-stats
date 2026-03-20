# 🏎️ F1 Academy — Qualifying Visualization

Script Python de visualisation des données de qualification pour la **F1 Academy**, générant un graphique des écarts au temps de la pole position.

---

## 📦 Dépendances

```bash
pip install pandas numpy matplotlib pillow
```

| Librairie      | Usage                                      |
|----------------|--------------------------------------------|
| `pandas`       | Structuration et manipulation des données  |
| `numpy`        | Calcul des graduations de l'axe x          |
| `matplotlib`   | Génération du graphique                    |
| `PIL (Pillow)` | Import (prévu pour les images/logos)       |

---

## 📁 Structure attendue du projet

```
projet/
├── script.py
├── logo/
│   ├── redbull.png
│   ├── ferrari.png
│   └── ...
└── F1-Academy-Livrery/
    └── background-false/
        ├── RedBull.png
        ├── Ferrari.png
        └── ...
```

---

## 📊 Données

Les données sont définies manuellement dans le dictionnaire `pilot_data` et contiennent pour chaque pilote :

| Champ          | Description                              |
|----------------|------------------------------------------|
| `ShortName`    | Nom court (ex: `A.PALMOWSKI`)            |
| `FullName`     | Nom complet                              |
| `Code`         | Code 3 lettres (ex: `PAL`)              |
| `Number`       | Numéro de voiture                        |
| `Team`         | Équipe                                   |
| `QualiTimeR1`  | Temps de qualification au format `m:ss.ms` |
| `Sector1/2/3`  | Temps par secteur (en secondes)          |
| `LapNumber`    | Numéro du tour chronométré               |
| `SpdTrap`      | Vitesse au speed trap (KPH, optionnel)   |

---

## ⚙️ Fonctions

### `convertStrTime(toConvert)`
Convertit une colonne de temps au format `m:ss.ms` en valeur numérique (secondes décimales), stockée dans une nouvelle colonne `{toConvert}Int`.

### `gap(lapTime)`
Calcule l'écart de chaque pilote par rapport au meilleur temps, et le stocke dans la colonne `Gap`.

### `showQualiData()`
Affiche dans le terminal le classement des pilotes du plus rapide au plus lent, avec leur temps, leurs secteurs et leur écart à la pole.

### `show_gap_graphic()`
Génère un **graphique à barres horizontales** représentant l'écart de chaque pilote par rapport à la pole position.

- Les barres sont colorées selon la couleur de l'équipe
- L'axe x affiche les temps au format `m:ss.00`
- Le texte à droite de chaque barre indique le temps de la pole ou l'écart (`+ x.xxx s`)
- Les pilotes sont classés du plus rapide (haut) au plus lent (bas)

---

## ▶️ Utilisation

```bash
python script.py
```

Les deux fonctions `showQualiData()` et `show_gap_graphic()` sont appelées automatiquement à l'exécution.

---

## 🎨 Personnalisation

Les couleurs et logos des équipes sont définis dans `team_colors` :

```python
team_colors = {
    "McLaren": ["#FB7F09", "logo/mclaren.png"],
    ...
}
```

Les livrées des monoplaces par pilote sont référencées dans `driver_cars` (disponibles pour un usage futur dans le graphique).
