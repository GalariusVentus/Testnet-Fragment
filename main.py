import termuxgui as tg
from termuxgui import ViewGroup, WebView

class FragmentApp:
    def __init__(self):
        # Создаем соединение с плагином Termux:GUI
        self.conn = tg.Connection()
        
        # Создаем основное окно на весь экран
        self.activity = tg.Activity(self.conn)
        
        # Создаем полноэкранный WebView
        self.webview = WebView(self.conn, self.activity)
        # Заполняем WebView все окно
        self.webview.setLayoutParams(ViewGroup.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT,
                                                            ViewGroup.LayoutParams.MATCH_PARENT))
        self.activity.setContentView(self.webview)
        
        # JavaScript-код для инъекции, как в вашем примере
        js_inject = """
        (function() {
            try {
                console.log('--- STARTING TESTNET INJECTION ---');
                
                window.AppConfig = window.AppConfig || {};
                window.AppConfig.testnet = true;
                window.AppConfig.isTestnet = true;
                
                if (window.TonConnect) {
                    window.TonConnect.testnet = true;
                    window.TonConnect.isTestnet = true;
                }
                
                var observer = new MutationObserver(function(mutations) {
                    if (window.TonConnect && !window.TonConnect.testnet) {
                        window.TonConnect.testnet = true;
                        window.TonConnect.isTestnet = true;
                        console.log('TonConnect dynamically detected and switched to Testnet');
                    }
                });
                
                observer.observe(document.documentElement, {
                    childList: true,
                    subtree: true
                });

                console.log('--- TESTNET INJECTION SUCCESSFUL ---');
            } catch (e) {
                console.error('Injection failed: ' + e.message);
            }
        })();
        """
        
        # Загружаем URL и выполняем JavaScript после загрузки страницы
        self.webview.loadUrl("https://fragment.com")
        self.webview.evaluateJavascript(js_inject, None)
        
        # Запускаем главный цикл обработки событий
        self.conn.run()

if __name__ == '__main__':
    app = FragmentApp()