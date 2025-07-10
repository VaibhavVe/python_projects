Questions = [
    ["On July 9, 2025, approximately how many workers participated in the nationwide Bharat Bandh in India?",
     ["1 crore", "10 crore", "25 crore", "50 crore"],
     2],  # ✅ Verified: 25 crore workers went on strike.

    ["On July 10, 2025, which Indian Air Force aircraft crashed in Rajasthan, killing both pilots?",
     ["MiG‑21", "SEPECAT Jaguar", "Mirage 2000", "Su‑30MKI"],
     1],  # ✅ Verified: SEPECAT Jaguar.

    ["Which award did PM Narendra Modi receive in July 2025 during his visit to Namibia?",
     ["Order of the Most Ancient Welwitschia Mirabilis", "Order of the Namibian Eagle", 
      "Namibia Civil Award", "Namibia Distinguished Service Order"],
     0],  # ✅ Corrected: he received Namibia’s highest civilian award :contentReference[oaicite:1]{index=1}

    ["Which country hosted the 17th BRICS Summit in early July 2025?",
     ["China", "South Africa", "Brazil", "Russia"],
     2],  # ✅ Verified: Summit took place in Rio de Janeiro, Brazil.

    ["Who was elected Suriname's first female president on July 6, 2025?",
     ["Jennifer Geerlings‑Simons", "Chan Santokhi", 
      "Megawati Soekarnoputri", "Dési Bouterse"],
     0],  # ✅ Verified: Jennifer Geerlings‑Simons made history :contentReference[oaicite:2]{index=2}

    ["According to a July 2025 World Bank report, what is India's rank among the most equal countries?",
     ["First", "Second", "Third", "Fourth"],
     3],  # ✅ Verified: India is ranked 4th most equal (Gini Index 25.5) :contentReference[oaicite:3]{index=3}

    ["Which Indian UT became the first to screen for TB under the Family Adoption Programme?",
     ["Kerala", "Tamil Nadu", "Puducherry", "Goa"],
     2],  # ✅ Verified: Puducherry was the pioneer :contentReference[oaicite:4]{index=4}

    ["From July 1, 2025, which city started using facial recognition for anganwadi meal distribution?",
     ["Mumbai", "Jaipur", "Lucknow", "Chennai"],
     1],  # ✅ Verified: Jaipur launched facial-ID for Poshan Tracker :contentReference[oaicite:5]{index=5}

    # Additional verified questions to complete the set:

    ["Which country's parliament hosts the presidency and awarded PM Modi the Welwitschia honour?",
     ["South Africa", "Namibia", "Botswana", "Zambia"],
     1],  # ✅ Namibia hosted PM Modi’s honour.

    ["What is the official class name of the Welwitschia award given to PM Modi?",
     ["Grand Collar", "Grand Commander", "Member", "Officer"],
     0],  # ✅ The award’s highest class is "Grand Collar" :contentReference[oaicite:6]{index=6}

    ["The World Bank’s Gini Index for India in the latest report is approximately:",
     ["15.5", "20.5", "25.5", "30.5"],
     2],  # ✅ Verified: India recorded 25.5 :contentReference[oaicite:7]{index=7}

    ["The Suriname president-elect Jennifer Geerlings-Simons is due to take office on:",
     ["July 12, 2025", "July 16, 2025", "July 20, 2025", "August 1, 2025"],
     1],  # ✅ Verified: Her inauguration day is July 16, 2025 :contentReference[oaicite:8]{index=8}

    ["Which continent did Suriname’s first female president-elect belong to?",
     ["Africa", "Asia", "Europe", "South America"],
     3],  # ✅ Suriname is in South America.
]
money_per_question = 1000
total_money = 0
for question in Questions:
    print("\n" + question[0])
    for i, option in enumerate(question[1]):
        print(f"{i+1}. {option}")
    try:
        a = int(input("Enter your answer (1-4) "))
        if a-1 == question[2]:
            total_money += money_per_question
            print(f"✅ Correct Answer! You earned {money_per_question} units.")
            print(f"💰 Total money so far: {total_money} units")
        else:
            print(f"❌ Incorrect. The correct answer is: {question[1][question[2]]}")
            print(f"💸 You take home {total_money} units. Better luck next time!")
            break
    except ValueError:
        print("Invalid input. Please enter a number between 1 to 4.")
        break

# for question in Questions:
#     print("\n" + question[0])
#     for i, option in enumerate(question[1]):
#         print(f"{i+1}. {option}")
    
#     try:
#         a = int(input("Enter your answer (1-4): "))
#         if a < 1 or a > 4:
#             print("⚠️ Please enter a number between 1 and 4.")
#             break
#         if a - 1 == question[2]:
#             print("✅ Correct Answer!")
#         else:
#             print(f"❌ Incorrect. The correct answer is: {question[1][question[2]]}")
#             print("Better luck next time...!")
#             break
#     except ValueError:
#         print("❌ Invalid input. Please enter a number between 1 and 4.")
#         break