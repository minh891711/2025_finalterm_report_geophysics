import gradio as gr

def get_chapter_info(chapter_name):
    """
    根據章節名稱回傳詳細的介紹。
    """
    # 這裡的頁碼參考來自你提供的圖片
    chapter_info = {
        "地球是一個星球 (第1章)": {
            "title": "地球是一個星球：探索我們居住的家園",
            "summary": "這章節是我們地球物理之旅的起點！我們會像太空人一樣，從外太空的視角來看地球，了解我們的太陽系鄰居，以及地球這顆星球的獨特之處。我們會深入探討地球的動態，像是板塊運動、火山、地震等，了解為什麼地球總是這麼「活潑」！",
            "topics": "太陽系、動態地球"
        },
        "重力、地球的形狀與地球動力學 (第2章)": {
            "title": "重力與地球動力學：地球的隱形力量",
            "summary": "重力不僅僅是讓你蘋果掉下來的力量！在這章節，我們會探討地球的真實形狀——它並不是一個完美的圓球，而是因為自轉而稍微扁平。我們會學習如何透過測量重力來研究地球內部，並了解板塊如何「漂浮」在地函上（這個過程稱為「均衡作用」），這一切都和重力息息相關。",
            "topics": "地球的大小與形狀、重力、地球自轉、重力異常、均衡作用"
        },
        "地震學與地球內部結構 (第3章)": {
            "title": "地震學：地球的超音波檢查",
            "summary": "地震學是我們研究地球內部最重要的方法之一。我們可以把地震波想像成一種特殊的「超音波」，透過分析地震波在地球內部傳播的速度和路徑，我們能像醫生做B超一樣，描繪出地函、地核的樣子。這章節會帶你了解地震是如何產生，以及地震波如何揭示地球的奧秘。",
            "topics": "地震學、彈性理論、地震波、地震儀、地震學與地球內部結構"
        },
        "地球的年齡、熱與電性質 (第4章)": {
            "title": "地球的熱力學：地球的溫度與歷史",
            "summary": "地球已經存在數十億年，但你知道我們是如何知道它的年紀嗎？這章節將會揭示地球的「出生證明」，也就是地質年代學。我們也會探討地球的內部有多熱，以及地球如何散熱，這些熱量是驅動板塊運動的重要能量。此外，我們還會討論地電學，了解地球的電性質。",
            "topics": "地質年代學、地球的熱量、地電學"
        },
        "地磁學與古地磁學 (第5章)": {
            "title": "地磁學：地球的指南針與歷史紀錄",
            "summary": "地球有一個巨大的磁場，就像一個巨大的條形磁鐵。這章節會帶你了解這個磁場是如何產生、如何保護我們免受太陽風的傷害，以及如何利用岩石中的磁性來追溯地球磁場的歷史（古地磁學）。你將會發現，地球的南北極並不是一成不變的，它們會隨著時間翻轉！",
            "topics": "地磁學、磁學物理、岩石磁學、地磁極性"
        },
        "附錄": {
            "title": "深入探討：進階數學與物理概念",
            "summary": "附錄部分通常包含更進階的數學推導，像是「三維波動方程」和「半無限半空間的冷卻」，這些是為了幫助有興趣的同學更深入了解地球物理背後的物理原理。別擔心，這部分是選修的，但如果你想成為地球物理學家，它們將是你的好幫手！",
            "topics": "三維波動方程、半無限半空間的冷卻"
        }
    }
    
    info = chapter_info.get(chapter_name, {
        "title": "未知章節", 
        "summary": "請選擇一個有效的章節來了解其內容。",
        "topics": ""
    })
    
    # 格式化輸出
    response = f"### {info['title']}\n\n"
    response += f"**主題精華：** {info['summary']}\n\n"
    response += f"**涵蓋子題：** {info['topics']}"
    
    return response

