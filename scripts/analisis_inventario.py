
import pandas as pd
import matplotlib.pyplot as plt

def generar_reporte(path_csv):
    df = pd.read_csv(path_csv)
    
    # Cálculos analíticos
    df['total_linea'] = df['cantidad'] * df['costo_unitario']
    ingresos_netos = df['total_linea'].sum()
    top_producto = df.groupby('instrumento')['cantidad'].sum().idxmax()
    
    # Agrupación temporal alternativa usando to_datetime
    df['mes'] = pd.to_datetime(df['fecha_venta']).dt.to_period('M')
    historico_mensual = df.groupby('mes')['total_linea'].sum()
    
    # Consola
    print(f"Monto Total: {ingresos_netos}")
    print(f"Top Ventas: {top_producto}")
    
    # Gráfico (Formato horizontal para diferenciarlo aún más)
    historico_mensual.plot(kind='barh', color='darkmagenta')
    plt.title('Reporte Mensual de Facturación')
    plt.xlabel('Ingresos ($)')
    plt.ylabel('Periodo')
    plt.tight_layout()
    plt.savefig('resultados/grafico_ventas.png')
    
    # Reporte
    with open('resultados/resumen_ventas.txt', 'w') as f:
        f.write(f"Monto Total: {ingresos_netos}\nTop Ventas: {top_producto}\n")

if __name__ == '__main__':
    generar_reporte('inventario_musica.csv')
