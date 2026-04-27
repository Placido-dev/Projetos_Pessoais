import pymysql, pymysql.cursors
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from dotenv import load_dotenv
import os

load_dotenv()

# ── paleta ────────────────────────────────────────────
BG_FIG   = '#0d0d1a'
BG_AX    = '#16213e'
GRID     = '#1e2a45'
AZUL     = '#4fc3f7'
VERDE    = '#69f0ae'
VERMELHO = '#ff5252'
AMBAR    = '#ffd740'
ROXO     = '#ce93d8'
CINZA    = '#607080'
TEXTO    = '#e0e0e0'

COR_STATUS = {
    'completed'    : VERDE,
    'watching'     : AZUL,
    'plan_to_watch': CINZA,
    'paused'       : ROXO,
    'dropped'      : VERMELHO,
}

# ── tema global ───────────────────────────────────────
plt.rcParams.update({
    'figure.facecolor' : BG_FIG,
    'axes.facecolor'   : BG_AX,
    'axes.edgecolor'   : GRID,
    'axes.labelcolor'  : CINZA,
    'axes.titlecolor'  : TEXTO,
    'axes.titlesize'   : 11,
    'axes.titleweight' : 'bold',
    'axes.titlepad'    : 12,
    'axes.grid'        : False,
    'xtick.color'      : CINZA,
    'ytick.color'      : CINZA,
    'text.color'       : TEXTO,
    'font.family'      : 'monospace',
    'font.size'        : 9,
})

# ── buscar dados ──────────────────────────────────────
conn = pymysql.connect(
    host='localhost',
    user=os.getenv('user'),
    password=os.getenv('password'),
    database=os.getenv('database'),
    cursorclass=pymysql.cursors.DictCursor
)

with conn.cursor() as cur:

    cur.execute('''SELECT status, COUNT(*) AS total
                   FROM series_favoritas WHERE deleted_at IS NULL
                   GROUP BY status''')
    status_map = {r['status']: r['total'] for r in cur.fetchall()}

    cur.execute('''SELECT name, rating FROM series_favoritas
                   WHERE deleted_at IS NULL AND rating IS NOT NULL
                   ORDER BY rating DESC, name ASC LIMIT 5''')
    top = cur.fetchall()

conn.close()

# ── métricas para os cards ────────────────────────────
total      = sum(status_map.values())
n_completed= status_map.get('completed', 0)
n_watching = status_map.get('watching', 0)
n_dropped  = status_map.get('dropped', 0)

# ── ordenar status pra barra horizontal (do maior pro menor) ──
# invertido porque barh desenha de baixo pra cima
ordem = ['dropped', 'paused', 'plan_to_watch', 'watching', 'completed']
lb_st = [s for s in ordem if s in status_map]
vl_st = [status_map[s] for s in lb_st]
cx_st = [COR_STATUS[s] for s in lb_st]

# ── top 5: dados ──────────────────────────────────────
top_names   = [t['name']   for t in top][::-1]   # inverte: maior em cima
top_ratings = [t['rating'] for t in top][::-1]
top_cores   = [AMBAR if r == 10 else AZUL for r in top_ratings]

# ── figura com layout customizado ─────────────────────
# GridSpec: 1 linha pros cards (altura menor) + 2 linhas pros gráficos
fig = plt.figure(figsize=(14, 8))
fig.patch.set_facecolor(BG_FIG)
gs = GridSpec(3, 4, figure=fig,
              height_ratios=[0.7, 2, 2],
              hspace=0.55, wspace=0.4)

fig.suptitle('Painel — series_favoritas',
             fontsize=15, fontweight='bold',
             color=TEXTO, y=0.98)

# ── linha 0: 4 metric cards ───────────────────────────
def draw_card(ax, valor, label, cor):
    ax.set_facecolor(BG_AX)
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values(): sp.set_visible(False)
    ax.text(0.08, 0.62, str(valor),
            transform=ax.transAxes,
            fontsize=28, fontweight='bold', color=cor,
            ha='left', va='center')
    ax.text(0.08, 0.22, label,
            transform=ax.transAxes,
            fontsize=10, color=CINZA,
            ha='left', va='center')

cards = [
    (n_completed, 'completed', VERDE),
    (n_watching,  'watching',  AZUL),
    (n_dropped,   'dropped',   VERMELHO),
    (total,       'total',     TEXTO),
]
for i, (v, l, c) in enumerate(cards):
    draw_card(fig.add_subplot(gs[0, i]), v, l, c)

# ── linha 1: distribuição por status (ocupa 4 colunas) ──
ax1 = fig.add_subplot(gs[1, :])
ax1.set_facecolor(BG_AX)
for sp in ax1.spines.values(): sp.set_edgecolor(GRID)

bars = ax1.barh(lb_st, vl_st, color=cx_st, height=0.55, zorder=2)
# valor à direita de cada barra
for b, v in zip(bars, vl_st):
    ax1.text(b.get_width() + max(vl_st)*0.015,
             b.get_y() + b.get_height()/2,
             str(v), va='center', color=TEXTO, fontsize=10)
ax1.set_title('Distribuição por status', loc='left')
ax1.set_xlim(0, max(vl_st) * 1.15)
ax1.tick_params(left=False, bottom=False)
ax1.xaxis.set_major_locator(plt.MaxNLocator(integer=True))

# ── linha 2: top 5 séries (ocupa 4 colunas) ───────────
ax2 = fig.add_subplot(gs[2, :])
ax2.set_facecolor(BG_AX)
for sp in ax2.spines.values(): sp.set_edgecolor(GRID)

bars2 = ax2.barh(top_names, top_ratings,
                 color=top_cores, height=0.55, zorder=2)
# nota + estrela ao lado das que têm 10
for b, r in zip(bars2, top_ratings):
    txt = f'{r} ★' if r == 10 else str(r)
    cor_txt = AMBAR if r == 10 else TEXTO
    ax2.text(b.get_width() + 0.15,
             b.get_y() + b.get_height()/2,
             txt, va='center', color=cor_txt,
             fontsize=11, fontweight='bold')
ax2.set_title('Top 5 — séries mais bem avaliadas', loc='left')
ax2.set_xlim(0, 11.5)
ax2.set_xticks(range(0, 11, 2))
ax2.tick_params(left=False, bottom=False)

plt.savefig('painel_series.png', dpi=150,
            bbox_inches='tight', facecolor=BG_FIG)
plt.show()