import streamlit as st
import random
import pandas as pd

def conceptos_app():
    st.title('Conceptos financieros básicos')
    st.subheader('A continuación, se va a explicar como se estudian las finanzas')
    st.write('----------')


    seleccion_info = ['','Fundamentos de los mercados financieros','Tipos de activos financieros','Análisis fundamental',
                      'Análisis técnico','Gestión del riesgo','Teoría de carteras','Economía y Macroeconomía','Psicología del mercado', 
                      'Trading','Inversión a largo plazo','Finanzas Cuantitativas']
    
    
    seleccion = st.selectbox('Selecciona el sector de finanzas que desea aprender:', seleccion_info)
    if seleccion == '':
        st.warning('Debes seleccionar una opción')


    elif seleccion == 'Fundamentos de los mercados financieros':
        st.write('Los **mercados financieros** son entornos físicos o digitales donde se compran y venden activos (acciones, bonos o idivisas. Su **función principal** es canalizar el capital desde los ahorradores hacia quienes necesitan financiación, permitiendo la inversión y el crecimiento económico')
        st.write('----------')
        st.markdown(""" 
        - **Bolsa de valores:** Mercado donde se compran y venden activos financieros, como acciones, bonos y ETFs. 
        - **Acción (Stock):** Parte de la propiedad de una empresa. Al comprar una acción, te conviertes en propietario de una pequeña fracción de la compañía.
        - **Índice bursátil:** Indicador que mide la evolución de un grupo de acciones representativas de un mercado o sector, por ejemplo: IBEX 35 o S&P 500.
        - **ETF (Exchange Traded Fund):** Fondo de inversión que cotiza en bolsa y puede comprarse y venderse como una acción. Suele replicar un índice o sector específico.
        - **Fondo de inversión:** Vehículo que reúne el dinero de varios inversores para invertirlo de forma conjunta en diferentes activos financieros.
        - **Bono:** Instrumento de deuda mediante el cual un inversor presta dinero a una empresa o gobierno a cambio de recibir intereses y recuperar el capital en una fecha futura.
        - **Materias primas:** Recursos naturales utilizados como base para la producción de bienes, por ejemplo: oro, plata, petróleo o trigo.
        - **Divisas:** Monedas utilizadas en distintos países y que pueden intercambiarse entre sí en el mercado de divisas (Forex). Ejemplos: euro (EUR) o dólar estadounidense (USD). 
        - **Criptomonedas:** Activos digitales que utilizan criptografía y tecnología blockchain para registrar y verificar transacciones, por ejemplo: Bitcoin.
        - **Capitalizacióon bursátil:** Valor total de mercado de una empresa cotizada. Se calcula multiplicando el precio de una acción por el número total de acciones en circulación.
        - **Liquidez:** Facilidad con la que un activo puede comprarse o venderse rápidamente sin afectar significativamente a su precio.
        - **Oferta y demanda:** Principio económico según el cual el precio de un activo aumenta cuando hay más compradores que vendedores y disminuye cuando ocurre lo contrario.
        - **Market Maker:** Entidad financiera que proporciona continuamente precios de compra y venta para un activo con el objetivo de facilitar las operaciones y aportar liquidez al mercado.
        - **Spread:** Diferencia entre el precio de compra (bid) y el precio de venta (ask) de un activo financiero.
        - **Volumen de negociación:** Cantidad de unidades de un activo que se compran y venden durante un período determinado. Un volumen alto suele indicar mayor actividad e interés del mercado.        
                    """)
        st.write('----------')


    elif seleccion == 'Tipos de activos financieros':
        st.write('Un **activo financiero** es un título o contrato digital que otorga a su comprador el derecho a recibir ingresos futuros por parte del vendedor')
        concepto_activos = st.radio('Elija el concepto a definir:',
                        ['Dinero en efectivo','Renta Variable','Renta Fija','Activos Alternativos'])
        st.write('----------')
        if concepto_activos == 'Dinero en efectivo':
            st.subheader('Dinero en efectivo')
            st.write('Es el activo con mayor liquidez')
        elif concepto_activos == 'Renta Variable':
            st.subheader('Renta Variable')
            st.write('Es un tipo de inversión donde se presta dinero a una empresa o al Estado a cambio de decibir intereses fijos y recuperar tu dinero en una fecha determinada.')
        elif concepto_activos == 'Renta Fija':
            st.subheader('Renta Fija')
            st.write('Es un tipo de inversión donde la rentabilidad no está garantizada, ya que se invierte en activos cuyo valor puede subir o bajar, como acciones.')
        elif concepto_activos == 'Activos Alternativos':
            st.subheader('Activos Alternativos')
            st.write('Son inversiones que no pertenecen a la renta fija ni variable tradicional y se suelen usar para diversificar.')
        st.write('----------')


    elif seleccion == 'Análisis fundamental':
        st.write('El **análisis fundamental** es una metodología utilizada para determinar el valor real o intrínseco de una empresa mediante el estudio de su situación financiera, económica y competitiva. Su **objetivo** es identificar si una acción está sobrevalorada o infravalorada en el mercado.')
        concepto = st.radio('Elija el concepto a definir:',
                        ['Estados financieros','Ratios','Conceptos Fundamentales'])
        st.write('----------')

        if concepto == 'Estados financieros':
            st.write('Los **estados financieros** son documentos que muestran la situación económica y financiera de una empresa.')
            st.subheader('Balance de Situación')
            st.write('Refleja los bienes, derechos y obligaciones de una empresa en un momento determinado.')
            st.write('Los componentes principales son los siguientes:')
            st.markdown("""
            - **Activo:** bienes y derechos que posee la empresa.
            - **Pasivo:** deudas y obligaciones.
            - **Patrimonio neto:** Recursos propios de la empresa.            
                        """)
            st.write('----------')
            st.subheader('Cuenta de Resultados')
            st.write('Muestra los ingresos, gastos y beneficios obtenidos durante un período determinado.')
            st.write('Los elementos principales son los siguientes:')
            st.markdown("""
            - Ingresos por ventas
            - Costes de producción
            - Gastos operativos 
            - Impuestos
            - Beneficio neto         
                        """)
            st.write('----------')
            st.subheader('Estado de Flujos de Efectivo')
            st.write('Indica cómo entra y sale el dinero de la empresa.')
            st.write('Se divide en:')
            st.markdown("""
            - Actividades operativas
            - Actividades de inversión
            - Actividades de financiación
                        """)
            
            st.write('--------------------')
            with st.expander('Ver Resumen'):
                st.image('imagenes/estados financieros.png', caption='Resumen de los estados financieros')
            

        elif concepto == 'Ratios':
            st.subheader('Ratios de Rentabilidad')
            st.write('**ROE (Return on Equity)**')
            st.write('Mide la rentabilidad obtenida sobre los recursos propios. Cuanto mayor ROE, mejor utilización del capital de los accionistas.')
            with st.expander('Ver Fórmula ROE'):
                st.image('imagenes/imagenRoe.png', caption='Fórmula ROE')
            st.write('----------')
            st.write('**ROA (Return on Assets)**')
            st.write('Mide la rentabilidad generada por todos los activos de la empresa.')
            with st.expander('Ver Fórmula ROA'):
                st.image('imagenes/imagenRoa.png', caption='Fórmula ROA')
            st.write('----------')
            st.write('**Ratios de Liquidez**')
            st.write('Ratio corriente: Mide la capacidad de la empresa para afrontar sus obligaciones a corto plazo. Cuando su valor es mayor que 1 es generalmente saludable, en caso contrario existe una posible dificultas para pagar deudas a corto plazo')
            with st.expander('Ver Fórmula Ratio Corriente'):
                st.image(r"imagenes/ratio_corriente.png", caption='Fórmula Ratio Corriente')
            st.write('----------')
            st.write('**Ratios de Endeudamiento**')
            st.write('Ratio de Deuda: Indica qué porcentaje de los activos está financiado mediante deuda.')
            with st.expander('Ver Fórmula Ratio de Endeudamiento'):
                st.image(r"imagenes/ratio_endeudamiento.png", caption='Fórmula Ratio de Deuda')
            st.write('----------')
            st.write('**Ratios de Valoración**')
            st.write('PER (Price to Earnings Ratio): Relaciona el precio de una acción con el beneficio generado por acción. Cuando PER es alto las expectativas de crecimiento son elevadas, en caso contrario hay problemas en la empresa o existe una posible infravaloración')
            with st.expander('Ver Fórmula Ratio PER'):
                st.image('imagenes\RATIO_PER.png', caption='Fórmula PER')
            st.write('**P/B (Price to Book)**')
            st.write('Compara el valor de mercado de la empresa con su valor contable')
            with st.expander('Ver Fórmula Ratio P/B'):    
                st.image(r"imagenes/ratio_PB.png", caption='Fórmula P/B')
        
        elif concepto == 'Conceptos Fundamentales':
            st.subheader('Beneficio por acción (BPA o EPS)')
            st.write('Representa el beneficio generado por cada acción en circulación.')
            st.subheader('Dividendos')
            st.write('Parte de los beneficios que la empresa distribuye a sus accionistas.')
            st.subheader('Margen de Beneficio')
            st.write('Mide qué porcentaje de los ingresos se convierte en beneficio.')
            st.subheader('Valor intrínseco')
            st.write('Valor teórico de una empresa calculado a partir de sus fundamentales financieros. Los inversores utilizan este concepto para comparar el valor real estimado con el precio actual de mercado.')
        st.write('----------')


    elif seleccion == 'Análisis técnico':
        st.write('El **análisis técnico** es un método para evaluar los movimientos pasados del precio y el volumen de un activo financiero con el objetivo de predecir sus movimientos futuros. Este análisis se basa en la idea de que los patrones históricos pueden repetirse y que los precios reflejan toda la información disponible en el mercado.')
        pregunta = st.radio('Los analistas técnicos intentan responder preguntas como',
                 ['¿La tendencia es alcista o bajista?','¿Es un buen momento para comprar?',
                  '¿Cuánta fuerza tiene el movimiento del precio?','¿Cuál es la dirección suavizada del precio?',
                  '¿El activo está sobrecomprado o sobrevendido?','¿Está cambiando la tendencia?',
                  '¿Cuánta volatilidad tiene el mercado?','¿Qué tan rápido se mueve el precio?',
                  '¿Qué tan inestable es el precio?','¿Qué patrones visuales forma el precio?'])
        st.write('----------')

        if pregunta == '¿La tendencia es alcista o bajista?':
            st.write('Para responder esta pregunta debemos comprender el siguiente concepto:')
            st.subheader('Tendencia')
            st.write('Dirección general en la que se mueve el precio de un activo durante un periodo de tiempo. La mayoría de las estrategias se basan en identificarla y seguirla')
            tendencia = st.selectbox('Elija un tipo de tendencia:',['Alcista','Bajista','Lateral'])
            st.write('---------')
            if tendencia == 'Alcista':
                st.subheader('Tendencia Alcista (Bullish)')
                st.write('El precio sube en el tiempo (máximos y mínimos crecientes).')
            elif tendencia == 'Bajista':
                st.subheader('Tendencia Bajista (Bearish)')
                st.write('El precio baja en el tiempo (máximos y mínimos decrecientes).')
            elif tendencia == 'Lateral':
                st.subheader('Tendencia Lateral')
                st.write('el precio se mueve en un rango sin dirección clara. Muy frecuente en mercados indecisos.')
            st.write('--------------------')
            with st.expander('Ver Comparación de las 3 Tendencias'):
                st.image(r'imagenes/tendencias.png', caption='Comparación Tendencias')
            st.write('---------')

        elif pregunta == '¿Es un buen momento para comprar?':
            st.write('Para responder esta pregunta debemos conocer los siguientes conceptos:')
            st.subheader('Soportes y Resistencias')
            st.write('**Soporte:** Zona de rebote hacia arriba, donde aparecen compradores, ya que estos consideran que el precio es barato. U.n ejemplo puede ser cuando una acción cae repetidamente hasta 50 euros y luego rebota hacia arriba de nuevo. Ese pico mínimo es un soporte.')
            st.write('**Resistencia:** Zona de rechazo hacia abajo, donde aparecen vendedores, porque consideran que ese precio en caro. Un ejemplo sería si una acción sube varias veces a 100 euros y vuelve a caer, ese pico máximo sería una resistencia')
            with st.expander('Ejemplo de Soportes y Resistencias'):
                st.image('imagenes/soportes y resistencias.png', caption = 'Identificando soportes y resistencias')

        elif pregunta == '¿Cuánta fuerza tiene el movimiento del precio?':
            st.write('Para responder esta pregunta debemos conocer el siguiente concepto:')
            st.subheader('Volumen')
            st.write('El volumen nos ayuda a identificar la cantidad de negociación real, confirmando si un movimiento es real o es débil')
            st.markdown("""
            - **Subida + volumen alto** -> Movimiento fuerte (alcista)
            - **Subida + volumen bajo** -> Movimiento débil 
            - **Caída + volumen alto** -> Presión bajista fuerte
                        """)
            with st.expander('Ver Ejemplo'):
                st.image(r"imagenes/volumen.png", caption = 'Fuerza del movimiento en función del volumen')
        
        elif pregunta == '¿Cuál es la dirección suavizada del precio?':
            st.write('El siguiente concepto es necesario para responder a esta pregunta:')
            st.subheader('Medias Móviles')
            st.write('Este indicador analiza la tendencia suavizada del mercado, con el objetivo de eliminar ruido y detectar tendencias claras')
            st.write('Los tipos principales de medias móviles son los siguientes:')
            st.markdown("""
            - **SMA (Media Móvil Simple)**: Da el mismo peso a todos los días del período. Es ideal para medir tendencias a largo plazo.
            - **EMA (Media Móvil Exponencial)**: Da más importancia a los precios más recientes, por lo que reacciona más rápido a los movimientos bruscos del mercado
                        """)
            with st.expander('Ver comparación entre tipos de medias Móviles'):
                st.image('imagenes\medias_moviles.jpg', caption = 'Comparación entre los tipos principales de medias móviles')

        elif pregunta == '¿El activo está sobrecomprado o sobrevendido?':
            st.write('El concepto necesario para responder a esta pregunta es el siguiente:')
            st.subheader('RSI (Relative Strength Index)')
            st.write('También conocido como Índice de Fuerza Relativa, este mide el equilibrio entre compras y ventas con el objetivo de detectar posibles giros del precio')
            st.write('En función de sus valores, el RSI se interpreta diferente')
            st.markdown("""
            - **RSI > 70** -> Sobrecompra (posible caída)
            - **RSI < 30** -> Sobreventa (posible rebore)
            - **40 < RSI < 60** -> Mercado neutro
                        """)
            with st.expander('Ver Índice Fuerza Relativa (RSI) '):
                st.image(r"imagenes\rsi.jpg", caption = 'Índice de fuerza Relativa (RSI)')

        elif pregunta == '¿Está cambiando la tendencia?':
            st.write('Para identificar los cambios de tendencia, se emplea el siguiente concepto:')
            st.subheader('MACD (Moving Average Convergence Divergence)')
            st.write('Este analiza el momentum (velocidad del movimiento del precio) y el cambio de tendencia, para detectar los cambios de tendencia de forma temprana.')
            st.write('Este indicador, se compone visualmente de 3 elementos clave:')
            st.markdown("""
            - **Línea MACD**: Mide la distancia entre dos medias móviles exponenciales (generalmente de 12 y 26 periodos) 
            - **Línea de señal**: Es una media móvil de la propia línea MACD (habitualmente de 9 periodos). Su función es suavizar el movimiento y actuar como detonante de alertas
            - **Histograma**: Muestra la distancia gráfica entre la línea MACD y la línea de señal. Cuando las barras son verdes y crecen, el impulso alcista es fuerte. Si se vuelven rojas, domina la presión vendedora
                        """)
            st.write('Existen las siguientes dos señales:')
            st.markdown("""
            - Cuando el MACD cruza hacia arriba la señal -> Compra
            - Cuando el MACD cruza hacia abajo la señal -> Venta
                        """)
            with st.expander('Ver Señales de compra o venta en función del MACD '):
                st.image('imagenes\MACD.webp', caption = 'Señales de compra o venta en función del MACD')

        elif pregunta == '¿Cuánta volatilidad tiene el mercado?':
            st.write('Teniendo en cuenta que la volatilidad mide la variación del precio en el tiempo para poder evaluar el riesgo del activo, el siguiente concepto va más allá y mide también las posibles explosiones de precio:')
            st.subheader('Bandas de Bollinger')
            st.write('Analizando las bandas superior, inferior y la media móvil, las Bandas de Bollinger mdiden la expansión o contracción del precio')
            st.write('Estas bandas se puede inter pretar de diferentes formas:')
            st.markdown("""
            - **Precio en banda superior** -> Posible sobrecompra
            - **Precio en banda inferior** -> Posible sobreventa
            - **Bandas estrechas** -> Posible gran movimiento futuro
                       """)
            with st.expander('Ver Ejemplo de Bandas de Bollinger'):
                st.image(r"imagenes\bandas-de-bollinger.jpg", caption = 'Ejemplo de Bandas de Bollinger')

        elif pregunta == '¿Qué tan rápido se mueve el precio?':
            st.write('Para respondes a esta pregunta, es necesario conocer el sogiente concepto:')
            st.subheader('Momentum')
            st.write('Este mide la velocidad del movimiento del precio, con el objetivo de detectar patrones fuertes. Incluye tanto la fuerza del movimiento como la comparación entre subidas rápidas y lentas')
        
        elif pregunta == '¿Qué tan inestable es el precio?':
            st.write('La inestabilidad del precio viene definida por el siguiente concepto:')
            st.subheader('Volatilidad')
            st.write('Se emplea para evaluar el riesgo del activo, midiendo la variación del precio en el tiempo')
            st.markdown("""
            - **Alta volatilidad** -> activos más arriesgados
            - **Baja volatilidad** -> activos más estables
                        """)

        elif pregunta == '¿Qué patrones visuales forma el precio?':
            st.write('Existen formas repetitivas en los gráficos, que ayudan a anticipar movimientos futuros. A continuación, de mencionan algunas de ellas:')
            st.subheader('Patrones gráficos')
            st.markdown("""
            - **Doble techo** -> Tendencia bajista
            - **Doble suelo** -> Tendencia alcista
            - **Hombro-cabeza-hombro** -> Señal bajista fuerte
            - **Triángulo ascendente** -> Ruptura alcista
            - **Triángulo descentende** -> Ruptura bajista
                        """)
            with st.expander('Ver Ejemplos de patrones visuales en bolsa'):
                st.image('imagenes\patrones_graficos.jpg', caption = 'Algunos ejemplos de patrones visuales en bolsa')


    elif seleccion == 'Gestión del riesgo':
        st.write('La **gestión del riesgo** es el proceso de identificar, evaluar y controlar los riesgos asociados con las inversiones financieras. Esto puede incluir estrategias como la diversificación, el uso de derivados para cubrir posiciones y la implementación de límites de pérdida para proteger el capital. El **objetivo** no es eliminar el riesgo, sino gestionarlo de forma eficiente para maximizar la rentabilidad sin asumir riesgos excesivos.')
        st.write('----------')
        punto_a_desarrollar = st.radio('Puntos clave sobre la gestión del riesgo:',['**Tipos principales de riesgo financiero**','**Pasos a seguir para identificar riesgos**'])
        st.write('----------')

        if punto_a_desarrollar == '**Tipos principales de riesgo financiero**':
            st.subheader('Tipos de riesgo financiero')
            st.write('**1. Riesgo de mercado**: Posibilidad de que un inversor o empresa sufra pérdidas debido a cambios en los precios de los mercados financieros. Estos cambios pueden afectar a acciones, bonos, divisas o materias primas.')
            with st.expander('**Ver los tipos principales de riesgo de mercado**'):
                st.markdown("""
                - **Riesgo de tipo de interés**: Es el riesgo de que los cambios en los tipos de interés afecten al valor de los activos financieros, especialmente bonos y préstamos. También afecta a hipotecas o préstamos bancarios.
                - **Riesgo de tipo de cambio (riesgo cambiario)**: Ocurre cuando las variaciones en las divisas afectan al valor de inversiones o transacciones internacionales.
                - **Riesgo de precio de acciones (riesgo de renta variable)**: Es el riesgo de que el precio de las acciones suba o baje por factores del mercado.
                - **Riesgo de materias primas (commodity risk)**: Es el riesgo de cambios en el precio de materias primas como petróleo, gas, oro o alimentos.
                            """)
            st.write('----------')
            st.write('**2. Riesgo de crédito**: Posibilidad de que una de las partes en una operación financiera no cumpla con sus obligaciones de pago, es decir, que no devuelva un préstamo, no pague intereses o incumpla un contrato financiero. Es uno de los riesgos más importantes en bancos, empresas y mercados de deuda, porque afecta directamente a la recuperación del dinero invertido o prestado. Cuanto mayor es la probabilidad de impago, mayor es el riesgo de crédito.')
            st.write('Factores que influyen en el riesgo de crédito:')
            st.markdown("""
            1. Solvencia del deudor
            2. Nivel de endeudamiento
            3. Historial crediticio
            4. Condiciones económicas generales
            5. Plazo de préstamo
                        """)
            with st.expander('**Ejemplos de riesgo de créditos**'):
                st.markdown("""
                - **Préstamo bancario**: Un banco concede un préstamo de 10.000€ a una persona. Si la persona pierde su trabajo y deja de pagar, el banco sufre una pérdida parcial o total del dinero prestado.
                - **Compra de bonos**: Una empresa emite bonos para financiarse y un inversor compra esos bonos esperando recibir intereses. Si la empresa quiebra o no genera suficiente liquidez, puede no pagar los intereses o el principal.
                - **Riesgo en empresas (clientes)**: Una empresa vende productos a otra “a crédito” (pago en 30 días). Si el cliente no paga la factura, la empresa pierde ingresos y puede tener problemas de liquidez.
                            """)
            
            st.write('----------')
            st.write('**3. Riesgo de liquidez**: Posibilidad de que una empresa o entidad financiera no pueda convertir sus activos en dinero en efectivo rápidamente sin sufrir pérdidas significativas, o que directamente no tenga suficiente efectivo para cumplir con sus obligaciones a corto plazo. El riesgo de liquidez no depende de “ser rico”, sino de tener capacidad de pago inmediata.')
            st.write('Formas de gestionar el riesgo de liquidez:')
            st.markdown("""
            - Mantener reservas de efectivo o activos líquido
            - Líneas de crédito disponibles
            - Planificación de flujos de caja
            - Diversificación de vencimientos de deuda
            - Supervisión constante del balance entre activos líquidos y obligaciones
                        """)
            with st.expander('**Ejemplos de riesgo de liquidez**'):
                st.markdown("""
                - **Banco con retirada masiva de depósitos (*bank run*)**: Muchos cl y entes quieren retirar su dinero al mismo tiempo y el banco tiene parte del dinero invertido en préstamos a largo plazo. Resultado: no puede devolver el dinero inmediatamente, aunque sea solvente.
                - **Empresa con problemas de caja**: Una empresa tiene activos (máquinas, edificios), pero no efectivo y debe pagar nóminas o proveedores este mes. Si no puede vender activos rápidamente, entra en problemas de liquidez.
                - **Activos difíciles de vender**: Una inversión en inmuebles o activos poco negociados, aunque tengan valor alto, pueden tardar meses en venderse. esultado: no se puede obtener efectivo rápido cuando se necesita
                            """)
                
            st.write('----------')
            st.write('**4. Riesgo operativo**: Riesgo de sufrir pérdidas debido a fallos internos en los procesos, personas, sistemas o por eventos externos inesperados. A diferencia de otros riesgos financieros, este no depende directamente del mercado, sino del funcionamiento interno de la organización.')
            st.write('Formas de gestionar el riesgo operativo:')
            st.markdown("""
            - Controles internos y auditorías
            - Automatización de procesos para reducir errores humanos
            - Sistemas de ciberseguridad
            - Planes de contingencia y continuidad del negocio
            - Formación del personal
                        """)
            with st.expander('**Tipos de riesgo operativo**'):
                st.markdown("""
                - **Errores humanos**: Fallos en la ejecución de tareas o mala gestión de datos o cálculos incorrectos.
                - **Fallos tecnológicos**: Caídas de sistemas informáticos o errores de software o ciberataques.
                - **Fallos en procesos internos**: Falta de control interno o procedimientos mal diseñados.
                - **Eventos externos**: Fraude, desastres naturales o crisis inesperadas.
                            """)


        elif punto_a_desarrollar == '**Pasos a seguir para identificar riesgos**':
            st.subheader('Pasos para identificar riesgos')
            with st.expander('**1. Detecctión**'):
                st.write('Consiste en detectar qué riesgos afectan a la empresa o inversión. Aquí se analizan factores internos (gestión, procesos) y externos (mercado, economía, regulación).')
            with st.expander('**2. Medición y Análisis**'):
                st.write('Una vez identificado, se cuantifica el riesgo para entender su impacto potencial')
                st.write('Herramientas comunes:')
                st.markdown("""
                - **VaR (Value at Risk)**: Estima la pérdida máxima esperada en un periodo con un nivel de confianza.
                - **Volatilidad**: Mide cuánto varía el valor de un activo.
                - **Análisis de escenarios**: Estudia qué pasaría en situaciones extremas.'
                            """)
            with st.expander('**3. Control y Mitigación**'):
                st.write('Rstrategias para reducir su impacto:')
                st.markdown("""
                - **Diversificación**: Invertir en distintos activos para no depender de uno solo.
                - **Cobertura (hedging)**: Uso de derivados como futuros u opciones para proteger inversiones.
                - **Límites de riesgo**: Establecer cuánto riesgo máximo se puede asumir.
                            """)
            with st.expander('**4. Monitorización continua**'):
                st.write('El riesgo no es estático, cambia constantemente, por eso es necesario un seguimiento continuo para ajustar estrategias según las condiciones del mercado.')



        
        



    elif seleccion == 'Teoría de carteras':
        st.header('Teoría de Carteras')
        st.write('La **teoría de carteras** es una rama de las finanzas que estudia cómo combinar diferentes inversiones para obtener la mejor relación posible entre rentabilidad y riesgo. Cuando una persona invierte en bolsa, una de las primeras preguntas que debe hacerse es: ¿es mejor invertir todo mi dinero en una sola empresa o repartirlo entre varias? La teoría de carteras responde precisamente a esta cuestión.')
        st.write('----------')
        st.write('Los conceptos clave son los siguientes:')
        st.markdown("""
        1) Cartera de inversión
        2) Diversificación
        3) Perfil del Inversor según el riesgo y la rentabilidad
        4) Frontera Eficiente
                    """)
        
        numero = st.number_input('Elige el número que desea desarrollar', min_value = 0, max_value = 4, step = 1)
        st.write('---------')
        
        if numero == 0:
            st.warning('Debe introducir un número del 1 al 4')

        elif numero == 1:
            st.subheader("Cartera de inversión")
            st.write('Una cartera de inversión es el conjunto de activos donde una persona tiene invertido su dinero')
            with st.expander('Ver ejemplos de activos:'):
                st.markdown("""
                - 📈 Acciones
                - 💰 Bonos
                - 📊 ETFs
                - 🏦 Fondos de inversión
                - 🥇 Oro y materias primas
                - 💵 Efectivo
                            """)
        elif numero == 2:
            st.subheader('Diversificación')
            st.write('Consiste en repartir el dinero entre varias inversiones para reducir el riesgo.')
            st.write('Las **ventajas de la diversificación** son las siguientes')
            st.markdown("""
            - Menor dependencia de una sola empresa.
            - Reducción del impacto de pérdidas individuales.
            - Mayor estabilidad a largo plazo.
                        """)
        
        elif numero == 3:
            st.subheader('Perfil del Inversor según el riesgo y la rentabilidad')
            st.write('Cada persona tiene una tolerancia distinta al riesgo, por tanto conocer el propio perfil es fundamental para construir una cartera adecuada.')
            perfil = st.selectbox('Seleccione cuál de los 3 perfiles desea definir:', ['Conservador','Moderado','Agresivo'])
            
            if perfil == 'Conservador':
                st.write('**Características del perfil conservador**:')
                st.markdown("""
                - Prioriza la seguridad.
                - Tolera pocas pérdidas.
                - Busca estabilidad.
                            """)
            elif perfil == 'Moderado':
                st.write('**Características del perfil moderado:**')
                st.markdown("""
                - Equilibrio entre riesgo y rentabilidad.
                - Horizonte de inversión medio-largo.
                            """)
            elif perfil == 'Agresivo':
                st.write('**Características del perfil agresivo:**')
                st.markdown("""
                - Acepta grandes fluctuaciones.
                - Busca maximizar beneficios.
                            """)

        elif numero == 4:
            st.subheader('Frontera Eficiente')
            st.write('La teoría moderna de carteras intenta encontrar la frontera eficiente entre:')
            st.markdown("""
            - La máxima rentabilidad para un riesgo determinado
            - El menor riesgo para una rentabilidad concreta
                        """)
            st.write('**El objetivo de la Frontera Eficiente es construir una cartera optimizada**')



    elif seleccion == 'Economía y Macroeconomía':
        st.subheader('Economía y Macroeconomía')
        st.write('La economía estudia cómo personas, empresas y gobiernos utilizan recursos limitados para satisfacer necesidades.')
        st.markdown("""
        - Consumo
        - Ahorro
        - Producción
        - Inversión
                    """)
        st.write('----------')
        st.subheader("¿Qué es la macroeconomía?")
        st.write('La **macroeconomía** analiza el comportamiento de la economía en su conjunto.')
        st.write('Depende de las siguientes variables:')
        st.markdown("""
        - 📈 PIB
        - 💸 Inflación
        - 🏦 Tipos de interés
        - 👨‍💼 Desempleo
        - 🌎 Comercio internacional
                    """)
        st.write('------')
        st.write('Puede hacer click en los siguientes botones para más información:')
        with st.expander("**PIB (Producto Interior Bruto)**"):
            st.image("imagenes/pib.jpg", caption = 'PIB')
            st.write('Este mide el valor total de bienes y servicios producidos en un país. Además tiene un gran impacto en bolsa. En función de si este crece o cae.')
            pib = st.radio('Elige uno de los dos casos:',['¿Qué ocurre si el PIB crece?', '¿Qué ocurre si el PIB decrece?'])

            if pib == '¿Qué ocurre si el PIB crece?':
                st.write('**La economía es fuerte**')
            else:
                st.write('**La economía es débil**')
            st.write('-------')
            st.write('Si desea ver un gráfico resumen de la evolución del PIB en España en los últimos 10 años pulse el siguiente botón')
            bimagenpib = st.button('Evolución PIB')
            if bimagenpib:
                st.image('imagenes\grafica_pib_espana_2016_2026.png', caption = 'Evolución PIB España 2016-2026')


        with st.expander("**Inflación**"):
            st.write('Se trata del aumento generalizado de los precios. Tiene un gran impacto en bolsa, por lo que es muy importante tenerla controlada.')
            st.image("imagenes/inflacion.jpg", caption = 'Ejemplo de la inflación')

            inf = st.radio('Elige uno de los dos casos:',['Inflación controlada', 'Inflación descontrolada'])

            if inf == 'Inflación controlada':
                st.write('**Impacto positivo en bolsa**')
            else: 
                st.write('**Impacto negativo en bolsa, además de afectar a empresas y consumidores**')
            st.write('-------')
            st.write('Si desea ver un gráfico resumen de la evolución de la inflación en España en los últimos años pulse el siguiente botón')
            bimageninf = st.button('Evolución inflación')
            if bimageninf:
                st.image('imagenes\grafica_inflacion_espana_2016_2026.png', caption = 'Evolución inflación en España 2016 - 2026')




        with st.expander("**Tipos de interés**"):
            st.write('Precio que se paga por pedir dinero prestado.')
            int = st.radio('Elige uno de los dos casos:',['Si suben', 'Si bajan'])

            if int == 'Si suben':
                st.write('**Consecuencias subida tipos de interés:**')
                st.markdown("""
                - Se reduce el consumo
                - Se reduce la inversión
                - Los préstamos son más caros
                            """)
            else: 
                st.write('**Consecuencias bajada tipos de interés:**')
                st.markdown("""
                - Aumenta el consumo
                - Aumenta la inversión
                - Los préstamos son más baratos
                            """)
            st.write('-------')
            st.write('Si desea ver un gráfico resumen de la evolución de los tipos de interés en Europa en los últimos años pulse el siguiente botón')
            bimagenint = st.button('Evolución tipos de interés')
            if bimagenint:
                st.image('imagenes\grafica_tipos_interes_bce_2018_2025.png', caption = 'Evolución tipos de interés Europa 2018 - 2025')




        with st.expander("**Desempleo**"):
            st.write('Mide el porcentaje de personas que quieren trabajar y no encuentran empleo.')
            des = st.radio('Elige uno de los dos casos:',['Bajo desempleo', 'Alto desempleo'])

            if des == 'Bajo desempleo':
                st.write('**Economía saludable**')
            else:
                st.write('**Posible desaceleración económica**')
            st.write('-------')
            st.write('Si desea ver un gráfico resumen de la evolución del desempleo en España en los últimos años pulse el siguiente botón')
            bimagendes = st.button('Evolución desempleo')
            if bimagendes:
                st.image('imagenes\grafica_desempleo_espana_2016_2026.png', caption = 'Evolución desempleo en España 2016 - 2026')


    elif seleccion == 'Psicología del mercado': 
        st.subheader('Psicología del mercado')
        st.write('La **psicología del mercado** se refiere al estudio de cómo las emociones y los comportamientos de los inversores pueden influir en los movimientos del mercado. Esto incluye fenómenos como el miedo, la codicia, el pánico y la euforia, que pueden llevar a decisiones irracionales y a la formación de burbujas o caídas en los precios.')
        st.write('----------')
        st.subheader('Emociones y su control')
        st.write('Las **emociones más comunes** son las siguientes:')
        st.markdown("""
        - 😨 Miedo: Puede provocar ventas precipitadas durante caídas del mercado. Su **consecuencia**: Vender en el peor momento.
        - 🤑 Codicia: Aparece cuando los precios suben rápidamente. Su **consecuencia**: Comprar demasiado tarde pensando que seguirá subiendo para siempre.
        - 😖 Arrepentimiento: Ocurre después de tomar una decisión incorrecta. Su **consecuencia**: Dudar constantemente de futuras inversiones.           
        - 😌 Exceso de confianza: Creer que siempre se puede predecir el mercado. Su **consecuencia**: Asumir riesgos excesivos.          
                                """)
        with st.expander('Haz click si quieres saber más:'):
            st.write('Para controlar las emociones, es importante realizar lo siguiente')
            st.markdown("""
            1) **Tener un plan de inversión**: Definiendo previamente los objetivos, los riesgos aceptados y el horizonte temporal
            2) **Diversificar**: De esta forma se reduce la preocupación por una única inversión.
            3) **Pensar a largo plazo**: Evitando reaccionar a movimientos diarios del mercado.
            4) **Basarse en datos**: Tomando decisiones utilizando análisis y no emociones.
                                    """)
        bimagen = st.button('Observar el ciclo emocional del inversor')
        if bimagen:
            st.image('imagenes\ciclo_emocional.png', caption = 'Ciclo emocional del inversor')

        st.write('---------')
        st.subheader('Sesgos Cognitivos:')
        st.write('Los **sesgos cognitivos** son errores mentales que afectan nuestras decisiones')
        st.markdown("""
        - **Sesgo de Confirmación**: Buscar únicamente información que confirme nuestra opinión. 
        - **Efecto Rebaño**: Seguir lo que hace la mayoría.
        - **Aversión a la Pérdida**: Las pérdidas suelen generar más dolor que satisfacción producen las ganancias.
                    """)
        st.write('---------')
        st.subheader('🧠¿Quieres descubrir tu propio perfil emocional como inversor?🧠')
        st.write('Solo tienes que responder a las siguientes preguntas')
        puntos = 0
        st.write('**Pregunta 1**')
        st.write('**Tu cartera pierde un 20% en una semana**')
        p1 = st.radio('¿Qué harías tú?',['Vendo todo inmediatamente','Vendo una parte','Mantengo mis posiciones','Compro más aprovechando la caída'])

        if p1 == 'Vendo todo inmediatamente':
            puntos += 1
        elif p1 == 'Vendo una parte':
            puntos += 2
        elif p1 == 'Mantengo mis posiciones':
            puntos += 3
        elif p1 == 'Compro más aprovechando la caída':
            puntos += 4
        st.write('------')

        st.write('**Pregunta 2**')
        st.write('**Todos tus amigos hablan de una acción que ha subido un 150%.**')
        p2 = st.radio('¿Qué harías tú?',['Compro cuanto antes','Investigo un poco y luego decido','Analizo la empresa','No invierto solo porque sea popular'])

        if p2 == 'Compro cuanto antes':
            puntos += 1
        elif p2 == 'Investigo un poco y luego decido':
            puntos += 2
        elif p2 == 'Analizo la empresa':
            puntos += 3
        elif p2 == 'No invierto solo porque sea popular':
            puntos += 4
        
        st.write('**Pregunta 3**')
        st.write('**Obtienes una ganancia del 30%**')
        p3 = st.radio('¿Qué harías tú?',['Vendo inmediatamente','Vendo parte','Mantengo','Reevalúo mis objetivos antes de decidir'])

        if p3 == 'Vendo inmediatamente':
            puntos += 1
        elif p3 == 'Vendo parte':
            puntos += 2
        elif p3 == 'Mantengo':
            puntos += 3
        elif p3 == 'Reevalúo mis objetivos antes de decidir':
            puntos += 4
        st.write('------')

        st.write('**Pregunta 4**')
        st.write('**Lees una noticia negativa sobre una empresa que posees**')
        p1 = st.radio('¿Qué harías tú?',['Vendo automáticamente','Me preocupo bastante','Busco más información','Analizo el impacto real antes de actuar'])

        if p1 == 'Vendo automáticamente':
            puntos += 1
        elif p1 == 'Me preocupo bastante':
            puntos += 2
        elif p1 == 'Busco más información':
            puntos += 3
        elif p1 == 'Analizo el impacto real antes de actuar':
            puntos += 4
        st.write('------')
        st.subheader('Resultado de tu perfl emocional como inversor:')
        if puntos <= 8:
            perfil = "🔴**Emocional: Las emociones influyen significativamente en sus decisiones, reacciona con rapidez ante noticias o movimientos del mercado, cambia frecuentemente de estrategia y tiene dificultades para mantener un plan de inversión.**"

        elif puntos <= 12:
            perfil = "🟠**Conservador: Prioriza proteger su capital, tolera mal las pérdidas, prefiere inversiones seguras y previsibles y busca estabilidad más que rentabilidades elevadas.**"

        elif puntos <= 15:
            perfil = "🟡**Prudente: Busca un equilibrio entre rentabilidad y seguridad, analiza antes de invertir, aunque también escucha su intuición, tolera cierto nivel de riesgo, pero evita situaciones extremas y prefiere inversiones relativamente estables.**"

        else:
            perfil = "🟢**Racional: Toma decisiones basadas en datos y análisis, no suele dejarse llevar por las emociones, mantiene su estrategia incluso durante períodos de volatilidad, analiza riesgos y oportunidades antes de actuar y tiene una visión de largo plazo**"
            
        bresult = st.button('Mostrar resultado: ')
        if bresult:
            st.success(perfil)

        


    elif seleccion == 'Trading':  
        st.subheader('Trading')  
        st.write('El **trading** es la compra y venta de activos financieros con el objetivo de obtener ganancias a corto plazo. Los traders pueden utilizar una variedad de estrategias, como el day trading, el swing trading o el scalping, y pueden operar en diferentes mercados, como acciones, divisas o criptomonedas.')
        st.write('----------')
        st.subheader('Mercados donde hacer Trading')
        st.write('Los **mercados** donde se puede hacer trading son los siguientes:')
        st.markdown("""
        1) **Acciones**: Participaciones de empresas.
        2) **Forex**: Mercado de divisas.
        3) **Criptomonedas**: Activos digitales como Bitcoin.
        4) **Índices**: Representan grupos de empresas.
        5) **Materias primas**: Oro, petróleo, plata, etc.
                    """)
        bimg = st.button('Comparación entre Invertir y Trading')
        if bimg:
            st.image('imagenes\invertir_vs_trading.png', caption = 'Tabla comparativa entre invertir y hacer trading')
        st.write('------------')
        st.subheader('Conceptos básicos de Tading')
        st.markdown("""
        - **Posición Larga**
        - **Posición Corta**
        - **Stop Loss**
        - **Take Profit**       
                    """)
        opc_concepto = st.text_input('Escribe el concepto a definir:')


        if opc_concepto == 'Posición Larga':
            st.subheader('**Posición Larga (Long)**')
            st.write('Comprar esperando que el precio suba.')
            st.write('Beneficio = Venta - Compra')
            
        

        elif opc_concepto == 'Posición Corta':
            st.subheader('**Posición Corta (Short)**')
            st.write('Vender esperando que el precio baje.')
            st.write('Beneficio = Precio de apertura - Precio de cierre')

        elif opc_concepto == 'Stop Loss':
            st.subheader('**Stop Loss**')
            st.write('Orden automática para limitar pérdidas.')
            with st.expander('Ver ejemplo'):
                st.markdown("""
                - Compras 100 €
                - Stop Loss 95 €
                            """)
                st.write('Si el precio llega a 95 €, la posición se cierra automáticamente.')

        elif opc_concepto == 'Take Profit':
            st.subheader('**Take Profit**')
            st.write('Orden automática para asegurar ganancias.')
            with st.expander('Ver ejemplo'):
                st.markdown("""
                - Compras 100 €
                - Take Profit 120 €
                            """)
                st.write('La posición se cierra cuando alcanza 120 €.')

        else:
            st.warning('No has escrito el concepto adecuadamente, debe ser igual que en la lista de conceptos')


        st.write('--------')
        st.subheader('Importancia de la gestión del riesgo en el Trading')
        st.write('Las **reglas básicas** son las siguientes:')
        st.markdown("""
        - ✅ **No arriesgar todo el capital en una operación**.
        - ✅ **Utilizar Stop Loss**.
        - ✅ **Mantener disciplina**.
        - ✅ **Evitar operar por impulsos**.
                    """)

        st.write('-----------')
        st.subheader('🎯 Simulador de Trading 🎯')
        
        if 'capital' not in st.session_state:
            st.session_state.capital = 10000
            st.session_state.acciones = 0
            st.session_state.precio = 100
            st.session_state.ronda = 1
            st.session_state.sesgos = 0

        
        if st.session_state.ronda > 10:
            patrimonio = (st.session_state.capital + st.session_state.acciones * st.session_state.precio)
            rentabilidad = ((patrimonio - 10000) / 10000 * 100)
            st.success('🎉 Simulación finalizada')

            st.write(f'💰 Capital final: {patrimonio:.2f} €')
            st.write(f'📊 Rentabilidad: {rentabilidad:.2f}%')
            st.write(f'🧠 Decisiones emocionales detectadas: ' f'{st.session_state.sesgos}')
        else:

            st.subheader(f'Ronda {st.session_state.ronda}/10')

            st.write(f'Precio actual: {st.session_state.precio:.2f} €')
            st.write(f'Capital: {st.session_state.capital:.2f} €')
            st.write(f'Acciones: {st.session_state.acciones}')

            opcion = st.radio('¿Qué quieres hacer?',['Comprar', 'Vender', 'Mantener'])

            if st.button('Confirmar'):

            
                if opcion == 'Comprar':
                    if st.session_state.capital >= st.session_state.precio:
                        st.session_state.capital -= st.session_state.precio
                        st.session_state.acciones += 1

                
                elif opcion == 'Vender':
                    if st.session_state.acciones > 0:
                        st.session_state.capital += st.session_state.precio
                        st.session_state.acciones -= 1

             
                cambio = random.randint(-15, 15)
                if opcion == 'Comprar' and cambio > 10:
                    st.session_state.sesgos += 1

                if opcion == 'Vender' and cambio < -10:
                    st.session_state.sesgos += 1

                st.session_state.precio *= (1 + cambio / 100)
                st.session_state.ronda += 1
                st.rerun()


    elif seleccion == 'Inversión a largo plazo':
        st.subheader('**Inversión a largo plazo**')
        st.write('La **inversión a largo plazo** es una estrategia que implica mantener activos financieros durante un período prolongado, generalmente años o décadas. Esta estrategia se basa en la idea de que, a largo plazo, los mercados tienden a crecer y que las inversiones pueden generar rendimientos significativos a través de la apreciación del capital y los dividendos.')
        st.write('----------')  
        st.subheader('Interés Compuesto')
        st.write('El **interés compuesto** es un mecanismo financiero mediante el cual los beneficios generados por una inversión se reinvierten para producir nuevos beneficios en el futuro.')
        st.write('**Funcionamiento:**')
        st.write('Cuando una inversión genera rentabilidad, los beneficios obtenidos se suman al capital invertido. En el siguiente período, la rentabilidad se calcula sobre esa cantidad mayor. Esto provoca que el crecimiento sea cada vez más rápido con el paso del tiempo.')
        with st.expander('Ver un ejemplo'):
            st.image('imagenes\interes_compuesto.png', caption = 'Ejemplo del interés compuesto')
        st.write('----------')  
        st.subheader('📈 Simulador de Interés Compuesto📈')

        capital_inicial = st.slider('Capital inicial (€)',100,100000,1000,100)
        aportacion_mensual = st.slider('Aportación mensual (€)',0,2000,200,50)
        rentabilidad = st.slider('Rentabilidad anual (%)',1,20, 8)
        años = st.slider('Años de inversión',1,40,20)
        capital = capital_inicial

        historial = []
        for a in range(1, años + 1):
            capital += aportacion_mensual * 12
            capital *= (1 + rentabilidad / 100)
            historial.append({
                'Año': a,
                'Capital': round(capital, 2)
            })

        df = pd.DataFrame(historial)
        st.subheader('💰 Resultado final💰')
        st.metric('Valor futuro', f'{capital:,.2f} €')

        invertido = capital_inicial + aportacion_mensual * 12 * años
        st.metric('Dinero aportado',f'{invertido:,.2f} €')
        st.metric( 'Beneficio generado',f'{capital - invertido:,.2f} €')
        
        st.subheader('📊 Evolución de la inversión📊')
        st.line_chart(df.set_index("Año"))

        
    elif seleccion == 'Finanzas Cuantitativas':
        st.subheader('Finanzas Cuantitativas')
        st.write('Las **finanzas cuantitativas** son una rama de las finanzas que utiliza modelos matemáticos, estadísticos e informáticos para analizar los mercados y ayudar en la toma de decisiones de inversión. En lugar de basarse únicamente en la intuición o la experiencia, utilizan datos y algoritmos para estudiar el comportamiento de los activos financieros.')
        with st.expander('Importancia de las Finanzas Cuantitativas'):
            st.markdown("""
            - Analizar miles de datos en segundos.
            - Detectar patrones difíciles de observar a simple vista.
            - Evaluar riesgos.
            - Optimizar carteras de inversión.
            -Desarrollar sistemas automáticos de trading.
                        """)
        st.write('----------')
        pilares = st.radio('Pilares de las Finanzas Cuantitativas',['Matemáticas', 'Estadística', 'Programación', 'Inteligencia Artificial'])
        if pilares == 'Matemáticas':
            st.write('**Matemáticas**')
            st.write('Permiten construir modelos que representan el comportamiento de los mercados.')

        elif pilares == 'Estadística':
            st.write('**Estadística**')
            st.write('Ayuda a analizar grandes cantidades de datos históricos.')


        elif pilares == 'Programación':
            st.write('**Programación**')
            st.write('Los modelos cuantitativos suelen implementarse mediante código.')
            
            
        elif pilares == 'Inteligencia Artificial':
            st.write('**Inteligencia Artificial**')
            st.write('Permite encontrar patrones complejos dentro de enormes volúmenes de información.')

        