# 定義問答功能
def get_quiz_question(chapter_name):
    """
    根據章節名稱提供一個相關的測驗問題。
    """
    quizzes = {
        "地球是一個星球 (第1章)": {
            "question": "請問地球物理學主要研究的是地球的哪部分？",
            "answer": "地球的物理性質與內部結構，例如地殼、地函、地核等。"
        },
        "重力、地球的形狀與地球動力學 (第2章)": {
            "question": "為什麼地球的形狀不是一個完美的圓球？",
            "answer": "因為地球的自轉產生的離心力，導致赤道部分稍微隆起，形成一個扁球體。"
        },
        "地震學與地球內部結構 (第3章)": {
            "question": "科學家如何透過地震學來「看見」地球內部？",
            "answer": "科學家利用地震波在地球不同介質中傳播速度和路徑的變化，來推斷地球內部各個層次的結構和組成。"
        },
        "地球的年齡、熱與電性質 (第4章)": {
            "question": "地球內部熱量的主要來源是什麼？",
            "answer": "主要來源是放射性元素（如鈾、釷、鉀）在衰變時釋放出的熱量。"
        },
        "地磁學與古地磁學 (第5章)": {
            "question": "什麼是「古地磁學」？它能告訴我們什麼？",
            "answer": "古地磁學是研究過去地球磁場的科學。它能告訴我們地磁極在過去的位置，並為板塊構造學提供關鍵證據，例如大陸漂移。"
        },
        "附錄": {
            "question": "三維波動方程主要用來描述什麼物理現象？",
            "answer": "它可以用來描述地震波在三維空間中的傳播。"
        }
    }
    quiz = quizzes.get(chapter_name, {"question": "請選擇一個章節來獲得測驗問題。", "answer": ""})
    return quiz["question"], quiz["answer"]

# Gradio 介面設定
with gr.Blocks(title="地球物理學概論：探索地球的秘密") as demo:
    gr.Markdown(
        """
        # 歡迎來到地球物理學的世界！
        
        嗨同學！我是你的地球物理學老師。這門課將帶領你透過物理學的視角，揭開地球深處的秘密。
        
        我們將一起探索從地球的起源到它每天發生的各種奇妙現象。準備好了嗎？
        """
    )
    
    # 章節選擇與介紹
    gr.Markdown("## 🌐 課程地圖：地球物理學概論")
    with gr.Row():
        chapter_dropdown = gr.Dropdown(
            ["地球是一個星球 (第1章)", 
             "重力、地球的形狀與地球動力學 (第2章)", 
             "地震學與地球內部結構 (第3章)", 
             "地球的年齡、熱與電性質 (第4章)", 
             "地磁學與古地磁學 (第5章)",
             "附錄"],
            label="請選擇一個你感興趣的章節",
            value="地球是一個星球 (第1章)"
        )
        info_button = gr.Button("點我了解章節內容！")

    chapter_info_output = gr.Markdown()
    
    info_button.click(
        fn=get_chapter_info,
        inputs=chapter_dropdown,
        outputs=chapter_info_output
    )

    gr.Markdown("---")
    
    # 互動式問答
    gr.Markdown("## 🧠 考考你：小試身手時間！")
    with gr.Row():
        quiz_button = gr.Button("生成一個問題！")
        quiz_question_box = gr.Textbox(label="問題", interactive=False)
        quiz_answer_box = gr.Textbox(label="答案", interactive=False, visible=False)
    
    with gr.Row():
        show_answer_button = gr.Button("顯示答案", visible=False)
        
    def show_quiz(chapter):
        question, answer = get_quiz_question(chapter)
        return question, answer, gr.update(visible=True)

    def show_answer(answer):
        return gr.update(visible=True, value=answer), gr.update(visible=False)

    quiz_button.click(
        fn=show_quiz,
        inputs=chapter_dropdown,
        outputs=[quiz_question_box, quiz_answer_box, show_answer_button]
    )

    show_answer_button.click(
        fn=lambda x: gr.update(visible=True, value=x),
        inputs=quiz_answer_box,
        outputs=quiz_answer_box
    )
    
# 啟動應用程式
if __name__ == "__main__":
    demo.launch()
